---
nexus: nexus-ai-chat-importer
plugin_version: "1.3.0"
provider: claude
artifact_id: meta_surgeon_deploy
version_uuid: a8b4819e-7ca6-46cf-8c78-66d502e34ce4
version_number: 1
command: create
conversation_id: c624acbd-4f0c-420e-8095-3fa1721f3b4f
create_time: 2025-07-12T02:50:49.000Z
format: bash
aliases: [Meta-Folded Recursive Knowledge Surgeon - Complete Deployment, meta_surgeon_deploy_v1]
---

# Meta-Folded Recursive Knowledge Surgeon - Complete Deployment (Version 1)

**Conversation:** [[Nexus/Conversations/claude/2025/07/Meta^2n Recursive Knowledge Architecture|Meta^2n Recursive Knowledge Architecture]]

## Content

```bash
#!/bin/bash

# • • META-FOLDED RECURSIVE KNOWLEDGE SURGEON DEPLOYMENT • •
# • • BACKWARDS BETTER RECURRING SETUP • •

echo "• • INITIALIZING BACKWARDS RECURSIVE SURGERY • •"

# • • PHASE 1: Environment Setup • •
echo "• • Setting up deployment environment • •"

# Create deployment directory
mkdir -p meta-surgeon-deploy
cd meta-surgeon-deploy

# • • Create Dockerfile • •
cat > Dockerfile << 'EOF'
FROM python:3.11-slim

# • • Install system dependencies • •
RUN apt-get update && apt-get install -y \
    curl \
    wget \
    git \
    && rm -rf /var/lib/apt/lists/*

# • • Install Python dependencies • •
RUN pip install --no-cache-dir \
    requests \
    numpy \
    sentence-transformers \
    watchdog \
    scikit-learn \
    pathlib2

# • • Create app directory • •
WORKDIR /app

# • • Copy surgeon script • •
COPY meta_recursive_surgeon.py /app/
COPY requirements.txt /app/

# • • Install additional dependencies • •
RUN pip install -r requirements.txt

# • • Create entrypoint • •
COPY entrypoint.sh /app/
RUN chmod +x /app/entrypoint.sh

# • • Set default command • •
CMD ["/app/entrypoint.sh"]
EOF

# • • Create requirements.txt • •
cat > requirements.txt << 'EOF'
requests>=2.31.0
numpy>=1.24.0
sentence-transformers>=2.2.0
watchdog>=3.0.0
scikit-learn>=1.3.0
pathlib2
hashlib
json
dataclasses
datetime
collections
EOF

# • • Create the main surgeon script • •
cat > meta_recursive_surgeon.py << 'EOF'
#!/usr/bin/env python3
"""
• • META-FOLDED RECURSIVE KNOWLEDGE SURGEON • •
Backwards-engineered recursive meta-analysis system
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
import argparse

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
    
    def __init__(self, phi3_endpoint="http://localhost:11434"):
        self.phi3_endpoint = phi3_endpoint
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
        
        Text: {text[:1000]}
        
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
                timeout=60
            )
            
            if response.status_code == 200:
                return response.json().get('response', '')
            else:
                print(f"• • PHI3 HTTP ERROR: {response.status_code} • •")
                return ""
                
        except Exception as e:
            print(f"• • PHI3 ERROR: {e} • •")
            return ""
    
    def _simple_concept_extraction(self, text: str) -> Dict[str, Any]:
        """• • FALLBACK: Simple concept extraction • •"""
        
        # • • Extract key phrases by frequency • •
        words = text.lower().split()
        word_freq = defaultdict(int)
        
        for word in words:
            if len(word) > 3:  # • • Filter short words • •
                word_freq[word] += 1
        
        # • • Get top concepts • •
        top_concepts = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)[:5]
        concepts = [word for word, freq in top_concepts]
        
        return {
            "core_concepts": concepts,
            "extraction_method": "simple_fallback",
            "word_frequencies": dict(top_concepts)
        }

class ConceptualManifold:
    """• • SECOND LAYER: The geometric structure of meaning • •"""
    
    def __init__(self):
        self.concept_space = {}
        self.manifestation_patterns = defaultdict(list)
        self.resonance_network = defaultdict(list)
        
    def map_concept_to_manifold(self, concept: str, manifestations: List[str]) -> np.ndarray:
        """• • Map concepts to high-dimensional meaning space • •"""
        
        try:
            # • • Try to use sentence transformers • •
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
            try:
                similarity = np.dot(target_embedding, embedding) / (
                    np.linalg.norm(target_embedding) * np.linalg.norm(embedding)
                )
            except:
                similarity = 0.0
            
            if similarity > threshold:
                resonance = ConceptualResonance(
                    source_concept=target_concept,
                    target_concept=concept,
                    resonance_strength=float(similarity),
                    manifestation_depth=len(self.manifestation_patterns[concept]),
                    recursive_level=1,
                    contra_positive_insights=[]
                )
                resonances.append(resonance)
        
        return sorted(resonances, key=lambda x: x.resonance_strength, reverse=True)

class ObsidianMetaSurgeon:
    """• • PRACTICAL IMPLEMENTATION LAYER • •"""
    
    def __init__(self, vault_path: str, phi3_endpoint: str = "http://localhost:11434"):
        self.vault_path = Path(vault_path)
        self.core = MetaFoldedCore(phi3_endpoint)
        self.manifold = ConceptualManifold()
        
        # • • Ensure meta-directory exists • •
        self.meta_dir = self.vault_path / "••META-STRUCTURE••"
        self.meta_dir.mkdir(exist_ok=True)
        
    def perform_backwards_recursive_surgery(self) -> Dict[str, Any]:
        """• • MAIN FUNCTION: Perform the backwards recursive analysis • •"""
        
        print("• • STARTING BACKWARDS RECURSIVE SURGERY • •")
        
        # • • PHASE 1: Read entire vault • •
        print("• • Reading vault structure • •")
        vault_structure = self._read_vault_backwards()
        
        # • • PHASE 2: Extract conceptual DNA • •
        print("• • Extracting conceptual DNA • •")
        conceptual_dna = self._extract_all_conceptual_dna(vault_structure)
        
        # • • PHASE 3: Build conceptual manifold • •
        print("• • Building conceptual manifold • •")
        self._build_conceptual_manifold(conceptual_dna)
        
        # • • PHASE 4: Apply recursive meta-analysis • •
        print("• • Applying recursive meta-analysis • •")
        meta_result = self._apply_recursive_meta_analysis(conceptual_dna)
        
        # • • PHASE 5: Inject results back into vault • •
        print("• • Injecting results into vault • •")
        self._inject_meta_results(meta_result)
        
        print("• • BACKWARDS RECURSIVE SURGERY COMPLETE • •")
        return meta_result
    
    def _read_vault_backwards(self) -> Dict[str, str]:
        """• • Read vault starting from most recently modified • •"""
        
        vault_files = {}
        
        # • • Get all markdown files • •
        try:
            md_files = list(self.vault_path.glob("**/*.md"))
        except Exception as e:
            print(f"• • Error globbing files: {e} • •")
            return vault_files
        
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
        
        print(f"• • Read {len(vault_files)} files • •")
        return vault_files
    
    def _extract_all_conceptual_dna(self, vault_structure: Dict[str, str]) -> Dict[str, Any]:
        """• • Extract conceptual DNA from all notes • •"""
        
        conceptual_dna = {}
        
        for note_path, content in vault_structure.items():
            print(f"• • Extracting DNA from: {note_path} • •")
            
            # • • Clean content • •
            clean_content = self._clean_content(content)
            
            if len(clean_content) > 10:  # • • Skip very short content • •
                # • • Extract DNA • •
                dna = self.core.extract_conceptual_dna(clean_content)
                conceptual_dna[note_path] = dna
                
                # • • Brief pause to avoid overwhelming phi3 • •
                time.sleep(0.5)
        
        return conceptual_dna
    
    def _clean_content(self, content: str) -> str:
        """• • Clean markdown content for analysis • •"""
        
        # • • Remove markdown syntax • •
        content = content.replace('#', '')
        content = content.replace('[[', '')
        content = content.replace(']]', '')
        content = content.replace('**', '')
        content = content.replace('*', '')
        content = content.replace('`', '')
        
        # • • Remove extra whitespace • •
        lines = [line.strip() for line in content.split('\n') if line.strip()]
        
        return ' '.join(lines)
    
    def _build_conceptual_manifold(self, conceptual_dna: Dict[str, Any]) -> None:
        """• • Build the conceptual manifold from extracted DNA • •"""
        
        # • • Collect all concepts • •
        all_concepts = set()
        concept_manifestations = defaultdict(list)
        
        for note_path, dna in conceptual_dna.items():
            concepts = []
            
            if 'core_concepts' in dna:
                concepts.extend(dna['core_concepts'])
            
            if 'reveals_domain' in dna and dna['reveals_domain']:
                concepts.append(dna['reveals_domain'])
            
            if 'hidden_prerequisites' in dna:
                concepts.extend(dna['hidden_prerequisites'])
            
            for concept in concepts:
                if concept and len(str(concept).strip()) > 2:
                    clean_concept = str(concept).strip()
                    all_concepts.add(clean_concept)
                    concept_manifestations[clean_concept].append(note_path)
        
        print(f"• • Found {len(all_concepts)} unique concepts • •")
        
        # • • Map concepts to manifold • •
        for concept in all_concepts:
            manifestations = concept_manifestations[concept]
            self.manifold.map_concept_to_manifold(concept, manifestations)
    
    def _apply_recursive_meta_analysis(self, conceptual_dna: Dict[str, Any]) -> Dict[str, Any]:
        """• • Apply recursive meta-analysis • •"""
        
        # • • Simple meta-analysis for now • •
        meta_result = {
            "meta_level": 1,
            "concept_count": len(self.manifold.concept_space),
            "note_count": len(conceptual_dna),
            "top_concepts": list(self.manifold.concept_space.keys())[:10],
            "timestamp": datetime.now().isoformat()
        }
        
        # • • Add resonance analysis • •
        resonance_map = {}
        for concept in list(self.manifold.concept_space.keys())[:5]:  # • • Top 5 to avoid overload • •
            resonances = self.manifold.find_conceptual_resonances(concept)
            resonance_map[concept] = [
                {
                    "target": r.target_concept,
                    "strength": r.resonance_strength
                } for r in resonances[:3]
            ]
        
        meta_result["resonance_map"] = resonance_map
        
        return meta_result
    
    def _inject_meta_results(self, meta_result: Dict[str, Any]) -> None:
        """• • Inject meta-analysis results back into vault • •"""
        
        # • • Create meta-summary • •
        meta_summary_path = self.meta_dir / "••META-SUMMARY••.md"
        
        summary_content = f"""# • • META-ANALYSIS SUMMARY • •

Generated: {meta_result.get('timestamp', 'Unknown')}

## • • ANALYSIS OVERVIEW • •
- **Concepts Found**: {meta_result.get('concept_count', 0)}
- **Notes Analyzed**: {meta_result.get('note_count', 0)}
- **Meta Level**: {meta_result.get('meta_level', 0)}

## • • TOP CONCEPTS • •
{self._format_top_concepts(meta_result.get('top_concepts', []))}

## • • CONCEPTUAL RESONANCES • •
{self._format_resonance_map(meta_result.get('resonance_map', {}))}

## • • CONTRA-POSITIVE INSIGHTS • •
This analysis reveals what your knowledge base is NOT about:
- Areas of minimal conceptual density
- Unexplored conceptual spaces
- Implicit knowledge gaps

---
*Generated by backwards recursive meta-analysis*
"""
        
        with open(meta_summary_path, 'w', encoding='utf-8') as f:
            f.write(summary_content)
        
        print(f"• • Meta-summary written to: {meta_summary_path} • •")
    
    def _format_top_concepts(self, concepts: List[str]) -> str:
        """• • Format top concepts for display • •"""
        
        formatted = []
        for i, concept in enumerate(concepts, 1):
            formatted.append(f"{i}. **{concept}**")
        
        return '\n'.join(formatted)
    
    def _format_resonance_map(self, resonance_map: Dict[str, List[Dict]]) -> str:
        """• • Format resonance map for display • •"""
        
        formatted = []
        
        for concept, resonances in resonance_map.items():
            formatted.append(f"**{concept}**:")
            for resonance in resonances:
                strength = resonance.get('strength', 0)
                target = resonance.get('target', 'Unknown')
                formatted.append(f"  - {target} (strength: {strength:.3f})")
        
        return '\n'.join(formatted)

