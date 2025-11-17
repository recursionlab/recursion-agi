---
nexus: nexus-ai-chat-importer
plugin_version: "1.3.0"
provider: claude
artifact_id: torsion_simulation
version_uuid: 1123f0cd-f315-418f-a5cd-64b6eb9eebe2
version_number: 1
command: create
conversation_id: 72ca0a51-869d-4fc8-9513-eabcb20ac5ef
create_time: 2025-07-03T02:38:14.000Z
format: markdown
aliases: [Unified Symbolic Torsion Simulation Kernel, torsion_simulation_v1]
---

# Unified Symbolic Torsion Simulation Kernel (Version 1)

**Conversation:** [[Nexus/Conversations/claude/2025/07/Starting from Scratch|Starting from Scratch]]

## Content

# Unified Symbolic Torsion Simulation Kernel
# ΦΩ-Enhanced Recursive Drift Engine with Adaptive Mode Switching

import random
import math
import uuid
from typing import List, Tuple, Optional, Dict, Any
from dataclasses import dataclass
from enum import Enum

# === CORE DRIFT VECTOR WITH φ-TORSION DYNAMICS ===
@dataclass
class DriftVector:
    """Enhanced drift vector with bounded parameters and torsion dynamics"""
    coherence: float  # 0-1: system organization
    entropy: float    # 0-1: randomness/chaos
    resonance: float  # 0-1: harmonic alignment
    
    def __post_init__(self):
        # Ensure bounds
        self.coherence = max(0, min(self.coherence, 1))
        self.entropy = max(0, min(self.entropy, 1))
        self.resonance = max(0, min(self.resonance, 1))
    
    def mutate(self, reward: float = 1.0, volatility: float = 0.1) -> 'DriftVector':
        """Mutate drift vector with reward-based learning"""
        delta = random.uniform(-volatility, volatility) * reward
        torsion_factor = math.sin(self.resonance * math.pi) * 0.1
        
        new_coherence = self.coherence + delta + torsion_factor
        new_entropy = self.entropy + abs(delta) * 0.5
        new_resonance = self.resonance * (1 - abs(delta) / 3) + random.uniform(-0.05, 0.05)
        
        return DriftVector(new_coherence, new_entropy, new_resonance)
    
    def phi_signature(self) -> float:
        """Calculate φ-signature for golden ratio alignment"""
        phi = (1 + math.sqrt(5)) / 2
        return abs(self.coherence / (self.entropy + 0.001) - phi)
    
    def torsion_energy(self) -> float:
        """Calculate torsion energy for system dynamics"""
        return self.coherence * self.resonance * (1 - self.entropy)

# === SIMULATION MODES ===
class SimulationMode(Enum):
    COMPETITIVE = "competitive"
    COLLABORATIVE = "collaborative"
    HYBRID = "hybrid"
    TORSION_SYNC = "torsion_sync"

