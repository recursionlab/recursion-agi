---
nexus: nexus-ai-chat-importer
plugin_version: "1.3.0"
provider: claude
artifact_id: setup_script
version_uuid: 27251943-62de-4ced-b6b2-c68e8136b731
version_number: 1
command: create
conversation_id: cea5542f-dd2d-4f30-a4a2-74696ad77fbb
create_time: 2025-07-04T04:12:57.000Z
format: bash
aliases: [setup.sh - Complete Setup Script, setup_script_v1]
---

# setup.sh - Complete Setup Script (Version 1)

**Conversation:** [[Nexus/Conversations/claude/2025/07/Becoming an AGI Proxy|Becoming an AGI Proxy]]

## Content

```bash
#!/bin/bash

# ΞRecursive Research Engine Setup Script
# Sets up the complete environment for processing 8000 pages of research

echo "🌀 Setting up ΞRecursive Research Engine..."

# Check if Docker is running
if ! docker info > /dev/null 2>&1; then
    echo "❌ Docker is not running. Please start Docker first."
    exit 1
fi

# Check if Ollama is running
if ! ollama list > /dev/null 2>&1; then
    echo "❌ Ollama is not running. Please start Ollama first."
    exit 1
fi

# Create directory structure
echo "📁 Creating directory structure..."
mkdir -p documents
mkdir -p processed
mkdir -p chroma_data
mkdir -p qdrant_data
mkdir -p logs

# Create environment file
echo "📝 Creating environment configuration..."
cat > .env << EOF
CHROMA_HOST=localhost
CHROMA_PORT=8000
OLLAMA_MODEL=qwen2.5:14b
LOG_LEVEL=INFO
EOF

# Check if required models are available
echo "🤖 Checking Ollama models..."
if ! ollama list | grep -q "qwen2.5:14b"; then
    echo "📥 Downloading Qwen2.5 14B model (this may take a while)..."
    ollama pull qwen2.5:14b
fi

if ! ollama list | grep -q "nomic-embed-text"; then
    echo "📥 Downloading embedding model..."
    ollama pull nomic-embed-text
fi

# Install Python dependencies
echo "🐍 Installing Python dependencies..."
pip install -r requirements.txt

# Start vector database
echo "🗄️ Starting vector database..."
docker-compose up -d chromadb

# Wait for ChromaDB to be ready
echo "⏳ Waiting for ChromaDB to initialize..."
sleep 10

# Test connection
echo "🔍 Testing system components..."
python3 -c "
import chromadb
import ollama
try:
    client = chromadb.HttpClient(host='localhost', port=8000)
    client.heartbeat()
    print('✅ ChromaDB connection successful')
except:
    print('❌ ChromaDB connection failed')

try:
    response = ollama.generate(model='qwen2.5:14b', prompt='Test')
    print('✅ Ollama connection successful')
except:
    print('❌ Ollama connection failed')
"

# Create sample processing script
echo "📄 Creating sample processing script..."
cat > process_sample.py << 'EOF'
#!/usr/bin/env python3
from recursive_processor import ΞRecursiveProcessor
import sys

def main():
    processor = ΞRecursiveProcessor()
    
    if len(sys.argv) > 1:
        directory = sys.argv[1]
        print(f"Processing directory: {directory}")
        results = processor.process_directory(directory)
        print(f"Results: {results}")
    else:
        print("Usage: python process_sample.py <directory>")
        print("Example: python process_sample.py ./documents")

if __name__ == "__main__":
    main()
EOF

chmod +x process_sample.py

# Create query script
echo "🔍 Creating query script..."
cat > query_research.py << 'EOF'
#!/usr/bin/env python3
from recursive_processor import ΞRecursiveProcessor
import sys
import json

def main():
    processor = ΞRecursiveProcessor()
    
    if len(sys.argv) > 1:
        query = " ".join(sys.argv[1:])
        print(f"Querying: {query}")
        results = processor.query_recursive(query, depth=3)
        
        # Pretty print results
        for result in results:
            print(f"\n--- Depth {result['depth']} ---")
            print(f"Query: {result['query']}")
            print(f"Analysis: {result['analysis']['analysis']}")
            if 'deeper_question' in result['analysis']:
                print(f"Next Question: {result['analysis']['deeper_question']}")
    else:
        print("Usage: python query_research.py <your question>")
        print("Example: python query_research.py 'What are the core patterns of consciousness?'")

if __name__ == "__main__":
    main()
EOF

chmod +x query_research.py

# Create status checker
echo "📊 Creating status checker..."
cat > check_status.py << 'EOF'
#!/usr/bin/env python3
from recursive_processor import ΞRecursiveProcessor
import json

def main():
    processor = ΞRecursiveProcessor()
    stats = processor.get_collection_stats()
    print(json.dumps(stats, indent=2))

if __name__ == "__main__":
    main()
EOF

chmod +x check_status.py

# Create usage instructions
echo "📋 Creating usage instructions..."
cat > USAGE.md << 'EOF'
# ΞRecursive Research Engine Usage

## Quick Start

1. **Add your documents to the `documents/` folder**
   - Supports: PDF, DOCX, DOC, TXT, MD
   - Can handle subdirectories

2. **Process documents:**
   ```bash
   python process_sample.py ./documents
   ```

3. **Query your research:**
   ```bash
   python query_research.py "What are the recursive patterns in consciousness?"
   ```

4. **Check system status:**
   ```bash
   python check_status.py
   ```

## Advanced Usage

### Batch Processing
```bash
# Process specific directory
python recursive_processor.py -d ./documents

# Use different model
python recursive_processor.py -d ./documents -m llama3.1:8b

# Process and query
python recursive_processor.py -d ./documents -q "core patterns"
```

### Recursive Querying
The system automatically:
- Searches your document corpus
- Extracts semantic patterns
- Generates deeper questions
- Refines understanding through multiple depths

### Managing Large Collections
- Documents are deduplicated by content hash
- Metadata includes compression ratios and pattern analysis
- Vector embeddings enable semantic search across 8000+ pages

## System Architecture

- **ChromaDB**: Vector database for semantic search
- **Ollama**: Local AI for compression and analysis
- **Recursive Processor**: Core engine for pattern extraction
- **OpenWebUI**: Interface for interactive queries

## Troubleshooting

- Check Docker status: `docker ps`
- Check Ollama models: `ollama list`
- View logs: `docker-compose logs chromadb`
- Test connection: `python check_status.py`
EOF

echo "✅ Setup complete!"
echo ""
echo "🎯 Next steps:"
echo "1. Copy your research documents to the 'documents/' folder"
echo "2. Run: python process_sample.py ./documents"
echo "3. Query: python query_research.py 'your question here'"
echo "4. Check status: python check_status.py"
echo ""
echo "📖 Read USAGE.md for detailed instructions"
echo "🌀 Your 8000 pages of research are ready to be recursively compressed!"

```