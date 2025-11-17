---
nexus: nexus-ai-chat-importer
plugin_version: "1.3.0"
provider: claude
artifact_id: ollama_aider_setup
version_uuid: 0b48b8fc-4bbf-47ac-b8a0-8ba39b760823
version_number: 1
command: create
conversation_id: fa968e89-4b1f-4488-b7ca-dad8e3bdd1a8
create_time: 2025-08-12T01:10:37.000Z
format: markdown
aliases: [Ollama + Aider Setup Guide, ollama_aider_setup_v1]
---

# Ollama + Aider Setup Guide (Version 1)

**Conversation:** [[Nexus/Conversations/claude/2025/08/Aider-Notion Meta-AI Integration|Aider-Notion Meta-AI Integration]]

## Content

# Ollama + Aider Setup Fix

## Current Issue
Your model names don't exist in Ollama's registry. The `:free` suffix and specific model paths you're using aren't valid Ollama model identifiers.

## Step 1: Check Available Models
```powershell
ollama list
```

If this shows nothing, you need to pull actual available models.

## Step 2: Pull Working Models for Aider

### Recommended Models (in order of capability):

#### For Coding (Best Options):
```powershell
# DeepSeek Coder (excellent for code, small size)
ollama pull deepseek-coder:6.7b

# Code Llama (Meta's code-focused model)
ollama pull codellama:7b

# Llama 2 (general purpose, reliable)
ollama pull llama2:7b
```

#### For Advanced Reasoning:
```powershell
# Mistral (good balance of performance/size)
ollama pull mistral:7b

# Neural Chat (Microsoft's model, good for conversations)
ollama pull neural-chat:7b
```

## Step 3: Test Model Installation
```powershell
ollama run deepseek-coder:6.7b
```

Type a simple test like "Hello" and press Enter. If it responds, the model is working. Press Ctrl+D to exit.

## Step 4: Configure Aider with Ollama

### Option A: Direct Model Specification
```powershell
aider --model ollama/deepseek-coder:6.7b
```

### Option B: Set Environment Variable
```powershell
$env:AIDER_MODEL="ollama/deepseek-coder:6.7b"
aider
```

### Option C: Config File
Create `.aider.conf.yml` in your project directory:
```yaml
model: ollama/deepseek-coder:6.7b
```

## Step 5: Verify Aider Connection
```powershell
aider --model ollama/deepseek-coder:6.7b --list-models
```

This should show your Ollama models in the list.

## Troubleshooting

### If Ollama Service Isn't Running:
```powershell
ollama serve
```
Leave this running in one terminal, open a new one for aider.

### If Models Are Too Slow:
Try smaller models:
```powershell
ollama pull tinyllama:1.1b    # Very fast, basic capability
ollama pull phi:2.7b          # Microsoft's efficient model
```

### If You Want Larger Models (if you have 16GB+ RAM):
```powershell
ollama pull llama2:13b        # Larger, more capable
ollama pull codellama:13b     # Better coding model
```

## Test Complete Setup
```powershell
# Terminal 1: Start Ollama service
ollama serve

# Terminal 2: Test Aider
cd D:\your-project-directory
aider --model ollama/deepseek-coder:6.7b README.md
```

## Expected Working Command Sequence
```powershell
# In your aider environment
ollama pull deepseek-coder:6.7b
ollama run deepseek-coder:6.7b  # Test it works
# Ctrl+D to exit
aider --model ollama/deepseek-coder:6.7b
```

## Why Your Original Commands Failed

1. `openai/gpt-oss-20b:free` - Not a valid Ollama model path
2. `gpt-oss-20b:free` - This model doesn't exist in Ollama registry
3. `cognitivecomputations/dolphin-mistral-24b-venice-edition:free` - Invalid model name format

Ollama uses a simpler naming convention: `modelname:size` (like `mistral:7b` or `llama2:13b`).

## Next Steps for Integration
Once you have Aider working with Ollama, we can:
1. Set up the file monitoring system we built earlier
2. Configure it to watch your Aider sessions
3. Begin building the Notion integration bridge

Try the `deepseek-coder:6.7b` model first - it's specifically trained for coding tasks and should work well with Aider.