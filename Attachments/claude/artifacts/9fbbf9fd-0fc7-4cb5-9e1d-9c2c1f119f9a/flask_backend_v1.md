---
nexus: nexus-ai-chat-importer
plugin_version: "1.3.0"
provider: claude
artifact_id: flask_backend
version_uuid: c3c089e5-a427-45aa-840d-6cbd99269a32
version_number: 1
command: create
conversation_id: 9fbbf9fd-0fc7-4cb5-9e1d-9c2c1f119f9a
create_time: 2025-07-12T17:22:38.000Z
format: markdown
aliases: [Flask Backend Server, flask_backend_v1]
---

# Flask Backend Server (Version 1)

**Conversation:** [[Nexus/Conversations/claude/2025/07/Knowledge Representation Topology|Knowledge Representation Topology]]

## Content

from flask import Flask, request, jsonify, render_template_string
from flask_cors import CORS
import sqlite3
import json
from datetime import datetime
import os

app = Flask(__name__)
CORS(app)

# Import your conversation processor
# from conversation_processor import ConversationProcessor

class ConversationAPI:
    def __init__(self, db_path="conversations.db"):
        self.db_path = db_path
        # self.processor = ConversationProcessor(db_path)
    
    def get_stats(self):
        """Get database statistics"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute("SELECT COUNT(*) FROM conversations")
            total_conversations = cursor.fetchone()[0]
            
            cursor.execute("SELECT COUNT(*) FROM topics")
            total_topics = cursor.fetchone()[0]
            
            cursor.execute("SELECT MAX(timestamp) FROM conversations")
            last_updated = cursor.fetchone()[0]
            
            conn.close()
            
            return {
                'total_conversations': total_conversations,
                'total_topics': total_topics,
                'last_updated': last_updated or 'Never'
            }
        except Exception as e:
            return {
                'total_conversations': 0,
                'total_topics': 0,
                'last_updated': 'Error',
                'error': str(e)
            }
    
    def search_conversations(self, query, limit=10):
        """Search conversations"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            # Simple text search first (for when embeddings aren't available)
            cursor.execute('''
                SELECT id, title, content, tags, timestamp
                FROM conversations
                WHERE content LIKE ? OR title LIKE ? OR tags LIKE ?
                ORDER BY timestamp DESC
                LIMIT ?
            ''', (f'%{query}%', f'%{query}%', f'%{query}%', limit))
            
            results = []
            for row in cursor.fetchall():
                conversation_id, title, content, tags, timestamp = row
                results.append({
                    'id': conversation_id,
                    'title': title,
                    'content': content[:500] + "..." if len(content) > 500 else content,
                    'tags': json.loads(tags) if tags else [],
                    'timestamp': timestamp,
                    'similarity': 0.8  # Mock similarity for now
                })
            
            conn.close()
            return results
            
        except Exception as e:
            return {'error': str(e)}

# Initialize API
api = ConversationAPI()

@app.route('/')
def index():
    """Serve the main search interface"""
    # In a real deployment, you'd serve the HTML file
    return "Conversation Search API is running. Use /search endpoint to search conversations."

@app.route('/api/stats')
def get_stats():
    """Get database statistics"""
    stats = api.get_stats()
    return jsonify(stats)

@app.route('/api/search', methods=['POST'])
def search():
    """Search conversations"""
    data = request.get_json()
    query = data.get('query', '')
    limit = data.get('limit', 10)
    
    if not query:
        return jsonify({'error': 'Query parameter is required'}), 400
    
    results = api.search_conversations(query, limit)
    return jsonify(results)

@app.route('/api/process', methods=['POST'])
def process_conversations():
    """Process conversation files"""
    data = request.get_json()
    directory = data.get('directory', '')
    
    if not directory or not os.path.exists(directory):
        return jsonify({'error': 'Valid directory path is required'}), 400
    
    try:
        # processor = ConversationProcessor()
        # processor.process_directory(directory)
        return jsonify({'success': True, 'message': f'Processing started for {directory}'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/topics')
def get_topics():
    """Get all topics"""
    try:
        conn = sqlite3.connect(api.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT t.name, t.description, COUNT(ct.conversation_id) as conversation_count
            FROM topics t
            LEFT JOIN conversation_topics ct ON t.id = ct.topic_id
            GROUP BY t.id, t.name, t.description
            ORDER BY conversation_count DESC
        ''')
        
        topics = []
        for row in cursor.fetchall():
            name, description, count = row
            topics.append({
                'name': name,
                'description': description,
                'conversation_count': count
            })
        
        conn.close()
        return jsonify(topics)
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Health check endpoint
@app.route('/health')
def health_check():
    return jsonify({'status': 'healthy', 'timestamp': datetime.now().isoformat()})

if __name__ == '__main__':
    # Create database if it doesn't exist
    if not os.path.exists('conversations.db'):
        print("Database not found. Run the conversation processor first to create it.")
    
    print("Starting Conversation Search API...")
    print("Access the API at: http://localhost:5000")
    print("Available endpoints:")
    print("  GET  /api/stats - Database statistics")
    print("  POST /api/search - Search conversations")
    print("  POST /api/process - Process conversation files")
    print("  GET  /api/topics - Get all topics")
    print("  GET  /health - Health check")
    
    app.run(debug=True, host='0.0.0.0', port=5000)
