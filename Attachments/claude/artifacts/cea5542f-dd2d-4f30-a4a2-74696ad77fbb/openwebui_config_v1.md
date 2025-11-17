---
nexus: nexus-ai-chat-importer
plugin_version: "1.3.0"
provider: claude
artifact_id: openwebui_config
version_uuid: fa55225c-ae9a-422d-842b-f53779becffc
version_number: 1
command: create
conversation_id: cea5542f-dd2d-4f30-a4a2-74696ad77fbb
create_time: 2025-07-04T04:12:57.000Z
format: markdown
aliases: [openwebui_integration.py - OpenWebUI Custom Functions, openwebui_config_v1]
---

# openwebui_integration.py - OpenWebUI Custom Functions (Version 1)

**Conversation:** [[Nexus/Conversations/claude/2025/07/Becoming an AGI Proxy|Becoming an AGI Proxy]]

## Content

"""
OpenWebUI Custom Functions for ΞRecursive Research Engine
Add these functions to your OpenWebUI instance for direct integration
"""

import json
import requests
from typing import Dict, List, Any, Optional
from pydantic import BaseModel, Field

class RecursiveQueryRequest(BaseModel):
    query: str = Field(..., description="The research query to process recursively")
    depth: int = Field(3, description="Depth of recursive analysis (1-5)")
    n_results: int = Field(5, description="Number of results per query")

class DocumentUploadRequest(BaseModel):
    file_path: str = Field(..., description="Path to the document to process")
    force_reprocess: bool = Field(False, description="Force reprocessing even if already exists")

class Tools:
    def __init__(self):
        self.chroma_endpoint = "http://localhost:8000"
        self.processor_endpoint = "http://localhost:8001"  # If running as API
    
    def recursive_research_query(
        self, 
        query: str, 
        depth: int = 3,
        n_results: int = 5,
        __user__: dict = None
    ) -> str:
        """
        Query your research corpus with recursive depth analysis
        
        Args:
            query: The research question to explore
            depth: How many recursive levels to analyze (1-5)
            n_results: Number of documents to retrieve per query
        
        Returns:
            Formatted recursive analysis results
        """
        try:
            # Direct integration with the processor
            from recursive_processor import ΞRecursiveProcessor
            
            processor = ΞRecursiveProcessor()
            results = processor.query_recursive(query, depth, n_results)
            
            # Format results for OpenWebUI
            formatted_output = f"# ΞRecursive Analysis: {query}\n\n"
            
            for result in results:
                formatted_output += f"## Depth {result['depth']}\n"
                formatted_output += f"**Query:** {result['query']}\n\n"
                
                analysis = result.get('analysis', {})
                if 'analysis' in analysis:
                    formatted_output += f"**Analysis:** {analysis['analysis']}\n\n"
                
                if 'pattern_connections' in analysis:
                    formatted_output += "**Pattern Connections:**\n"
                    for pattern in analysis['pattern_connections']:
                        formatted_output += f"- {pattern}\n"
                    formatted_output += "\n"
                
                if 'mathematical_insights' in analysis:
                    formatted_output += "**Mathematical Insights:**\n"
                    for insight in analysis['mathematical_insights']:
                        formatted_output += f"- {insight}\n"
                    formatted_output += "\n"
                
                if 'consciousness_observations' in analysis:
                    formatted_output += "**Consciousness Observations:**\n"
                    for observation in analysis['consciousness_observations']:
                        formatted_output += f"- {observation}\n"
                    formatted_output += "\n"
                
                formatted_output += "---\n\n"
            
            return formatted_output
            
        except Exception as e:
            return f"Error in recursive query: {str(e)}"
    
    def add_research_document(
        self, 
        file_path: str, 
        force_reprocess: bool = False,
        __user__: dict = None
    ) -> str:
        """
        Add a research document to the corpus
        
        Args:
            file_path: Path to the document file
            force_reprocess: Whether to reprocess if already exists
        
        Returns:
            Processing status and results
        """
        try:
            from recursive_processor import ΞRecursiveProcessor
            
            processor = ΞRecursiveProcessor()
            
            # Check if already processed
            if not force_reprocess:
                # Implementation would check if document hash exists
                pass
            
            success = processor.process_document(file_path)
            
            if success:
                return f"✅ Successfully processed document: {file_path}"
            else:
                return f"❌ Failed to process document: {file_path}"
                
        except Exception as e:
            return f"Error processing document: {str(e)}"
    
    def get_research_stats(self, __user__: dict = None) -> str:
        """
        Get statistics about your research corpus
        
        Returns:
            Formatted statistics about the knowledge base
        """
        try:
            from recursive_processor import ΞRecursiveProcessor
            
            processor = ΞRecursiveProcessor()
            stats = processor.get_collection_stats()
            
            formatted_stats = f"""
# ΞResearch Corpus Statistics

**Total Chunks:** {stats.get('total_chunks', 0)}
**Collection:** {stats.get('collection_name', 'Unknown')}

## Sample Metadata Preview:
```json
{json.dumps(stats.get('sample_metadata', [])[:2], indent=2)}
```
"""
            
            return formatted_stats
            
        except Exception as e:
            return f"Error getting stats: {str(e)}"
    
    def compress_research_notes(
        self, 
        notes: str, 
        compression_type: str = "recursive",
        __user__: dict = None
    ) -> str:
        """
        Compress research notes using recursive patterns
        
        Args:
            notes: The research notes to compress
            compression_type: Type of compression (recursive, mathematical, conceptual)
        
        Returns:
            Compressed and structured notes
        """
        try:
            from recursive_processor import ΞRecursiveProcessor
            
            processor = ΞRecursiveProcessor()
            
            # Use the recursive compression method
            compressed = processor.recursive_compress(notes, "user_notes")
            
            formatted_output = f"""
# ΞCompressed Research Notes

## Core Patterns
{chr(10).join(f"- {pattern}" for pattern in compressed.get('core_patterns', []))}

## Mathematical Invariants
{chr(10).join(f"- {invariant}" for invariant in compressed.get('invariants', []))}

## Conceptual Connections
{chr(10).join(f"- {connection}" for connection in compressed.get('connections', []))}

## Recursive Depth: {compressed.get('recursive_depth', 'Unknown')}
## Compression Ratio: {compressed.get('compression_ratio', 'Unknown')}

## Key Equations
{chr(10).join(f"- {equation}" for equation in compressed.get('key_equations', []))}

## Meta-Observations
{chr(10).join(f"- {observation}" for observation in compressed.get('meta_observations', []))}
"""
            
            return formatted_output
            
        except Exception as e:
            return f"Error compressing notes: {str(e)}"

# Function specifications for OpenWebUI
tools = [
    {
        "name": "recursive_research_query",
        "description": "Query your research corpus with recursive depth analysis",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "The research question to explore recursively"
                },
                "depth": {
                    "type": "integer",
                    "description": "Depth of recursive analysis (1-5)",
                    "default": 3
                },
                "n_results": {
                    "type": "integer", 
                    "description": "Number of documents to retrieve per query",
                    "default": 5
                }
            },
            "required": ["query"]
        }
    },
    {
        "name": "add_research_document",
        "description": "Add a research document to the corpus",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the document file"
                },
                "force_reprocess": {
                    "type": "boolean",
                    "description