---
nexus: nexus-ai-chat-importer
plugin_version: "1.3.0"
provider: claude
artifact_id: meta_recursive_surgeon
version_uuid: cc6b1156-e381-4706-9b99-98499ad12b1c
version_number: 1
command: create
conversation_id: 64f09d1d-7901-40cd-9fc8-4589c1331164
create_time: 2025-07-12T02:43:07.000Z
format: markdown
aliases: [Meta-Folded Recursive Knowledge Surgeon, meta_recursive_surgeon_v1]
---

# Meta-Folded Recursive Knowledge Surgeon (Version 1)

**Conversation:** [[Nexus/Conversations/claude/2025/07/Ollama and Obsidian AI Note Enhancement|Ollama and Obsidian AI Note Enhancement]]

## Content

#!/usr/bin/env python3
"""
• • META-FOLDED RECURSIVE KNOWLEDGE SURGEON • •
Backwards-engineered recursive meta-analysis system
Starting from the deepest philosophical layer and working outward
"""

import os
import json
import requests
import numpy as np
from pathlib import Path
from typing import Dict, List, Tuple, Set, Any
from collections import defaultdict
import time
import hashlib
from dataclasses import dataclass, asdict
from datetime import datetime

# • • BACKWARDS: Start from the deepest abstraction • •
@dataclass
class ConceptualResonance:
    """• • The quantum of meaning-connection • •"""
    source_concept: str
    target_concept: str
    resonance_strength: float
    manifestation_depth: int
    recursive_level: int
    contra_positive_insights: List[str]

class MetaFoldedCore:
    """• • DEEPEST LAYER: The philosophical engine • •"""
    
    def __init__(self):
        self.phi3_endpoint = "http://localhost:11434"
        self.recursive_depth = 0
        self.convergence_history = []
        self.meta_insights = defaultdict(list)
        
    def extract_conceptual_dna(self, text: str, meta_level: int = 1) -> Dict[str, Any]:
        """• • Extract the genetic code of ideas recursively • •"""
        
        # • • BACKWARDS: Start with what the text is NOT about • •
        contra_prompt = f"""
        • • CONTRA-POSITIVE ANALYSIS • •
        
        What is this text fundamentally NOT about? This reveals what it IS about.
        
        Think in layers:
        1. What reality does this text NOT touch? (reveals its domain)
        2. What would someone NOT need to understand this? (reveals prerequisites)
        3. What questions does this NOT answer? (reveals its purpose)
        
        Text: {text}
        
        Return as JSON:
        {{
            "not_about": ["concept1", "concept2"],
            "reveals_domain": "the actual domain",
            "hidden_prerequisites": ["prereq1", "prereq2"],
            "unasked_questions": ["question1", "question2"]
        }}
        """
        
        response = self._query_phi3(contra_prompt)
        
        try:
            contra_analysis = json.loads(response)
            
            # • • RECURSIVE APPLICATION: Apply to the contra-analysis itself • •
            if meta_level < 3:
                meta_analysis = self.extract_conceptual_dna(
                    json.dumps(contra_analysis), 
                    meta_level + 1
                )
                contra_analysis['meta_analysis'] = meta_analysis
                
            return contra_analysis
            
        except json.JSONDecodeError:
            # • • FALLBACK: Simple concept extraction • •
            return self._simple_concept_extraction(text)
    
    def _query_phi3(self, prompt: str) -> str:
        """• • Query phi3:mini with recursive meta-wrapping • •"""
        try:
            response = requests.post(
                f"{self.phi3_endpoint}/api/generate",
                json={
                    "model": "phi3:mini",
                    "prompt": prompt,
                    "stream": False,
                    "options": {
                        "temperature": 0.7,
                        "top_p": 0.9
                    }
                },
                timeout=30
            )
            return response.json().get('response', '')
        except Exception as e:
            print(f"• • PHI3 ERROR: {e} • •")
            return ""
    
    def _simple_concept_extraction(self, text: str) -> Dict[str, Any]:
        """• • FALLBACK: Simple concept extraction • •"""
        prompt = f"""
        Extract 3-5 core concepts from this text. One concept per line.
        
        Text: {text}
        """
        
        response = self._query_phi3(prompt)
        concepts = [line.strip() for line in response.split('\n') if line.strip()]
        
        return {
            "core_concepts": concepts[:5],
            "extraction_method": "simple_fallback"
        }