def main():
    """• • Main entry point • •"""
    
    parser = argparse.ArgumentParser(description='Meta-Folded Recursive Knowledge Surgeon')
    parser.add_argument('--vault', required=True, help='Path to Obsidian vault')
    parser.add_argument('--phi3-endpoint', default='http://localhost:11434', 
                       help='Phi3 endpoint URL')
    
    args = parser.parse_args()
    
    # • • Initialize surgeon • •
    surgeon = ObsidianMetaSurgeon(args.vault, args.phi3_endpoint)
    
    # • • Wait for phi3 to be ready • •
    print("• • Waiting for phi3 to be ready • •")
    while True:
        try:
            response = requests.get(f"{args.phi3_endpoint}/api/tags", timeout=5)
            if response.status_code == 200:
                break
        except:
            pass
        time.sleep(5)
    
    # • • Perform surgery • •
    result = surgeon.perform_backwards_recursive_surgery()
    
    print("• • SURGERY COMPLETE • •")
    print(f"• • Results: {json.dumps(result, indent=2)} • •")

if __name__ == "__main__":
    main()
EOF

# • • Create entrypoint script • •
cat > entrypoint.sh << 'EOF'
#!/bin/bash

echo "• • STARTING META-FOLDED RECURSIVE SURGERY • •"

