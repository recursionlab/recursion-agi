---
nexus: nexus-ai-chat-importer
plugin_version: "1.3.0"
provider: claude
artifact_id: unified_mcp_config
version_uuid: b1041c76-9656-4cf9-8052-e327ad1f29f8
version_number: 2
command: update
conversation_id: 8f90798f-51a3-4cf3-873d-5a5815a9364f
create_time: 2025-07-29T02:05:56.000Z
format: json
aliases: [Untitled Artifact, unified_mcp_config_v2]
---

# Untitled Artifact (Version 2)

**Conversation:** [[Nexus/Conversations/claude/2025/07/VS Code MCP Extension|VS Code MCP Extension]]

## Content

```json
{
  "mcpServers": {
    "memory": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-memory"],
      "env": {}
    },
    "qwen-bridge": {
      "command": "node",
      "args": ["./qwen-mcp-bridge.js"],
      "env": {
        "QWEN_ENDPOINT": "http://127.0.0.1:1234/v1/"
      }
    },
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "C:/Users/steve/Projects"],
      "env": {}
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "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"
      }
    }
  }
}
```