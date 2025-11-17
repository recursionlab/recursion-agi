---
nexus: nexus-ai-chat-importer
plugin_version: "1.3.0"
provider: claude
artifact_id: minimal_db_test
version_uuid: 3a0fbd07-9d3d-40b5-8ba5-ef735509bb3c
version_number: 1
command: create
conversation_id: 8171ff4f-5806-43fa-8c46-da21f61b9075
create_time: 2025-08-22T07:16:05.000Z
format: markdown
aliases: [Minimal Database Test, minimal_db_test_v1]
---

# Minimal Database Test (Version 1)

**Conversation:** [[Nexus/Conversations/claude/2025/08/Python Script Execution Error|Python Script Execution Error]]

## Content

#!/usr/bin/env python3
"""
Minimal test to check database connectivity and structure
"""
import sqlite3
import os
import sys

def test_database():
    """Test basic database operations"""
    try:
        # Change to the correct directory
        os.chdir('D:\\agent-zero')
        
        db_path = 'knowledge_vault.db'
        print(f"Checking database at: {os.path.abspath(db_path)}")
        
        if not os.path.exists(db_path):
            print("❌ Database file does not exist!")
            return False
        
        # Connect to database
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        print("✅ Successfully connected to database")
        
        # List all tables
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = [row[0] for row in cursor.fetchall()]
        print(f"📊 Found tables: {tables}")
        
        # Check documents table
        if 'documents' in tables:
            cursor.execute("SELECT COUNT(*) FROM documents;")
            doc_count = cursor.fetchone()[0]
            print(f"📄 Documents table has {doc_count} rows")
            
            if doc_count > 0:
                cursor.execute("SELECT id, original_path FROM documents LIMIT 3;")
                samples = cursor.fetchall()
                print("📝 Sample documents:")
                for doc_id, path in samples:
                    exists = "✅" if os.path.exists(path) else "❌"
                    print(f"   {doc_id}: {os.path.basename(path)} {exists}")
        
        # Check/create knowledge_layers table
        if 'knowledge_layers' not in tables:
            print("🔧 Creating knowledge_layers table...")
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
            print("✅ knowledge_layers table created")
        else:
            cursor.execute("SELECT COUNT(*) FROM knowledge_layers;")
            layer_count = cursor.fetchone()[0]
            print(f"🧠 knowledge_layers table has {layer_count} rows")
        
        conn.close()
        print("✅ Database test completed successfully!")
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_database()
    if success:
        print("\n🚀 Ready to run process_with_dynamic_recursion.py")
    else:
        print("\n💥 Fix database issues before proceeding")
    sys.exit(0 if success else 1)
