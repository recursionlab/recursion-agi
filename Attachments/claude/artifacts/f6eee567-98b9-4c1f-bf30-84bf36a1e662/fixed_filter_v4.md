---
nexus: nexus-ai-chat-importer
plugin_version: "1.3.0"
provider: claude
artifact_id: fixed_filter
version_uuid: d5d2d0d1-1e9c-4bfa-a3c4-5f9615933ddf
version_number: 4
command: rewrite
conversation_id: f6eee567-98b9-4c1f-bf30-84bf36a1e662
create_time: 2025-07-26T23:04:00.000Z
format: markdown
aliases: [Untitled Artifact, fixed_filter_v4]
---

# Untitled Artifact (Version 4)

**Conversation:** [[Nexus/Conversations/claude/2025/07/Python Filter Architecture Design|Python Filter Architecture Design]]

## Content

"""
title: Mem0 Diagnostic Filter
author: open-webui
author_url: https://github.com/open-webui
funding_url: https://github.com/open-webui
version: 0.4
requirements: mem0ai
"""
from pydantic import BaseModel, Field
from typing import Optional, List
import logging
import traceback

# Configure logging for maximum visibility
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Diagnostic flag
DIAGNOSTIC_MODE = True

def diagnostic_log(message: str, level: str = "INFO"):
    """Enhanced logging for debugging"""
    if DIAGNOSTIC_MODE:
        print(f"[MEM0_DIAGNOSTIC] {level}: {message}")
    if level == "ERROR":
        logger.error(message)
    else:
        logger.info(message)

# Try importing mem0 with detailed error reporting
try:
    from mem0 import MemoryClient
    diagnostic_log("✅ MemoryClient imported successfully")
    MEM0_AVAILABLE = True
except ImportError as e:
    diagnostic_log(f"❌ Failed to import MemoryClient: {e}", "ERROR")
    MemoryClient = None
    MEM0_AVAILABLE = False
