---
nexus: nexus-ai-chat-importer
plugin_version: "1.3.0"
provider: claude
aliases: OODA Subagents Local Model Integration
conversation_id: e64e515d-b7d9-4b14-a687-67c022c18e52
create_time: 2025-07-26T21:00:40.000Z
update_time: 2025-07-26T21:01:34.000Z
---

# Title: OODA Subagents Local Model Integration

Created: 07/26/2025 at 4:00:40 PM
Last Updated: 07/26/2025 at 4:01:34 PM
Chat URL: https://claude.ai/chat/e64e515d-b7d9-4b14-a687-67c022c18e52


>[!nexus_user] **User** - 07/26/2025 at 4:00:40 PM
> https://github.com/al3rez/ooda-subagents
> 
> Can I get this going with a local model on open web ui
<!-- UID: d8c1b9b3-8836-4520-9607-349db76cad2e -->
>[!nexus_agent] **Assistant** - 07/26/2025 at 4:01:33 PM
>  I'll fetch the repository to understand what you're working with and then help you set it up with a local model on Open WebUI.
> 
> **[Tool: web_fetch]**
> ```
> {
>   "url": "https://github.com/al3rez/ooda-subagents"
> }
> ```
> 
> Let me get more detailed information about the repository structure and implementation:
> 
> **[Tool: web_fetch]**
> ```
> {
>   "url": "https://github.com/al3rez/ooda-subagents/tree/main"
> }
> ```
> 
> Let me search for more information about this OODA subagents project to understand its structure:
> 
> Based on what I can see from the repository, this appears to be a collection of Claude agents that implement the OODA loop (Observe, Orient, Decide, Act) framework for systematic problem-solving. The project seems designed to work with Claude's agent system, but I can help you adapt it to work with Open WebUI and local models.
> 
> Here's how you can get this working with a local model on Open WebUI:
> 
> ## Adapting OODA Agents for Open WebUI
> 
> Since the original project appears to be designed for Claude's agent system, you'll need to adapt the approach for Open WebUI. Here's a practical implementation:
> 
> >[!nexus_artifact] **OODA Loop Agents for Open WebUI Setup Guide** v1
> > 🎨 [[Nexus/Attachments/claude/artifacts/e64e515d-b7d9-4b14-a687-67c022c18e52/ooda_openwebui_guide_v1|View Artifact]]
> 
> ## Key Steps to Get Started:
> 
> 1. **Clone the original repo** to see the agent structures:
>    ```bash
>    git clone https://github.com/al3rez/ooda-subagents.git
>    ```
> 
> 2. **Adapt for Open WebUI** by:
>    - Converting Claude agent prompts to Open WebUI custom functions
>    - Creating structured prompt templates for each OODA stage
>    - Setting up multi-step workflows
> 
> 3. **Configure your local model** with appropriate parameters for structured reasoning (temperature ~0.5, sufficient context length)
> 
> The main adaptation needed is converting from Claude's agent system to Open WebUI's function/workflow system, but the core OODA methodology (Observe → Orient → Decide → Act) remains the same and works excellently with local models.
> 
> Would you like me to help you implement any specific part of this setup, or do you have questions about adapting particular agents from the original repository?
<!-- UID: 3aeecefe-7ddc-4ed9-8afd-0e8dc567e016 -->

---