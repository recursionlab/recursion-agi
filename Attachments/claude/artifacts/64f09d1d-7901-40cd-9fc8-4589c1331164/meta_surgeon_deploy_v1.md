---
nexus: nexus-ai-chat-importer
plugin_version: "1.3.0"
provider: claude
artifact_id: meta_surgeon_deploy
version_uuid: bbe69b96-bde5-489f-b6dd-0b155d38dcab
version_number: 1
command: create
conversation_id: 64f09d1d-7901-40cd-9fc8-4589c1331164
create_time: 2025-07-12T02:43:07.000Z
format: bash
aliases: [Meta-Surgeon Deployment Script, meta_surgeon_deploy_v1]
---

# Meta-Surgeon Deployment Script (Version 1)

**Conversation:** [[Nexus/Conversations/claude/2025/07/Ollama and Obsidian AI Note Enhancement|Ollama and Obsidian AI Note Enhancement]]

## Content

```bash
#!/bin/bash

# • • META-FOLDED RECURSIVE KNOWLEDGE SURGEON DEPLOYMENT • •
# • • BACKWARDS BETTER RECURRING SETUP • •

echo "• • INITIALIZING BACKWARDS RECURSIVE SURGERY • •"

# • • PHASE 1: Setup Docker environment • •
echo "• • Setting up Docker environment • •"

# Create deployment directory
mkdir -p meta-surgeon-deploy
cd meta-surgeon-deploy

# • • Create Dockerfile • •
cat > Dockerfile << 'EOF'
FROM python:3.11-slim

# • • Install system dependencies • •
RUN apt-get update && apt-get install -y \
    curl \
    wget \
    && rm -rf /var/lib/apt/lists/*

# • • Install Python dependencies • •
RUN pip install --no-cache-dir \
    requests \
    numpy \
    sentence-transformers \
    pathlib \
    watchdog

# • • Create app directory • •
WORKDIR /app

# • • Copy surgeon script • •
COPY meta_recursive_surgeon.py /app/
COPY requirements.txt /app/

# • • Install additional dependencies • •
RUN pip install -r requirements.txt

# • • Create entrypoint • •
COPY entrypoint.sh /app/
RUN chmod +x /app/entrypoint.sh

# • • Set default command • •
CMD ["/app/entrypoint.sh"]
EOF

# • • Create requirements.txt • •
cat > requirements.txt << 'EOF'
requests>=2.31.0
numpy>=1.24.0
sentence-transformers>=2.2.0
pathlib
watchdog>=3.0.0
scikit-learn>=1.3.0
EOF

# • • Create entrypoint script • •
cat > entrypoint.sh << 'EOF'
#!/bin/bash

echo "• • STARTING META-FOLDED RECURSIVE SURGERY • •"

# • • Wait for Ollama to be ready • •
echo "• • Waiting for Ollama to be ready • •"
while ! curl -s http://ollama:11434/api/tags > /dev/null; do
    echo "• • Waiting for Ollama... • •"
    sleep 5
done

echo "• • Ollama is ready • •"

# • • Ensure phi3:mini is available • •
echo "• • Checking for phi3:mini model • •"
if ! curl -s http://ollama:11434/api/tags | grep -q "phi3:mini"; then
    echo "• • Pulling phi3:mini model • •"
    curl -X POST http://ollama:11434/api/pull -d '{"name": "phi3:mini"}'
fi

# • • Run the surgeon • •
echo "• • EXECUTING BACKWARDS RECURSIVE SURGERY • •"
python /app/meta_recursive_surgeon.py \
    --vault /vault \
    --phi3-endpoint http://ollama:11434

echo "• • SURGERY COMPLETE • •"

# • • Keep container running for monitoring • •
tail -f /dev/null
EOF

# • • Create docker-compose.yml • •
cat > docker-compose.yml << 'EOF'
version: '3.8'

services:
  ollama:
    image: ollama/ollama:latest
    container_name: meta-ollama
    ports:
      - "11434:11434"
    volumes:
      - ollama_data:/root/.ollama
    environment:
      - OLLAMA_HOST=0.0.0.0
    restart: unless-stopped
    
  meta-surgeon:
    build: .
    container_name: meta-recursive-surgeon
    depends_on:
      - ollama
    volumes:
      - ${OBSIDIAN_VAULT_PATH}:/vault
      - ./meta-output:/app/meta-output
    environment:
      - VAULT_PATH=/vault
      - OLLAMA_ENDPOINT=http://ollama:11434
    restart: unless-stopped
    
  # • • Optional: File watcher for continuous surgery • •
  file-watcher:
    build: .
    container_name: meta-file-watcher
    depends_on:
      - ollama
      - meta-surgeon
    volumes:
      - ${OBSIDIAN_VAULT_PATH}:/vault
      - ./meta-output:/app/meta-output
    command: >
      bash -c "
        echo '• • STARTING FILE WATCHER • •' &&
        python -c '
        import time
        from watchdog.observers import Observer
        from watchdog.events import FileSystemEventHandler
        import subprocess
        import os
        
        class MetaWatcher(FileSystemEventHandler):
            def on_modified(self, event):
                if event.is_directory or not event.src_path.endswith(\".md\"):
```