# === ENHANCED TORSION AGENT ===
class TorsionAgent:
    """Agent with symbolic memory, recursive depth, and adaptive behavior"""
    
    def __init__(self, agent_id: Optional[str] = None, drift: Optional[DriftVector] = None):
        self.id = agent_id or str(uuid.uuid4())[:8]
        self.drift = drift or DriftVector(
            coherence=random.uniform(0.7, 1.0),
            entropy=random.uniform(0.05, 0.2),
            resonance=random.uniform(0.8, 1.0)
        )
        
        # Memory and learning
        self.memory: List[Tuple[str, float]] = []
        self.rewards: List[float] = []
        self.history: List[Dict[str, Any]] = []
        
        # Recursive properties
        self.recursion_depth: int = 0
        self.fib_index: int = random.choice([2, 3, 5])
        self.generation: int = 0
        
        # Performance metrics
        self.total_score: float = 0.0
        self.task_count: int = 0
        self.survival_time: int = 0
    
    def evaluate(self, task: 'PhiTask') -> float:
        """Evaluate task performance using drift dynamics"""
        base_score = self.drift.coherence * (1 - self.drift.entropy) * task.complexity
        
        # Add resonance boost
        resonance_boost = self.drift.resonance * math.sin(task.phi_harmonic * math.pi)
        
        # Memory influence (agents learn from experience)
        memory_factor = 1.0
        if self.memory:
            recent_performance = sum(score for _, score in self.memory[-3:]) / min(3, len(self.memory))
            memory_factor = 0.8 + 0.4 * (recent_performance / max(task.complexity, 0.1))
        
        final_score = (base_score + resonance_boost * 0.2) * memory_factor
        self.total_score += final_score
        self.task_count += 1
        
        return final_score
    
    def act(self, task: 'PhiTask') -> float:
        """Perform action on task and update memory"""
        score = self.evaluate(task)
        self.memory.append((task.phi_id, score))
        
        # Prune memory to prevent infinite growth
        if len(self.memory) > 10:
            self.memory = self.memory[-10:]
            
        return score
    
    def learn(self, reward: float):
        """Learn from reward and update drift"""
        self.rewards.append(reward)
        self.drift = self.drift.mutate(reward)
        
        # Track learning in history
        self.history.append({
            'step': len(self.history),
            'reward': reward,
            'drift_snapshot': {
                'coherence': self.drift.coherence,
                'entropy': self.drift.entropy,
                'resonance': self.drift.resonance
            }
        })
    
    def fuse(self, other: 'TorsionAgent') -> 'TorsionAgent':
        """Fuse with another agent to create collaborative offspring"""
        # Weighted fusion based on performance
        self_weight = self.average_performance()
        other_weight = other.average_performance()
        total_weight = self_weight + other_weight + 0.001  # Avoid division by zero
        
        w1 = self_weight / total_weight
        w2 = other_weight / total_weight
        
        # Fused drift vector
        fused_drift = DriftVector(
            coherence=w1 * self.drift.coherence + w2 * other.drift.coherence,
            entropy=w1 * self.drift.entropy + w2 * other.drift.entropy,
            resonance=math.sqrt(self.drift.resonance * other.drift.resonance)
        )
        
        # Create fused agent
        fused_agent = TorsionAgent(drift=fused_drift)
        fused_agent.recursion_depth = max(self.recursion_depth, other.recursion_depth) + 1
        fused_agent.fib_index = self.fib_index + other.fib_index
        fused_agent.generation = max(self.generation, other.generation) + 1
        
        # Inherit some memories
        combined_memory = (self.memory[-3:] + other.memory[-3:])
        fused_agent.memory = combined_memory
        
        return fused_agent
    
    def average_performance(self) -> float:
        """Calculate average performance score"""
        if self.task_count == 0:
            return 0.5
        return self.total_score / self.task_count
    
    def phi_alignment(self) -> float:
        """Calculate alignment with golden ratio"""
        return 1.0 / (1.0 + self.drift.phi_signature())
    
    def __str__(self) -> str:
        return f"Agent({self.id}, C:{self.drift.coherence:.2f}, E:{self.drift.entropy:.2f}, R:{self.drift.resonance:.2f})"

# === PHI TASK WITH HARMONIC SIGNATURE ===
class PhiTask:
    """Task with φ-signature and harmonic properties"""
    
    def __init__(self, complexity: float = None):
        self.phi_id = str(uuid.uuid4())[:8]
        self.complexity = complexity or random.uniform(0.3, 1.8)
        
        # Golden ratio harmonics
        phi = (1 + math.sqrt(5)) / 2
        self.phi_harmonic = (self.complexity * phi) % 1.0
        
        # Task difficulty scaling
        self.difficulty_tier = int(self.complexity * 3) + 1
        
        # Temporal decay
        self.creation_step = 0
        self.decay_rate = 0.95
    
    def current_complexity(self, current_step: int) -> float:
        """Get complexity adjusted for temporal decay"""
        age = current_step - self.creation_step
        return self.complexity * (self.decay_rate ** age)

