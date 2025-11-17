---
nexus: nexus-ai-chat-importer
plugin_version: "1.3.0"
provider: claude
artifact_id: sticky_note_schema
version_uuid: cfb6edef-0498-40d6-88af-17696d9da00e
version_number: 1
command: create
conversation_id: be3e0849-4c3b-44df-b21e-365455699ba8
create_time: 2025-09-22T19:44:35.000Z
format: json
aliases: [Recursive StickyNote JSON Schema, sticky_note_schema_v1]
---

# Recursive StickyNote JSON Schema (Version 1)

**Conversation:** [[Nexus/Conversations/claude/2025/09/Starting from scratch|Starting from scratch]]

## Content

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Recursive StickyNote System",
  "type": "object",
  "properties": {
    "id": {
      "type": "string",
      "description": "Unique identifier for this note"
    },
    "content": {
      "type": "string",
      "description": "Main text content of the note"
    },
    "title": {
      "type": "string",
      "description": "Brief title/summary of the note"
    },
    "abstractionLevel": {
      "type": "integer",
      "minimum": 0,
      "description": "Depth level (0 = top level, higher = more detailed)"
    },
    "position": {
      "type": "object",
      "properties": {
        "x": {"type": "number"},
        "y": {"type": "number"},
        "z": {"type": "number", "description": "Z-axis for layering"}
      },
      "required": ["x", "y"]
    },
    "metadata": {
      "type": "object",
      "properties": {
        "created": {"type": "string", "format": "date-time"},
        "modified": {"type": "string", "format": "date-time"},
        "tags": {
          "type": "array",
          "items": {"type": "string"}
        },
        "color": {"type": "string", "description": "Visual theme/color"},
        "priority": {"type": "integer", "minimum": 1, "maximum": 5}
      }
    },
    "connections": {
      "type": "object",
      "properties": {
        "parent": {
          "type": "string",
          "description": "ID of parent note"
        },
        "children": {
          "type": "array",
          "items": {"type": "string"},
          "description": "Array of child note IDs"
        },
        "linkedNotes": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "id": {"type": "string"},
              "relationship": {"type": "string", "enum": ["relates", "contradicts", "builds-on", "example-of"]}
            }
          }
        }
      }
    },
    "viewState": {
      "type": "object",
      "properties": {
        "isExpanded": {"type": "boolean"},
        "isVisible": {"type": "boolean"},
        "scale": {"type": "number", "minimum": 0.1, "maximum": 3.0}
      }
    },
    "content_layers": {
      "type": "object",
      "description": "Different representations of the same concept",
      "properties": {
        "summary": {"type": "string"},
        "detailed": {"type": "string"},
        "visual": {"type": "string", "description": "ASCII art, diagrams, or image references"},
        "examples": {
          "type": "array",
          "items": {"type": "string"}
        }
      }
    }
  },
  "required": ["id", "content", "abstractionLevel", "position"]
}
```