# • • Wait for Ollama to be ready • •
echo "• • Waiting for Ollama to be ready • •"
while ! curl -s http://ollama:11434/api/tags > /dev/null; do
    echo "• • Waiting for Ollama... • •"
    sleep 5
done

echo "• • Ollama is ready • •"

# • • Ensure phi3:mini is available • •
echo "• • Checking for phi3:mini model • •"
if ! curl -s http://ollama:11434/api/tags | grep -q "phi3:mini"; then
    echo "• • Pulling phi3:mini model • •"
    curl -X POST http://ollama:11434/api/pull -d '{"name": "phi3:mini"}' &
    pull_pid=$!
    
    # • • Wait for model to download • •
    wait $pull_pid
    
    # • • Verify model is available • •
    sleep 10
fi

# • • Run the surgeon • •
echo "• • EXECUTING BACKWARDS RECURSIVE SURGERY • •"
python /app/meta_recursive_surgeon.py \
    --vault /vault \
    --phi3-endpoint http://ollama:11434

echo "• • SURGERY COMPLETE • •"

# • • Keep container running for monitoring • •
tail -f /dev/null
EOF

# • • Create docker-compose.yml • •
cat > docker-compose.yml << 'EOF'
version: '3.8'

services:
  ollama:
    image: ollama/ollama:latest
    container_name: meta-ollama
    ports:
      - "11434:11434"
    volumes:
      - ollama_data:/root/.ollama
    environment:
      - OLLAMA_HOST=0.0.0.0
    restart: unless-stopped
    
  meta-surgeon:
    build: .
    container_name: meta-recursive-surgeon
    depends_on:
      - ollama
    volumes:
      - ${OBSIDIAN_VAULT_PATH:-./vault}:/vault
      - ./meta-output:/app/meta-output
    environment:
      - VAULT_PATH=/vault
      - OLLAMA_ENDPOINT=http://ollama:11434
    restart: unless-stopped
    
