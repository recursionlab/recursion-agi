---
nexus: nexus-ai-chat-importer
plugin_version: "1.3.0"
provider: claude
artifact_id: conversation_processor
version_uuid: 32744f66-cebe-4c3f-990d-b4886323eb5f
version_number: 1
command: create
conversation_id: 9fbbf9fd-0fc7-4cb5-9e1d-9c2c1f119f9a
create_time: 2025-07-12T17:22:38.000Z
format: markdown
aliases: [Conversation Processing Script, conversation_processor_v1]
---

# Conversation Processing Script (Version 1)

**Conversation:** [[Nexus/Conversations/claude/2025/07/Knowledge Representation Topology|Knowledge Representation Topology]]

## Content

import json
import os
import sqlite3
from pathlib import Path
import requests
from typing import List, Dict
import hashlib

class ConversationProcessor:
    def __init__(self, db_path="conversations.db"):
        self.db_path = db_path
        self.ollama_url = "http://localhost:11434"
        self.init_database()
    
    def init_database(self):
        """Initialize SQLite database for conversation storage"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS conversations (
                id TEXT PRIMARY KEY,
                title TEXT,
                content TEXT,
                embedding BLOB,
                tags TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS topics (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE,
                description TEXT
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS conversation_topics (
                conversation_id TEXT,
                topic_id INTEGER,
                relevance_score REAL,
                FOREIGN KEY (conversation_id) REFERENCES conversations (id),
                FOREIGN KEY (topic_id) REFERENCES topics (id)
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def get_embedding(self, text: str) -> List[float]:
        """Get embedding from local Ollama model"""
        try:
            response = requests.post(
                f"{self.ollama_url}/api/embeddings",
                json={
                    "model": "all-minilm",
                    "prompt": text
                }
            )
            if response.status_code == 200:
                return response.json()["embedding"]
            else:
                print(f"Error getting embedding: {response.status_code}")
                return []
        except Exception as e:
            print(f"Error connecting to Ollama: {e}")
            return []
    
    def extract_topics(self, text: str) -> List[str]:
        """Extract topics using local phi3 model"""
        try:
            response = requests.post(
                f"{self.ollama_url}/api/generate",
                json={
                    "model": "phi3",
                    "prompt": f"Extract 3-5 key topics from this conversation. Return only the topics, separated by commas:\n\n{text[:2000]}",
                    "stream": False
                }
            )
            if response.status_code == 200:
                topics_text = response.json()["response"]
                topics = [topic.strip() for topic in topics_text.split(",")]
                return topics[:5]  # Limit to 5 topics
            else:
                print(f"Error extracting topics: {response.status_code}")
                return []
        except Exception as e:
            print(f"Error connecting to Ollama: {e}")
            return []
    
    def process_conversation_file(self, file_path: str):
        """Process a single conversation file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                conversation_data = json.load(f)
            
            # Extract conversation content
            if isinstance(conversation_data, dict):
                if 'messages' in conversation_data:
                    # Standard format
                    content = "\n".join([
                        f"{msg.get('role', 'unknown')}: {msg.get('content', '')}"
                        for msg in conversation_data['messages']
                    ])
                    title = conversation_data.get('title', f"Conversation {Path(file_path).stem}")
                else:
                    # Custom format
                    content = str(conversation_data)
                    title = f"Conversation {Path(file_path).stem}"
            else:
                content = str(conversation_data)
                title = f"Conversation {Path(file_path).stem}"
            
            # Generate unique ID
            conversation_id = hashlib.md5(content.encode()).hexdigest()
            
            # Check if already processed
            if self.conversation_exists(conversation_id):
                print(f"Skipping {file_path} (already processed)")
                return
            
            print(f"Processing {file_path}...")
            
            # Get embedding
            embedding = self.get_embedding(content)
            if not embedding:
                print(f"Failed to get embedding for {file_path}")
                return
            
            # Extract topics
            topics = self.extract_topics(content)
            
            # Store in database
            self.store_conversation(conversation_id, title, content, embedding, topics)
            print(f"Processed {file_path} successfully")
            
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
    
    def conversation_exists(self, conversation_id: str) -> bool:
        """Check if conversation already exists in database"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM conversations WHERE id = ?", (conversation_id,))
        exists = cursor.fetchone() is not None
        conn.close()
        return exists
    
    def store_conversation(self, conversation_id: str, title: str, content: str, 
                          embedding: List[float], topics: List[str]):
        """Store conversation and topics in database"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Store conversation
        cursor.execute('''
            INSERT OR REPLACE INTO conversations (id, title, content, embedding, tags)
            VALUES (?, ?, ?, ?, ?)
        ''', (conversation_id, title, content, json.dumps(embedding), json.dumps(topics)))
        
        # Store topics
        for topic in topics:
            cursor.execute('''
                INSERT OR IGNORE INTO topics (name, description)
                VALUES (?, ?)
            ''', (topic, f"Auto-extracted topic: {topic}"))
            
            # Get topic ID
            cursor.execute("SELECT id FROM topics WHERE name = ?", (topic,))
            topic_id = cursor.fetchone()[0]
            
            # Link conversation to topic
            cursor.execute('''
                INSERT OR REPLACE INTO conversation_topics (conversation_id, topic_id, relevance_score)
                VALUES (?, ?, ?)
            ''', (conversation_id, topic_id, 1.0))
        
        conn.commit()
        conn.close()
    
    def process_directory(self, directory_path: str):
        """Process all JSON files in a directory"""
        directory = Path(directory_path)
        if not directory.exists():
            print(f"Directory {directory_path} does not exist")
            return
        
        json_files = list(directory.glob("*.json"))
        print(f"Found {len(json_files)} JSON files to process")
        
        for file_path in json_files:
            self.process_conversation_file(str(file_path))
    
    def search_conversations(self, query: str, limit: int = 5) -> List[Dict]:
        """Search conversations by similarity"""
        query_embedding = self.get_embedding(query)
        if not query_embedding:
            return []
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT id, title, content, embedding, tags
            FROM conversations
        ''')
        
        results = []
        for row in cursor.fetchall():
            conversation_id, title, content, embedding_json, tags = row
            stored_embedding = json.loads(embedding_json)
            
            # Calculate cosine similarity
            similarity = self.cosine_similarity(query_embedding, stored_embedding)
            
            results.append({
                'id': conversation_id,
                'title': title,
                'content': content[:500] + "..." if len(content) > 500 else content,
                'tags': json.loads(tags),
                'similarity': similarity
            })
        
        conn.close()
        
        # Sort by similarity and return top results
        results.sort(key=lambda x: x['similarity'], reverse=True)
        return results[:limit]
    
    def cosine_similarity(self, vec1: List[float], vec2: List[float]) -> float:
        """Calculate cosine similarity between two vectors"""
        import math
        
        dot_product = sum(a * b for a, b in zip(vec1, vec2))
        magnitude1 = math.sqrt(sum(a * a for a in vec1))
        magnitude2 = math.sqrt(sum(a * a for a in vec2))
        
        if magnitude1 == 0 or magnitude2 == 0:
            return 0
        
        return dot_product / (magnitude1 * magnitude2)

# Usage example
if __name__ == "__main__":
    processor = ConversationProcessor()
    
    # Process all conversations in a directory
    # processor.process_directory("/path/to/your/conversations")
    
    # Search example
    # results = processor.search_conversations("machine learning concepts")
    # for result in results:
    #     print(f"Title: {result['title']}")
    #     print(f"Similarity: {result['similarity']:.3f}")
    #     print(f"Tags: {', '.join(result['tags'])}")
    #     print("-" * 50)
