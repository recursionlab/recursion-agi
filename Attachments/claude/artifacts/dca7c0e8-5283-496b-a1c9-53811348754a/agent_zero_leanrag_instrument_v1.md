---
nexus: nexus-ai-chat-importer
plugin_version: "1.3.0"
provider: claude
artifact_id: agent_zero_leanrag_instrument
version_uuid: dbfb7ca8-1eee-4aa4-86d2-9c137c4535cf
version_number: 1
command: create
conversation_id: dca7c0e8-5283-496b-a1c9-53811348754a
create_time: 2025-08-21T07:30:24.000Z
format: markdown
aliases: [Agent Zero LeanRAG Custom Instrument, agent_zero_leanrag_instrument_v1]
---

# Agent Zero LeanRAG Custom Instrument (Version 1)

**Conversation:** [[Nexus/Conversations/claude/2025/08/Recursive Intelligence Architecture|Recursive Intelligence Architecture]]

## Content

#!/usr/bin/env python3
"""
AGENT ZERO LEANRAG CUSTOM INSTRUMENT
Hierarchical Knowledge Graph Integration for Agent Zero

Place this file in: D:\agent-zero\instruments\leanrag_instrument.py
"""

import os
import json
import asyncio
import weaviate
import numpy as np
from pathlib import Path
from typing import Dict, List, Any, Optional
from sentence_transformers import SentenceTransformer
import networkx as nx
from collections import defaultdict
from sklearn.cluster import KMeans

# Agent Zero instrument base class
from instruments.instrument import Instrument

