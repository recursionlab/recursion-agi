---
nexus: nexus-ai-chat-importer
plugin_version: "1.3.0"
provider: claude
artifact_id: unified_mcp_config
version_uuid: e66b334c-ce35-4d50-9844-e0e067451f3f
version_number: 1
command: create
conversation_id: 8f90798f-51a3-4cf3-873d-5a5815a9364f
create_time: 2025-07-29T02:01:32.000Z
format: json
aliases: [Unified MCP Configuration, unified_mcp_config_v1]
---

# Unified MCP Configuration (Version 1)

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
    "optuna": {
      "command": "uvx",
      "args": ["optuna-mcp", "--storage", "sqlite:///optuna.db"],
      "env": {}
    },
    "playwright": {
      "command": "npx",
      "args": ["-y", "@playwright/mcp@latest"],
      "env": {}
    },
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "C:/Users/YOU/Projects"],
      "env": {}
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "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"
      }
    },
    "context7": {
      "command": "npx",
      "args": ["-y", "@context7/mcp"],
      "env": {}
    },
    "sequential-thinking": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-sequential-thinking"],
      "env": {}
    }
  }
}
```