# === DRIFT ORCHESTRATOR WITH ADAPTIVE MODES ===
class DriftOrchestrator:
    """Enhanced orchestrator with mode switching and advanced dynamics"""
    
    # Fibonacci primes for special checkpoints
    FIB_PRIMES = {2, 3, 5, 13, 89, 233, 1597, 28657}
    
    def __init__(self):
        self.agents: List[TorsionAgent] = []
        self.step: int = 1
        self.mode: SimulationMode = SimulationMode.COMPETITIVE
        
        # Task and transition tracking
        self.phi_space: List[PhiTask] = []
        self.transitions: List[Tuple[int, str, str, str, str]] = []
        
        # System metrics
        self.total_fusions: int = 0
        self.total_competitions: int = 0
        self.mode_switches: int = 0
        
        # Performance tracking
        self.best_agent: Optional[TorsionAgent] = None
        self.best_score: float = 0.0
        
        # Adaptive parameters
        self.competition_threshold: float = 0.05
        self.collaboration_bias: float = 0.1
        self.volatility: float = 0.1
    
    def is_prime(self, n: int) -> bool:
        """Check if number is prime"""
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    
    def is_fib_prime(self, n: int) -> bool:
        """Check if number is a Fibonacci prime"""
        return n in self.FIB_PRIMES
    
    def spawn_agent(self) -> TorsionAgent:
        """Spawn new agent with adaptive parameters"""
        # Bias new agents based on system state
        if self.best_agent:
            # Spawn near best agent with some variation
            base_drift = self.best_agent.drift.mutate(reward=0.5, volatility=0.2)
        else:
            # Random spawn
            base_drift = DriftVector(
                coherence=random.uniform(0.6, 1.0),
                entropy=random.uniform(0.05, 0.3),
                resonance=random.uniform(0.7, 1.0)
            )
        
        agent = TorsionAgent(drift=base_drift)
        self.agents.append(agent)
        return agent
    
    def competitive_step(self, a: TorsionAgent, b: TorsionAgent, task: PhiTask):
        """Execute competitive interaction"""
        score_a = a.act(task)
        score_b = b.act(task)
        
        # Determine winner and reward
        if abs(score_a - score_b) < self.competition_threshold:
            # Too close - switch to collaboration
            self.mode = SimulationMode.COLLABORATIVE
            self.collaboration_bias += 0.05
            self.transitions.append((self.step, "comp→collab", a.id, b.id, "tie"))
        else:
            # Clear winner
            winner = a if score_a > score_b else b
            loser = b if score_a > score_b else a
            
            # Winner learns from success
            reward = abs(score_a - score_b)
            winner.learn(reward)
            
            # Create mutated offspring
            offspring = TorsionAgent(drift=winner.drift.mutate(reward, self.volatility))
            offspring.generation = winner.generation + 1
            self.agents.append(offspring)
            
            # Track performance
            if winner.average_performance() > self.best_score:
                self.best_agent = winner
                self.best_score = winner.average_performance()
            
            self.total_competitions += 1
            self.transitions.append((self.step, "compete", a.id, b.id, offspring.id))
    
    def collaborative_step(self, a: TorsionAgent, b: TorsionAgent, task: PhiTask):
        """Execute collaborative interaction"""
        # Both agents work on task
        score_a = a.act(task)
        score_b = b.act(task)
        
        # Create fused agent
        fused = a.fuse(b)
        fused_score = fused.act(task)
        
        # Reward based on collaborative success
        collaboration_reward = (score_a + score_b + fused_score) / 3.0
        a.learn(collaboration_reward * 0.5)
        b.learn(collaboration_reward * 0.5)
        fused.learn(collaboration_reward)
        
        self.agents.append(fused)
        self.total_fusions += 1
        
        # Switch back to competitive mode
        self.mode = SimulationMode.COMPETITIVE
        self.collaboration_bias = max(0.0, self.collaboration_bias - 0.02)
        
        self.transitions.append((self.step, "collaborate", a.id, b.id, fused.id))
    
    def torsion_sync_step(self):
        """Execute torsion synchronization - system-wide rebalancing"""
        if len(self.agents) < 2:
            return
        
        # Sort agents by phi alignment
        self.agents.sort(key=lambda ag: ag.phi_alignment(), reverse=True)
        
        # Apply torsion field effects
        for agent in self.agents:
            torsion_energy = agent.drift.torsion_energy()
            agent.drift = agent.drift.mutate(torsion_energy, volatility=0.05)
            agent.survival_time += 1
        
        # Prune poorly performing agents
        if len(self.agents) > 20:
            # Keep top performers and some random agents for diversity
            top_agents = self.agents[:15]
            random_agents = random.sample(self.agents[15:], min(5, len(self.agents) - 15))
            self.agents = top_agents + random_agents
        
        self.transitions.append((self.step, "torsion-sync", None, None, f"{len(self.agents)} agents"))
    
    def run_step(self):
        """Execute one simulation step"""
        # Create new task
        task = PhiTask()
        task.creation_step = self.step
        self.phi_space.append(task)
        
        # Ensure minimum agents
        while len(self.agents) < 2:
            self.spawn_agent()
        
        # Select agents for interaction
        if len(self.agents) >= 2:
            # Select based on recent performance and diversity
            candidates = self.agents[-10:]  # Recent agents
            a, b = random.sample(candidates, 2)
            
            # Execute step based on mode
            if self.mode == SimulationMode.COMPETITIVE:
                self.competitive_step(a, b, task)
            elif self.mode == SimulationMode.COLLABORATIVE:
                self.collaborative_step(a, b, task)
            elif self.mode == SimulationMode.TORSION_SYNC:
                self.torsion_sync_step()
                self.mode = SimulationMode.COMPETITIVE
        
        # Special checkpoints
        if self.is_prime(self.step):
            self.transitions.append((self.step, "prime-checkpoint", None, None, None))
        
        if self.is_fib_prime(self.step):
            self.mode = SimulationMode.TORSION_SYNC
            self.transitions.append((self.step, "fib-prime-sync", None, None, None))
        
        # Adaptive parameter adjustment
        if self.step % 10 == 0:
            self.volatility = max(0.05, self.volatility * 0.99)  # Gradual cooling
        
        self.step += 1
    
    def run_simulation(self, steps: int = 100) -> Dict[str, Any]:
        """Run full simulation and return results"""
        print(f"Starting Torsion Simulation for {steps} steps...")
        
        for i in range(steps):
            self.run_step()
            
            # Progress reporting
            if (i + 1) % 20 == 0:
                print(f"Step {i + 1}: {len(self.agents)} agents, "
                      f"Mode: {self.mode.value}, "
                      f"Best Score: {self.best_score:.3f}")
        
        # Compile results
        results = {
            'total_steps': steps,
            'final_agents': len(self.agents),
            'total_fusions': self.total_fusions,
            'total_competitions': self.total_competitions,
            'mode_switches': self.mode_switches,
            'best_score': self.best_score,
            'best_agent': str(self.best_agent) if self.best_agent else None,
            'transitions': self.transitions,
            'agent_summary': [
                {
                    'id': agent.id,
                    'generation': agent.generation,
                    'avg_performance': agent.average_performance(),
                    'phi_alignment': agent.phi_alignment(),
                    'coherence': agent.drift.coherence,
                    'entropy': agent.drift.entropy,
                    'resonance': agent.drift.resonance
                }
                for agent in sorted(self.agents, key=lambda a: a.average_performance(), reverse=True)[:5]
            ]
        }
        
        return results

# === MAIN SIMULATION RUNNER ===
if __name__ == "__main__":
    # Initialize and run simulation
    orchestrator = DriftOrchestrator()
    results = orchestrator.run_simulation(steps=150)
    
    # Display results
    print("\n" + "="*50)
    print("SIMULATION RESULTS")
    print("="*50)
    
    print(f"Total Steps: {results['total_steps']}")
    print(f"Final Agents: {results['final_agents']}")
    print(f"Total Fusions: {results['total_fusions']}")
    print(f"Total Competitions: {results['total_competitions']}")
    print(f"Best Score: {results['best_score']:.3f}")
    print(f"Best Agent: {results['best_agent']}")
    
    print("\nTop 5 Agents:")
    for i, agent in enumerate(results['agent_summary'], 1):
        print(f"{i}. {agent['id']} - Gen:{agent['generation']}, "
              f"Perf:{agent['avg_performance']:.3f}, "
              f"Phi:{agent['phi_alignment']:.3f}")
    
    print(f"\nLast 10 Transitions:")
    for transition in results['transitions'][-10:]:
        step, action, a, b, result = transition
        print(f"Step {step}: {action} ({a} + {b} → {result})")
    
    print("\nSimulation Complete!")
