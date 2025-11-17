---
nexus: nexus-ai-chat-importer
plugin_version: "1.3.0"
provider: claude
artifact_id: claude_mcp_config
version_uuid: 61d047ac-681c-4617-9334-3b0865c5e603
version_number: 1
command: create
conversation_id: 644807bb-1f67-4300-96b3-ad046826e5eb
create_time: 2025-08-26T01:57:27.000Z
format: json
aliases: [Claude Desktop MCP Configuration, claude_mcp_config_v1]
---

# Claude Desktop MCP Configuration (Version 1)

**Conversation:** [[Nexus/Conversations/claude/2025/08/Random Facts in Obsidian|Random Facts in Obsidian]]

## Content

```json
{
  "mcpServers": {
    "mcp-obsidian": {
      "command": "uvx",
      "args": ["mcp-obsidian"],
      "env": {
        "OBSIDIAN_API_KEY": "7894f970b73da527e6b2304b5057b6165ddea675fd27920167c7281df8244749",
        "OBSIDIAN_HOST": "127.0.0.1",
        "OBSIDIAN_PORT": "8443"
      }
    }
  }
}
```