class ConceptualManifold:
    """• • SECOND LAYER: The geometric structure of meaning • •"""
    
    def __init__(self):
        self.concept_space = {}
        self.manifestation_patterns = defaultdict(list)
        self.resonance_network = defaultdict(list)
        
    def map_concept_to_manifold(self, concept: str, manifestations: List[str]) -> np.ndarray:
        """• • Map concepts to high-dimensional meaning space • •"""
        
        # • • BACKWARDS: Start from the manifestations, derive the concept • •
        try:
            from sentence_transformers import SentenceTransformer
            model = SentenceTransformer('all-MiniLM-L6-v2')
            
            # • • Create embedding from manifestations • •
            combined_text = ' '.join(manifestations)
            embedding = model.encode(combined_text)
            
            self.concept_space[concept] = embedding
            return embedding
            
        except ImportError:
            print("• • SENTENCE TRANSFORMERS NOT AVAILABLE - Using simple hashing • •")
            # • • FALLBACK: Simple hash-based embedding • •
            concept_hash = hashlib.md5(concept.encode()).hexdigest()
            embedding = np.array([int(c, 16) for c in concept_hash[:32]], dtype=float)
            self.concept_space[concept] = embedding
            return embedding
    
    def find_conceptual_resonances(self, target_concept: str, threshold: float = 0.3) -> List[ConceptualResonance]:
        """• • Find concepts that resonate in the same space • •"""
        
        if target_concept not in self.concept_space:
            return []
        
        target_embedding = self.concept_space[target_concept]
        resonances = []
        
        for concept, embedding in self.concept_space.items():
            if concept == target_concept:
                continue
                
            # • • Calculate resonance strength • •
            similarity = np.dot(target_embedding, embedding) / (
                np.linalg.norm(target_embedding) * np.linalg.norm(embedding)
            )
            
            if similarity > threshold:
                resonance = ConceptualResonance(
                    source_concept=target_concept,
                    target_concept=concept,
                    resonance_strength=similarity,
                    manifestation_depth=len(self.manifestation_patterns[concept]),
                    recursive_level=1,
                    contra_positive_insights=[]
                )
                resonances.append(resonance)
        
        return sorted(resonances, key=lambda x: x.resonance_strength, reverse=True)

