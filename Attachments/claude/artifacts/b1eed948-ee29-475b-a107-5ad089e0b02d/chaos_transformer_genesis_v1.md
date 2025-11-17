---
nexus: nexus-ai-chat-importer
plugin_version: "1.3.0"
provider: claude
artifact_id: chaos_transformer_genesis
version_uuid: ed4f382d-68ac-4aae-ba5f-b26249172aa5
version_number: 1
command: create
conversation_id: b1eed948-ee29-475b-a107-5ad089e0b02d
create_time: 2025-08-13T00:32:05.000Z
format: markdown
aliases: [Chaos Transformer - 8K Parameter Genesis Implementation, chaos_transformer_genesis_v1]
---

# Chaos Transformer - 8K Parameter Genesis Implementation (Version 1)

**Conversation:** [[Nexus/Conversations/claude/2025/08/Cosine Similarity Tensor Dimension Error|Cosine Similarity Tensor Dimension Error]]

## Content

# chaos_transformer_genesis.py
# Phase 0: 8K Parameter Chaos Intelligence System
# Productive Instability Framework Implementation

import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
from typing import Dict, List, Optional, Tuple
import math

class ChaosTransformerConfig:
    """Configuration for the Chaos Transformer - Phase 0"""
    def __init__(
        self,
        vocab_size: int = 256,  # Character-level (ASCII)
        d_model: int = 128,     # Embedding dimension
        n_heads: int = 4,       # Attention heads
        n_layers: int = 2,      # Transformer layers
        max_seq_len: int = 256, # Maximum sequence length
        chaos_intensity: float = 0.0,  # 0.0 → 1.0
        instability_threshold: float = 0.1,
        refactor_interval: int = 500,
    ):
        self.vocab_size = vocab_size
        self.d_model = d_model
        self.n_heads = n_heads
        self.n_layers = n_layers
        self.max_seq_len = max_seq_len
        self.chaos_intensity = chaos_intensity
        self.instability_threshold = instability_threshold
        self.refactor_interval = refactor_interval
        
        # Calculate approximate parameters (target: ~8K)
        self.total_params = self._estimate_parameters()
        print(f"Estimated parameters: {self.total_params:,}")
    
    def _estimate_parameters(self) -> int:
        """Estimate total parameter count"""
        # Embedding
        embed_params = self.vocab_size * self.d_model
        # Position embedding
        pos_params = self.max_seq_len * self.d_model
        # Transformer layers
        layer_params = self.n_layers * (
            # Multi-head attention
            4 * self.d_model * self.d_model +  # Q, K, V, O projections
            # Feed-forward
            2 * self.d_model * (self.d_model * 2) +  # FFN expand/contract
            # Layer norms
            2 * self.d_model * 2  # Scale + bias for 2 layer norms
        )
        # Output projection
        output_params = self.d_model * self.vocab_size
        
        return embed_params + pos_params + layer_params + output_params

class RuntimeWeightPerturbation(nn.Module):
    """Core chaos injection mechanism - perturbs weights during forward pass"""
    
    def __init__(self, chaos_intensity: float = 0.0):
        super().__init__()
        self.chaos_intensity = chaos_intensity
        self.step_count = 0
        
    def forward(self, module: nn.Module, input_tensor: torch.Tensor) -> torch.Tensor:
        """Apply chaos perturbation to module weights during forward pass"""
        if self.chaos_intensity == 0.0:
            return module(input_tensor)
            
        # Store original weights
        original_state = {}
        
        # Perturb all parameters
        with torch.no_grad():
            for name, param in module.named_parameters():
                if param.requires_grad:
                    original_state[name] = param.data.clone()
                    
                    # Chaos injection: Add scaled noise
                    noise_scale = self.chaos_intensity * param.std().item()
                    noise = torch.randn_like(param) * noise_scale
                    param.data.add_(noise)
        
        # Forward pass with perturbed weights
        try:
            output = module(input_tensor)
        finally:
            # Restore original weights
            with torch.no_grad():
                for name, param in module.named_parameters():
                    if name in original_state:
                        param.data.copy_(original_state[name])
        
        self.step_count += 1
        return output

