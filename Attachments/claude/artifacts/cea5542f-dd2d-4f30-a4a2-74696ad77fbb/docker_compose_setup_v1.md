---
nexus: nexus-ai-chat-importer
plugin_version: "1.3.0"
provider: claude
artifact_id: docker_compose_setup
version_uuid: ea52f81b-ddf2-435d-846d-abcb55abef22
version_number: 1
command: create
conversation_id: cea5542f-dd2d-4f30-a4a2-74696ad77fbb
create_time: 2025-07-04T04:12:57.000Z
format: markdown
aliases: [docker-compose.yml - Vector Database Setup, docker_compose_setup_v1]
---

# docker-compose.yml - Vector Database Setup (Version 1)

**Conversation:** [[Nexus/Conversations/claude/2025/07/Becoming an AGI Proxy|Becoming an AGI Proxy]]

## Content

version: '3.8'
services:
  chromadb:
    image: chromadb/chroma:latest
    ports:
      - "8000:8000"
    volumes:
      - ./chroma_data:/chroma/chroma
    environment:
      - CHROMA_SERVER_HOST=0.0.0.0
      - CHROMA_SERVER_PORT=8000
    restart: unless-stopped
    
  # Optional: Add Qdrant as alternative vector DB
  qdrant:
    image: qdrant/qdrant:latest
    ports:
      - "6333:6333"
    volumes:
      - ./qdrant_data:/qdrant/storage
    environment:
      - QDRANT__SERVICE__HTTP_PORT=6333
    restart: unless-stopped
    profiles: ["qdrant"]