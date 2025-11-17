---
nexus: nexus-ai-chat-importer
plugin_version: "1.3.0"
provider: claude
artifact_id: weaviate_setup_fix
version_uuid: 5441eb69-17b7-4e10-a26b-866f9b77961e
version_number: 1
command: create
conversation_id: dca7c0e8-5283-496b-a1c9-53811348754a
create_time: 2025-08-21T07:30:24.000Z
format: markdown
aliases: [Fixed Weaviate Setup + Agent Zero Custom Instrument, weaviate_setup_fix_v1]
---

# Fixed Weaviate Setup + Agent Zero Custom Instrument (Version 1)

**Conversation:** [[Nexus/Conversations/claude/2025/08/Recursive Intelligence Architecture|Recursive Intelligence Architecture]]

## Content

# FIXED WEAVIATE SETUP FOR AGENT ZERO INTEGRATION

# 1. Start Weaviate with correct image name
echo "🚀 Starting Weaviate vector database..."
docker run -d \
  --name weaviate-container \
  -p 8080:8080 \
  -e AUTHENTICATION_ANONYMOUS_ACCESS_ENABLED=true \
  -e PERSISTENCE_DATA_PATH=/var/lib/weaviate \
  -e DEFAULT_VECTORIZER_MODULE=text2vec-transformers \
  -e ENABLE_MODULES=text2vec-transformers \
  -e TRANSFORMERS_INFERENCE_API=http://t2v-transformers:8080 \
  semitechnologies/weaviate:1.21.1

# 2. Start text2vec-transformers module
echo "🔧 Starting transformers module..."
docker run -d \
  --name t2v-transformers \
  -p 8081:8080 \
  semitechnologies/transformers-inference:sentence-transformers-all-MiniLM-L6-v2

# 3. Verify setup
echo "⏳ Waiting for services to start..."
sleep 10

echo "🔍 Checking Weaviate health..."
curl -s http://localhost:8080/v1/meta

echo "✅ Weaviate setup complete!"
echo "Weaviate UI: http://localhost:8080"
echo "Ready for LeanRAG integration!"
