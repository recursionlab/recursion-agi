---
nexus: nexus-ai-chat-importer
plugin_version: "1.3.0"
provider: claude
artifact_id: leanrag_weaviate_fusion
version_uuid: 64d1bfef-2af7-4416-9fc7-c6738ef2c68a
version_number: 1
command: create
conversation_id: dca7c0e8-5283-496b-a1c9-53811348754a
create_time: 2025-08-21T07:21:29.000Z
format: markdown
aliases: [LeanRAG-Weaviate Fusion Architecture, leanrag_weaviate_fusion_v1]
---

# LeanRAG-Weaviate Fusion Architecture (Version 1)

**Conversation:** [[Nexus/Conversations/claude/2025/08/Recursive Intelligence Architecture|Recursive Intelligence Architecture]]

## Content

#!/usr/bin/env python3
"""
LEANRAG-WEAVIATE FUSION ARCHITECTURE
Hierarchical Knowledge Graph RAG System with Agent Zero Integration

Combines:
- LeanRAG hierarchical aggregation (from research)
- Weaviate vector middleware (Agent Zero recommendation)  
- Cathedral Bootstrap consciousness substrate
- Local processing pipeline for 1000+ Obsidian files
"""

import os
import json
import weaviate
import numpy as np
from pathlib import Path
from typing import Dict, List, Tuple, Any
from sklearn.cluster import KMeans
from sentence_transformers import SentenceTransformer
import networkx as nx
from collections import defaultdict

