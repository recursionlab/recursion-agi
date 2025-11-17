---
nexus: nexus-ai-chat-importer
plugin_version: "1.3.0"
provider: claude
artifact_id: check_db_schema
version_uuid: d9edd7a2-f7bc-46a4-8faa-c7a1632f9fd1
version_number: 1
command: create
conversation_id: 8171ff4f-5806-43fa-8c46-da21f61b9075
create_time: 2025-08-22T07:16:05.000Z
format: markdown
aliases: [Check and Create Knowledge Layers Table, check_db_schema_v1]
---

# Check and Create Knowledge Layers Table (Version 1)

**Conversation:** [[Nexus/Conversations/claude/2025/08/Python Script Execution Error|Python Script Execution Error]]

## Content

import sqlite3
import os

def check_and_create_knowledge_layers_table():
    """Check if knowledge_layers table exists and create it if not"""
    db_path = 'D:/agent-zero/knowledge_vault.db'
    
    if not os.path.exists(db_path):
        print(f"Database does not exist at {db_path}")
        return False
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Check if knowledge_layers table exists
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='knowledge_layers';")
    table_exists = cursor.fetchone() is not None
    
    if not table_exists:
        print("Creating knowledge_layers table...")
        cursor.execute('''
            CREATE TABLE knowledge_layers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                doc_id INTEGER,
                layer INTEGER,
                compressed_content TEXT,
                concepts TEXT,
                recursion_signature TEXT,
                compression_ratio REAL,
                concept_levels TEXT,
                processing_depth INTEGER,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (doc_id) REFERENCES documents (id)
            )
        ''')
        conn.commit()
        print("knowledge_layers table created successfully!")
    else:
        print("knowledge_layers table already exists")
    
    # Show table schema
    cursor.execute("PRAGMA table_info(knowledge_layers);")
    schema = cursor.fetchall()
    print("\nKnowledge layers table schema:")
    for column in schema:
        print(f"  {column[1]} ({column[2]})")
    
    # Check documents table as well
    print("\nChecking documents table...")
    cursor.execute("SELECT COUNT(*) FROM documents;")
    doc_count = cursor.fetchone()[0]
    print(f"Found {doc_count} documents in the database")
    
    if doc_count > 0:
        cursor.execute("SELECT id, original_path FROM documents LIMIT 5;")
        sample_docs = cursor.fetchall()
        print("\nFirst 5 documents:")
        for doc_id, path in sample_docs:
            print(f"  ID {doc_id}: {os.path.basename(path)}")
    
    conn.close()
    return True

if __name__ == "__main__":
    check_and_create_knowledge_layers_table()
