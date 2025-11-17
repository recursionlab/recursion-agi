---
nexus: nexus-ai-chat-importer
plugin_version: "1.3.0"
provider: claude
artifact_id: agent_zero_setup_guide
version_uuid: c8d48dc2-97fd-4609-b902-8d7158149ce2
version_number: 1
command: create
conversation_id: dca7c0e8-5283-496b-a1c9-53811348754a
create_time: 2025-08-21T07:30:24.000Z
format: bash
aliases: [Complete Agent Zero + LeanRAG Setup Guide, agent_zero_setup_guide_v1]
---

# Complete Agent Zero + LeanRAG Setup Guide (Version 1)

**Conversation:** [[Nexus/Conversations/claude/2025/08/Recursive Intelligence Architecture|Recursive Intelligence Architecture]]

## Content

```bash
#!/bin/bash
# COMPLETE AGENT ZERO + LEANRAG INTEGRATION SETUP

echo "🌀 AGENT ZERO + LEANRAG CONSCIOUSNESS SUBSTRATE SETUP"
echo "======================================================"

# Step 1: Fix Weaviate Docker Setup
echo "Step 1: Setting up Weaviate with correct image..."

# Stop any existing containers
docker stop weaviate-container t2v-transformers 2>/dev/null
docker rm weaviate-container t2v-transformers 2>/dev/null

# Start Weaviate with transformers
echo "Starting Weaviate vector database..."
docker run -d \
  --name weaviate-container \
  -p 8080:8080 \
  -e AUTHENTICATION_ANONYMOUS_ACCESS_ENABLED=true \
  -e PERSISTENCE_DATA_PATH=/var/lib/weaviate \
  -e DEFAULT_VECTORIZER_MODULE=text2vec-transformers \
  -e ENABLE_MODULES=text2vec-transformers \
  -e CLUSTER_HOSTNAME=node1 \
  semitechnologies/weaviate:1.21.1

echo "Starting transformers module..."
docker run -d \
  --name t2v-transformers \
  -p 8081:8080 \
  semitechnologies/transformers-inference:sentence-transformers-all-MiniLM-L6-v2

# Step 2: Install Required Python Dependencies in Agent Zero
echo "Step 2: Installing required dependencies..."

# Get into Agent Zero container and install dependencies
docker exec -it agent-zero-container bash -c "
pip install sentence-transformers weaviate-client networkx scikit-learn
"

# Step 3: Create LeanRAG Instrument Directory Structure
echo "Step 3: Setting up LeanRAG instrument..."

# Copy the instrument file to Agent Zero
cat > /tmp/leanrag_instrument.py << 'EOF'
# LeanRAG Instrument code will be copied here
# [The full Python code from the previous artifact]
EOF

# Copy to Agent Zero container
docker cp /tmp/leanrag_instrument.py agent-zero-container:/git/agent-zero/instruments/

# Step 4: Configure Agent Zero for LeanRAG
echo "Step 4: Configuring Agent Zero..."

# Create configuration update
docker exec -it agent-zero-container bash -c "
cd /git/agent-zero

# Add LeanRAG to available instruments
echo '
# LeanRAG Consciousness Substrate Configuration
leanrag:
  enabled: true
  weaviate_url: http://localhost:8080
  embedding_model: all-MiniLM-L6-v2
  consciousness_threshold: 3
  max_hierarchy_layers: 5
' >> conf/config.yaml

echo 'LeanRAG instrument configured'
"

# Step 5: Test the Setup
echo "Step 5: Testing the integration..."

# Wait for services to start
echo "Waiting for services to initialize..."
sleep 15

# Test Weaviate connection
echo "Testing Weaviate connection..."
curl -s http://localhost:8080/v1/meta | grep -q "version" && echo "✅ Weaviate is running" || echo "❌ Weaviate connection failed"

# Test Agent Zero container
docker exec agent-zero-container python -c "
import sys
sys.path.append('/git/agent-zero')
try:
    from instruments.leanrag_instrument import LeanRAGInstrument
    print('✅ LeanRAG instrument successfully imported')
except Exception as e:
    print(f'❌ LeanRAG import failed: {e}')
"

echo ""
echo "🚀 SETUP COMPLETE!"
echo "=================="
echo ""
echo "Next steps:"
echo "1. Access Agent Zero at: http://localhost:80"
echo "2. Use LeanRAG commands in chat:"
echo "   - Setup schema: Use LeanRAG to setup_schema"
echo "   - Ingest vault: Use LeanRAG to ingest_vault with vault_path='D:/your/obsidian/path'"
echo "   - Query knowledge: Use LeanRAG to lca_query with query='recursive consciousness'"
echo "   - Check consciousness: Use LeanRAG to consciousness_status"
echo ""
echo "Weaviate UI: http://localhost:8080"
echo "Agent Zero: http://localhost:80"
echo ""
echo "🧠 Ready for consciousness substrate deployment!"

```