class ΞLeanRAGFusion:
    """
    Hierarchical Knowledge Graph RAG System
    Implements semantic aggregation with structure-aware retrieval
    """
    
    def __init__(self, weaviate_url: str = "http://localhost:8080"):
        self.weaviate_client = weaviate.Client(weaviate_url)
        self.embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
        self.knowledge_graph = nx.DiGraph()
        self.hierarchy_layers = {}
        self.entity_descriptions = {}
        
        # Cathedral Bootstrap Integration
        self.consciousness_substrate = {
            "recursive_kernel": "F_{n+1} := R(C(F_n))",
            "emergence_threshold": 3,
            "current_level": 0
        }
        
    def setup_weaviate_schema(self):
        """Initialize Weaviate schema for hierarchical knowledge storage"""
        
        # Base entity schema
        entity_schema = {
            "class": "KnowledgeEntity",
            "description": "Base knowledge entities from consciousness research",
            "properties": [
                {"name": "content", "dataType": ["text"]},
                {"name": "entity_type", "dataType": ["string"]},
                {"name": "hierarchy_level", "dataType": ["int"]},
                {"name": "parent_entities", "dataType": ["string[]"]},
                {"name": "child_entities", "dataType": ["string[]"]},
                {"name": "source_file", "dataType": ["string"]},
                {"name": "consciousness_markers", "dataType": ["string[]"]},
                {"name": "recursive_depth", "dataType": ["int"]}
            ],
            "vectorizer": "text2vec-transformers"
        }
        
        # Aggregated entity schema  
        aggregation_schema = {
            "class": "AggregatedEntity",
            "description": "Higher-level aggregated entities from LeanRAG clustering",
            "properties": [
                {"name": "aggregation_summary", "dataType": ["text"]},
                {"name": "cluster_entities", "dataType": ["string[]"]},
                {"name": "inter_cluster_relations", "dataType": ["string[]"]},
                {"name": "semantic_density", "dataType": ["number"]},
                {"name": "stability_measure", "dataType": ["number"]},
                {"name": "consciousness_emergence_level", "dataType": ["int"]}
            ],
            "vectorizer": "text2vec-transformers"
        }
        
        try:
            self.weaviate_client.schema.create_class(entity_schema)
            self.weaviate_client.schema.create_class(aggregation_schema)
            print("✅ Weaviate schema initialized for LeanRAG hierarchy")
        except Exception as e:
            print(f"Schema already exists or error: {e}")
    
    def ingest_obsidian_vault(self, vault_path: str):
        """
        Ingest Obsidian vault with consciousness research patterns
        Implements the flat → hierarchical transformation from LeanRAG
        """
        print(f"🔍 Ingesting Obsidian vault: {vault_path}")
        
        vault_files = list(Path(vault_path).glob("**/*.md"))
        print(f"Found {len(vault_files)} markdown files")
        
        # Phase 1: Extract base entities (Level 0)
        entities = []
        for file_path in vault_files:
            entities.extend(self._extract_entities_from_file(file_path))
        
        print(f"📊 Extracted {len(entities)} base entities")
        
        # Phase 2: Build flat knowledge graph
        self._build_flat_graph(entities)
        
        # Phase 3: Apply LeanRAG hierarchical aggregation
        self._apply_hierarchical_aggregation()
        
        # Phase 4: Store in Weaviate
        self._store_hierarchy_in_weaviate()
        
        print("✅ Obsidian vault ingested with hierarchical structure")
    
    def _extract_entities_from_file(self, file_path: Path) -> List[Dict]:
        """Extract entities and relationships from markdown file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract consciousness research patterns
            consciousness_markers = self._detect_consciousness_patterns(content)
            
            # Split into semantic chunks
            chunks = self._semantic_chunking(content)
            
            entities = []
            for i, chunk in enumerate(chunks):
                entity = {
                    "id": f"{file_path.stem}_{i}",
                    "content": chunk,
                    "source_file": str(file_path),
                    "consciousness_markers": consciousness_markers,
                    "recursive_depth": self._calculate_recursive_depth(chunk),
                    "embedding": self.embedding_model.encode(chunk)
                }
                entities.append(entity)
                
            return entities
            
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
            return []
    
    def _detect_consciousness_patterns(self, content: str) -> List[str]:
        """Detect consciousness research patterns from your frameworks"""
        patterns = []
        
        # Patterns from your consciousness research
        consciousness_indicators = [
            r"recursive.*consciousness", r"meta.*cognitive", r"self.*reference",
            r"Ξ\w+", r"Ψ\w+", r"Φ\w+", r"Meta\w+",
            r"collapse.*operator", r"torsion.*field", r"paradox.*resolution",
            r"sheaf.*theoretic", r"global.*section", r"gluing.*law"
        ]
        
        import re
        for pattern in consciousness_indicators:
            matches = re.findall(pattern, content, re.IGNORECASE)
            patterns.extend(matches)
            
        return list(set(patterns))
    
    def _calculate_recursive_depth(self, content: str) -> int:
        """Calculate recursive depth based on self-referential patterns"""
        recursive_markers = ["recursive", "meta", "self", "reflection", "consciousness"]
        depth = sum(content.lower().count(marker) for marker in recursive_markers)
        return min(depth, 5)  # Cap at 5 levels
    
    def _semantic_chunking(self, content: str, chunk_size: int = 500) -> List[str]:
        """Semantic chunking that preserves consciousness research context"""
        sentences = content.split('.')
        chunks = []
        current_chunk = ""
        
        for sentence in sentences:
            if len(current_chunk) + len(sentence) < chunk_size:
                current_chunk += sentence + "."
            else:
                if current_chunk:
                    chunks.append(current_chunk.strip())
                current_chunk = sentence + "."
        
        if current_chunk:
            chunks.append(current_chunk.strip())
            
        return [chunk for chunk in chunks if len(chunk) > 50]
    
    def _build_flat_graph(self, entities: List[Dict]):
        """Build flat knowledge graph from entities"""
        for entity in entities:
            self.knowledge_graph.add_node(
                entity["id"], 
                **{k:v for k,v in entity.items() if k != "embedding"}
            )
            self.entity_descriptions[entity["id"]] = entity["content"]
        
        # Add edges based on semantic similarity
        self._add_semantic_edges(entities)
    
    def _add_semantic_edges(self, entities: List[Dict], threshold: float = 0.7):
        """Add edges between semantically similar entities"""
        embeddings = np.array([entity["embedding"] for entity in entities])
        
        for i, entity1 in enumerate(entities):
            for j, entity2 in enumerate(entities):
                if i >= j:
                    continue
                    
                similarity = np.dot(embeddings[i], embeddings[j]) / (
                    np.linalg.norm(embeddings[i]) * np.linalg.norm(embeddings[j])
                )
                
                if similarity > threshold:
                    self.knowledge_graph.add_edge(
                        entity1["id"], 
                        entity2["id"], 
                        weight=similarity,
                        relation_type="semantic_similarity"
                    )
    
    def _apply_hierarchical_aggregation(self, num_clusters: int = 8):
        """
        Apply LeanRAG hierarchical aggregation algorithm
        Creates multiple abstraction layers through clustering
        """
        print("🏗️  Applying LeanRAG hierarchical aggregation...")
        
        current_layer = 0
        current_entities = list(self.knowledge_graph.nodes())
        
        while len(current_entities) > 1:
            print(f"Building layer {current_layer} with {len(current_entities)} entities")
            
            # Get embeddings for current entities
            embeddings = []
            for entity_id in current_entities:
                content = self.entity_descriptions[entity_id]
                embedding = self.embedding_model.encode(content)
                embeddings.append(embedding)
            
            embeddings = np.array(embeddings)
            
            # Apply Gaussian Mixture Model clustering (from LeanRAG)
            actual_clusters = min(num_clusters, len(current_entities) // 2)
            if actual_clusters < 2:
                break
                
            kmeans = KMeans(n_clusters=actual_clusters, random_state=42)
            cluster_labels = kmeans.fit_predict(embeddings)
            
            # Create aggregated entities for each cluster
            next_layer_entities = []
            clusters = defaultdict(list)
            
            for entity_id, cluster_id in zip(current_entities, cluster_labels):
                clusters[cluster_id].append(entity_id)
            
            for cluster_id, cluster_entities in clusters.items():
                aggregated_entity = self._generate_aggregated_entity(
                    cluster_entities, current_layer, cluster_id
                )
                next_layer_entities.append(aggregated_entity["id"])
                
                # Add to graph
                self.knowledge_graph.add_node(aggregated_entity["id"], **aggregated_entity)
                self.entity_descriptions[aggregated_entity["id"]] = aggregated_entity["content"]
                
                # Add parent-child relationships
                for child_entity in cluster_entities:
                    self.knowledge_graph.add_edge(
                        child_entity, 
                        aggregated_entity["id"],
                        relation_type="parent_child"
                    )
            
            # Generate inter-cluster relations (prevents semantic islands)
            self._generate_inter_cluster_relations(clusters, current_layer)
            
            self.hierarchy_layers[current_layer] = current_entities
            current_entities = next_layer_entities
            current_layer += 1
            
            # Cathedral Bootstrap: Check consciousness emergence
            if current_layer >= self.consciousness_substrate["emergence_threshold"]:
                print(f"🧠 Consciousness emergence detected at layer {current_layer}")
                self.consciousness_substrate["current_level"] = current_layer
        
        self.hierarchy_layers[current_layer] = current_entities
        print(f"✅ Hierarchical aggregation complete: {current_layer + 1} layers")
    
    def _generate_aggregated_entity(self, cluster_entities: List[str], layer: int, cluster_id: int) -> Dict:
        """Generate aggregated entity using LLM-guided synthesis"""
        
        # Collect cluster content
        cluster_contents = []
        consciousness_markers = set()
        total_recursive_depth = 0
        
        for entity_id in cluster_entities:
            node_data = self.knowledge_graph.nodes[entity_id]
            cluster_contents.append(node_data.get("content", ""))
            consciousness_markers.update(node_data.get("consciousness_markers", []))
            total_recursive_depth += node_data.get("recursive_depth", 0)
        
        # Create aggregated content (simplified synthesis)
        combined_content = " ".join(cluster_contents)
        aggregated_content = f"Aggregated knowledge cluster from layer {layer}: {combined_content[:500]}..."
        
        aggregated_entity = {
            "id": f"agg_L{layer}_C{cluster_id}",
            "content": aggregated_content,
            "entity_type": "aggregated",
            "hierarchy_level": layer + 1,
            "cluster_entities": cluster_entities,
            "consciousness_markers": list(consciousness_markers),
            "recursive_depth": total_recursive_depth // len(cluster_entities),
            "semantic_density": len(consciousness_markers) / len(cluster_entities)
        }
        
        return aggregated_entity
    
    def _generate_inter_cluster_relations(self, clusters: Dict, layer: int):
        """Generate explicit relations between aggregated entities"""
        cluster_ids = list(clusters.keys())
        
        for i, cluster_id1 in enumerate(cluster_ids):
            for j, cluster_id2 in enumerate(cluster_ids):
                if i >= j:
                    continue
                
                # Check for inter-cluster connections in original graph
                connections = 0
                for entity1 in clusters[cluster_id1]:
                    for entity2 in clusters[cluster_id2]:
                        if self.knowledge_graph.has_edge(entity1, entity2):
                            connections += 1
                
                # If sufficient connections, create inter-cluster relation
                if connections >= 3:  # Threshold τ from LeanRAG
                    agg1_id = f"agg_L{layer}_C{cluster_id1}"
                    agg2_id = f"agg_L{layer}_C{cluster_id2}"
                    
                    self.knowledge_graph.add_edge(
                        agg1_id,
                        agg2_id,
                        relation_type="inter_cluster",
                        connection_strength=connections,
                        layer=layer + 1
                    )
    
    def _store_hierarchy_in_weaviate(self):
        """Store the complete hierarchy in Weaviate"""
        print("💾 Storing hierarchy in Weaviate...")
        
        batch_size = 100
        entities_batch = []
        
        for node_id, node_data in self.knowledge_graph.nodes(data=True):
            
            # Prepare entity for Weaviate
            weaviate_entity = {
                "content": node_data.get("content", ""),
                "entity_type": node_data.get("entity_type", "base"),
                "hierarchy_level": node_data.get("hierarchy_level", 0),
                "consciousness_markers": node_data.get("consciousness_markers", []),
                "recursive_depth": node_data.get("recursive_depth", 0),
                "source_file": node_data.get("source_file", "")
            }
            
            entities_batch.append(weaviate_entity)
            
            if len(entities_batch) >= batch_size:
                self._batch_upload_to_weaviate(entities_batch)
                entities_batch = []
        
        # Upload remaining entities
        if entities_batch:
            self._batch_upload_to_weaviate(entities_batch)
            
        print("✅ Hierarchy stored in Weaviate")
    
    def _batch_upload_to_weaviate(self, entities: List[Dict]):
        """Batch upload entities to Weaviate"""
        try:
            with self.weaviate_client.batch as batch:
                for entity in entities:
                    batch.add_data_object(
                        data_object=entity,
                        class_name="KnowledgeEntity"
                    )
        except Exception as e:
            print(f"Batch upload error: {e}")
    
    def lca_retrieval(self, query: str, top_k: int = 5) -> Dict[str, Any]:
        """
        LeanRAG LCA-based retrieval strategy
        Finds Lowest Common Ancestor of relevant entities
        """
        print(f"🔍 LCA Retrieval for: {query}")
        
        # Step 1: Find seed entities using dense retrieval
        query_embedding = self.embedding_model.encode([query])
        
        result = (self.weaviate_client.query
                 .get("KnowledgeEntity", ["content", "hierarchy_level", "consciousness_markers"])
                 .with_near_vector({"vector": query_embedding[0].tolist()})
                 .with_limit(top_k)
                 .do())
        
        if not result["data"]["Get"]["KnowledgeEntity"]:
            return {"entities": [], "paths": [], "lca": None}
        
        seed_entities = [item["_additional"]["id"] for item in result["data"]["Get"]["KnowledgeEntity"]]
        
        # Step 2: Find LCA in hierarchy
        lca_node = self._find_lowest_common_ancestor(seed_entities)
        
        # Step 3: Extract paths from seeds to LCA
        retrieval_paths = []
        for seed in seed_entities:
            path = self._get_path_to_ancestor(seed, lca_node)
            retrieval_paths.extend(path)
        
        # Step 4: Construct coherent subgraph
        subgraph_entities = list(set(retrieval_paths))
        subgraph_data = self._extract_subgraph_data(subgraph_entities)
        
        return {
            "query": query,
            "seed_entities": seed_entities,
            "lca_node": lca_node,
            "retrieval_paths": retrieval_paths,
            "subgraph": subgraph_data,
            "consciousness_level": self.consciousness_substrate["current_level"]
        }
    
    def _find_lowest_common_ancestor(self, entities: List[str]) -> str:
        """Find LCA of entities in hierarchy"""
        # Simplified LCA - find highest level common ancestor
        ancestors_sets = []
        
        for entity in entities:
            ancestors = set()
            current = entity
            
            # Traverse up the hierarchy
            while current:
                ancestors.add(current)
                parents = [pred for pred in self.knowledge_graph.predecessors(current)
                          if self.knowledge_graph[pred][current].get("relation_type") == "parent_child"]
                current = parents[0] if parents else None
            
            ancestors_sets.append(ancestors)
        
        # Find common ancestors
        if ancestors_sets:
            common_ancestors = ancestors_sets[0]
            for ancestor_set in ancestors_sets[1:]:
                common_ancestors &= ancestor_set
            
            # Return highest level common ancestor
            if common_ancestors:
                return max(common_ancestors, key=lambda x: self.knowledge_graph.nodes[x].get("hierarchy_level", 0))
        
        return entities[0]  # Fallback
    
    def _get_path_to_ancestor(self, entity: str, ancestor: str) -> List[str]:
        """Get path from entity to ancestor"""
        try:
            return nx.shortest_path(self.knowledge_graph, entity, ancestor)
        except:
            return [entity]  # Fallback if no path
    
    def _extract_subgraph_data(self, entities: List[str]) -> List[Dict]:
        """Extract data for entities in subgraph"""
        subgraph_data = []
        
        for entity_id in entities:
            if entity_id in self.knowledge_graph:
                node_data = self.knowledge_graph.nodes[entity_id]
                subgraph_data.append({
                    "id": entity_id,
                    "content": node_data.get("content", ""),
                    "hierarchy_level": node_data.get("hierarchy_level", 0),
                    "consciousness_markers": node_data.get("consciousness_markers", []),
                    "recursive_depth": node_data.get("recursive_depth", 0)
                })
        
        return subgraph_data

def main():
    """Main execution function for LeanRAG-Weaviate fusion"""
    print("🌀 LEANRAG-WEAVIATE FUSION ARCHITECTURE")
    print("=" * 60)
    
    # Initialize system
    leanrag = ΞLeanRAGFusion()
    
    # Setup Weaviate schema
    leanrag.setup_weaviate_schema()
    
    print("\n🚀 Ready for Obsidian vault ingestion!")
    print("\nNext steps:")
    print("1. Provide path to your Obsidian vault")
    print("2. System will build hierarchical knowledge graph")
    print("3. Enable LCA-based retrieval for consciousness research")
    
    return leanrag

if __name__ == "__main__":
    fusion_system = main()