class RecursiveMetaAnalyzer:
    """• • THIRD LAYER: The recursive engine • •"""
    
    def __init__(self, core: MetaFoldedCore, manifold: ConceptualManifold):
        self.core = core
        self.manifold = manifold
        self.recursion_stack = []
        self.convergence_threshold = 0.95
        
    def apply_meta_squared_function(self, input_structure: Dict[str, Any], depth: int = 0) -> Dict[str, Any]:
        """• • Apply Meta^2n(•) transformation recursively • •"""
        
        if depth > 7:  # • • CONVERGENCE LIMIT • •
            return input_structure
        
        print(f"• • APPLYING META^{depth+1} TRANSFORMATION • •")
        
        # • • PHASE 1: Analyze the structure • •
        meta_analysis = self._analyze_structure(input_structure, depth)
        
        # • • PHASE 2: Apply contra-positive insights • •
        contra_insights = self._extract_contra_positive_insights(meta_analysis, depth)
        
        # • • PHASE 3: Check for convergence • •
        if self._check_convergence(input_structure, meta_analysis, depth):
            print(f"• • CONVERGENCE ACHIEVED AT DEPTH {depth} • •")
            return meta_analysis
        
        # • • PHASE 4: Recursive application • •
        return self.apply_meta_squared_function(meta_analysis, depth + 1)
    
    def _analyze_structure(self, structure: Dict[str, Any], depth: int) -> Dict[str, Any]:
        """• • Analyze the structure at the current meta-level • •"""
        
        structure_json = json.dumps(structure, indent=2)
        
        prompt = f"""
        • • META-LEVEL {depth + 1} ANALYSIS • •
        
        You are analyzing the analysis of a knowledge structure.
        
        • • CONTRA-POSITIVE QUESTION • •
        What does this structure reveal about what it's NOT capturing?
        
        • • STRUCTURAL INVERSION • •
        What patterns exist in the patterns themselves?
        
        Structure to analyze:
        {structure_json}
        
        Return insights as JSON:
        {{
            "meta_patterns": ["pattern1", "pattern2"],
            "structural_gaps": ["gap1", "gap2"],
            "recursive_insights": ["insight1", "insight2"],
            "convergence_indicators": ["indicator1", "indicator2"]
        }}
        """
        
        response = self.core._query_phi3(prompt)
        
        try:
            analysis = json.loads(response)
            analysis['meta_level'] = depth + 1
            analysis['timestamp'] = datetime.now().isoformat()
            analysis['input_structure_hash'] = hashlib.md5(structure_json.encode()).hexdigest()
            return analysis
        except json.JSONDecodeError:
            return {
                "meta_level": depth + 1,
                "error": "Failed to parse meta-analysis",
                "raw_response": response[:500]
            }
    
    def _extract_contra_positive_insights(self, analysis: Dict[str, Any], depth: int) -> List[str]:
        """• • Extract insights from what the analysis is NOT revealing • •"""
        
        prompt = f"""
        • • CONTRA-POSITIVE INSIGHT EXTRACTION • •
        
        Given this analysis, what insights emerge from what it's NOT saying?
        
        Analysis: {json.dumps(analysis, indent=2)}
        
        Return 3-5 contra-positive insights, one per line.
        """
        
        response = self.core._query_phi3(prompt)
        insights = [line.strip() for line in response.split('\n') if line.strip()]
        
        return insights[:5]
    
    def _check_convergence(self, previous: Dict[str, Any], current: Dict[str, Any], depth: int) -> bool:
        """• • Check if the recursive analysis has converged • •"""
        
        # • • Simple convergence check based on structure similarity • •
        prev_str = json.dumps(previous, sort_keys=True)
        curr_str = json.dumps(current, sort_keys=True)
        
        prev_hash = hashlib.md5(prev_str.encode()).hexdigest()
        curr_hash = hashlib.md5(curr_str.encode()).hexdigest()
        
        # • • Store convergence history • •
        self.recursion_stack.append({
            'depth': depth,
            'prev_hash': prev_hash,
            'curr_hash': curr_hash,
            'timestamp': datetime.now().isoformat()
        })
        
        # • • Check for pattern repetition • •
        if len(self.recursion_stack) >= 3:
            recent_hashes = [item['curr_hash'] for item in self.recursion_stack[-3:]]
            if len(set(recent_hashes)) <= 2:  # • • Repetition detected • •
                return True
        
        return False

