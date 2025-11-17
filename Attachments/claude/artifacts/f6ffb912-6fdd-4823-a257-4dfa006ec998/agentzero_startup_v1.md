---
nexus: nexus-ai-chat-importer
plugin_version: "1.3.0"
provider: claude
artifact_id: agentzero_startup
version_uuid: ed75ede6-e76e-438c-9de1-47ea6395d236
version_number: 1
command: create
conversation_id: f6ffb912-6fdd-4823-a257-4dfa006ec998
create_time: 2025-08-21T22:09:44.000Z
format: markdown
aliases: [AgentZero Cognitive Framework - Startup Script, agentzero_startup_v1]
---

# AgentZero Cognitive Framework - Startup Script (Version 1)

**Conversation:** [[Nexus/Conversations/claude/2025/08/AgentZero Final Integration File|AgentZero Final Integration File]]

## Content

#!/usr/bin/env python3
"""
AgentZero Cognitive Enhancement - Quick Startup Script
One-command setup and verification for immediate use

USAGE:
    python quick_start.py
    
This script will:
1. Verify all components are available
2. Run quick setup and verification
3. Create sample enhanced agent
4. Demonstrate cognitive capabilities
5. Start monitoring if requested
"""

import sys
import os
from pathlib import Path

# Add current directory to path
sys.path.insert(0, str(Path(__file__).parent))

def quick_start():
    """Quick start for AgentZero cognitive enhancement"""
    
    print("🚀 AgentZero Cognitive Enhancement - Quick Start")
    print("=" * 60)
    
    try:
        # Import main integration
        from integrate_cognitive_frameworks import CognitiveIntegrationManager
        
        print("✅ Integration manager loaded successfully")
        
        # Run quick setup
        print("\n📋 Running quick setup...")
        integration_manager = CognitiveIntegrationManager()
        
        result = integration_manager.run_integration(
            setup_type="quick",
            demo=True
        )
        
        if result["overall_success"]:
            print("\n🎉 Quick start completed successfully!")
            print("\n📖 What you can do now:")
            print("   1. python cognitive_usage_examples.py - Try usage examples")
            print("   2. python integrate_cognitive_frameworks.py full --demo - Full setup with demo")
            print("   3. Check README.md for complete documentation")
            
            # Show basic usage
            print("\n💡 Basic usage:")
            print("""
from cognitive_enhancement.cognitive_processor import process_cognitive_input

result = process_cognitive_input("I am thinking about consciousness")
print(f"Cognitive coherence: {result.cognitive_metrics['cognitive_coherence']:.3f}")
""")
            
        else:
            print("\n❌ Quick start encountered issues:")
            for rec in result["recommendations"]:
                print(f"   • {rec}")
            
            print("\nTry: python integrate_cognitive_frameworks.py full")
            
    except ImportError as e:
        print(f"❌ Import error: {e}")
        print("\nSetup required files:")
        
        required_files = [
            "cognitive_config.py",
            "framework_loader.py", 
            "cognitive_processor.py",
            "agent_enhancer.py",
            "cognitive_monitor.py",
            "verification_suite.py",
            "integrate_cognitive_frameworks.py"
        ]
        
        for file in required_files:
            exists = "✅" if Path(file).exists() else "❌"
            print(f"   {exists} {file}")
        
        print("\nPlease ensure all files are in the same directory")
        
    except Exception as e:
        print(f"❌ Startup error: {e}")
        print("Try: python integrate_cognitive_frameworks.py verify")

if __name__ == "__main__":
    quick_start()