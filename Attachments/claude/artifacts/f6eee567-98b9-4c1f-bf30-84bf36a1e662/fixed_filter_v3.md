---
nexus: nexus-ai-chat-importer
plugin_version: "1.3.0"
provider: claude
artifact_id: fixed_filter
version_uuid: c1b07af4-0cef-46f0-9b70-e9b2794d7dba
version_number: 3
command: rewrite
conversation_id: f6eee567-98b9-4c1f-bf30-84bf36a1e662
create_time: 2025-07-26T22:58:31.000Z
format: markdown
aliases: [Untitled Artifact, fixed_filter_v3]
---

# Untitled Artifact (Version 3)

**Conversation:** [[Nexus/Conversations/claude/2025/07/Python Filter Architecture Design|Python Filter Architecture Design]]

## Content

"""
title: Mem0 Memory Filter Pipeline
author: open-webui
author_url: https://github.com/open-webui
funding_url: https://github.com/open-webui
version: 0.3
requirements: mem0ai
"""
from pydantic import BaseModel, Field
from typing import Optional, List
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

try:
    from mem0 import MemoryClient
except ImportError:
    logger.error("mem0ai package not installed. Run: pip install mem0ai")
    MemoryClient = None


class Filter:
    class Valves(BaseModel):
        priority: int = Field(
            default=0, description="Priority level for the filter operations."
        )
        max_turns: int = Field(
            default=8, description="Maximum allowable conversation turns for a user."
        )
        mem0_api_key: str = Field(
            default="m0-XF9slYnC0YuK8184W3Ad83cv9Eyp9tnSR73m6Y3o", 
            description="Mem0 API key for memory persistence."
        )
        mem0_enabled: bool = Field(
            default=True, description="Enable Mem0 memory storage."
        )
        mem0_user_id: str = Field(
            default="default_user", description="Default user ID for memory storage."
        )

    class UserValves(BaseModel):
        max_turns: int = Field(
            default=4, description="Maximum allowable conversation turns for a user."
        )

    def __init__(self):
        # Initialize valves with specific configurations
        self.valves = self.Valves()
        
        # Initialize Mem0 client if available
        self.mem0_client = None
        if MemoryClient and self.valves.mem0_enabled and self.valves.mem0_api_key:
            try:
                self.mem0_client = MemoryClient(api_key=self.valves.mem0_api_key)
                logger.info("Mem0 client initialized successfully")
            except Exception as e:
                logger.error(f"Failed to initialize Mem0 client: {e}")

    def inlet(self, body: dict, user: Optional[dict] = None) -> dict:
        """
        Pre-process incoming messages before they reach the LLM.
        Validates conversation turn limits.
        """
        logger.info(f"Inlet processing: {body.get('messages', [])[-1:] if body.get('messages') else 'No messages'}")
        
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
        """
        Post-process assistant responses and store them in Mem0.
        """
        logger.info("Outlet processing: storing assistant response in memory")
        
        # Store assistant response in Mem0 if enabled
        if self.valves.mem0_enabled and self.mem0_client:
            try:
                messages = body.get("messages", [])
                if messages:
                    latest_message = messages[-1]
                    if latest_message.get("role") == "assistant":
                        content = latest_message.get("content", "")
                        if content:
                            # Determine user ID
                            user_id = self.valves.mem0_user_id
                            if user and user.get("id"):
                                user_id = str(user["id"])
                            
                            # Store in Mem0
                            result = self.mem0_client.add(
                                messages=[{"role": "assistant", "content": content}],
                                user_id=user_id
                            )
                            logger.info(f"✅ Memory stored successfully: {result}")
                        else:
                            logger.warning("No content to store in memory")
            except Exception as e:
                logger.error(f"❌ Memory storage failed: {e}")
        else:
            if not self.valves.mem0_enabled:
                logger.info("Mem0 storage is disabled")
            elif not self.mem0_client:
                logger.warning("Mem0 client not available")
        
        return body


class MemoryFunction:
    """
    Legacy function class - now replaced by direct Mem0 client integration
    """
    @staticmethod
    def on_action(context: dict, api_key: str) -> str:
        """
        Deprecated: Use Mem0 client directly instead of raw API calls
        """
        return "⚠️ This function is deprecated. Use Mem0 client integration instead."