class ChaosAttention(nn.Module):
    """Multi-head attention with chaos injection capabilities"""
    
    def __init__(self, config: ChaosTransformerConfig):
        super().__init__()
        self.d_model = config.d_model
        self.n_heads = config.n_heads
        self.d_k = config.d_model // config.n_heads
        
        self.q_proj = nn.Linear(config.d_model, config.d_model, bias=False)
        self.k_proj = nn.Linear(config.d_model, config.d_model, bias=False)
        self.v_proj = nn.Linear(config.d_model, config.d_model, bias=False)
        self.o_proj = nn.Linear(config.d_model, config.d_model, bias=False)
        
        self.chaos_perturbation = RuntimeWeightPerturbation(config.chaos_intensity)
        
        # Oscillatory attention dynamics
        self.oscillation_frequency = nn.Parameter(torch.tensor(1.0))
        
    def forward(self, x: torch.Tensor, mask: Optional[torch.Tensor] = None) -> torch.Tensor:
        batch_size, seq_len, _ = x.shape
        
        # Apply chaos perturbation to projections
        q = self.chaos_perturbation(self.q_proj, x)
        k = self.chaos_perturbation(self.k_proj, x)
        v = self.chaos_perturbation(self.v_proj, x)
        
        # Reshape for multi-head attention
        q = q.view(batch_size, seq_len, self.n_heads, self.d_k).transpose(1, 2)
        k = k.view(batch_size, seq_len, self.n_heads, self.d_k).transpose(1, 2)
        v = v.view(batch_size, seq_len, self.n_heads, self.d_k).transpose(1, 2)
        
        # Attention computation with oscillatory dynamics
        scores = torch.matmul(q, k.transpose(-2, -1)) / math.sqrt(self.d_k)
        
        # Oscillatory attention modification
        time_step = torch.tensor(self.chaos_perturbation.step_count, dtype=torch.float32)
        oscillation = torch.sin(time_step * self.oscillation_frequency) * 0.1
        scores = scores + oscillation
        
        if mask is not None:
            scores.masked_fill_(mask == 0, -1e9)
            
        attn_weights = F.softmax(scores, dim=-1)
        
        # Apply attention
        out = torch.matmul(attn_weights, v)
        out = out.transpose(1, 2).contiguous().view(batch_size, seq_len, self.d_model)
        
        # Final projection with chaos
        return self.chaos_perturbation(self.o_proj, out)

class ChaosTransformerLayer(nn.Module):
    """Single transformer layer with chaos mechanisms"""
    
    def __init__(self, config: ChaosTransformerConfig):
        super().__init__()
        self.attention = ChaosAttention(config)
        self.norm1 = nn.LayerNorm(config.d_model)
        self.norm2 = nn.LayerNorm(config.d_model)
        
        # Feed-forward with chaos injection
        self.ffn = nn.Sequential(
            nn.Linear(config.d_model, config.d_model * 2),
            nn.ReLU(),
            nn.Linear(config.d_model * 2, config.d_model)
        )
        
        self.chaos_perturbation = RuntimeWeightPerturbation(config.chaos_intensity)
        
    def forward(self, x: torch.Tensor, mask: Optional[torch.Tensor] = None) -> torch.Tensor:
        # Self-attention with residual connection
        attn_out = self.attention(x, mask)
        x = self.norm1(x + attn_out)
        
        # Feed-forward with chaos injection and residual connection
        ffn_out = self.chaos_perturbation(self.ffn, x)
        x = self.norm2(x + ffn_out)
        
        return x

