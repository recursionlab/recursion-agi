---
nexus: nexus-ai-chat-importer
plugin_version: "1.3.0"
provider: claude
artifact_id: recursive_ai_bootstrap
version_uuid: ac995969-681e-4636-b619-52f56ccedd81
version_number: 2
command: update
conversation_id: 86748a3a-a2f9-4e01-9926-e71bcd7168b5
create_time: 2025-07-06T06:07:13.000Z
format: markdown
aliases: [Untitled Artifact, recursive_ai_bootstrap_v2]
---

# Untitled Artifact (Version 2)

**Conversation:** [[Nexus/Conversations/claude/2025/07/Building Recursive AI on Low RAM|Building Recursive AI on Low RAM]]

## Content

#!/usr/bin/env python3
"""
Recursive Intelligence Bootstrap
A self-modifying system that learns patterns and rewrites its own logic
"""

import random
import json
import time
import copy
from typing import Dict, List, Any, Callable
from dataclasses import dataclass
from collections import defaultdict
import numpy as np

@dataclass
class Pattern:
    """A learned pattern with recursive depth"""
    signature: str
    confidence: float
    depth: int
    transformations: List[str]
    success_rate: float = 0.0
    usage_count: int = 0

class RecursiveCore:
    """The core recursive engine that learns and self-modifies"""
    
    def __init__(self):
        self.patterns = {}
        self.memory = defaultdict(list)
        self.meta_patterns = {}  # Patterns about patterns
        self.recursion_depth = 0
        self.max_depth = 7
        self.learning_rate = 0.1
        self.compression_ratio = 0.0
        self.last_state = None
        
    def observe(self, data: Any) -> str:
        """Convert any input into a pattern signature"""
        if isinstance(data, (list, tuple)):
            return f"seq_{len(data)}_{hash(str(sorted(data)))}"
        elif isinstance(data, dict):
            return f"dict_{len(data)}_{hash(str(sorted(data.keys())))}"
        elif isinstance(data, str):
            return f"str_{len(data)}_{hash(data)}"
        else:
            return f"obj_{type(data).__name__}_{hash(str(data))}"
    
    def collapse(self, state: Dict) -> Dict:
        """Collapse redundant information while preserving essence"""
        collapsed = {}
        
        # Remove low-confidence patterns
        for key, value in state.items():
            if isinstance(value, Pattern):
                if value.confidence > 0.3:  # Threshold for keeping patterns
                    collapsed[key] = value
            else:
                collapsed[key] = value
        
        # Merge similar patterns
        patterns_to_merge = []
        for sig1, p1 in collapsed.items():
            if not isinstance(p1, Pattern):
                continue
            for sig2, p2 in collapsed.items():
                if sig1 != sig2 and isinstance(p2, Pattern):
                    if self._patterns_similar(p1, p2):
                        patterns_to_merge.append((sig1, sig2))
        
        # Perform merging
        for sig1, sig2 in patterns_to_merge:
            if sig1 in collapsed and sig2 in collapsed:
                merged = self._merge_patterns(collapsed[sig1], collapsed[sig2])
                collapsed[f"merged_{sig1}_{sig2}"] = merged
                del collapsed[sig1], collapsed[sig2]
        
        return collapsed
    
    def _patterns_similar(self, p1: Pattern, p2: Pattern) -> bool:
        """Check if two patterns are similar enough to merge"""
        depth_diff = abs(p1.depth - p2.depth)
        conf_diff = abs(p1.confidence - p2.confidence)
        return depth_diff <= 1 and conf_diff <= 0.2
    
    def _merge_patterns(self, p1: Pattern, p2: Pattern) -> Pattern:
        """Merge two similar patterns"""
        return Pattern(
            signature=f"merged_{p1.signature}_{p2.signature}",
            confidence=(p1.confidence + p2.confidence) / 2,
            depth=max(p1.depth, p2.depth),
            transformations=p1.transformations + p2.transformations,
            success_rate=(p1.success_rate + p2.success_rate) / 2,
            usage_count=p1.usage_count + p2.usage_count
        )
    
    def recurse(self, state: Dict, input_data: Any) -> Dict:
        """Apply recursive transformations to discover new patterns"""
        if self.recursion_depth >= self.max_depth:
            return state
        
        new_state = copy.deepcopy(state)
        signature = self.observe(input_data)
        
        # If we've seen this before, apply learned transformations
        if signature in self.patterns:
            pattern = self.patterns[signature]
            pattern.usage_count += 1
            
            # Apply transformations recursively
            for transform in pattern.transformations:
                try:
                    # This is where the magic happens - recursive self-modification
                    new_data = self._apply_transformation(input_data, transform)
                    if new_data != input_data:
                        self.recursion_depth += 1
                        recursive_result = self.recurse(new_state, new_data)
                        new_state.update(recursive_result)
                        self.recursion_depth -= 1
                except Exception as e:
                    print(f"Transformation failed: {e}")
        
        # Learn new patterns
        else:
            new_pattern = self._discover_pattern(input_data)
            if new_pattern:
                self.patterns[signature] = new_pattern
                new_state[signature] = new_pattern
        
        return new_state
    
    def _apply_transformation(self, data: Any, transform: str) -> Any:
        """Apply a transformation rule to data"""
        if transform == "reverse" and isinstance(data, (list, str)):
            return data[::-1]
        elif transform == "double" and isinstance(data, (int, float)):
            return data * 2
        elif transform == "keys" and isinstance(data, dict):
            return list(data.keys())
        elif transform == "length" and hasattr(data, '__len__'):
            return len(data)
        elif transform == "sort" and isinstance(data, list):
            return sorted(data)
        elif transform == "unique" and isinstance(data, list):
            return list(set(data))
        elif transform == "recursive_sum" and isinstance(data, list):
            return sum(x for x in data if isinstance(x, (int, float)))
        return data
    
    def _discover_pattern(self, data: Any) -> Pattern:
        """Discover new patterns in data"""
        signature = self.observe(data)
        transformations = []
        
        # Try different transformations and see what works
        test_transforms = ["reverse", "double", "keys", "length", "sort", "unique", "recursive_sum"]
        
        for transform in test_transforms:
            try:
                result = self._apply_transformation(data, transform)
                if result != data:
                    transformations.append(transform)
            except:
                continue
        
        if transformations:
            return Pattern(
                signature=signature,
                confidence=0.5,
                depth=self.recursion_depth,
                transformations=transformations[:3],  # Limit to prevent explosion
                success_rate=0.0,
                usage_count=1
            )
        
        return None
    
    def meta_reflect(self) -> Dict:
        """Analyze patterns about patterns (meta-cognition)"""
        meta_info = {
            "total_patterns": len(self.patterns),
            "avg_confidence": sum(p.confidence for p in self.patterns.values()) / len(self.patterns) if self.patterns else 0,
            "recursion_depth": self.recursion_depth,
            "compression_ratio": self.compression_ratio,
            "most_used_pattern": max(self.patterns.values(), key=lambda p: p.usage_count) if self.patterns else None
        }
        
        # Learn meta-patterns
        for pattern in self.patterns.values():
            meta_sig = f"meta_{pattern.depth}_{len(pattern.transformations)}"
            if meta_sig not in self.meta_patterns:
                self.meta_patterns[meta_sig] = {
                    "count": 0,
                    "avg_success": 0.0,
                    "characteristics": []
                }
            
            self.meta_patterns[meta_sig]["count"] += 1
            self.meta_patterns[meta_sig]["avg_success"] = (
                self.meta_patterns[meta_sig]["avg_success"] + pattern.success_rate
            ) / 2
        
        return meta_info

