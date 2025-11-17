---
nexus: nexus-ai-chat-importer
plugin_version: "1.3.0"
provider: claude
artifact_id: setup_agi_system
version_uuid: d2814065-d4a6-48aa-9561-f67ce585db3b
version_number: 1
command: create
conversation_id: f482712b-8040-48e1-939f-11149f468b09
create_time: 2025-08-20T19:09:51.000Z
format: markdown
aliases: [setup_agi_system.py, setup_agi_system_v1]
---

# setup_agi_system.py (Version 1)

**Conversation:** [[Nexus/Conversations/claude/2025/08/LeanRAG System Architecture Challenge|LeanRAG System Architecture Challenge]]

## Content

#!/usr/bin/env python3
"""
Setup script for AGI Meta-Pattern Analysis System
Creates directory structure and installs dependencies
"""

import os
import sys
import subprocess
import json
from pathlib import Path

def run_command(command, check=True):
    """Run shell command and return result"""
    print(f"Running: {command}")
    result = subprocess.run(command, shell=True, check=check, capture_output=True, text=True)
    if result.stdout:
        print(result.stdout)
    if result.stderr:
        print(result.stderr)
    return result

def setup_directories():
    """Create necessary directory structure"""
    
    directories = [
        "D:/LeanRAG",
        "D:/LeanRAG/data",
        "D:/LeanRAG/models",
        "D:/LeanRAG/logs",
        "D:/LeanRAG/exports",
        "D:/CognitiveLabs",  # May already exist
        "D:/Aider"  # May already exist
    ]
    
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
        print(f"Created directory: {directory}")

def install_requirements():
    """Install Python requirements"""
    
    requirements = [
        "numpy>=1.24.0",
        "scikit-learn>=1.3.0",
        "sentence-transformers>=2.2.0",
        "networkx>=3.0",
        "transformers>=4.20.0",
        "torch>=1.13.0",
        "pandas>=1.5.0",
        "regex>=2022.0.0",
        "aiofiles>=22.0.0",
        "fastapi>=0.95.0",
        "uvicorn>=0.20.0",
        "click>=8.0.0",
        "rich>=13.0.0"
    ]
    
    print("Installing Python requirements...")
    
    for req in requirements:
        try:
            run_command(f"pip install \"{req}\"")
        except subprocess.CalledProcessError as e:
            print(f"Warning: Failed to install {req}: {e}")

def create_config():
    """Create configuration file"""
    
    config = {
        "paths": {
            "cognitive_labs": "D:/CognitiveLabs",
            "leanrag": "D:/LeanRAG", 
            "aider": "D:/Aider",
            "conversations": None  # Will be auto-detected
        },
        "embedding_model": "all-MiniLM-L6-v2",
        "leanrag_config": {
            "cluster_size": 20,
            "max_hierarchy_layers": 3,
            "top_n_retrieval": 10,
            "similarity_threshold": 0.3
        },
        "processgod_config": {
            "max_recursive_depth": 5,
            "void_absorption_capacity": 1000,
            "meta_analysis_depth": 3
        },
        "database": {
            "path": "D:/LeanRAG/agi_meta_system.db",
            "backup_interval": 3600
        },
        "logging": {
            "level": "INFO",
            "file": "D:/LeanRAG/logs/agi_system.log"
        }
    }
    
    config_path = Path("D:/LeanRAG/config.json")
    with open(config_path, 'w') as f:
        json.dump(config, f, indent=2)
    
    print(f"Created config file: {config_path}")

def create_launcher_script():
    """Create launcher script for easy execution"""
    
    launcher_content = '''#!/usr/bin/env python3
"""
AGI Meta-Pattern Analysis System Launcher
"""

import sys
import json
from pathlib import Path

# Add LeanRAG to Python path
sys.path.insert(0, str(Path(__file__).parent))

try:
    from agi_meta_system import AGIMetaSystem, main
    
    if __name__ == "__main__":
        main()
        
except ImportError as e:
    print(f"Error importing AGI system: {e}")
    print("Make sure all requirements are installed:")
    print("pip install -r requirements.txt")
    sys.exit(1)
except Exception as e:
    print(f"Error running AGI system: {e}")
    sys.exit(1)
'''
    
    launcher_path = Path("D:/LeanRAG/launch_agi.py")
    with open(launcher_path, 'w') as f:
        f.write(launcher_content)
    
    print(f"Created launcher script: {launcher_path}")

