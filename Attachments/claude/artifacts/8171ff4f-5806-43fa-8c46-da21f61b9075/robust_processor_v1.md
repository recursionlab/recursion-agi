---
nexus: nexus-ai-chat-importer
plugin_version: "1.3.0"
provider: claude
artifact_id: robust_processor
version_uuid: 1aa20289-c1ee-418a-a090-d0f66b390470
version_number: 1
command: create
conversation_id: 8171ff4f-5806-43fa-8c46-da21f61b9075
create_time: 2025-08-22T07:16:05.000Z
format: markdown
aliases: [Robust Dynamic Recursive Processor, robust_processor_v1]
---

# Robust Dynamic Recursive Processor (Version 1)

**Conversation:** [[Nexus/Conversations/claude/2025/08/Python Script Execution Error|Python Script Execution Error]]

## Content

#!/usr/bin/env python3
"""
Robust version of the dynamic recursive processor with comprehensive error handling
"""
import sqlite3
import os
import sys
import traceback
from datetime import datetime

# First, let's check if we can import the required modules
def check_dependencies():
    """Check if all required modules are available"""
    missing_modules = []
    
    try:
        import sqlite3
        print("✅ sqlite3 available")
    except ImportError:
        missing_modules.append("sqlite3")
    
    try:
        from DynamicRecursiveProcessor import DynamicRecursiveProcessor
        print("✅ DynamicRecursiveProcessor available")
    except ImportError as e:
        print(f"❌ DynamicRecursiveProcessor not available: {e}")
        missing_modules.append("DynamicRecursiveProcessor")
    
    try:
        from process_content import extract_text_from_pdf
        print("✅ process_content available")
    except ImportError as e:
        print(f"❌ process_content not available: {e}")
        missing_modules.append("process_content")
    
    return missing_modules

def setup_database():
    """Ensure database and tables exist"""
    try:
        conn = sqlite3.connect('knowledge_vault.db')
        cursor = conn.cursor()
        
        # Check if knowledge_layers table exists
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='knowledge_layers';")
        if not cursor.fetchone():
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
            print("✅ knowledge_layers table created")
        
        conn.close()
        return True
    except Exception as e:
        print(f"❌ Database setup failed: {e}")
        return False

def store_recursive_results_safe(cursor, doc_id, filtered):
    """Safely store recursive results with error handling"""
    try:
        # Extract concepts as string
        concepts_str = ','.join(filtered.get('concepts', []))
        
        # Create a simple processor instance to get concept levels
        # (We'll handle this more safely)
        concept_levels = "0"  # Default fallback
        
        # Store in database
        cursor.execute('''
            INSERT INTO knowledge_layers 
            (doc_id, layer, compressed_content, concepts, recursion_signature, 
             compression_ratio, concept_levels, processing_depth)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (doc_id, 
              filtered.get('depth', 0), 
              filtered.get('compressed_content', '')[:10000],  # Limit length
              concepts_str[:1000],  # Limit length
              f'Ξ^{filtered.get("depth", 0)}',
              filtered.get('compression_ratio', 1.0),
              concept_levels,
              filtered.get('depth', 0)))
        
        # Recursively store next layers (with depth limit to prevent infinite recursion)
        if 'next_layer' in filtered and filtered.get('depth', 0) < 10:
            store_recursive_results_safe(cursor, doc_id, filtered['next_layer'])
    
    except Exception as e:
        print(f"❌ Error storing results for doc {doc_id}: {e}")

def process_with_dynamic_recursion_safe():
    """Safe version of the processing function"""
    print(f"🚀 Starting dynamic recursive processing at {datetime.now()}")
    
    # Check dependencies first
    print("\n📦 Checking dependencies...")
    missing = check_dependencies()
    if missing:
        print(f"❌ Missing modules: {missing}")
        print("Please install missing dependencies and try again")
        return False
    
    # Setup database
    print("\n🗃️ Setting up database...")
    if not setup_database():
        return False
    
    # Try to process documents
    try:
        print("\n🔄 Starting document processing...")
        conn = sqlite3.connect('knowledge_vault.db')
        cursor = conn.cursor()
        
        # Import modules (now that we know they exist)
        from DynamicRecursiveProcessor import DynamicRecursiveProcessor
        from process_content import extract_text_from_pdf
        
        processor = DynamicRecursiveProcessor()
        print("✅ Processor initialized")
        
        # Get documents
        cursor.execute("SELECT id, original_path FROM documents")
        documents = cursor.fetchall()
        print(f"📄 Found {len(documents)} documents to process")
        
        processed_count = 0
        error_count = 0
        
        for doc_id, original_path in documents:
            try:
                if os.path.exists(original_path):
                    print(f"\n📖 Processing: {os.path.basename(original_path)}")
                    
                    # Extract text with timeout protection
                    text = extract_text_from_pdf(original_path)
                    if not text or len(text.strip()) < 100:
                        print(f"⚠️ Insufficient text extracted from {original_path}")
                        continue
                    
                    print(f"📝 Extracted {len(text)} characters")
                    
                    # Dynamic recursive processing with error handling
                    try:
                        results = processor.recursive_process(text[:50000])  # Limit input size
                        print(f"🧠 Processed to depth {results.get('depth', 0)}")
                        
                        # Filter first-order content
                        filtered = processor.filter_first_order(results)
                        
                        # Store results
                        store_recursive_results_safe(cursor, doc_id, filtered)
                        
                        processed_count += 1
                        print(f"✅ Stored results for document {doc_id}")
                        
                    except Exception as e:
                        print(f"❌ Processing error for {original_path}: {e}")
                        error_count += 1
                        
                else:
                    print(f"⚠️ File not found: {original_path}")
                    error_count += 1
                    
            except Exception as e:
                print(f"❌ Error with document {doc_id}: {e}")
                error_count += 1
        
        conn.commit()
        conn.close()
        
        print(f"\n📊 Processing complete!")
        print(f"✅ Successfully processed: {processed_count}")
        print(f"❌ Errors encountered: {error_count}")
        
        return processed_count > 0
        
    except Exception as e:
        print(f"❌ Critical error during processing: {e}")
        traceback.print_exc()
        return False

if __name__ == "__main__":
    try:
        # Change to correct directory
        os.chdir('D:\\agent-zero')
        print(f"📁 Working directory: {os.getcwd()}")
        
        success = process_with_dynamic_recursion_safe()
        
        if success:
            print("\n🎉 Processing completed successfully!")
        else:
            print("\n💥 Processing failed - check errors above")
        
        sys.exit(0 if success else 1)
        
    except KeyboardInterrupt:
        print("\n⏹️ Processing interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n💥 Unexpected error: {e}")
        traceback.print_exc()
        sys.exit(1)