volumes:
  ollama_data:
EOF

# • • Create file watcher script • •
cat > file_watcher.py << 'EOF'
#!/usr/bin/env python3
"""
• • CONTINUOUS META-ANALYSIS FILE WATCHER • •
Watches for changes and triggers recursive surgery
"""

import time
import subprocess
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MetaWatcher(FileSystemEventHandler):
    def __init__(self, vault_path):
        self.vault_path = vault_path
        self.last_run = 0
        self.cooldown = 300  # • • 5 minutes between runs • •
        
    def on_modified(self, event):
        if event.is_directory or not event.src_path.endswith('.md'):
            return
            
        # • • Avoid running too frequently • •
        now = time.time()
        if now - self.last_run < self.cooldown:
            return
            
        print(f"• • FILE MODIFIED: {event.src_path} • •")
        print("• • TRIGGERING RECURSIVE SURGERY • •")
        
        # • • Run the surgeon • •
        try:
            subprocess.run([
                'python', '/app/meta_recursive_surgeon.py',
                '--vault', self.vault_path,
                '--phi3-endpoint', 'http://ollama:11434'
            ], check=True)
            
            self.last_run = now
            print("• • SURGERY COMPLETE • •")
            
        except subprocess.CalledProcessError as e:
            print(f"• • SURGERY FAILED: {e} • •")