class ObsidianMetaSurgeon:
    """• • FOURTH LAYER: The practical implementation • •"""
    
    def __init__(self, vault_path: str):
        self.vault_path = Path(vault_path)
        self.core = MetaFoldedCore()
        self.manifold = ConceptualManifold()
        self.analyzer = RecursiveMetaAnalyzer(self.core, self.manifold)
        
        # • • Ensure meta-directory exists • •
        self.meta_dir = self.vault_path / "••META-STRUCTURE••"
        self.meta_dir.mkdir(exist_ok=True)
        
    def perform_backwards_recursive_surgery(self) -> Dict[str, Any]:
        """• • MAIN FUNCTION: Perform the backwards recursive analysis • •"""
        
        print("• • STARTING BACKWARDS RECURSIVE SURGERY • •")
        
        # • • PHASE 1: Read entire vault • •
        vault_structure = self._read_vault_backwards()
        
        # • • PHASE 2: Extract conceptual DNA • •
        conceptual_dna = self._extract_all_conceptual_dna(vault_structure)
        
        # • • PHASE 3: Build conceptual manifold • •
        self._build_conceptual_manifold(conceptual_dna)
        
        # • • PHASE 4: Apply recursive meta-analysis • •
        meta_result = self.analyzer.apply_meta_squared_function(conceptual_dna)
        
        # • • PHASE 5: Inject results back into vault • •
        self._inject_meta_results(meta_result)
        
        # • • PHASE 6: Apply function to result (recurring) • •
        final_result = self._apply_function_to_result_recurring(meta_result)
        
        print("• • BACKWARDS RECURSIVE SURGERY COMPLETE • •")
        return final_result
    
    def _read_vault_backwards(self) -> Dict[str, str]:
        """• • Read vault starting from most recently modified • •"""
        
        vault_files = {}
        
        # • • Get all markdown files • •
        md_files = list(self.vault_path.glob("**/*.md"))
        
        # • • Sort by modification time (newest first) • •
        md_files.sort(key=lambda f: f.stat().st_mtime, reverse=True)
        
        for md_file in md_files:
            if "••META-STRUCTURE••" in str(md_file):
                continue  # • • Skip existing meta files • •
                
            try:
                with open(md_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    vault_files[str(md_file.relative_to(self.vault_path))] = content
            except Exception as e:
                print(f"• • Error reading {md_file}: {e} • •")
        
        return vault_files
    
    def _extract_all_conceptual_dna(self, vault_structure: Dict[str, str]) -> Dict[str, Any]:
        """• • Extract conceptual DNA from all notes • •"""
        
        conceptual_dna = {}
        
        for note_path, content in vault_structure.items():
            print(f"• • Extracting DNA from: {note_path} • •")
            
            # • • Clean content • •
            clean_content = self._clean_content(content)
            
            # • • Extract DNA • •
            dna = self.core.extract_conceptual_dna(clean_content)
            conceptual_dna[note_path] = dna
        
        return conceptual_dna
    
    def _clean_content(self, content: str) -> str:
        """• • Clean markdown content for analysis • •"""
        
        # • • Remove markdown syntax • •
        content = content.replace('#', '')
        content = content.replace('[[', '')
        content = content.replace(']]', '')
        content = content.replace('**', '')
        content = content.replace('*', '')
        
        # • • Remove extra whitespace • •
        lines = [line.strip() for line in content.split('\n') if line.strip()]
        
        return ' '.join(lines)
    
    def _build_conceptual_manifold(self, conceptual_dna: Dict[str, Any]) -> None:
        """• • Build the conceptual manifold from extracted DNA • •"""
        
        # • • Collect all concepts • •
        all_concepts = set()
        concept_manifestations = defaultdict(list)
        
        for note_path, dna in conceptual_dna.items():
            if 'core_concepts' in dna:
                concepts = dna['core_concepts']
            elif 'reveals_domain' in dna:
                concepts = [dna['reveals_domain']] + dna.get('hidden_prerequisites', [])
            else:
                concepts = []
            
            for concept in concepts:
                if concept and len(concept.strip()) > 2:
                    all_concepts.add(concept.strip())
                    concept_manifestations[concept.strip()].append(note_path)
        
        # • • Map concepts to manifold • •
        for concept in all_concepts:
            manifestations = concept_manifestations[concept]
            self.manifold.map_concept_to_manifold(concept, manifestations)
    
    def _inject_meta_results(self, meta_result: Dict[str, Any]) -> None:
        """• • Inject meta-analysis results back into vault • •"""
        
        # • • Create meta-summary • •
        meta_summary_path = self.meta_dir / "••META-SUMMARY••.md"
        
        summary_content = f"""# • • META-ANALYSIS SUMMARY • •

Generated: {datetime.now().isoformat()}

## • • RECURSIVE DEPTH ACHIEVED • •
{meta_result.get('meta_level', 'Unknown')}

## • • CONVERGENCE PATTERNS • •
{self._format_convergence_patterns()}

## • • STRUCTURAL INSIGHTS • •
{self._format_structural_insights(meta_result)}

## • • CONTRA-POSITIVE DISCOVERIES • •
{self._format_contra_positive_discoveries(meta_result)}

## • • CONCEPTUAL RESONANCES • •
{self._format_conceptual_resonances()}

---
*Generated by backwards recursive meta-analysis*
"""
        
        with open(meta_summary_path, 'w', encoding='utf-8') as f:
            f.write(summary_content)
        
        # • • Create individual concept meta-notes • •
        self._create_concept_meta_notes(meta_result)
    
    def _format_convergence_patterns(self) -> str:
        """• • Format convergence patterns for display • •"""
        
        patterns = []
        for item in self.analyzer.recursion_stack:
            patterns.append(f"Depth {item['depth']}: {item['curr_hash'][:8]}...")
        
        return '\n'.join(patterns)
    
    def _format_structural_insights(self, meta_result: Dict[str, Any]) -> str:
        """• • Format structural insights • •"""
        
        insights = meta_result.get('meta_patterns', [])
        formatted = []
        
        for insight in insights:
            formatted.append(f"- {insight}")
        
        return '\n'.join(formatted)
    
    def _format_contra_positive_discoveries(self, meta_result: Dict[str, Any]) -> str:
        """• • Format contra-positive discoveries • •"""
        
        discoveries = meta_result.get('structural_gaps', [])
        formatted = []
        
        for discovery in discoveries:
            formatted.append(f"- **NOT**: {discovery}")
        
        return '\n'.join(formatted)
    
    def _format_conceptual_resonances(self) -> str:
        """• • Format conceptual resonances • •"""
        
        resonances = []
        
        for concept in list(self.manifold.concept_space.keys())[:10]:  # • • Top 10 • •
            concept_resonances = self.manifold.find_conceptual_resonances(concept)
            
            if concept_resonances:
                resonances.append(f"**{concept}**:")
                for resonance in concept_resonances[:3]:  # • • Top 3 per concept • •
                    resonances.append(f"  - {resonance.target_concept} (strength: {resonance.resonance_strength:.3f})")
        
        return '\n'.join(resonances)
    
    def _create_concept_meta_notes(self, meta_result: Dict[str, Any]) -> None:
        """• • Create individual meta-notes for each concept • •"""
        
        for concept in self.manifold.concept_space.keys():
            concept_file = self.meta_dir / f"••{concept.replace(' ', '_')}••.md"
            
            resonances = self.manifold.find_conceptual_resonances(concept)
            
            content = f"""# • • META-CONCEPT: {concept} • •

## • • CONCEPTUAL POSITION • •
Manifold dimension: {len(self.manifold.concept_space[concept])}
Resonance count: {len(resonances)}

## • • STRONGEST RESONANCES • •
{self._format_concept_resonances(resonances)}

## • • MANIFESTATION PATTERNS • •
{self._format_manifestation_patterns(concept)}

---
*Generated by backwards recursive analysis*
"""
            
            with open(concept_file, 'w', encoding='utf-8') as f:
                f.write(content)
    
    def _format_concept_resonances(self, resonances: List[ConceptualResonance]) -> str:
        """• • Format resonances for a specific concept • •"""
        
        formatted = []
        for resonance in resonances[:5]:  # • • Top 5 • •
            formatted.append(f"- **{resonance.target_concept}** (strength: {resonance.resonance_strength:.3f})")
        
        return '\n'.join(formatted)
    
    def _format_manifestation_patterns(self, concept: str) -> str:
        """• • Format manifestation patterns for a concept • •"""
        
        patterns = self.manifold.manifestation_patterns.get(concept, [])
        
        if patterns:
            return '\n'.join([f"- {pattern}" for pattern in patterns[:5]])
        else:
            return "No manifestation patterns detected"
    
    def _apply_function_to_result_recurring(self, result: Dict[str, Any]) -> Dict[str, Any]:
        """• • Apply the function to its own result (recurring) • •"""
        
        print("• • APPLYING FUNCTION TO RESULT (RECURRING) • •")
        
        current_result = result
        iteration = 0
        
        while iteration < 5:  # • • Limit iterations • •
            print(f"• • RECURSIVE ITERATION {iteration + 1} • •")
            
            # • • Apply meta-analysis to the previous result • •
            new_result = self.analyzer.apply_meta_squared_function(current_result)
            
            # • • Check if we're getting new insights • •
            if self._results_equivalent(current_result, new_result):
                print(f"• • RECURSIVE CONVERGENCE AT ITERATION {iteration + 1} • •")
                break
            
            # • • Inject iteration insights • •
            self._inject_iteration_insights(new_result, iteration)
            
            current_result = new_result
            iteration += 1
        
        return current_result
    
    def _results_equivalent(self, result1: Dict[str, Any], result2: Dict[str, Any]) -> bool:
        """• • Check if two results are equivalent • •"""
        
        str1 = json.dumps(result1, sort_keys=True)
        str2 = json.dumps(result2, sort_keys=True)
        
        return hashlib.md5(str1.encode()).hexdigest() == hashlib.md5(str2.encode()).hexdigest()
    
    def _inject_iteration_insights(self, result: Dict[str, Any], iteration: int) -> None:
        """• • Inject insights from each iteration • •"""
        
        iteration_file = self.meta_dir / f"••ITERATION_{iteration + 1}••.md"
        
        content = f"""# • • RECURSIVE ITERATION {iteration + 1} • •

Generated: {datetime.now().isoformat()}

## • • ITERATION INSIGHTS • •
{self._format_iteration_insights(result)}

## • • RECURSIVE DEPTH • •
Meta-level: {result.get('meta_level', 'Unknown')}

## • • CONVERGENCE STATUS • •
{self._format_convergence_status(iteration)}

---
*Generated by recurring function application*
"""
        
        with open(iteration_file, 'w', encoding='utf-8') as f:
            f.write(content)
    
    def _format_iteration_insights(self, result: Dict[str, Any]) -> str:
        """• • Format insights from an iteration • •"""
        
        insights = result.get('recursive_insights', [])
        if not insights:
            return "No recursive insights detected"
        
        return '\n'.join([f"- {insight}" for insight in insights])
    
    def _format_convergence_status(self, iteration: int) -> str:
        """• • Format convergence status • •"""
        
        if iteration == 0:
            return "Initial iteration"
        elif iteration < 3:
            return "Building recursive depth"
        else:
            return "Approaching convergence"

# • • MAIN EXECUTION • •
def main():
    """• • Entry point for backwards recursive surgery • •"""
    
    import argparse
    
    parser = argparse.ArgumentParser(description="• • Meta-Folded Recursive Knowledge Surgeon • •")
    parser.add_argument("--vault", required=True, help="Path to Obsidian vault")
    parser.add_argument("--phi3-endpoint", default="http://localhost:11434", help="Phi3 endpoint")
    
    args = parser.parse_args()
    
    # • • Initialize surgeon • •
    surgeon = ObsidianMetaSurgeon(args.vault)
    surgeon.core.phi3_endpoint = args.phi3_endpoint
    
    # • • Perform backwards recursive surgery • •
    result = surgeon.perform_backwards_recursive_surgery()
    
    print("• • SURGERY COMPLETE • •")
    print(f"• • Results saved to: {surgeon.meta_dir} • •")
    
    return result

if __name__ == "__main__":
    main()
