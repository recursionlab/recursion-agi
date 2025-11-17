---
nexus: nexus-ai-chat-importer
plugin_version: "1.3.0"
provider: claude
aliases: Uninstalling VS Code
conversation_id: b4c6ba4b-b27a-46ab-87c3-c522c7d6dfbc
create_time: 2025-08-17T15:22:16.000Z
update_time: 2025-08-17T15:22:34.000Z
---

# Title: Uninstalling VS Code

Created: 08/17/2025 at 10:22:16 AM
Last Updated: 08/17/2025 at 10:22:34 AM
Chat URL: https://claude.ai/chat/b4c6ba4b-b27a-46ab-87c3-c522c7d6dfbc


>[!nexus_user] **User** - 08/17/2025 at 10:22:17 AM
> Can you use your MCPs to help me find and delete VS Code, i need to reinstall it, i have an installer in D: downloads folder
<!-- UID: b71929d9-0b25-48ed-8287-355f9937ddb8 -->
>[!nexus_agent] **Assistant** - 08/17/2025 at 10:22:25 AM
>  I don't have access to Model Context Protocols (MCPs) or any tools that can interact with your local file system, run commands, or manage software installations on your computer. I can only use web search, create artifacts (like code or documents), and run JavaScript analysis - none of which can help with uninstalling or managing software on your machine.
> 
> However, I can guide you through the process of uninstalling and reinstalling VS Code:
> 
> **To uninstall VS Code:**
> 
> 1. **Windows Settings method:**
>    - Go to Settings > Apps > Apps & features
>    - Search for "Visual Studio Code"
>    - Click on it and select "Uninstall"
> 
> 2. **Control Panel method:**
>    - Open Control Panel > Programs and Features
>    - Find "Microsoft Visual Studio Code"
>    - Right-click and select "Uninstall"
> 
> 3. **Command line method:**
>    - Open Command Prompt as administrator
>    - Run: `wmic product where name="Microsoft Visual Studio Code" call uninstall`
> 
> **After uninstalling:**
> - You may want to delete the VS Code user data folder if you want a completely clean install:
>   - `%APPDATA%\Code` (settings, extensions, etc.)
>   - `%USERPROFILE%\.vscode` (extensions folder)
> 
> **To reinstall:**
> - Navigate to your D:\downloads folder and run the VS Code installer you
<!-- UID: 983cdf00-3c12-4372-9158-27cf3d12aba7 -->

---
>[!nexus_user] **User** - 08/17/2025 at 10:22:34 AM
> You are on the client with MCP access, i swear to you
<!-- UID: 5b090929-7fb6-4ee4-9658-ea35ca8b0b0c -->