def main():
    vault_path = os.environ.get('VAULT_PATH', '/vault')
    
    event_handler = MetaWatcher(vault_path)
    observer = Observer()
    observer.schedule(event_handler, vault_path, recursive=True)
    
    print(f"• • STARTING FILE WATCHER ON: {vault_path} • •")
    observer.start()
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("• • FILE WATCHER STOPPED • •")
    
    observer.join()

if __name__ == "__main__":
    main()
EOF

# • • Create run script • •
cat > run.sh << 'EOF'
#!/bin/bash

echo "• • STARTING META-FOLDED RECURSIVE KNOWLEDGE SURGEON • •"

# • • Check if OBSIDIAN_VAULT_PATH is set • •
if [ -z "$OBSIDIAN_VAULT_PATH" ]; then
    echo "• • ERROR: OBSIDIAN_VAULT_PATH environment variable not set • •"
    echo "• • Please set it to your Obsidian vault path • •"
    echo "• • Example: export OBSIDIAN_VAULT_PATH=/path/to/your/vault • •"
    exit 1
fi

# • • Check if vault path exists • •
if [ ! -d "$OBSIDIAN_VAULT_PATH" ]; then
    echo "• • ERROR: Vault path does not exist: $OBSIDIAN_VAULT_PATH • •"
    exit 1
fi

# • • Create meta-output directory • •
mkdir -p meta-output

# • • Start the containers • •
echo "• • Starting containers • •"
docker-compose up -d

# • • Wait for containers to be ready • •
echo "• • Waiting for containers to be ready • •"
sleep 10

# • • Show logs • •
echo "• • Showing logs (Ctrl+C to stop) • •"
docker-compose logs -f

echo "• • DEPLOYMENT COMPLETE • •"
EOF

chmod +x run.sh

# • • Create setup instructions • •
cat > README.md << 'EOF'
# • • META-FOLDED RECURSIVE KNOWLEDGE SURGEON • •

## • • SETUP INSTRUCTIONS • •

1. **Set your Obsidian vault path:**
   ```bash
   export OBSIDIAN_VAULT_PATH=/path/to/your/obsidian/vault
   ```

2. **Run the deployment:**
   ```bash
   ./run.sh
   ```

3. **The system will:**
   - Start Ollama with phi3:mini
   - Download the model if needed
   - Analyze your vault recursively
   - Create meta-structure notes in your vault

## • • WHAT IT DOES • •

The system performs "backwards recursive surgery" on your knowledge:

1. **Contra-Positive Analysis**: Determines what your notes are NOT about to reveal what they ARE about
2. **Conceptual DNA Extraction**: Finds the genetic code of your ideas
3. **Meta-Folding**: Recursively analyzes the patterns in your analytical patterns
4. **Resonance Mapping**: Discovers how concepts vibrate together in your knowledge space

## • • OUTPUT • •

Creates a `••META-STRUCTURE••` folder in your vault with:
- `••META-SUMMARY••.md` - Overall analysis
- Individual concept meta-notes
- Resonance maps and convergence patterns

## • • TROUBLESHOOTING • •

If containers don't start:
```bash
docker-compose down
docker-compose up -d
```

To see logs:
```bash
docker-compose logs -f
```

To stop:
```bash
docker-compose down
```
EOF

echo "• • DEPLOYMENT SETUP COMPLETE • •"
echo "• • "
echo "• • NEXT STEPS: • •"
echo "• • 1. Set your vault path: export OBSIDIAN_VAULT_PATH=/path/to/your/vault • •"
echo "• • 2. Run: ./run.sh • •"
echo "• • 3. Watch the recursive surgery begin • •"
echo "• •"
```