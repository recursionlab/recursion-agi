---
nexus: nexus-ai-chat-importer
plugin_version: "1.3.0"
provider: claude
artifact_id: mcp_weather_debug
version_uuid: 6b157cb2-6243-4ee5-9613-a47dbe74d5a2
version_number: 1
command: create
conversation_id: 1887284d-2df4-41da-8157-4c3a883caf34
create_time: 2025-07-10T05:23:43.000Z
format: markdown
aliases: [MCP Weather Server Debug Guide, mcp_weather_debug_v1]
---

# MCP Weather Server Debug Guide (Version 1)

**Conversation:** [[Nexus/Conversations/claude/2025/07/Claude Desktop Interface Access|Claude Desktop Interface Access]]

## Content

# MCP Weather Server Debug Guide

## Common Disconnection Triggers

### 1. **Protocol Initialization Failures**
```python
# Check if your weather.py has proper MCP protocol setup
import asyncio
from mcp.server import Server
from mcp.types import Tool, TextContent

# Common failure: Missing or incorrect server initialization
server = Server("weather-server")

# Debug point: Ensure server name matches MCP config
@server.list_tools()
async def list_tools():
    return [
        Tool(
            name="get_weather",
            description="Get current weather for a location",
            inputSchema={
                "type": "object",
                "properties": {
                    "location": {"type": "string"}
                },
                "required": ["location"]
            }
        )
    ]
```

### 2. **Dependency Resolution Issues**
Check if these dependencies are properly installed:
```bash
# Run these in your mcp-obsidian directory
uv pip list | grep -E "(mcp|requests|aiohttp)"
```

Required packages for weather MCP:
- `mcp` - Core MCP protocol implementation
- `requests` or `aiohttp` - HTTP client for weather API calls
- `pydantic` - Data validation (often required)

### 3. **Runtime Exception Patterns**

#### **API Key Configuration**
```python
# Common failure: Missing or invalid API keys
import os
from typing import Optional

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
if not WEATHER_API_KEY:
    raise ValueError("WEATHER_API_KEY environment variable not set")
```

#### **Network Connection Failures**
```python
# Add proper error handling for weather API calls
import aiohttp
import asyncio

async def get_weather_data(location: str) -> dict:
    try:
        async with aiohttp.ClientSession() as session:
            # OpenWeatherMap example
            url = f"https://api.openweathermap.org/data/2.5/weather"
            params = {
                "q": location,
                "appid": WEATHER_API_KEY,
                "units": "metric"
            }
            async with session.get(url, params=params) as response:
                if response.status != 200:
                    raise Exception(f"Weather API error: {response.status}")
                return await response.json()
    except Exception as e:
        # Log the error instead of crashing
        print(f"Weather API error: {e}")
        return {"error": str(e)}
```

### 4. **Server Main Loop Issues**
```python
# Ensure proper async main function
async def main():
    # Setup server
    server = Server("weather-server")
    
    # Register tools
    @server.call_tool()
    async def call_tool(name: str, arguments: dict):
        if name == "get_weather":
            location = arguments.get("location", "")
            if not location:
                return TextContent(type="text", text="Location is required")
            
            weather_data = await get_weather_data(location)
            return TextContent(
                type="text", 
                text=f"Weather for {location}: {weather_data}"
            )
    
    # Critical: Proper stdio transport setup
    from mcp.server.stdio import stdio_server
    async with stdio_server() as streams:
        await server.run(
            streams[0], streams[1], 
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

## Debugging Steps

### Step 1: **Check Script Execution**
```bash
# Test the script directly outside MCP
cd D:/Hub/mcp-obsidian/src
python weather.py
```

### Step 2: **Verify UV Environment**
```bash
# Check if uv is properly managing dependencies
uv pip list
uv pip show mcp
```

### Step 3: **Enable Debug Logging**
Add to your weather.py:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

### Step 4: **Test MCP Protocol Handshake**
```python
# Add at the start of your main() function
import sys
print("Starting weather MCP server...", file=sys.stderr)

# Add before server.run()
print("Initializing MCP protocol...", file=sys.stderr)
```

### Step 5: **Check Environment Variables**
```python
# Add environment diagnostics
import os
print(f"Working directory: {os.getcwd()}", file=sys.stderr)
print(f"Python path: {sys.path}", file=sys.stderr)
print(f"Environment: {list(os.environ.keys())}", file=sys.stderr)
```

## Common Fix Patterns

### **Pattern 1: Missing Dependencies**
```bash
cd D:/Hub/mcp-obsidian/src
uv add mcp requests python-dotenv
```

### **Pattern 2: Async/Await Issues**
```python
# Ensure all I/O operations are properly awaited
async def get_weather(location):
    # Wrong: requests.get() - blocking
    # Right: aiohttp async call
    pass
```

### **Pattern 3: Protocol Compliance**
```python
# Ensure tool responses match MCP specification
from mcp.types import TextContent, ImageContent

# Always return proper MCP content types
return TextContent(type="text", text="Weather data...")
```

### **Pattern 4: Error Propagation**
```python
# Don't let exceptions crash the server
try:
    weather_data = await get_weather_data(location)
    return TextContent(type="text", text=str(weather_data))
except Exception as e:
    # Return error as content, don't crash
    return TextContent(type="text", text=f"Error: {str(e)}")
```

## Verification Commands

```bash
# 1. Check if script runs standalone
python weather.py

# 2. Test with explicit uv environment
uv run python weather.py

# 3. Check MCP protocol communication
echo '{"jsonrpc": "2.0", "method": "initialize", "params": {}, "id": 1}' | python weather.py

# 4. Verify dependencies
uv pip show mcp
uv pip show requests
```

## Next Steps

1. **Share your weather.py code** - I'll analyze the specific implementation
2. **Run the verification commands** above and share the output
3. **Check the MCP configuration** in Claude desktop for any parameter mismatches
4. **Test environment variables** - many weather APIs require API keys

The **"Server disconnected"** error typically indicates the Python process is terminating unexpectedly during the MCP handshake or initial tool registration phase.