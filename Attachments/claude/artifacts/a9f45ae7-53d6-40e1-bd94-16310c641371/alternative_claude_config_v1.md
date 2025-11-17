---
nexus: nexus-ai-chat-importer
plugin_version: "1.3.0"
provider: claude
artifact_id: alternative_claude_config
version_uuid: fbe1225f-5785-4dd8-a4ee-d763ecc0bacf
version_number: 1
command: create
conversation_id: a9f45ae7-53d6-40e1-bd94-16310c641371
create_time: 2025-08-12T18:48:27.000Z
format: json
aliases: [Alternative Claude Config, alternative_claude_config_v1]
---

# Alternative Claude Config (Version 1)

**Conversation:** [[Nexus/Conversations/claude/2025/08/Filesystem Bootstrap Development|Filesystem Bootstrap Development]]

## Content

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "node",
      "args": [
        "C:\\Program Files\\nodejs\\node_modules\\@modelcontextprotocol\\server-filesystem\\dist\\index.js",
        "D:\\aider-projects"
      ]
    }
  }
}
```