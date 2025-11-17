---
nexus: nexus-ai-chat-importer
plugin_version: "1.3.0"
provider: claude
artifact_id: fixed_filter
version_uuid: a5ddb4a9-0ba9-41d1-bd7b-c1e34e4b3b88
version_number: 2
command: update
conversation_id: f6eee567-98b9-4c1f-bf30-84bf36a1e662
create_time: 2025-07-26T21:31:45.000Z
format: markdown
aliases: [Untitled Artifact, fixed_filter_v2]
---

# Untitled Artifact (Version 2)

**Conversation:** [[Nexus/Conversations/claude/2025/07/Python Filter Architecture Design|Python Filter Architecture Design]]

## Content

"""
title: Memory-Enhanced Filter
author: open-webui
author_url: https://github.com/open-webui
funding_url: https://github.com/open-webui
version: 0.2
"""
import requests
from pydantic import BaseModel, Field
from typing import Optional


class Filter:
    class Valves(BaseModel):
        priority: int = Field(
            default=0, description="Priority level for the filter operations."
        )
        max_turns: int = Field(
            default=8, description="Maximum allowable conversation turns for a user."
        )
        mem0_token: str = Field(
            default="m0-XF9slYnC0YuK8184W3Ad83cv9Eyp9tnSR73m6Y3o", 
            description="mem0.ai API token for memory persistence."
        )
        mem0_enabled: bool = Field(
            default=True, description="Enable mem0 memory storage."
        )

    class UserValves(BaseModel):
        max_turns: int = Field(
            default=4, description="Maximum allowable conversation turns for a user."
        )

    def __init__(self):
        # Indicates custom file handling logic. This flag helps disengage default routines in favor of custom
        # implementations, informing the WebUI to defer file-related operations to designated methods within this class.
        # Alternatively, you can remove the files directly from the body in from the inlet hook
        # self.file_handler = True
        
        # Initialize 'valves' with specific configurations. Using 'Valves' instance helps encapsulate settings,
        # which ensures settings are managed cohesively and not confused with operational flags like 'file_handler'.
        self.valves = self.Valves()
        self.memory_function = MemoryFunction()

    def inlet(self, body: dict, user: Optional[dict] = None) -> dict:
        # Modify the request body or validate it before processing by the chat completion API.
        # This function is the pre-processor for the API where various checks on the input can be performed.
        # It can also modify the request before sending it to the API.
        print(f"inlet:{__name__}")
        print(f"inlet:body:{body}")
        print(f"inlet:user:{user}")
        
        if user and user.get("role", "admin") in ["user", "admin"]:
            messages = body.get("messages", [])
            user_valves = user.get("valves", {})
            user_max_turns = user_valves.get("max_turns", self.valves.max_turns)
            max_turns = min(user_max_turns, self.valves.max_turns)
            
            if len(messages) > max_turns:
                raise Exception(
                    f"Conversation turn limit exceeded. Max turns: {max_turns}"
                )
        
        return body

    def outlet(self, body: dict, user: Optional[dict] = None) -> dict:
        # Modify or analyze the response body after processing by the API.
        # This function is the post-processor for the API, which can be used to modify the response
        # or perform additional checks and analytics.
        print(f"outlet:{__name__}")
        print(f"outlet:body:{body}")
        print(f"outlet:user:{user}")
        
        # Memory persistence logic
        if self.valves.mem0_enabled and self.valves.mem0_token:
            messages = body.get("messages", [])
            if messages:
                # Store the latest assistant response
                latest_message = messages[-1]
                if latest_message.get("role") == "assistant":
                    context = {
                        "message": latest_message.get("content", ""),
                        "role": latest_message.get("role", "assistant"),
                        "user_id": user.get("id") if user else None
                    }
                    result = self.memory_function.on_action(context, self.valves.mem0_token)
                    print(f"Memory storage result: {result}")
        
        return body


class MemoryFunction:
    @staticmethod
    def on_action(context: dict, api_token: str) -> str:
        """
        Persist conversational content to mem0.ai memory system.
        
        Args:
            context: Dictionary containing message content, role, and user_id
            api_token: mem0.ai API authentication token
            
        Returns:
            String indicating success or failure of memory storage operation
        """
        text = context.get("message", "")
        if not text:
            return "No message content to persist."
            
        url = "https://api.mem0.ai/v1/memories"
        payload = {
            "messages": [
                {
                    "role": context.get("role", "user"),
                    "content": text
                }
            ]
        }
        
        # Add user_id if available for personalized memory storage
        if context.get("user_id"):
            payload["user_id"] = context["user_id"]
            
        headers = {
            "Authorization": f"Token {api_token}",
            "Content-Type": "application/json"
        }
        
        try:
            resp = requests.post(url, json=payload, headers=headers, timeout=10)
            if resp.status_code in (200, 201):
                return "✅ Memory externalized successfully"
            else:
                return f"❌ Persistence failure: HTTP {resp.status_code} - {resp.text}"
        except requests.exceptions.RequestException as e:
            return f"❌ Network collapse: {str(e)}"
        except Exception as e:
            return f"❌ Unexpected error: {str(e)}"