---
nexus: nexus-ai-chat-importer
plugin_version: "1.3.0"
provider: claude
artifact_id: unified_mcp_config
version_uuid: c9227fb3-784f-4a1c-a37f-6fa6156a0f27
version_number: 1
command: create
conversation_id: 4e59e8e5-39cd-4a48-98e3-b22eb68b0090
create_time: 2025-07-29T02:16:20.000Z
format: json
aliases: [Unified MCP Server Configuration, unified_mcp_config_v1]
---

# Unified MCP Server Configuration (Version 1)

**Conversation:** [[Nexus/Conversations/claude/2025/07/Context7 MCP Server Configuration|Context7 MCP Server Configuration]]

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
      "args": ["-y", "@modelcontextprotocol/server-playwright"],
      "env": {}
    },
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "C:\\Users\\ANN\\Projects"],
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