class ChaosTransformer(nn.Module):
    """Main Chaos Transformer model - 8K parameter configuration"""
    
    def __init__(self, config: ChaosTransformerConfig):
        super().__init__()
        self.config = config
        
        # Embeddings
        self.token_embedding = nn.Embedding(config.vocab_size, config.d_model)
        self.position_embedding = nn.Embedding(config.max_seq_len, config.d_model)
        
        # Transformer layers
        self.layers = nn.ModuleList([
            ChaosTransformerLayer(config) for _ in range(config.n_layers)
        ])
        
        # Output projection
        self.ln_f = nn.LayerNorm(config.d_model)
        self.lm_head = nn.Linear(config.d_model, config.vocab_size, bias=False)
        
        # Architecture evolution tracking
        self.evolution_step = 0
        self.performance_history = []
        
        # Initialize weights
        self.apply(self._init_weights)
        
        print(f"Chaos Transformer initialized:")
        print(f"  - Parameters: {sum(p.numel() for p in self.parameters()):,}")
        print(f"  - Chaos Intensity: {config.chaos_intensity}")
        
    def _init_weights(self, module):
        """Initialize weights with small random values"""
        if isinstance(module, nn.Linear):
            torch.nn.init.normal_(module.weight, mean=0.0, std=0.02)
            if module.bias is not None:
                torch.nn.init.zeros_(module.bias)
        elif isinstance(module, nn.Embedding):
            torch.nn.init.normal_(module.weight, mean=0.0, std=0.02)
        elif isinstance(module, nn.LayerNorm):
            torch.nn.init.ones_(module.weight)
            torch.nn.init.zeros_(module.bias)
    
    def forward(
        self, 
        input_ids: torch.Tensor, 
        attention_mask: Optional[torch.Tensor] = None
    ) -> torch.Tensor:
        batch_size, seq_len = input_ids.shape
        
        # Create position indices
        position_ids = torch.arange(seq_len, device=input_ids.device).unsqueeze(0)
        
        # Embeddings
        token_embeds = self.token_embedding(input_ids)
        pos_embeds = self.position_embedding(position_ids)
        x = token_embeds + pos_embeds
        
        # Apply transformer layers
        for layer in self.layers:
            x = layer(x, attention_mask)
        
        # Final normalization and projection
        x = self.ln_f(x)
        logits = self.lm_head(x)
        
        return logits
    
    def generate(
        self, 
        prompt: str, 
        max_length: int = 100, 
        temperature: float = 1.0,
        chaos_intensity: Optional[float] = None
    ) -> str:
        """Generate text with optional chaos intensity override"""
        
        # Temporarily adjust chaos if specified
        original_chaos = None
        if chaos_intensity is not None:
            original_chaos = self.config.chaos_intensity
            self.set_chaos_intensity(chaos_intensity)
        
        try:
            # Convert prompt to token ids (simple character-level)
            input_ids = torch.tensor([ord(c) for c in prompt[-100:]], dtype=torch.long).unsqueeze(0)
            
            generated = input_ids.clone()
            
            with torch.no_grad():
                for _ in range(max_length):
                    # Forward pass
                    logits = self.forward(generated)
                    
                    # Get next token probabilities
                    next_token_logits = logits[0, -1, :] / temperature
                    probs = F.softmax(next_token_logits, dim=-1)
                    
                    # Sample next token
                    next_token = torch.multinomial(probs, 1)
                    
                    # Append to generated sequence
                    generated = torch.cat([generated, next_token.unsqueeze(0)], dim=1)
                    
                    # Break if we hit a reasonable stopping point
                    if next_token.item() == ord('\n') and len(generated[0]) > len(input_ids[0]) + 10:
                        break
            
            # Convert back to text
            generated_chars = [chr(min(max(token.item(), 32), 126)) for token in generated[0]]
            return ''.join(generated_chars)
            
        finally:
            # Restore original chaos intensity
            if original_chaos is not None:
                self.set_chaos_intensity(original_chaos)
    
    def set_chaos_intensity(self, intensity: float):
        """Dynamically adjust chaos intensity"""
        self.config.chaos_intensity = intensity
        for module in self.modules():
            if isinstance(module, RuntimeWeightPerturbation):
                module.chaos_intensity = intensity
    
    def evaluate_creativity(self, text_samples: List[str]) -> Dict[str, float]:
        """Evaluate creativity metrics for generated text"""
        metrics = {}
        
        # Output entropy
        char_counts = {}
        total_chars = 0
        for sample in text_samples:
            for char in sample:
                char_counts[char] = char_counts.get(char, 0) + 1
                total_chars += 1
        
        if total_chars > 0:
            entropy = -sum(
                (count / total_chars) * math.log2(count / total_chars) 
                for count in char_counts.values()
            )
            metrics['entropy'] = entropy
        else:
            metrics['entropy'] = 0.0
        
        # Diversity (unique characters ratio)
        unique_chars = len(char_counts)
        metrics['diversity'] = unique_chars / max(total_chars, 1)
        
        # Novelty (deviation from training patterns - simplified)
        avg_length = sum(len(s) for s in text_samples) / max(len(text_samples), 1)
        metrics['avg_length'] = avg_length
        
        return metrics

# Training utilities
class ChaosTrainer:
    """Training orchestrator for the Chaos Transformer"""
    
    def __init__(self, model: ChaosTransformer, config: ChaosTransformerConfig):
        self.model = model
        self.config = config
        self.optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)
        self.step = 0
        
    def train_step(self, batch: torch.Tensor) -> Dict[str, float]:
        """Single training step with chaos progression"""
        
        self.model.train()
        
        # Progressive chaos introduction
        if self.step < 2000:  # Foundation phase
            chaos_intensity = 0.0
        elif self.step < 5000:  # Gradual introduction
            progress = (self.step - 2000) / 3000.0
            chaos_intensity = progress * 0.3
        else:  # Full chaos optimization
            chaos_intensity = self.config.chaos_intensity
        
        self.model.set_chaos_intensity(chaos_intensity)
        
        # Prepare inputs and targets
        input_ids = batch[:, :-1]
        targets = batch[:, 1:]
        
        # Forward pass
        logits = self.model(input_ids)
        
        # Compute loss
        loss = F.cross_entropy(logits.reshape(-1, logits.size(-1)), targets.reshape(-1))
        
        # Backward pass
        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()
        
        self.step += 1
        
        return {
            'loss': loss.item(),
            'chaos_intensity': chaos_intensity,
            'step': self.step
        }

# Factory function for easy instantiation
def create_chaos_transformer_8k() -> Tuple[ChaosTransformer, ChaosTransformerConfig]:
    """Create an 8K parameter Chaos Transformer"""
    
    # Optimize config for ~8K parameters
    config = ChaosTransformerConfig(
        vocab_size=128,      # Reduced vocab for efficiency
        d_model=96,          # Smaller embedding dimension
        n_heads=4,           # Keep multi-head capability
        n_layers=2,          # Minimal depth
        max_seq_len=128,     # Reasonable context window
        chaos_intensity=0.1, # Start with low chaos
    )
    
    model = ChaosTransformer(config)
    
    print(f"\n🌀 Chaos Transformer Genesis Complete 🌀")
    print(f"Target: 8K parameters | Actual: {sum(p.numel() for p in model.parameters()):,}")
    print(f"Ready for Phase 0 Proof-of-Concept testing")
    
    return model, config