def create_aider_integration():
    """Create Aider integration script"""
    
    aider_integration = '''#!/usr/bin/env python3
"""
Aider Integration for AGI Meta-Pattern Analysis System
"""

import json
import sys
from pathlib import Path
from agi_meta_system import AGIMetaSystem

class AiderAGIInterface:
    """Interface between Aider and AGI Meta-Pattern Analysis System"""
    
    def __init__(self):
        self.agi_system = AGIMetaSystem()
    
    def query_knowledge(self, query: str) -> str:
        """Query the AGI system and return formatted response for Aider"""
        
        result = self.agi_system.query(query, max_meta_depth=2)
        
        response = f"""
AGI Meta-Analysis for: {query}

Retrieved {result['retrieved_entities_count']} entities and {result['retrieved_relations_count']} relations
Hierarchy depth: {result['hierarchy_layers']} layers
Patterns detected: {result['patterns_detected']}

Key Entities:
"""
        
        for entity in result['retrieved_entities'][:5]:
            response += f"- {entity['name']}: {entity['description'][:100]}...\\n"
        
        response += f"""
Topology: {result['topology_name']}
System State: {result['system_state']['void_state']}
"""
        
        return response
    
    def get_relevant_context(self, file_path: str, query: str) -> str:
        """Get relevant context for a specific file being edited"""
        
        # Enhanced query with file context
        enhanced_query = f"Context for {file_path}: {query}"
        return self.query_knowledge(enhanced_query)

def aider_query(query: str):
    """Command-line interface for Aider queries"""
    
    interface = AiderAGIInterface()
    result = interface.query_knowledge(query)
    print(result)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        query = " ".join(sys.argv[1:])
        aider_query(query)
    else:
        print("Usage: python aider_agi.py <query>")
'''
    
    aider_path = Path("D:/LeanRAG/aider_agi.py")
    with open(aider_path, 'w') as f:
        f.write(aider_integration)
    
    print(f"Created Aider integration: {aider_path}")

def find_conversations_json():
    """Find conversations.json in common locations"""
    
    search_paths = [
        "D:/conversations.json",
        "D:/CognitiveLabs/conversations.json", 
        "D:/Downloads/conversations.json",
        Path.home() / "Downloads/conversations.json",
        Path.home() / "conversations.json"
    ]
    
    for path in search_paths:
        if Path(path).exists():
            print(f"Found conversations.json at: {path}")
            return str(path)
    
    print("conversations.json not found. You can:")
    print("1. Export conversations from Claude and place in D:/conversations.json")
    print("2. Update config.json with the correct path")
    return None

def create_batch_scripts():
    """Create Windows batch scripts for easy execution"""
    
    # Main launcher batch
    launcher_batch = '''@echo off
cd /d D:\\LeanRAG
python launch_agi.py
pause
'''
    
    with open("D:/LeanRAG/run_agi.bat", 'w') as f:
        f.write(launcher_batch)
    
    # Aider integration batch
    aider_batch = '''@echo off
cd /d D:\\LeanRAG
python aider_agi.py %*
'''
    
    with open("D:/LeanRAG/aider_query.bat", 'w') as f:
        f.write(aider_batch)
    
    print("Created batch scripts: run_agi.bat, aider_query.bat")

def main():
    """Main setup function"""
    
    print("Setting up AGI Meta-Pattern Analysis System...")
    print("="*60)
    
    # Create directories
    setup_directories()
    
    # Install requirements
    install_requirements()
    
    # Create configuration
    create_config()
    
    # Create launcher and integration scripts
    create_launcher_script()
    create_aider_integration()
    create_batch_scripts()
    
    # Find conversations.json
    conversations_path = find_conversations_json()
    
    # Update config with conversations path if found
    if conversations_path:
        config_path = Path("D:/LeanRAG/config.json")
        with open(config_path, 'r') as f:
            config = json.load(f)
        
        config['paths']['conversations'] = conversations_path
        
        with open(config_path, 'w') as f:
            json.dump(config, f, indent=2)
        
        print(f"Updated config with conversations path: {conversations_path}")
    
    print("="*60)
    print("Setup complete!")
    print("")
    print("To run the AGI system:")
    print("1. Double-click D:/LeanRAG/run_agi.bat")
    print("2. Or run: python D:/LeanRAG/launch_agi.py")
    print("")
    print("For Aider integration:")
    print("D:/LeanRAG/aider_query.bat \"your query here\"")
    print("")
    print("Configuration file: D:/LeanRAG/config.json")

if __name__ == "__main__":
    main()
