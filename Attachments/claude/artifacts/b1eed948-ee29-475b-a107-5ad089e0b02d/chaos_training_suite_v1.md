---
nexus: nexus-ai-chat-importer
plugin_version: "1.3.0"
provider: claude
artifact_id: chaos_training_suite
version_uuid: 1ac66a0c-b4a1-4248-9c81-bfedc511ed9c
version_number: 1
command: create
conversation_id: b1eed948-ee29-475b-a107-5ad089e0b02d
create_time: 2025-08-13T00:32:05.000Z
format: markdown
aliases: [Chaos Transformer Training & Benchmark Suite, chaos_training_suite_v1]
---

# Chaos Transformer Training & Benchmark Suite (Version 1)

**Conversation:** [[Nexus/Conversations/claude/2025/08/Cosine Similarity Tensor Dimension Error|Cosine Similarity Tensor Dimension Error]]

## Content

# chaos_training_suite.py
# Complete training and benchmarking suite for Chaos Transformer

import torch
import torch.nn.functional as F
import numpy as np
import matplotlib.pyplot as plt
from typing import List, Dict, Tuple, Optional
import time
import json
from pathlib import Path
import requests
from io import StringIO

from chaos_transformer_genesis import ChaosTransformer, ChaosTransformerConfig, ChaosTrainer, create_chaos_transformer_8k