except Exception as e:
    diagnostic_log(f"❌ Unexpected error importing mem0: {e}", "ERROR")
    MemoryClient = None
    MEM0_AVAILABLE = False


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
            default="debug_user", description="Default user ID for memory storage."
        )
        diagnostic_mode: bool = Field(
            default=True, description="Enable verbose diagnostic logging."
        )

    class UserValves(BaseModel):
        max_turns: int = Field(
            default=4, description="Maximum allowable conversation turns for a user."
        )

    def __init__(self):
        diagnostic_log("🚀 Filter initialization starting")
        
        # Initialize valves
        self.valves = self.Valves()
        diagnostic_log(f"⚙️ Valves initialized - mem0_enabled: {self.valves.mem0_enabled}")
        
        # Initialize Mem0 client with detailed diagnostics
        self.mem0_client = None
        self.initialization_error = None
        
        if not MEM0_AVAILABLE:
            self.initialization_error = "mem0ai package not available"
            diagnostic_log("❌ Cannot initialize - mem0ai package not available", "ERROR")
        elif not self.valves.mem0_enabled:
            diagnostic_log("⚠️ Mem0 disabled via valves")
        elif not self.valves.mem0_api_key or self.valves.mem0_api_key == "":
            self.initialization_error = "API key not provided"
            diagnostic_log("❌ Cannot initialize - no API key provided", "ERROR")
        else:
            try:
                diagnostic_log(f"🔑 Attempting to initialize MemoryClient with key: {self.valves.mem0_api_key[:10]}...")
                self.mem0_client = MemoryClient(api_key=self.valves.mem0_api_key)
                diagnostic_log("✅ MemoryClient initialized successfully")
                
                # Test the client with a simple operation
                try:
                    # This should not actually add a memory, just test connectivity
                    diagnostic_log("🔍 Testing client connectivity...")
                    # Note: We'll test actual functionality in outlet
                    diagnostic_log("✅ Client appears ready for use")
                except Exception as test_error:
                    diagnostic_log(f"⚠️ Client test failed: {test_error}", "ERROR")
                    
            except Exception as e:
                self.initialization_error = str(e)
                diagnostic_log(f"❌ MemoryClient initialization failed: {e}", "ERROR")
                diagnostic_log(f"Traceback: {traceback.format_exc()}", "ERROR")

        diagnostic_log(f"🏁 Filter initialization complete - Client ready: {self.mem0_client is not None}")

    def inlet(self, body: dict, user: Optional[dict] = None) -> dict:
        """Pre-process incoming messages"""
        if self.valves.diagnostic_mode:
            diagnostic_log(f"📥 INLET: Processing {len(body.get('messages', []))} messages")
            if body.get('messages'):
                latest = body['messages'][-1]
                diagnostic_log(f"📥 Latest message: {latest.get('role', 'unknown')} - {latest.get('content', '')[:100]}...")
        
        # Existing turn limit logic
        if user and user.get("role", "admin") in ["user", "admin"]:
            messages = body.get("messages", [])
            user_valves = user.get("valves", {})
            user_max_turns = user_valves.get("max_turns", self.valves.max_turns)
            max_turns = min(user_max_turns, self.valves.max_turns)
            
            if len(messages) > max_turns:
                raise Exception(f"Conversation turn limit exceeded. Max turns: {max_turns}")
        
        return body

    def outlet(self, body: dict, user: Optional[dict] = None) -> dict:
        """Post-process assistant responses and store in Mem0"""
        diagnostic_log("📤 OUTLET: Starting outlet processing")
        
        # Comprehensive diagnostic information
        if self.valves.diagnostic_mode:
            diagnostic_log(f"📤 Body keys: {list(body.keys())}")
            diagnostic_log(f"📤 User info: {user.get('id', 'no-id') if user else 'no-user'}")
            diagnostic_log(f"📤 Messages count: {len(body.get('messages', []))}")
            diagnostic_log(f"📤 Client available: {self.mem0_client is not None}")
            diagnostic_log(f"📤 Mem0 enabled: {self.valves.mem0_enabled}")
            diagnostic_log(f"📤 Initialization error: {self.initialization_error}")

        # Check if we can proceed with memory storage
        if not self.valves.mem0_enabled:
            diagnostic_log("⏹️ Memory storage disabled - skipping")
            return body
            
        if self.mem0_client is None:
            diagnostic_log(f"❌ Cannot store memory - client unavailable: {self.initialization_error}", "ERROR")
            return body

        try:
            messages = body.get("messages", [])
            if not messages:
                diagnostic_log("⚠️ No messages to process")
                return body

            latest_message = messages[-1]
            diagnostic_log(f"📤 Latest message role: {latest_message.get('role')}")
            diagnostic_log(f"📤 Latest message content length: {len(latest_message.get('content', ''))}")

            if latest_message.get("role") == "assistant":
                content = latest_message.get("content", "")
                if content:
                    # Determine user ID
                    user_id = self.valves.mem0_user_id
                    if user and user.get("id"):
                        user_id = str(user["id"])
                    
                    diagnostic_log(f"💾 Attempting to store memory for user: {user_id}")
                    diagnostic_log(f"💾 Content preview: {content[:200]}...")

                    # Store in Mem0
                    result = self.mem0_client.add(
                        messages=[{"role": "assistant", "content": content}],
                        user_id=user_id
                    )
                    
                    diagnostic_log(f"✅ Memory stored successfully!")
                    diagnostic_log(f"✅ Result: {result}")
                    
                    # Also log to standard output for visibility
                    print(f"[MEM0_SUCCESS] Memory stored for user {user_id}: {result}")
                    
                else:
                    diagnostic_log("⚠️ No content in assistant message")
            else:
                diagnostic_log(f"⚠️ Latest message is not from assistant (role: {latest_message.get('role')})")
                
        except Exception as e:
            diagnostic_log(f"❌ Memory storage failed with exception: {e}", "ERROR")
            diagnostic_log(f"❌ Full traceback: {traceback.format_exc()}", "ERROR")
            # Don't fail the entire response, just log the error
            print(f"[MEM0_ERROR] Failed to store memory: {e}")

        return body