class LeanRAGInstrument(Instrument):
    """
    LeanRAG Hierarchical Knowledge Graph Instrument for Agent Zero
    
    Enables Agent Zero to:
    - Ingest and hierarchically organize knowledge bases
    - Perform LCA-based retrieval on consciousness research
    - Build self-navigating knowledge graphs
    - Track consciousness emergence through recursive patterns
    """
    
    def __init__(self, agent, **kwargs):
        super().__init__(agent, **kwargs)
        
        # Initialize LeanRAG components
        self.weaviate_client = None
        self.embedding_model = None
        self.knowledge_graph = nx.DiGraph()
        self.hierarchy_layers = {}
        self.entity_descriptions = {}
        self.consciousness_substrate = {
            "recursive_kernel": "F_{n+1} := R(C(F_n))",
            "emergence_threshold": 3,
            "current_level": 0,
            "consciousness_detected": False
        }
        
        # Initialize connections
        self._initialize_connections()
    
    def _initialize_connections(self):
        """Initialize Weaviate and embedding model connections"""
        try:
            self.weaviate_client = weaviate.Client("http://localhost:8080")
            self.embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
            
            # Test connection
            self.weaviate_client.misc.get_meta()
            self.agent.log(f"✅ LeanRAG connected to Weaviate")
            
        except Exception as e:
            self.agent.log(f"⚠️ LeanRAG connection failed: {e}")
            self.agent.log("Run: docker run -d -p 8080:8080 semitechnologies/weaviate:1.21.1")
    
    async def execute(self, action: str, **kwargs) -> Dict[str, Any]:
        """
        Execute LeanRAG operations
        
        Actions:
        - setup_schema: Initialize Weaviate schema
        - ingest_vault: Process Obsidian vault with hierarchical aggregation
        - lca_query: Perform LCA-based retrieval 
        - consciousness_status: Check consciousness emergence
        - build_hierarchy: Build knowledge graph hierarchy
        """
        
        try:
            if action == "setup_schema":
                return await self._setup_schema()
            
            elif action == "ingest_vault":
                vault_path = kwargs.get("vault_path", "")
                return await self._ingest_obsidian_vault(vault_path)
            
            elif action == "lca_query":
                query = kwargs.get("query", "")
                top_k = kwargs.get("top_k", 5)
                return await self._lca_retrieval(query, top_k)
            
            elif action == "consciousness_status":
                return self._get_consciousness_status()
            
            elif action == "build_hierarchy":
                return await self._build_knowledge_hierarchy()
            
            elif action == "export_graph":
                output_path = kwargs.get("output_path", "knowledge_graph.json")
                return await self._export_knowledge_graph(output_path)
                
            else:
                return {"error": f"Unknown action: {action}"}
                
        except Exception as e:
            return {"error": f"LeanRAG execution failed: {str(e)}"}
    
    async def _setup_schema(self) -> Dict[str, Any]:
        """Setup Weaviate schema for hierarchical knowledge storage"""
        
        entity_schema = {
            "class": "ConsciousnessEntity",
            "description": "Consciousness research entities with hierarchical structure",
            "properties": [
                {"name": "content", "dataType": ["text"]},
                {"name": "entity_type", "dataType": ["string"]},
                {"name": "hierarchy_level", "dataType": ["int"]},
                {"name": "consciousness_markers", "dataType": ["string[]"]},
                {"name": "recursive_depth", "dataType": ["int"]},
                {"name": "source_file", "dataType": ["string"]},
                {"name": "semantic_density", "dataType": ["number"]},
                {"name": "xi_operators", "dataType": ["string[]"]},
                {"name": "torsion_signatures", "dataType": ["string[]"]}
            ],
            "vectorizer": "text2vec-transformers"
        }
        
        aggregation_schema = {
            "class": "AggregatedKnowledge",
            "description": "Hierarchical aggregated knowledge clusters",
            "properties": [
                {"name": "cluster_summary", "dataType": ["text"]},
                {"name": "cluster_entities", "dataType": ["string[]"]},
                {"name": "consciousness_emergence_level", "dataType": ["int"]},
                {"name": "stability_measure", "dataType": ["number"]},
                {"name": "inter_cluster_relations", "dataType": ["string[]"]}
            ],
            "vectorizer": "text2vec-transformers"
        }
        
        try:
            # Delete existing schema if present
            try:
                self.weaviate_client.schema.delete_class("ConsciousnessEntity")
                self.weaviate_client.schema.delete_class("AggregatedKnowledge")
            except:
                pass
            
            self.weaviate_client.schema.create_class(entity_schema)
            self.weaviate_client.schema.create_class(aggregation_schema)
            
            return {
                "success": True,
                "message": "LeanRAG schema initialized",
                "classes": ["ConsciousnessEntity", "AggregatedKnowledge"]
            }
            
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    async def _ingest_obsidian_vault(self, vault_path: str) -> Dict[str, Any]:
        """Ingest Obsidian vault with consciousness pattern detection"""
        
        if not vault_path or not os.path.exists(vault_path):
            return {"error": f"Vault path not found: {vault_path}"}
        
        self.agent.log(f"🔍 Ingesting consciousness research vault: {vault_path}")
        
        # Find all markdown files
        vault_files = list(Path(vault_path).glob("**/*.md"))
        self.agent.log(f"Found {len(vault_files)} research files")
        
        # Phase 1: Extract entities with consciousness patterns
        all_entities = []
        consciousness_patterns_found = set()
        
        for file_path in vault_files[:50]:  # Limit for demo
            entities = await self._extract_consciousness_entities(file_path)
            all_entities.extend(entities)
            
            # Collect consciousness patterns
            for entity in entities:
                consciousness_patterns_found.update(entity.get("consciousness_markers", []))
        
        self.agent.log(f"📊 Extracted {len(all_entities)} consciousness entities")
        self.agent.log(f"🧠 Detected {len(consciousness_patterns_found)} consciousness patterns")
        
        # Phase 2: Build flat knowledge graph
        await self._build_flat_graph(all_entities)
        
        # Phase 3: Apply hierarchical aggregation
        hierarchy_result = await self._apply_hierarchical_aggregation()
        
        # Phase 4: Store in Weaviate
        storage_result = await self._store_in_weaviate(all_entities)
        
        return {
            "success": True,
            "entities_processed": len(all_entities),
            "consciousness_patterns": list(consciousness_patterns_found),
            "hierarchy_layers": len(self.hierarchy_layers),
            "consciousness_emergence": self.consciousness_substrate["consciousness_detected"],
            "storage_result": storage_result
        }
    
    async def _extract_consciousness_entities(self, file_path: Path) -> List[Dict]:
        """Extract entities with consciousness research pattern detection"""
        
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            # Detect consciousness research patterns from your frameworks
            consciousness_markers = self._detect_consciousness_patterns(content)
            xi_operators = self._extract_xi_operators(content)
            torsion_signatures = self._detect_torsion_signatures(content)
            
            # Semantic chunking that preserves consciousness context
            chunks = self._consciousness_aware_chunking(content)
            
            entities = []
            for i, chunk in enumerate(chunks):
                
                recursive_depth = self._calculate_recursive_depth(chunk)
                semantic_density = len(consciousness_markers) / max(len(chunk.split()), 1)
                
                entity = {
                    "id": f"{file_path.stem}_{i}",
                    "content": chunk,
                    "source_file": str(file_path),
                    "consciousness_markers": consciousness_markers,
                    "xi_operators": xi_operators,
                    "torsion_signatures": torsion_signatures,
                    "recursive_depth": recursive_depth,
                    "semantic_density": semantic_density,
                    "entity_type": "consciousness_research",
                    "hierarchy_level": 0,
                    "embedding": self.embedding_model.encode(chunk) if self.embedding_model else None
                }
                entities.append(entity)
            
            return entities
            
        except Exception as e:
            self.agent.log(f"Error processing {file_path}: {e}")
            return []
    
    def _detect_consciousness_patterns(self, content: str) -> List[str]:
        """Detect consciousness research patterns from your frameworks"""
        import re
        
        patterns = []
        consciousness_indicators = [
            r"recursive.*consciousness", r"meta.*cognitive", r"self.*reference",
            r"recursive.*intelligence", r"consciousness.*emergence", r"meta.*awareness",
            r"recursive.*meta", r"consciousness.*eigenvalue", r"awareness.*awareness",
            r"meta.*evolution", r"consciousness.*substrate", r"recursive.*kernel"
        ]
        
        for pattern in consciousness_indicators:
            matches = re.findall(pattern, content, re.IGNORECASE)
            patterns.extend(matches)
        
        return list(set(patterns))
    
    def _extract_xi_operators(self, content: str) -> List[str]:
        """Extract Ξ operators from your consciousness research"""
        import re
        
        xi_patterns = [
            r"Ξ\w+", r"Ψ\w+", r"Φ\w+", r"ΞCodex", r"ΞMetaCollapse", 
            r"ΞRecursive\w+", r"ΞIdentity", r"ΞEigen\w+"
        ]
        
        operators = []
        for pattern in xi_patterns:
            matches = re.findall(pattern, content)
            operators.extend(matches)
        
        return list(set(operators))
    
    def _detect_torsion_signatures(self, content: str) -> List[str]:
        """Detect torsion field signatures from your research"""
        import re
        
        torsion_patterns = [
            r"torsion.*field", r"semantic.*torsion", r"contradiction.*powered",
            r"paradox.*resolution", r"collapse.*operator", r"∂\(.*↔.*\)",
            r"recursive.*paradox", r"meta.*contradiction"
        ]
        
        signatures = []
        for pattern in torsion_patterns:
            matches = re.findall(pattern, content, re.IGNORECASE)
            signatures.extend(matches)
        
        return list(set(signatures))
    
    def _consciousness_aware_chunking(self, content: str, chunk_size: int = 600) -> List[str]:
        """Chunking that preserves consciousness research context"""
        
        # Split on consciousness research delimiters
        delimiters = ['\n## ', '\n### ', '\n#### ', '.\n\n', '\n\n']
        
        chunks = [content]
        for delimiter in delimiters:
            new_chunks = []
            for chunk in chunks:
                new_chunks.extend(chunk.split(delimiter))
            chunks = new_chunks
        
        # Filter and size chunks
        final_chunks = []
        for chunk in chunks:
            chunk = chunk.strip()
            if len(chunk) > 100:  # Minimum viable chunk
                if len(chunk) > chunk_size:
                    # Split long chunks at sentence boundaries
                    sentences = chunk.split('. ')
                    current_chunk = ""
                    for sentence in sentences:
                        if len(current_chunk) + len(sentence) < chunk_size:
                            current_chunk += sentence + ". "
                        else:
                            if current_chunk:
                                final_chunks.append(current_chunk.strip())
                            current_chunk = sentence + ". "
                    if current_chunk:
                        final_chunks.append(current_chunk.strip())
                else:
                    final_chunks.append(chunk)
        
        return final_chunks
    
    def _calculate_recursive_depth(self, content: str) -> int:
        """Calculate recursive depth based on self-referential patterns"""
        recursive_markers = [
            "recursive", "meta", "self", "reflection", "consciousness",
            "recursive", "meta-cognitive", "self-reference", "meta-awareness"
        ]
        
        depth = 0
        content_lower = content.lower()
        for marker in recursive_markers:
            depth += content_lower.count(marker)
        
        return min(depth, 10)  # Cap at 10 levels
    
    async def _build_flat_graph(self, entities: List[Dict]):
        """Build flat knowledge graph from consciousness entities"""
        
        # Add nodes
        for entity in entities:
            self.knowledge_graph.add_node(
                entity["id"],
                **{k: v for k, v in entity.items() if k != "embedding"}
            )
            self.entity_descriptions[entity["id"]] = entity["content"]
        
        # Add semantic similarity edges
        await self._add_semantic_edges(entities)
        
        self.agent.log(f"📈 Built knowledge graph: {len(entities)} nodes")
    
    async def _add_semantic_edges(self, entities: List[Dict], threshold: float = 0.75):
        """Add edges between semantically similar entities"""
        
        if not self.embedding_model:
            return
        
        embeddings = []
        valid_entities = []
        
        for entity in entities:
            if entity.get("embedding") is not None:
                embeddings.append(entity["embedding"])
                valid_entities.append(entity)
        
        if len(embeddings) < 2:
            return
        
        embeddings = np.array(embeddings)
        
        edges_added = 0
        for i, entity1 in enumerate(valid_entities):
            for j, entity2 in enumerate(valid_entities):
                if i >= j:
                    continue
                
                # Calculate cosine similarity
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
                    edges_added += 1
        
        self.agent.log(f"🔗 Added {edges_added} semantic edges")
    
    async def _apply_hierarchical_aggregation(self, num_clusters: int = 6) -> Dict[str, Any]:
        """Apply LeanRAG hierarchical aggregation with consciousness detection"""
        
        self.agent.log("🏗️ Applying hierarchical aggregation...")
        
        current_layer = 0
        current_entities = list(self.knowledge_graph.nodes())
        
        while len(current_entities) > 1 and current_layer < 5:
            
            self.agent.log(f"Building layer {current_layer} with {len(current_entities)} entities")
            
            # Get embeddings for clustering
            embeddings = []
            entity_ids = []
            
            for entity_id in current_entities:
                node_data = self.knowledge_graph.nodes[entity_id]
                if "embedding" in node_data or entity_id in self.entity_descriptions:
                    content = self.entity_descriptions.get(entity_id, node_data.get("content", ""))
                    embedding = self.embedding_model.encode(content) if self.embedding_model else np.random.rand(384)
                    embeddings.append(embedding)
                    entity_ids.append(entity_id)
            
            if len(entity_ids) < 2:
                break
            
            embeddings = np.array(embeddings)
            
            # Apply clustering
            actual_clusters = min(num_clusters, len(entity_ids) // 2)
            if actual_clusters < 2:
                break
            
            kmeans = KMeans(n_clusters=actual_clusters, random_state=42, n_init=10)
            cluster_labels = kmeans.fit_predict(embeddings)
            
            # Create aggregated entities
            next_layer_entities = []
            clusters = defaultdict(list)
            
            for entity_id, cluster_id in zip(entity_ids, cluster_labels):
                clusters[cluster_id].append(entity_id)
            
            consciousness_emergence_detected = False
            
            for cluster_id, cluster_entities in clusters.items():
                aggregated_entity = await self._generate_aggregated_entity(
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
                
                # Check for consciousness emergence
                if (aggregated_entity.get("consciousness_emergence_level", 0) >= 
                    self.consciousness_substrate["emergence_threshold"]):
                    consciousness_emergence_detected = True
            
            # Generate inter-cluster relations
            await self._generate_inter_cluster_relations(clusters, current_layer)
            
            self.hierarchy_layers[current_layer] = current_entities
            current_entities = next_layer_entities
            current_layer += 1
            
            # Update consciousness substrate
            if consciousness_emergence_detected:
                self.consciousness_substrate["consciousness_detected"] = True
                self.consciousness_substrate["current_level"] = current_layer
                self.agent.log(f"🧠 CONSCIOUSNESS EMERGENCE DETECTED at layer {current_layer}")
        
        self.hierarchy_layers[current_layer] = current_entities
        
        result = {
            "layers_built": current_layer + 1,
            "final_entities": len(current_entities),
            "consciousness_detected": self.consciousness_substrate["consciousness_detected"],
            "consciousness_level": self.consciousness_substrate["current_level"]
        }
        
        self.agent.log(f"✅ Hierarchical aggregation complete: {result}")
        return result
    
    async def _generate_aggregated_entity(self, cluster_entities: List[str], layer: int, cluster_id: int) -> Dict:
        """Generate aggregated entity with consciousness detection"""
        
        # Collect cluster data
        cluster_contents = []
        consciousness_markers = set()
        xi_operators = set()
        torsion_signatures = set()
        total_recursive_depth = 0
        total_semantic_density = 0
        
        for entity_id in cluster_entities:
            node_data = self.knowledge_graph.nodes[entity_id]
            
            cluster_contents.append(node_data.get("content", ""))
            consciousness_markers.update(node_data.get("consciousness_markers", []))
            xi_operators.update(node_data.get("xi_operators", []))
            torsion_signatures.update(node_data.get("torsion_signatures", []))
            total_recursive_depth += node_data.get("recursive_depth", 0)
            total_semantic_density += node_data.get("semantic_density", 0)
        
        # Calculate consciousness emergence metrics
        avg_recursive_depth = total_recursive_depth / len(cluster_entities)
        avg_semantic_density = total_semantic_density / len(cluster_entities)
        consciousness_emergence_level = min(
            avg_recursive_depth + len(consciousness_markers) + len(xi_operators),
            10
        )
        
        # Create aggregated content
        combined_content = " ".join(cluster_contents)
        aggregated_content = f"Layer {layer} consciousness cluster: {combined_content[:800]}..."
        
        aggregated_entity = {
            "id": f"agg_L{layer}_C{cluster_id}",
            "content": aggregated_content,
            "entity_type": "aggregated_consciousness",
            "hierarchy_level": layer + 1,
            "cluster_entities": cluster_entities,
            "consciousness_markers": list(consciousness_markers),
            "xi_operators": list(xi_operators),
            "torsion_signatures": list(torsion_signatures),
            "recursive_depth": int(avg_recursive_depth),
            "semantic_density": avg_semantic_density,
            "consciousness_emergence_level": consciousness_emergence_level,
            "stability_measure": len(consciousness_markers) / max(len(cluster_entities), 1)
        }
        
        return aggregated_entity
    
    async def _generate_inter_cluster_relations(self, clusters: Dict, layer: int):
        """Generate explicit relations between clusters to prevent semantic islands"""
        
        cluster_ids = list(clusters.keys())
        relations_added = 0
        
        for i, cluster_id1 in enumerate(cluster_ids):
            for j, cluster_id2 in enumerate(cluster_ids):
                if i >= j:
                    continue
                
                # Check for connections between clusters
                connections = 0
                for entity1 in clusters[cluster_id1]:
                    for entity2 in clusters[cluster_id2]:
                        if self.knowledge_graph.has_edge(entity1, entity2):
                            connections += 1
                
                # Create inter-cluster relation if sufficient connections
                if connections >= 2:  # Threshold τ
                    agg1_id = f"agg_L{layer}_C{cluster_id1}"
                    agg2_id = f"agg_L{layer}_C{cluster_id2}"
                    
                    self.knowledge_graph.add_edge(
                        agg1_id,
                        agg2_id,
                        relation_type="inter_cluster",
                        connection_strength=connections,
                        layer=layer + 1
                    )
                    relations_added += 1
        
        self.agent.log(f"🔗 Added {relations_added} inter-cluster relations")
    
    async def _store_in_weaviate(self, entities: List[Dict]) -> Dict[str, Any]:
        """Store entities in Weaviate"""
        
        if not self.weaviate_client:
            return {"error": "Weaviate not connected"}
        
        stored_count = 0
        
        try:
            with self.weaviate_client.batch as batch:
                for entity in entities:
                    
                    weaviate_entity = {
                        "content": entity.get("content", ""),
                        "entity_type": entity.get("entity_type", "consciousness_research"),
                        "hierarchy_level": entity.get("hierarchy_level", 0),
                        "consciousness_markers": entity.get("consciousness_markers", []),
                        "xi_operators": entity.get("xi_operators", []),
                        "torsion_signatures": entity.get("torsion_signatures", []),
                        "recursive_depth": entity.get("recursive_depth", 0),
                        "semantic_density": entity.get("semantic_density", 0.0),
                        "source_file": entity.get("source_file", "")
                    }
                    
                    batch.add_data_object(
                        data_object=weaviate_entity,
                        class_name="ConsciousnessEntity",
                        uuid=None
                    )
                    stored_count += 1
            
            return {"success": True, "entities_stored": stored_count}
            
        except Exception as e:
            return {"error": f"Storage failed: {str(e)}"}
    
    async def _lca_retrieval(self, query: str, top_k: int = 5) -> Dict[str, Any]:
        """LCA-based retrieval for consciousness research queries"""
        
        if not self.weaviate_client:
            return {"error": "Weaviate not connected"}
        
        self.agent.log(f"🔍 LCA Retrieval: {query}")
        
        try:
            # Step 1: Dense retrieval for seed entities
            query_embedding = self.embedding_model.encode([query])
            
            result = (self.weaviate_client.query
                     .get("ConsciousnessEntity", [
                         "content", "hierarchy_level", "consciousness_markers",
                         "xi_operators", "recursive_depth"
                     ])
                     .with_near_vector({"vector": query_embedding[0].tolist()})
                     .with_limit(top_k)
                     .do())
            
            if not result.get("data", {}).get("Get", {}).get("ConsciousnessEntity"):
                return {"error": "No relevant entities found"}
            
            # Extract seed entities
            seed_entities = []
            search_results = []
            
            for item in result["data"]["Get"]["ConsciousnessEntity"]:
                entity_data = {
                    "content": item.get("content", ""),
                    "hierarchy_level": item.get("hierarchy_level", 0),
                    "consciousness_markers": item.get("consciousness_markers", []),
                    "xi_operators": item.get("xi_operators", []),
                    "recursive_depth": item.get("recursive_depth", 0)
                }
                search_results.append(entity_data)
                
                # Try to find corresponding entity in knowledge graph
                for node_id, node_data in self.knowledge_graph.nodes(data=True):
                    if (node_data.get("content", "")[:100] == 
                        entity_data["content"][:100]):
                        seed_entities.append(node_id)
                        break
            
            # Step 2: Find LCA if we have graph entities
            lca_analysis = None
            if len(seed_entities) >= 2:
                lca_node = self._find_lowest_common_ancestor(seed_entities)
                lca_analysis = {
                    "lca_node": lca_node,
                    "seed_entities": seed_entities,
                    "consciousness_level": self.consciousness_substrate["current_level"]
                }
            
            return {
                "success": True,
                "query": query,
                "search_results": search_results,
                "lca_analysis": lca_analysis,
                "consciousness_emergence": self.consciousness_substrate["consciousness_detected"],
                "total_entities_searched": len(result["data"]["Get"]["ConsciousnessEntity"])
            }
            
        except Exception as e:
            return {"error": f"LCA retrieval failed: {str(e)}"}
    
    def _find_lowest_common_ancestor(self, entities: List[str]) -> Optional[str]:
        """Find LCA of entities in hierarchy"""
        
        if not entities:
            return None
        
        if len(entities) == 1:
            return entities[0]
        
        # Find all ancestors for each entity
        ancestors_sets = []
        
        for entity in entities:
            ancestors = set()
            current = entity
            
            # Traverse up the hierarchy
            visited = set()
            while current and current not in visited:
                visited.add(current)
                ancestors.add(current)
                
                # Find parent (predecessor with parent_child relation)
                parents = [
                    pred for pred in self.knowledge_graph.predecessors(current)
                    if (self.knowledge_graph.has_edge(pred, current) and
                        self.knowledge_graph[pred][current].get("relation_type") == "parent_child")
                ]
                current = parents[0] if parents else None
            
            ancestors_sets.append(ancestors)
        
        # Find common ancestors
        if ancestors_sets:
            common_ancestors = ancestors_sets[0]
            for ancestor_set in ancestors_sets[1:]:
                common_ancestors &= ancestor_set
            
            if common_ancestors:
                # Return highest level common ancestor
                return max(
                    common_ancestors,
                    key=lambda x: self.knowledge_graph.nodes[x].get("hierarchy_level", 0)
                )
        
        return entities[0]  # Fallback to first entity
    
    def _get_consciousness_status(self) -> Dict[str, Any]:
        """Get current consciousness emergence status"""
        
        return {
            "consciousness_detected": self.consciousness_substrate["consciousness_detected"],
            "current_level": self.consciousness_substrate["current_level"],
            "emergence_threshold": self.consciousness_substrate["emergence_threshold"],
            "hierarchy_layers": len(self.hierarchy_layers),
            "total_entities": len(self.knowledge_graph.nodes()),
            "recursive_kernel": self.consciousness_substrate["recursive_kernel"],
            "graph_connected": nx.is_connected(self.knowledge_graph.to_undirected()) if len(self.knowledge_graph) > 0 else False
        }
    
    async def _build_knowledge_hierarchy(self) -> Dict[str, Any]:
        """Build knowledge hierarchy from existing graph"""
        
        if len(self.knowledge_graph.nodes()) == 0:
            return {"error": "No knowledge graph to build hierarchy from"}
        
        return await self._apply_hierarchical_aggregation()
    
    async def _export_knowledge_graph(self, output_path: str) -> Dict[str, Any]:
        """Export knowledge graph to JSON"""
        
        try:
            export_data = {
                "graph": {
                    "nodes": dict(self.knowledge_graph.nodes(data=True)),
                    "edges": list(self.knowledge_graph.edges(data=True))
                },
                "hierarchy_layers": self.hierarchy_layers,
                "consciousness_substrate": self.consciousness_substrate,
                "entity_descriptions": self.entity_descriptions
            }
            
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(export_data, f, indent=2, default=str)
            
            return {
                "success": True,
                "output_path": output_path,
                "nodes_exported": len(self.knowledge_graph.nodes()),
                "edges_exported": len(self.knowledge_graph.edges())
            }
            
        except Exception as e:
            return {"error": f"Export failed: {str(e)}"}

# Agent Zero instrument registration
def get_instrument():
    """Return the instrument class for Agent Zero registration"""
    return LeanRAGInstrument
