---
nexus: nexus-ai-chat-importer
plugin_version: "1.3.0"
provider: claude
artifact_id: ollama_setup
version_uuid: 414bdd60-d416-4d26-ba1d-01740511ca46
version_number: 1
command: create
conversation_id: 9fbbf9fd-0fc7-4cb5-9e1d-9c2c1f119f9a
create_time: 2025-07-12T17:22:38.000Z
format: markdown
aliases: [Ollama Setup Script, ollama_setup_v1]
---

# Ollama Setup Script (Version 1)

**Conversation:** [[Nexus/Conversations/claude/2025/07/Knowledge Representation Topology|Knowledge Representation Topology]]

## Content

# Install Ollama (Linux/macOS)
curl -fsSL https://ollama.com/install.sh | sh

# Pull required models
ollama pull phi3
ollama pull all-minilm  # Lightweight embedding model (~80MB)

# Verify installation
ollama list