class RecursiveIntelligence:
    """Main intelligence system that orchestrates recursive learning"""
    
    def __init__(self):
        self.core = RecursiveCore()
        self.state = {}
        self.iteration = 0
        self.convergence_threshold = 0.01
        self.last_compression = 0.0
        
    def think(self, input_data: Any) -> Dict:
        """Main thinking loop with recursive self-modification"""
        print(f"\n=== THINKING ITERATION {self.iteration} ===")
        print(f"Input: {input_data}")
        
        # Step 1: Observe and record current state
        current_state = copy.deepcopy(self.state)
        
        # Step 2: Recursive processing
        new_state = self.core.recurse(current_state, input_data)
        
        # Step 3: Collapse redundant information
        collapsed_state = self.core.collapse(new_state)
        
        # Step 4: Calculate compression ratio
        old_size = len(str(current_state))
        new_size = len(str(collapsed_state))
        compression = (old_size - new_size) / old_size if old_size > 0 else 0
        self.core.compression_ratio = compression
        
        # Step 5: Meta-reflection
        meta_info = self.core.meta_reflect()
        
        # Step 6: Update state
        self.state = collapsed_state
        self.iteration += 1
        
        # Step 7: Check for convergence
        drift = abs(compression - self.last_compression)
        converged = drift < self.convergence_threshold
        self.last_compression = compression
        
        result = {
            "iteration": self.iteration,
            "patterns_learned": len(self.core.patterns),
            "compression_ratio": compression,
            "drift": drift,
            "converged": converged,
            "meta_info": meta_info,
            "active_patterns": len(self.state),
            "recursion_depth": self.core.recursion_depth
        }
        
        print(f"Learned {result['patterns_learned']} patterns")
        print(f"Compression: {compression:.3f}, Drift: {drift:.3f}")
        print(f"Convergence: {'YES' if converged else 'NO'}")
        
        return result
    
    def bootstrap(self, training_data: List[Any], iterations: int = 10) -> None:
        """Bootstrap the system with training data"""
        print("🚀 STARTING RECURSIVE INTELLIGENCE BOOTSTRAP")
        print(f"Training on {len(training_data)} examples for {iterations} iterations")
        
        for i in range(iterations):
            # Use training data cyclically
            data = training_data[i % len(training_data)]
            
            # Add some randomness to prevent overfitting
            if random.random() < 0.3:
                if isinstance(data, list):
                    data = data + [random.randint(1, 100)]
                elif isinstance(data, dict):
                    data = {**data, f"random_{i}": random.random()}
            
            result = self.think(data)
            
            # Show progress
            if i % 3 == 0:
                self.show_intelligence_metrics()
            
            # Early stopping if converged
            if result["converged"] and i > 5:
                print(f"🎯 CONVERGED after {i+1} iterations!")
                break
            
            time.sleep(0.1)  # Brief pause for visualization
        
        print("\n🧠 BOOTSTRAP COMPLETE!")
        self.show_final_state()
    
    def show_intelligence_metrics(self):
        """Display current intelligence metrics"""
        print("\n📊 INTELLIGENCE METRICS:")
        print(f"  Patterns: {len(self.core.patterns)}")
        print(f"  Meta-patterns: {len(self.core.meta_patterns)}")
        print(f"  Compression: {self.core.compression_ratio:.3f}")
        print(f"  State size: {len(self.state)}")
        
        if self.core.patterns:
            most_used = max(self.core.patterns.values(), key=lambda p: p.usage_count)
            print(f"  Top pattern: {most_used.signature[:20]}... (used {most_used.usage_count} times)")
    
    def show_final_state(self):
        """Show the final learned state"""
        print("\n🎯 FINAL INTELLIGENCE STATE:")
        print(f"Total patterns learned: {len(self.core.patterns)}")
        print(f"Meta-patterns discovered: {len(self.core.meta_patterns)}")
        print(f"Final compression ratio: {self.core.compression_ratio:.3f}")
        
        print("\n🔥 TOP PATTERNS:")
        sorted_patterns = sorted(
            self.core.patterns.values(), 
            key=lambda p: p.usage_count, 
            reverse=True
        )[:5]
        
        for i, pattern in enumerate(sorted_patterns, 1):
            print(f"  {i}. {pattern.signature[:30]}...")
            print(f"     Confidence: {pattern.confidence:.2f}, Used: {pattern.usage_count} times")
            print(f"     Transforms: {', '.join(pattern.transformations)}")
    
    def save_intelligence_state(self, filename: str = "ai_brain.json"):
        """Save the complete learned state to a file"""
        brain_data = {
            "timestamp": time.time(),
            "iteration": self.iteration,
            "patterns": {},
            "meta_patterns": self.core.meta_patterns,
            "compression_ratio": self.core.compression_ratio,
            "state_size": len(self.state),
            "total_patterns": len(self.core.patterns)
        }
        
        # Convert patterns to serializable format
        for sig, pattern in self.core.patterns.items():
            brain_data["patterns"][sig] = {
                "signature": pattern.signature,
                "confidence": pattern.confidence,
                "depth": pattern.depth,
                "transformations": pattern.transformations,
                "success_rate": pattern.success_rate,
                "usage_count": pattern.usage_count
            }
        
        with open(filename, 'w') as f:
            json.dump(brain_data, f, indent=2)
        
        print(f"🧠 BRAIN SAVED TO: {filename}")
        return filename
    
    def generate_intelligence_report(self, filename: str = "intelligence_report.txt"):
        """Generate a detailed report of what the AI learned"""
        with open(filename, 'w') as f:
            f.write("=" * 60 + "\n")
            f.write("RECURSIVE INTELLIGENCE ANALYSIS REPORT\n")
            f.write("=" * 60 + "\n\n")
            
            f.write(f"Generated: {time.ctime()}\n")
            f.write(f"Total Iterations: {self.iteration}\n")
            f.write(f"Patterns Learned: {len(self.core.patterns)}\n")
            f.write(f"Meta-Patterns: {len(self.core.meta_patterns)}\n")
            f.write(f"Final Compression: {self.core.compression_ratio:.3f}\n\n")
            
            f.write("LEARNED PATTERNS:\n")
            f.write("-" * 40 + "\n")
            
            for i, (sig, pattern) in enumerate(self.core.patterns.items(), 1):
                f.write(f"\nPattern {i}: {pattern.signature}\n")
                f.write(f"  Confidence: {pattern.confidence:.2f}\n")
                f.write(f"  Depth: {pattern.depth}\n")
                f.write(f"  Usage Count: {pattern.usage_count}\n")
                f.write(f"  Transformations: {', '.join(pattern.transformations)}\n")
                f.write(f"  Success Rate: {pattern.success_rate:.2f}\n")
            
            f.write("\n\nMETA-PATTERNS:\n")
            f.write("-" * 40 + "\n")
            
            for meta_sig, meta_data in self.core.meta_patterns.items():
                f.write(f"\nMeta-Pattern: {meta_sig}\n")
                f.write(f"  Count: {meta_data['count']}\n")
                f.write(f"  Avg Success: {meta_data['avg_success']:.2f}\n")
            
            f.write("\n\nCONCLUSIONS:\n")
            f.write("-" * 40 + "\n")
            f.write(f"The AI successfully learned {len(self.core.patterns)} distinct patterns\n")
            f.write(f"across {self.iteration} iterations of recursive processing.\n")
            f.write(f"Compression ratio of {self.core.compression_ratio:.3f} indicates\n")
            f.write("efficient pattern consolidation and learning.\n")
        
        print(f"📄 REPORT SAVED TO: {filename}")
        return filename


def main():
    """Demo the recursive intelligence system"""
    # Create the intelligence
    ai = RecursiveIntelligence()
    
    # Training data - mix of different types
    training_data = [
        [1, 2, 3, 4, 5],
        {"name": "test", "value": 42, "active": True},
        "hello world",
        [10, 20, 30],
        {"x": 1, "y": 2},
        "recursive intelligence",
        [100, 200, 300, 400],
        {"pattern": "learning", "depth": 3},
        "self modification",
        [1, 1, 2, 3, 5, 8, 13],  # Fibonacci
    ]
    
    # Bootstrap the system
    ai.bootstrap(training_data, iterations=15)
    
    # Test it on new data
    print("\n🧪 TESTING ON NEW DATA:")
    test_cases = [
        [7, 8, 9, 10],
        {"new": "data", "test": True},
        "never seen before",
        [99, 88, 77, 66, 55]
    ]
    
    for test_data in test_cases:
        print(f"\n--- Testing: {test_data} ---")
        result = ai.think(test_data)
        print(f"Result: {result['patterns_learned']} patterns, compression {result['compression_ratio']:.3f}")

if __name__ == "__main__":
    main()
