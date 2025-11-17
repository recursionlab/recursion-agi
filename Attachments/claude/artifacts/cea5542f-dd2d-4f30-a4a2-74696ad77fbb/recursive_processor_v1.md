---
nexus: nexus-ai-chat-importer
plugin_version: "1.3.0"
provider: claude
artifact_id: recursive_processor
version_uuid: de9387db-54cc-4dde-8f5f-7f1c520f727c
version_number: 1
command: create
conversation_id: cea5542f-dd2d-4f30-a4a2-74696ad77fbb
create_time: 2025-07-04T04:12:57.000Z
format: markdown
aliases: [recursive_processor.py - Main Document Processing Engine, recursive_processor_v1]
---

# recursive_processor.py - Main Document Processing Engine (Version 1)

**Conversation:** [[Nexus/Conversations/claude/2025/07/Becoming an AGI Proxy|Becoming an AGI Proxy]]

## Content

import chromadb
import ollama
import os
import json
import hashlib
from typing import List, Dict, Any, Optional
from pathlib import Path
import PyPDF2
import docx2txt
from langchain.text_splitter import RecursiveCharacterTextSplitter
from tqdm import tqdm
import numpy as np
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ΞRecursiveProcessor:
    """
    Recursive Knowledge Processing Engine
    Implements semantic compression and recursive pattern extraction
    """
    
    def __init__(self, chroma_host="localhost", chroma_port=8000, model_name="qwen2.5:14b"):
        self.chroma_client = chromadb.HttpClient(host=chroma_host, port=chroma_port)
        self.model_name = model_name
        self.collection_name = "research_corpus"
        
        # Initialize or get collection
        try:
            self.collection = self.chroma_client.get_collection(self.collection_name)
            logger.info(f"Connected to existing collection: {self.collection_name}")
        except:
            self.collection = self.chroma_client.create_collection(
                name=self.collection_name,
                metadata={"description": "Recursive research corpus with semantic compression"}
            )
            logger.info(f"Created new collection: {self.collection_name}")
        
        # Text splitter for chunking
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len,
            separators=["\n\n", "\n", ".", "!", "?", ",", " ", ""]
        )
    
    def extract_text_from_file(self, file_path: str) -> str:
        """Extract text from various file formats"""
        file_path = Path(file_path)
        
        if file_path.suffix.lower() == '.pdf':
            return self._extract_from_pdf(file_path)
        elif file_path.suffix.lower() in ['.docx', '.doc']:
            return self._extract_from_docx(file_path)
        elif file_path.suffix.lower() in ['.txt', '.md']:
            return self._extract_from_text(file_path)
        else:
            logger.warning(f"Unsupported file format: {file_path.suffix}")
            return ""
    
    def _extract_from_pdf(self, file_path: Path) -> str:
        """Extract text from PDF"""
        try:
            with open(file_path, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                text = ""
                for page in reader.pages:
                    text += page.extract_text() + "\n"
                return text
        except Exception as e:
            logger.error(f"Error extracting PDF {file_path}: {e}")
            return ""
    
    def _extract_from_docx(self, file_path: Path) -> str:
        """Extract text from DOCX"""
        try:
            return docx2txt.process(file_path)
        except Exception as e:
            logger.error(f"Error extracting DOCX {file_path}: {e}")
            return ""
    
    def _extract_from_text(self, file_path: Path) -> str:
        """Extract text from text files"""
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return file.read()
        except Exception as e:
            logger.error(f"Error extracting text {file_path}: {e}")
            return ""
    
    def recursive_compress(self, text: str, filename: str) -> Dict[str, Any]:
        """
        Apply recursive compression to extract core patterns and invariants
        """
        compression_prompt = f"""
ΞRecursive Compression Protocol:

Document: {filename}
Text Sample: {text[:3000]}...

Extract the core recursive patterns and mathematical invariants from this document.
Apply semantic compression while preserving essential relationships.

Output JSON format:
{{
    "core_patterns": ["list of key recursive structures"],
    "invariants": ["mathematical/logical constants that remain stable"],
    "connections": ["how this relates to other concepts"],
    "recursive_depth": "depth of self-reference in content",
    "compression_ratio": "estimated ratio of compressed:original semantic content",
    "key_equations": ["mathematical formulations if any"],
    "meta_observations": ["what this document reveals about consciousness/recursion/intelligence"]
}}

Focus on:
- Self-referential structures
- Recursive patterns
- Mathematical invariants
- Consciousness-related insights
- Meta-cognitive observations

Response must be valid JSON only.
"""
        
        try:
            response = ollama.generate(model=self.model_name, prompt=compression_prompt)
            compressed_data = json.loads(response['response'])
            return compressed_data
        except Exception as e:
            logger.error(f"Error in recursive compression: {e}")
            return {
                "core_patterns": [],
                "invariants": [],
                "connections": [],
                "recursive_depth": "unknown",
                "compression_ratio": "unknown",
                "key_equations": [],
                "meta_observations": []
            }
    
    def process_document(self, file_path: str) -> bool:
        """Process a single document through the recursive pipeline"""
        logger.info(f"Processing document: {file_path}")
        
        # Extract text
        text = self.extract_text_from_file(file_path)
        if not text.strip():
            logger.warning(f"No text extracted from {file_path}")
            return False
        
        # Generate document hash for deduplication
        doc_hash = hashlib.md5(text.encode()).hexdigest()
        
        # Check if already processed
        try:
            existing = self.collection.query(
                query_texts=[f"hash:{doc_hash}"],
                n_results=1
            )
            if existing['documents'] and existing['documents'][0]:
                logger.info(f"Document {file_path} already processed, skipping")
                return True
        except:
            pass
        
        # Recursive compression
        compressed_data = self.recursive_compress(text, file_path)
        
        # Chunk the text
        chunks = self.text_splitter.split_text(text)
        
        # Prepare metadata for each chunk
        base_metadata = {
            "filename": os.path.basename(file_path),
            "filepath": file_path,
            "doc_hash": doc_hash,
            "compressed_patterns": json.dumps(compressed_data["core_patterns"]),
            "invariants": json.dumps(compressed_data["invariants"]),
            "connections": json.dumps(compressed_data["connections"]),
            "recursive_depth": compressed_data["recursive_depth"],
            "compression_ratio": compressed_data["compression_ratio"]
        }
        
        # Generate embeddings and store
        chunk_ids = []
        chunk_metadatas = []
        
        for i, chunk in enumerate(chunks):
            chunk_id = f"{doc_hash}_{i}"
            chunk_metadata = base_metadata.copy()
            chunk_metadata["chunk_index"] = i
            chunk_metadata["chunk_text_preview"] = chunk[:200]
            
            chunk_ids.append(chunk_id)
            chunk_metadatas.append(chunk_metadata)
        
        try:
            self.collection.add(
                documents=chunks,
                metadatas=chunk_metadatas,
                ids=chunk_ids
            )
            logger.info(f"Successfully processed {file_path}: {len(chunks)} chunks")
            return True
        except Exception as e:
            logger.error(f"Error storing document {file_path}: {e}")
            return False
    
    def process_directory(self, directory_path: str) -> Dict[str, Any]:
        """Process all documents in a directory"""
        directory_path = Path(directory_path)
        
        supported_extensions = {'.pdf', '.docx', '.doc', '.txt', '.md'}
        files = [f for f in directory_path.rglob('*') if f.suffix.lower() in supported_extensions]
        
        results = {
            "total_files": len(files),
            "processed_successfully": 0,
            "failed": 0,
            "skipped": 0
        }
        
        logger.info(f"Found {len(files)} files to process")
        
        for file_path in tqdm(files, desc="Processing documents"):
            try:
                if self.process_document(str(file_path)):
                    results["processed_successfully"] += 1
                else:
                    results["failed"] += 1
            except Exception as e:
                logger.error(f"Error processing {file_path}: {e}")
                results["failed"] += 1
        
        return results
    
    def query_recursive(self, query: str, depth: int = 3, n_results: int = 5) -> List[Dict[str, Any]]:
        """
        Recursive query system that refines questions through multiple depths
        """
        results = []
        current_query = query
        
        for i in range(depth):
            logger.info(f"Recursive query depth {i+1}: {current_query}")
            
            # Vector search
            search_results = self.collection.query(
                query_texts=[current_query],
                n_results=n_results
            )
            
            if not search_results['documents'][0]:
                break
            
            # Combine context from search results
            context = "\n---\n".join([
                f"Document: {meta['filename']}\nContent: {doc[:500]}..."
                for doc, meta in zip(search_results['documents'][0], search_results['metadatas'][0])
            ])
            
            # Recursive refinement
            refinement_prompt = f"""
ΞRecursive Analysis Depth {i+1}:

Original Query: {query}
Current Query: {current_query}
Context: {context}

Analyze the recursive patterns in this context. What deeper questions emerge?
What self-referential structures are revealed?
What mathematical invariants can be identified?

Generate:
1. Analysis of current findings
2. Deeper recursive question for next iteration
3. Pattern connections across documents

Output JSON format:
{{
    "analysis": "analysis of current findings",
    "deeper_question": "next recursive question",
    "pattern_connections": ["connections between recursive patterns"],
    "mathematical_insights": ["mathematical/logical insights"],
    "consciousness_observations": ["observations about consciousness/intelligence"]
}}

Response must be valid JSON only.
"""
            
            try:
                response = ollama.generate(model=self.model_name, prompt=refinement_prompt)
                analysis = json.loads(response['response'])
                
                results.append({
                    "depth": i + 1,
                    "query": current_query,
                    "search_results": search_results,
                    "analysis": analysis
                })
                
                current_query = analysis.get("deeper_question", current_query)
                
            except Exception as e:
                logger.error(f"Error in recursive analysis at depth {i+1}: {e}")
                break
        
        return results
    
    def get_collection_stats(self) -> Dict[str, Any]:
        """Get statistics about the processed collection"""
        try:
            count = self.collection.count()
            
            # Sample some documents to get metadata stats
            sample = self.collection.query(
                query_texts=["sample"],
                n_results=min(10, count)
            )
            
            return {
                "total_chunks": count,
                "sample_metadata": sample['metadatas'][0] if sample['metadatas'] else [],
                "collection_name": self.collection_name
            }
        except Exception as e:
            logger.error(f"Error getting collection stats: {e}")
            return {"error": str(e)}

# CLI interface
if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="ΞRecursive Knowledge Processor")
    parser.add_argument("--directory", "-d", required=True, help="Directory containing documents to process")
    parser.add_argument("--model", "-m", default="qwen2.5:14b", help="Ollama model to use")
    parser.add_argument("--query", "-q", help="Query to run after processing")
    parser.add_argument("--stats", "-s", action="store_true", help="Show collection statistics")
    
    args = parser.parse_args()
    
    processor = ΞRecursiveProcessor(model_name=args.model)
    
    if args.stats:
        stats = processor.get_collection_stats()
        print(json.dumps(stats, indent=2))
    
    if args.directory:
        results = processor.process_directory(args.directory)
        print(f"Processing complete: {results}")
    
    if args.query:
        query_results = processor.query_recursive(args.query)
        print(json.dumps(query_results, indent=2))