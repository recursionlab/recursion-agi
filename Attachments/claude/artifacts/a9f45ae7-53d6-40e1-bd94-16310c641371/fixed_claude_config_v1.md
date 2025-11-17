---
nexus: nexus-ai-chat-importer
plugin_version: "1.3.0"
provider: claude
artifact_id: fixed_claude_config
version_uuid: 8428a444-1dab-474d-b3d8-a2c9f352cf9c
version_number: 1
command: create
conversation_id: a9f45ae7-53d6-40e1-bd94-16310c641371
create_time: 2025-08-12T18:48:27.000Z
format: json
aliases: [Fixed Claude Desktop Config, fixed_claude_config_v1]
---

# Fixed Claude Desktop Config (Version 1)

**Conversation:** [[Nexus/Conversations/claude/2025/08/Filesystem Bootstrap Development|Filesystem Bootstrap Development]]

## Content

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": [
        "@modelcontextprotocol/server-filesystem",
        "D:\\aider-projects"
      ]
    }
  }
}
```