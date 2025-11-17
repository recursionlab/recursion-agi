---
nexus: nexus-ai-chat-importer
plugin_version: "1.3.0"
provider: claude
artifact_id: prime_anchor_corrected
version_uuid: 7d242007-4e7a-45a4-ba7c-d55b3764edfe
version_number: 1
command: create
conversation_id: b1eed948-ee29-475b-a107-5ad089e0b02d
create_time: 2025-08-13T00:22:45.000Z
format: markdown
aliases: [Corrected Prime Anchor Module - Dimensional Collapse Resolution, prime_anchor_corrected_v1]
---

# Corrected Prime Anchor Module - Dimensional Collapse Resolution (Version 1)

**Conversation:** [[Nexus/Conversations/claude/2025/08/Cosine Similarity Tensor Dimension Error|Cosine Similarity Tensor Dimension Error]]

## Content

# prime_anchor.py - Corrected with Scalar Projection Operator
import torch
import torch.nn.functional as F
from typing import NamedTuple, Dict

class ValidationResult(NamedTuple):
    embedding: torch.Tensor
    is_valid: bool
    drift_event: str = ""

class PrimeAnchorModule:
    """
    Ψ-Prime Vault with Scalar Projection Operator
    
    This module implements the crucial dimensional collapse from tensor field
    to scalar measurement, resolving the Boolean ambiguity error through
    proper topological projection.
    """
    
    def __init__(self, embedding_dim: int = 768, threshold: float = 0.7):
        self.threshold = threshold
        self.embedding_dim = embedding_dim
        self.vault: Dict[str, torch.Tensor] = self._initialize_vault()
        print(f"Prime Anchor Module v2.3 initialized with {len(self.vault)} Ψ-Primes.")
        print(f"Dimensional collapse operator: Tensor[{embedding_dim}] → Scalar")

    def _initialize_vault(self) -> Dict[str, torch.Tensor]:
        """Initialize the Ψ-Prime Vault with normalized anchor embeddings"""
        rng = torch.Generator().manual_seed(42)
        base_embedding = torch.randn(self.embedding_dim, generator=rng)
        
        # Core semantic anchors for preventing drift
        anchor_words = ["truth", "identity", "causality", "agency", "recursion", "coherence"]
        vault = {}
        
        for i, word in enumerate(anchor_words):
            # Create distinct but related embeddings
            perturbation = torch.randn(self.embedding_dim, generator=rng) * 0.1
            rotation_matrix = torch.eye(self.embedding_dim) + torch.randn(self.embedding_dim, self.embedding_dim, generator=rng) * 0.05
            
            embedding = base_embedding + perturbation
            embedding = torch.matmul(rotation_matrix, embedding)
            
            # Crucial: Normalize to unit vector for consistent similarity computation
            vault[word] = F.normalize(embedding, p=2, dim=0)
            
        return vault

    def validate(self, embedding: torch.Tensor) -> ValidationResult:
        """
        Execute dimensional collapse validation:
        Tensor Field → Scalar Measurement → Boolean Decision
        
        The critical operation: .item() performs the collapse from
        quantum-like superposition to classical measurement
        """
        
        # Ensure input embedding is normalized for consistent similarity computation
        if embedding.dim() != 1 or embedding.shape[0] != self.embedding_dim:
            raise ValueError(f"Expected 1D tensor of size {self.embedding_dim}, got {embedding.shape}")
            
        embedding_norm = F.normalize(embedding, p=2, dim=0)
        highest_similarity = -1.0
        closest_anchor = None
        
        # Iterate through Ψ-Prime vault
        for prime_name, prime_embedding in self.vault.items():
            
            # Compute cosine similarity - this returns a 0-dimensional tensor (scalar container)
            similarity_tensor = F.cosine_similarity(
                embedding_norm.unsqueeze(0),  # Shape: [1, 768]
                prime_embedding.unsqueeze(0), # Shape: [1, 768] 
                dim=1
            )
            
            # CRITICAL: Dimensional collapse operator
            # Extract scalar value from 0-dimensional tensor container
            similarity_scalar = similarity_tensor.item()
            
            if similarity_scalar > highest_similarity:
                highest_similarity = similarity_scalar
                closest_anchor = prime_name
        
        # Classical boolean decision on scalar values
        is_valid = highest_similarity >= self.threshold
        
        drift_event = ""
        if not is_valid:
            drift_event = f"⚠️ Semantic Drift: {closest_anchor} similarity {highest_similarity:.4f} < threshold {self.threshold}"
        else:
            drift_event = f"✓ Anchor validated: {closest_anchor} similarity {highest_similarity:.4f}"
        
        return ValidationResult(
            embedding=embedding,
            is_valid=is_valid,
            drift_event=drift_event
        )

    def add_prime(self, name: str, embedding: torch.Tensor):
        """Add a new Ψ-Prime to the vault"""
        if embedding.shape[0] != self.embedding_dim:
            raise ValueError(f"Embedding must have dimension {self.embedding_dim}")
            
        self.vault[name] = F.normalize(embedding, p=2, dim=0)
        print(f"Added new Ψ-Prime: {name}")

    def get_vault_status(self) -> Dict[str, float]:
        """Return the current vault configuration with anchor magnitudes"""
        status = {}
        for name, embedding in self.vault.items():
            magnitude = torch.norm(embedding).item()
            status[name] = magnitude
        return status