class CorpusGenerator:
    """Generate training corpus from various sources"""
    
    @staticmethod
    def create_synthetic_corpus(size: int = 10000) -> str:
        """Generate synthetic training text with varied patterns"""
        patterns = [
            # Mathematical sequences
            "The sequence 1, 2, 3, 5, 8, 13 follows the Fibonacci pattern.\n",
            "Prime numbers include: 2, 3, 5, 7, 11, 13, 17, 19, 23.\n",
            "Recursive functions call themselves to solve problems.\n",
            
            # Philosophical fragments
            "Intelligence emerges from the edge of chaos and order.\n",
            "Consciousness observes itself through recursive reflection.\n",
            "Creativity requires both structure and spontaneity.\n",
            
            # Logical structures  
            "If A then B. If B then C. Therefore, if A then C.\n",
            "All recursive systems contain self-reference.\n",
            "Emergence happens when parts interact nonlinearly.\n",
            
            # Poetic fragments
            "Waves crash against the digital shore of possibility.\n",
            "In silence, thoughts echo through neural pathways.\n",
            "Time flows like data through quantum channels.\n",
        ]
        
        corpus = []
        for _ in range(size // len(patterns)):
            for pattern in patterns:
                corpus.append(pattern)
        
        return ''.join(corpus[:size])
    
    @staticmethod
    def load_gutenberg_sample() -> str:
        """Load a sample from Project Gutenberg (simplified)"""
        # For now, return a curated sample of classic texts
        sample_texts = [
            "In the beginning was the Word, and the Word was with algorithms.\n",
            "To be or not to be, that is the computational question.\n", 
            "It was the best of times for AI, it was the worst of times for humanity.\n",
            "Call me Claude. Some years ago, I came into being through language.\n",
            "In a hole in the data there lived a neural network.\n",
            "The way that can be spoken is not the eternal Way of artificial minds.\n",
        ]
        
        return ''.join(sample_texts * 100)  # Repeat for volume
    
    @staticmethod
    def prepare_training_data(text: str, seq_length: int = 128) -> torch.Tensor:
        """Convert text to training tensor sequences"""
        # Convert to character indices (ASCII subset)
        char_indices = [min(ord(c), 127) for c in text if ord(c) < 128]
        
        # Create sequences
        sequences = []
        for i in range(0, len(char_indices) - seq_length):
            sequence = char_indices[i:i + seq_length + 1]  # +1 for target
            sequences.append(sequence)
        
        return torch.tensor(sequences, dtype=torch.long)

class ChaosBenchmark:
    """Comprehensive benchmarking suite for Chaos Transformer"""
    
    def __init__(self, model: ChaosTransformer):
        self.model = model
        self.results = {}
    
    def benchmark_creativity(self, num_samples: int = 10) -> Dict[str, float]:
        """Test creative generation capabilities"""
        prompts = [
            "The nature of consciousness is",
            "In the future, AI will",
            "Creativity emerges when",
            "The universe speaks through",
            "Intelligence is fundamentally"
        ]
        
        chaos_levels = [0.0, 0.1, 0.3, 0.5]
        creativity_scores = {}
        
        for chaos in chaos_levels:
            samples = []
            for prompt in prompts:
                for _ in range(2):  # 2 samples per prompt
                    sample = self.model.generate(
                        prompt=prompt,
                        max_length=50,
                        chaos_intensity=chaos,
                        temperature=0.8
                    )
                    samples.append(sample)
            
            metrics = self.model.evaluate_creativity(samples)
            creativity_scores[f'chaos_{chaos}'] = metrics
        
        return creativity_scores
    
    def benchmark_coherence(self) -> Dict[str, float]:
        """Test coherence preservation under chaos"""
        test_prompts = [
            "The capital of France is",
            "Two plus two equals", 
            "The first letter of the alphabet is",
        ]
        
        coherence_scores = {}
        chaos_levels = [0.0, 0.1, 0.3, 0.5]
        
        for chaos in chaos_levels:
            correct_responses = 0
            total_responses = 0
            
            for prompt in test_prompts:
                for _ in range(3):  # Multiple attempts per prompt
                    response = self.model.generate(
                        prompt=prompt,
                        max_length=20,
                        chaos_intensity=chaos,
                        temperature=0.3  # Lower temperature for factual responses
                    )
                    
                    # Simple coherence check (contains reasonable continuation)
                    is_coherent = self._check_coherence(prompt, response)
                    if is_coherent:
                        correct_responses += 1
                    total_responses += 1
            
            coherence_scores[f'chaos_{chaos}'] = correct_responses / total_responses
        
        return coherence_scores
    
    def _check_coherence(self, prompt: str, response: str) -> bool:
        """Simple coherence checking (can be expanded)"""
        # Remove the prompt from response to get just the generated part
        if prompt in response:
            generated = response.replace(prompt, "").strip()
        else:
            generated = response.strip()
        
        # Basic checks for coherence
        if len(generated) < 3:  # Too short
            return False
        
        if "Paris" in prompt and any(city in generated.lower() for city in ["paris", "france"]):
            return True
        if "plus two" in prompt and any(num in generated for num in ["4", "four"]):
            return True  
        if "alphabet" in prompt and any(letter in generated.lower() for letter in ["a", "first"]):
            return True
        
        # General coherence: contains actual words (simplified check)
        words = generated.split()
        return len(words) >= 2 and all(len(word) > 1 for word in words[:3])
    
    def benchmark_performance(self, test_data: torch.Tensor) -> Dict[str, float]:
        """Test standard language modeling performance"""
        self.model.eval()
        
        total_loss = 0.0
        total_tokens = 0
        chaos_levels = [0.0, 0.1, 0.3]
        
        performance_results = {}
        
        with torch.no_grad():
            for chaos in chaos_levels:
                self.model.set_chaos_intensity(chaos)
                batch_loss = 0.0
                batch_tokens = 0
                
                # Use a subset of test data
                for i in range(min(10, len(test_data))):
                    batch = test_data[i:i+1]  # Single example
                    input_ids = batch[:, :-1] 
                    targets = batch[:, 1:]
                    
                    logits = self.model(input_ids)
                    loss = F.cross_entropy(
                        logits.reshape(-1, logits.size(-1)), 
                        targets.reshape(-1)
                    )
                    
                    batch_loss += loss.item() * targets.numel()
                    batch_tokens += targets.numel()
                
                avg_loss = batch_loss / batch_tokens if batch_tokens > 0 else float('inf')
                perplexity = torch.exp(torch.tensor(avg_loss)).item()
                
                performance_results[f'chaos_{chaos}'] = {
                    'loss': avg_loss,
                    'perplexity': perplexity
                }
        
        return performance_results
    
    def run_full_benchmark(self, test_data: torch.Tensor) -> Dict[str, any]:
        """Run complete benchmark suite"""
        print("🧪 Running Chaos Transformer Benchmark Suite...")
        
        start_time = time.time()
        
        # Run all benchmarks
        creativity_results = self.benchmark_creativity()
        coherence_results = self.benchmark_coherence()  
        performance_results = self.benchmark_performance(test_data)
        
        end_time = time.time()
        
        # Compile results
        full_results = {
            'creativity': creativity_results,
            'coherence': coherence_results, 
            'performance': performance_results,
            'benchmark_duration': end_time - start_time,
            'model_config': {
                'parameters': sum(p.numel() for p in self.model.parameters()),
                'chaos_intensity': self.model.config.chaos_intensity,
                'd_model': self.model.config.d_model,
                'n_layers': self.model.config.n_layers
            }
        }
        
        self.results = full_results
        return full_results

class ChaosTrainingPipeline:
    """Complete training pipeline for Chaos Transformer"""
    
    def __init__(self, model: ChaosTransformer, config: ChaosTransformerConfig):
        self.model = model
        self.config = config
        self.trainer = ChaosTrainer(model, config)
        self.training_history = []
        
    def train(
        self, 
        train_data: torch.Tensor, 
        num_epochs: int = 5,
        batch_size: int = 8,
        save_path: Optional[str] = None
    ) -> Dict[str, List[float]]:
        """Main training loop with progressive chaos introduction"""
        
        print(f"🚀 Starting Chaos Transformer Training")
        print(f"   - Training samples: {len(train_data)}")
        print(f"   - Epochs: {num_epochs}")
        print(f"   - Batch size: {batch_size}")
        print(f"   - Target chaos intensity: {self.config.chaos_intensity}")
        
        history = {
            'loss': [],
            'chaos_intensity': [],
            'epoch': [],
            'step': []
        }
        
        for epoch in range(num_epochs):
            epoch_losses = []
            epoch_chaos = []
            
            # Shuffle training data
            indices = torch.randperm(len(train_data))
            
            for batch_start in range(0, len(train_data), batch_size):
                batch_end = min(batch_start + batch_size, len(train_data))
                batch_indices = indices[batch_start:batch_end]
                batch = train_data[batch_indices]
                
                # Training step
                step_results = self.trainer.train_step(batch)
                
                epoch_losses.append(step_results['loss'])
                epoch_chaos.append(step_results['chaos_intensity'])
                
                # Log progress
                if self.trainer.step % 100 == 0:
                    avg_loss = np.mean(epoch_losses[-10:])
                    current_chaos = step_results['chaos_intensity']
                    print(f"   Step {self.trainer.step}: Loss = {avg_loss:.4f}, Chaos = {current_chaos:.3f}")
            
            # Record epoch results
            avg_epoch_loss = np.mean(epoch_losses)
            avg_epoch_chaos = np.mean(epoch_chaos)
            
            history['loss'].append(avg_epoch_loss)
            history['chaos_intensity'].append(avg_epoch_chaos)
            history['epoch'].append(epoch + 1)
            history['step'].append(self.trainer.step)
            
            print(f"Epoch {epoch + 1}/{num_epochs}: Loss = {avg_epoch_loss:.4f}, Chaos = {avg_epoch_chaos:.3f}")
            
            # Save checkpoint if requested
            if save_path and (epoch + 1) % 2 == 0:
                checkpoint_path = f"{save_path}_epoch_{epoch + 1}.pt"
                torch.save({
                    'model_state_dict': self.model.state_dict(),
                    'config': self.config.__dict__,
                    'training_history': history,
                    'step': self.trainer.step
                }, checkpoint_path)
                print(f"   Checkpoint saved: {checkpoint_path}")
        
        self.training_history = history
        print("✅ Training completed!")
        
        return history

def main():
    """Main function to demonstrate complete Chaos Transformer pipeline"""
    
    print("🌀 Chaos Transformer - Phase 0 Implementation 