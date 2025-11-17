---
nexus: nexus-ai-chat-importer
plugin_version: "1.3.0"
provider: claude
aliases: OpenWebUI Embedding Model Troubleshooting
conversation_id: 2c0f8a6e-f612-4db5-beb8-daf73514de45
create_time: 2025-07-04T05:05:55.000Z
update_time: 2025-07-04T05:09:52.000Z
---

# Title: OpenWebUI Embedding Model Troubleshooting

Created: 07/04/2025 at 12:05:55 AM
Last Updated: 07/04/2025 at 12:09:52 AM
Chat URL: https://claude.ai/chat/2c0f8a6e-f612-4db5-beb8-daf73514de45


>[!nexus_user] **User** - 07/04/2025 at 12:05:55 AM
> my embedding model isnt working on OpenWebUI , cant get anywhere with ChatGPT
>>[!nexus_attachment] **image.png** (image/png)
>> ⚠️ Not included in archive. [Open original conversation](https://claude.ai/chat/2c0f8a6e-f612-4db5-beb8-daf73514de45)
<!-- UID: 9be4d921-4a2a-4641-b790-d2e51a1aea2a -->
>[!nexus_agent] **Assistant** - 07/04/2025 at 12:06:11 AM
>  Looking at your OpenWebUI configuration, I can see several potential issues with your embedding setup. Let me help you troubleshoot this systematically.
> 
> ## Immediate Issues I Notice:
> 
> 1. **Embedding Model Engine**: You have "Ollama" selected, but your embedding model is `nomic-embed-text`
> 2. **API Endpoint**: `http://localhost:11434` - this needs to be accessible to OpenWebUI
> 3. **Model Availability**: The model needs to be properly pulled and available
> 
> ## Diagnostic Steps:
> 
> ### 1. Verify Ollama is Running
> ```bash
> # Check if Ollama is running
> curl http://localhost:11434/api/tags
> 
> # If not running, start it
> ollama serve
> ```
> 
> ### 2. Check if Your Embedding Model is Available
> ```bash
> # List available models
> ollama list
> 
> # If nomic-embed-text isn't there, pull it
> ollama pull nomic-embed-text
> ```
> 
> ### 3. Test the Embedding Model Directly
> ```bash
> # Test the embedding model
> curl http://localhost:11434/api/embeddings -d '{
>   "model": "nomic-embed-text",
>   "prompt": "test embedding"
> }'
> ```
> 
> ## Configuration Fixes:
> 
> ### Option 1: Use Ollama Embedding (Recommended)
> - Keep "Ollama" as your embedding engine
> - Ensure `nomic-embed-text` is pulled: `ollama pull nomic-embed-text`
> - Verify the endpoint is `http://localhost:11434`
> 
> ### Option 2: Use OpenAI-Compatible Embedding
> If you want to use an OpenAI-compatible endpoint:
> - Change embedding engine to "OpenAI"
> - Update the endpoint to your OpenAI-compatible service
> - Add the appropriate API key
> 
> ## Common Issues & Solutions:
> 
> 1. **Port Conflicts**: Make sure port 11434 isn't blocked
> 2. **Docker Networking**: If running in Docker, ensure proper network configuration
> 3. **Model Loading**: Large embedding models take time to load initially
> 
> ## Quick Test:
> Try this simple test to verify your setup:
> ```bash
> # Test if Ollama API responds
> curl -X GET http://localhost:11434/api/tags
> 
> # Test embedding specifically
> curl -X POST http://localhost:11434/api/embeddings \
>   -H "Content-Type: application/json" \
>   -d '{"model": "nomic-embed-text", "prompt": "hello world"}'
> ```
> 
> What specific error messages are you seeing? Are you getting connection errors, model loading issues, or something else? This will help me provide more targeted assistance.
<!-- UID: aaabc814-be36-49e6-bd5b-9c425ebee580 -->

---
>[!nexus_user] **User** - 07/04/2025 at 12:07:17 AM
> 555176,0.09018232673406601,-0.1917143017053604]}
> C:\WINDOWS\system32>
> pulling manifest
> pulling 970aa74c0a90: 100% ▕██████████████████████████████████████████████████████████▏ 274 MB
> pulling c71d239df917: 100% ▕██████████████████████████████████████████████████████████▏  11 KB
> pulling ce4a164fc046: 100% ▕██████████████████████████████████████████████████████████▏   17 B
> pulling 31df23ea7daa: 100% ▕██████████████████████████████████████████████████████████▏  420 B
> verifying sha256 digest
> writing manifest
> success
> C:\WINDOWS\system32>curl -X GET http://localhost:11434/api/tags
> {"models":[{"name":"nomic-embed-text:latest","model":"nomic-embed-text:latest","modified_at":"2025-07-04T00:06:28.7598032-05:00","size":274302450,"digest":"0a109f422b47e3a30ba2b10eca18548e944e8a23073ee3f3e947efcf3c45e59f","details":{"parent_model":"","format":"gguf","family":"nomic-bert","families":["nomic-bert"],"parameter_size":"137M","quantization_level":"F16"}},{"name":"phi3:mini","model":"phi3:mini","modified_at":"2025-06-24T21:25:06.7301948-05:00","size":2176178913,"digest":"4f222292793889a9a40a020799cfd28d53f3e01af25d48e06c5e708610fc47e9","details":{"parent_model":"","format":"gguf","family":"phi3","families":["phi3"],"parameter_size":"3.8B","quantization_level":"Q4_0"}}]}
> C:\WINDOWS\system32>curl -X POST http://localhost:11434/api/embeddings \  -H "Content-Type: application/json" \  -d '{"model": "nomic-embed-text", "prompt": "hello world"}'
> {"error":"invalid character '\\'' looking for beginning of value"}curl: (3) URL rejected: Bad hostname
> curl: (3) URL rejected: Bad hostname
> curl: (3) URL rejected: Bad hostname
> curl: (3) URL rejected: Port number was not a decimal number between 0 and 65535
> curl: (3) unmatched close brace/bracket in URL position 12:
> hello world}'
>            ^
> C:\WINDOWS\system32>curl -X POST http://localhost:11434/api/embeddings \  -H "Content-Type: application/json" \  -d '{"model": "nomic-embed-text", "prompt": "hello world"}'
> {"error":"invalid character '\\'' looking for beginning of value"}curl: (3) URL rejected: Bad hostname
> curl: (3) URL rejected: Bad hostname
> curl: (3) URL rejected: Bad hostname
> curl: (3) URL rejected: Port number was not a decimal number between 0 and 65535
> curl: (3) unmatched close brace/bracket in URL position 12:
> hello world}'
>            ^
> C:\WINDOWS\system32>
>>[!nexus_attachment] **image.png** (image/png)
>> ⚠️ Not included in archive. [Open original conversation](https://claude.ai/chat/2c0f8a6e-f612-4db5-beb8-daf73514de45)
<!-- UID: 89fdfde8-52ff-4339-90c2-740af28f76df -->
>[!nexus_agent] **Assistant** - 07/04/2025 at 12:07:33 AM
>  Perfect! I can see what's happening. Your Ollama setup is working correctly - the model `nomic-embed-text` is successfully installed and the API is responding. The curl command syntax is just having issues with Windows Command Prompt.
> 
> Let me give you the correct Windows syntax and then we'll focus on your OpenWebUI configuration:
> 
> ## Test Your Embedding (Windows Command Prompt):
> 
> ```cmd
> curl -X POST http://localhost:11434/api/embeddings -H "Content-Type: application/json" -d "{\"model\": \"nomic-embed-text\", \"prompt\": \"hello world\"}"
> ```
> 
> ## Your OpenWebUI Configuration Looks Correct
> 
> Based on your screenshots, your settings should work:
> - ✅ Embedding Model Engine: Ollama  
> - ✅ Embedding Model: nomic-embed-text
> - ✅ API Endpoint: http://localhost:11434
> - ✅ Model is installed and available
> 
> ## Troubleshooting Steps:
> 
> ### 1. Check OpenWebUI Logs
> Look for error messages in your OpenWebUI logs. Common issues:
> 
> ### 2. Restart OpenWebUI
> After changing embedding settings, restart OpenWebUI completely:
> ```cmd
> # Stop OpenWebUI (Ctrl+C if running in terminal)
> # Then restart it
> ```
> 
> ### 3. Test Document Upload
> Try uploading a simple text document and see if it processes. The embedding should kick in during document processing.
> 
> ### 4. Check OpenWebUI Network Access
> If OpenWebUI is running in Docker, ensure it can reach `localhost:11434`. You might need to use `host.docker.internal:11434` instead of `localhost:11434`.
> 
> ### 5. Verify RAG is Enabled
> Make sure you have "Full Context Mode" enabled in your RAG settings (which I can see you do).
> 
> ## What specific error are you seeing in OpenWebUI?
> 
> - Does document upload fail?
> - Are you getting embedding errors in the UI?
> - Is the search not working?
> 
> The fact that your Ollama is working and the model is installed suggests the issue is likely in the OpenWebUI configuration or network connectivity between OpenWebUI and Ollama.
> 
> Can you try uploading a document and let me know what specific error message you get?
<!-- UID: 2565e050-578e-4813-b50a-a57c001bca9e -->

---
>[!nexus_user] **User** - 07/04/2025 at 12:09:35 AM
> [No content found]
>>[!nexus_attachment] **image.png** (image/png)
>> ⚠️ Not included in archive. [Open original conversation](https://claude.ai/chat/2c0f8a6e-f612-4db5-beb8-daf73514de45)
<!-- UID: f7f01439-512e-4a4a-b0c9-fa908baa1ea2 -->
>[!nexus_agent] **Assistant** - 07/04/2025 at 12:09:52 AM
>  Perfect! Now I can see the exact issue. The error message "400: 'NoneType' object is not iterable" is a clear indicator of what's happening.
> 
> ## The Problem
> This error typically occurs when OpenWebUI tries to process the embedding response from Ollama but receives an unexpected format or null response. The issue is likely in the communication between OpenWebUI and your Ollama embedding service.
> 
> ## Solutions to Try:
> 
> ### 1. **Check OpenWebUI Backend Logs**
> First, let's see what's happening in the backend. Open your OpenWebUI logs (usually in the terminal where you started OpenWebUI) to see the full error stack trace.
> 
> ### 2. **Test the Embedding API Response Format**
> Let's verify the exact response format from your Ollama embedding endpoint:
> 
> ```cmd
> curl -X POST http://localhost:11434/api/embeddings -H "Content-Type: application/json" -d "{\"model\": \"nomic-embed-text\", \"prompt\": \"test\"}"
> ```
> 
> ### 3. **Common Fixes:**
> 
> #### Option A: Restart Both Services
> ```cmd
> # Stop OpenWebUI
> # Stop Ollama
> ollama stop
> 
> # Restart Ollama
> ollama serve
> 
> # Restart OpenWebUI
> ```
> 
> #### Option B: Check Embedding Model Format
> Sometimes the issue is with the embedding model itself. Try pulling a different embedding model:
> 
> ```cmd
> ollama pull mxbai-embed-large
> ```
> 
> Then change your OpenWebUI embedding model to `mxbai-embed-large`.
> 
> #### Option C: Reset OpenWebUI Database
> The issue might be corrupted embedding data. You can try:
> - Delete the uploaded document
> - Clear the knowledge base
> - Re-upload the document
> 
> ### 4. **Alternative Embedding Configuration**
> If the issue persists, try switching to a different embedding approach:
> 
> - **Option 1**: Use `all-minilm` (smaller, faster)
>   ```cmd
>   ollama pull all-minilm
>   ```
> 
> - **Option 2**: Use OpenAI embeddings (if you have API access)
>   - Change engine to "OpenAI"
>   - Use `text-embedding-3-small` model
> 
> ### 5. **Check Network Configuration**
> If OpenWebUI is running in Docker, the endpoint might need to be:
> - `host.docker.internal:11434` (Windows/Mac Docker)
> - `172.17.0.1:11434` (Linux Docker)
> 
> ## Debug Steps:
> 1. Check what the actual embedding API returns
> 2. Look at OpenWebUI backend logs for the full error
> 3. Try a different embedding model
> 4. Restart both services clean
> 
> Can you run that curl command and show me the exact response? Also, if you can share the OpenWebUI backend logs (the terminal output), that would help identify the exact issue.
<!-- UID: fe92ac1a-2709-44df-a724-4368a5c1f873 -->

---