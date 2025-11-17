"""
Unsolution Manifold Explorer v1.0
==================================
Maps solved problems back to their pre-solution problem-space,
revealing alternative formulations and hidden assumptions.

Operators:
  un_S: Solution → ProblemManifold
  ◊_K: Keyword → AgnosticState  
  Q_K: Text → QuestionStructure
  Ξ_bridge: Keyword × Keyword → StructuralPattern
"""

import re
from typing import List, Dict, Set, Tuple, Optional
from dataclasses import dataclass, field
from collections import defaultdict
import json


# ============================================================================
# CORE DATA STRUCTURES
# ============================================================================

@dataclass
class Keyword:
    """A keyword with domain commitment state"""
    term: str
    domains: Set[str] = field(default_factory=set)
    commitment_level: str = "unknown"  # specific, cross-domain, agnostic
    structural_role: Optional[str] = None
    
    def is_agnostic(self) -> bool:
        return len(self.domains) > 4 or self.commitment_level == "agnostic"
    
    def is_question_keyword(self) -> bool:
        interrogatives = {'what', 'why', 'how', 'when', 'where', 'which'}
        epistemic = {'unknown', 'uncertain', 'mystery', 'paradox', 'puzzle'}
        return self.term.lower() in interrogatives or self.term.lower() in epistemic


@dataclass
class QuestionStructure:
    """Interrogative structure extracted from text"""
    interrogatives: List[str]
    epistemic_markers: List[str]
    modal_markers: List[str]
    target_unknowns: List[str]
    presuppositions: List[str]
    
    def to_dict(self) -> dict:
        return {
            'interrogatives': self.interrogatives,
            'epistemic_markers': self.epistemic_markers,
            'modal_markers': self.modal_markers,
            'unknowns': self.target_unknowns,
            'presuppositions': self.presuppositions
        }


@dataclass
class ProblemSpace:
    """The unsolution manifold for a given solution"""
    original_solution: str
    generating_questions: List[str]
    alternative_formulations: List[str]
    hidden_assumptions: List[str]
    agnostic_keywords: List[Keyword]
    domain_specific_keywords: List[Keyword]
    structural_patterns: Dict[str, str]
    epistemic_state: str  # solved, partial, open, paradoxical
    
    def to_dict(self) -> dict:
        return {
            'solution': self.original_solution,
            'questions': self.generating_questions,
            'alternatives': self.alternative_formulations,
            'assumptions': self.hidden_assumptions,
            'agnostic_keywords': [k.term for k in self.agnostic_keywords],
            'domain_keywords': [k.term for k in self.domain_specific_keywords],
            'patterns': self.structural_patterns,
            'epistemic_state': self.epistemic_state
        }


# ============================================================================
# OPERATOR: un_S (Unsolution)
# ============================================================================

class UnsolutionOperator:
    """Maps solutions back to problem-space"""
    
    def __init__(self):
        # Pattern database for reverse inference
        self.solution_patterns = self._initialize_patterns()
        
    def _initialize_patterns(self) -> Dict[str, List[str]]:
        """Known solution→question patterns"""
        return {
            'definition': [
                'What is {concept}?',
                'How do we define {concept}?',
                'What constitutes {concept}?'
            ],
            'mechanism': [
                'How does {process} work?',
                'What mechanism underlies {process}?',
                'By what means does {process} occur?'
            ],
            'causation': [
                'Why does {effect} occur?',
                'What causes {effect}?',
                'What is responsible for {effect}?'
            ],
            'composition': [
                'What is {system} made of?',
                'What are the components of {system}?',
                'What constitutes {system}?'
            ],
            'emergence': [
                'How does {complex} arise from {simple}?',
                'What generates {emergent_property}?',
                'Why does {pattern} emerge?'
            ],
            'relation': [
                'How does {A} relate to {B}?',
                'What is the connection between {A} and {B}?',
                'Why are {A} and {B} linked?'
            ]
        }
    
    def apply(self, solution: str) -> ProblemSpace:
        """Apply unsolution operator: solution → problem-space"""
        
        # Extract key components
        keywords = self._extract_keywords(solution)
        structure = self._analyze_structure(solution)
        
        # Generate questions
        questions = self._generate_questions(solution, structure)
        
        # Find alternatives
        alternatives = self._generate_alternatives(solution, structure)
        
        # Extract assumptions
        assumptions = self._extract_assumptions(solution, keywords)
        
        # Classify keywords
        agnostic, domain_specific = self._classify_keywords(keywords)
        
        # Identify patterns
        patterns = self._identify_patterns(keywords)
        
        # Determine epistemic state
        epistemic_state = self._assess_epistemic_state(solution)
        
        return ProblemSpace(
            original_solution=solution,
            generating_questions=questions,
            alternative_formulations=alternatives,
            hidden_assumptions=assumptions,
            agnostic_keywords=agnostic,
            domain_specific_keywords=domain_specific,
            structural_patterns=patterns,
            epistemic_state=epistemic_state
        )
    
    def _extract_keywords(self, text: str) -> List[Keyword]:
        """Extract keywords from solution text"""
        # Simple implementation - in production use NLP
        words = re.findall(r'\b[a-z]{3,}\b', text.lower())
        
        # Filter stopwords
        stopwords = {'the', 'and', 'but', 'for', 'with', 'from', 'this', 'that', 'are', 'was'}
        keywords = [w for w in words if w not in stopwords]
        
        # Create Keyword objects
        return [Keyword(term=k) for k in set(keywords)]
    
    def _analyze_structure(self, solution: str) -> str:
        """Identify solution structure type"""
        solution_lower = solution.lower()
        
        if any(word in solution_lower for word in ['is', 'are', 'defined as', 'means']):
            return 'definition'
        elif any(word in solution_lower for word in ['because', 'due to', 'caused by']):
            return 'causation'
        elif any(word in solution_lower for word in ['works by', 'functions through', 'mechanism']):
            return 'mechanism'
        elif any(word in solution_lower for word in ['consists of', 'composed of', 'made of']):
            return 'composition'
        elif any(word in solution_lower for word in ['emerges', 'arises', 'generated from']):
            return 'emergence'
        elif any(word in solution_lower for word in ['relates to', 'connected to', 'linked']):
            return 'relation'
        else:
            return 'general'
    
    def _generate_questions(self, solution: str, structure: str) -> List[str]:
        """Reverse-engineer questions that generated this solution"""
        questions = []
        
        # Use pattern templates
        if structure in self.solution_patterns:
            templates = self.solution_patterns[structure]
            
            # Extract main concepts (simplified - use NLP in production)
            concepts = self._extract_main_concepts(solution)
            
            for template in templates:
                # Fill templates with concepts
                if '{concept}' in template and concepts:
                    questions.append(template.format(concept=concepts[0]))
                elif '{process}' in template and concepts:
                    questions.append(template.format(process=concepts[0]))
                elif '{effect}' in template and concepts:
                    questions.append(template.format(effect=concepts[0]))
        
        # Add meta-questions
        questions.extend([
            f"Is this the only way to understand this?",
            f"What alternatives exist?",
            f"What assumptions enable this answer?"
        ])
        
        return questions
    
    def _extract_main_concepts(self, text: str) -> List[str]:
        """Extract main concepts from text"""
        # Simplified - look for capitalized or multi-word terms
        words = text.split()
        concepts = []
        
        for i, word in enumerate(words):
            if word[0].isupper() and i > 0:
                concepts.append(word.lower())
            elif i < len(words) - 1 and words[i+1][0].isupper():
                concepts.append(f"{word} {words[i+1]}".lower())
        
        return concepts[:3] if concepts else [words[0] if words else "concept"]
    
    def _generate_alternatives(self, solution: str, structure: str) -> List[str]:
        """Generate alternative problem formulations"""
        alternatives = []
        
        # Generic alternatives based on structure
        if structure == 'definition':
            alternatives.extend([
                "Operational definition: Define by what it does",
                "Ostensive definition: Define by examples",
                "Negative definition: Define by what it's not",
                "Functional definition: Define by purpose"
            ])
        elif structure == 'causation':
            alternatives.extend([
                "Multiple causation: Are there other contributing factors?",
                "Reverse causation: Could the effect cause the cause?",
                "Correlation not causation: Is this just association?",
                "Systemic causation: Is it emergent from system dynamics?"
            ])
        elif structure == 'mechanism':
            alternatives.extend([
                "Alternative mechanisms: Other pathways to same outcome?",
                "Multiple realizability: Can different substrates produce this?",
                "Emergent mechanism: Is it higher-level phenomenon?",
                "Reductive mechanism: Is it fully decomposable?"
            ])
        else:
            alternatives.extend([
                "Could this be framed differently?",
                "What if we change the level of analysis?",
                "What if we change the domain?",
                "What if we invert the relationship?"
            ])
        
        return alternatives
    
    def _extract_assumptions(self, solution: str, keywords: List[Keyword]) -> List[str]:
        """Extract hidden assumptions"""
        assumptions = []
        
        # Ontological assumptions
        assumptions.append("ONTOLOGICAL: Assumes entities mentioned actually exist")
        
        # Epistemological assumptions
        if any(word in solution.lower() for word in ['is', 'are', 'must be']):
            assumptions.append("EPISTEMOLOGICAL: Assumes we can know this with certainty")
        
        # Methodological assumptions
        if any(word in solution.lower() for word in ['because', 'therefore', 'thus']):
            assumptions.append("METHODOLOGICAL: Assumes causal inference is valid")
        
        # Domain assumptions
        assumptions.append("DOMAIN: Assumes problem belongs to specific domain")
        
        # Reductionism/holism
        if any(word in solution.lower() for word in ['consists of', 'made of', 'composed']):
            assumptions.append("REDUCTIONIST: Assumes whole can be understood through parts")
        
        # Temporal assumptions
        assumptions.append("TEMPORAL: Assumes static solution or specific time-scale")
        
        return assumptions
    
    def _classify_keywords(self, keywords: List[Keyword]) -> Tuple[List[Keyword], List[Keyword]]:
        """Classify keywords as agnostic or domain-specific"""
        
        # Agnostic keywords (structural/process terms)
        agnostic_terms = {
            'system', 'process', 'structure', 'pattern', 'relation',
            'emergence', 'recursion', 'feedback', 'network', 'dynamic',
            'transformation', 'interaction', 'boundary', 'integration',
            'differentiation', 'complexity', 'organization', 'function'
        }
        
        agnostic = []
        domain_specific = []
        
        for kw in keywords:
            if kw.term in agnostic_terms:
                kw.commitment_level = 'agnostic'
                kw.structural_role = f"structural-{kw.term}"
                agnostic.append(kw)
            else:
                kw.commitment_level = 'specific'
                domain_specific.append(kw)
        
        return agnostic, domain_specific
    
    def _identify_patterns(self, keywords: List[Keyword]) -> Dict[str, str]:
        """Identify structural patterns in keywords"""
        patterns = {}
        
        keyword_terms = {kw.term for kw in keywords}
        
        # Check for common patterns
        if 'recursion' in keyword_terms or 'recursive' in keyword_terms:
            patterns['self-reference'] = '↻ (recursive structure detected)'
        
        if 'emergence' in keyword_terms or 'emergent' in keyword_terms:
            patterns['emergence'] = '⬆ (bottom-up complexity generation)'
        
        if 'boundary' in keyword_terms or 'interface' in keyword_terms:
            patterns['boundary'] = '◎ (inside/outside distinction)'
        
        if 'integration' in keyword_terms or 'synthesis' in keyword_terms:
            patterns['integration'] = '⧉ (part-whole composition)'
        
        if 'potential' in keyword_terms or 'possible' in keyword_terms:
            patterns['potentiality'] = '◊ (unrealized possibility)'
        
        return patterns
    
    def _assess_epistemic_state(self, solution: str) -> str:
        """Determine epistemic status of solution"""
        solution_lower = solution.lower()
        
        if any(word in solution_lower for word in ['unknown', 'unclear', 'mystery']):
            return 'open'
        elif any(word in solution_lower for word in ['paradox', 'contradiction', 'inconsistent']):
            return 'paradoxical'
        elif any(word in solution_lower for word in ['partially', 'somewhat', 'likely']):
            return 'partial'
        else:
            return 'solved'


# ============================================================================
# OPERATOR: Q_K (Question-Keyword Extraction)
# ============================================================================

class QuestionKeywordOperator:
    """Extract question structure from text"""
    
    def __init__(self):
        self.interrogatives = {'what', 'why', 'how', 'when', 'where', 'which', 'who'}
        self.epistemic_markers = {
            'unknown', 'uncertain', 'unclear', 'mystery', 'puzzle',
            'paradox', 'question', 'wonder', 'doubt'
        }
        self.modal_markers = {
            'could', 'would', 'should', 'might', 'may', 'can',
            'possible', 'necessary', 'contingent'
        }
    
    def apply(self, text: str) -> QuestionStructure:
        """Extract question structure from text"""
        text_lower = text.lower()
        words = set(text_lower.split())
        
        # Extract each component
        interrogatives = [w for w in words if w in self.interrogatives]
        epistemic = [w for w in words if w in self.epistemic_markers]
        modal = [w for w in words if w in self.modal_markers]
        
        # Identify unknowns (marked by question words)
        unknowns = self._identify_unknowns(text)
        
        # Extract presuppositions
        presuppositions = self._extract_presuppositions(text)
        
        return QuestionStructure(
            interrogatives=interrogatives,
            epistemic_markers=epistemic,
            modal_markers=modal,
            target_unknowns=unknowns,
            presuppositions=presuppositions
        )
    
    def _identify_unknowns(self, text: str) -> List[str]:
        """Identify what is being asked about"""
        unknowns = []
        
        # Look for patterns like "What is X?" or "How does X work?"
        patterns = [
            r'what (?:is|are|was|were) ([^?]+)',
            r'how (?:does|do|did) ([^?]+)',
            r'why (?:is|are|does|do) ([^?]+)',
            r'where (?:is|are|does|do) ([^?]+)',
            r'when (?:is|are|does|do) ([^?]+)'
        ]
        
        for pattern in patterns:
            matches = re.findall(pattern, text.lower())
            unknowns.extend(matches)
        
        return unknowns[:5]  # Limit to 5
    
    def _extract_presuppositions(self, text: str) -> List[str]:
        """Extract implicit assumptions in question"""
        presuppositions = []
        
        # Questions presuppose existence of entities mentioned
        if 'what is' in text.lower():
            presuppositions.append("Presupposes: Entity exists and has definable nature")
        
        if 'how does' in text.lower():
            presuppositions.append("Presupposes: Process exists and has mechanism")
        
        if 'why' in text.lower():
            presuppositions.append("Presupposes: Phenomenon exists and has cause/purpose")
        
        return presuppositions


# ============================================================================
# OPERATOR: ◊_K (Agnostic Keyword)
# ============================================================================

class AgnosticOperator:
    """Strip domain commitment from keywords"""
    
    def __init__(self):
        # Database of cross-domain keyword meanings
        self.agnostic_mappings = {
            'network': {
                'structural_role': 'nodes connected by edges',
                'domains': {'neuroscience', 'cs', 'sociology', 'ecology'},
                'pattern': 'graph structure'
            },
            'recursion': {
                'structural_role': 'self-referential iteration',
                'domains': {'math', 'cs', 'linguistics', 'philosophy', 'biology'},
                'pattern': 'strange loop'
            },
            'emergence': {
                'structural_role': 'higher-order properties from lower-order components',
                'domains': {'physics', 'chemistry', 'biology', 'sociology', 'ai'},
                'pattern': 'bottom-up complexity'
            },
            'feedback': {
                'structural_role': 'output influences input',
                'domains': {'control-theory', 'ecology', 'economics', 'psychology'},
                'pattern': 'circular causation'
            },
            'boundary': {
                'structural_role': 'inside/outside distinction',
                'domains': {'topology', 'systems-theory', 'psychology', 'biology'},
                'pattern': 'containment'
            }
        }
    
    def apply(self, keyword: Keyword) -> Keyword:
        """Strip domain commitment, return agnostic form"""
        term = keyword.term.lower()
        
        if term in self.agnostic_mappings:
            mapping = self.agnostic_mappings[term]
            keyword.structural_role = mapping['structural_role']
            keyword.domains = mapping['domains']
            keyword.commitment_level = 'agnostic'
        
        return keyword
    
    def find_structural_pattern(self, kw1: Keyword, kw2: Keyword) -> Optional[str]:
        """Find structural isomorphism between keywords (Ξ_bridge)"""
        
        # Check if both are agnostic
        if not (kw1.is_agnostic() and kw2.is_agnostic()):
            return None
        
        # Check for pattern matches
        if kw1.structural_role and kw2.structural_role:
            # Both involve self-reference
            if 'self' in kw1.structural_role and 'self' in kw2.structural_role:
                return "shared: self-referential structure (↻)"
            
            # Both involve part-whole
            if any(word in kw1.structural_role for word in ['component', 'part', 'whole']):
                if any(word in kw2.structural_role for word in ['component', 'part', 'whole']):
                    return "shared: part-whole composition (⧉)"
        
        return None


# ============================================================================
# MAIN EXPLORER CLASS
# ============================================================================

class UnsolutionManifoldExplorer:
    """
    Main explorer that integrates all operators
    """
    
    def __init__(self):
        self.un_S = UnsolutionOperator()
        self.Q_K = QuestionKeywordOperator()
        self.agnostic_op = AgnosticOperator()
    
    def explore(self, solution: str) -> ProblemSpace:
        """
        Main exploration function: solution → unsolution manifold
        """
        print("=" * 80)
        print("UNSOLUTION MANIFOLD EXPLORER")
        print("=" * 80)
        print(f"\nOriginal Solution:\n  {solution}\n")
        
        # Apply unsolution operator
        problem_space = self.un_S.apply(solution)
        
        # Apply agnostic operator to keywords
        for kw in problem_space.agnostic_keywords:
            self.agnostic_op.apply(kw)
        
        return problem_space
    
    def display(self, problem_space: ProblemSpace):
        """Display the unsolution manifold"""
        print("\n" + "─" * 80)
        print("PROBLEM-SPACE ANALYSIS")
        print("─" * 80)
        
        print(f"\n◎ EPISTEMIC STATE: {problem_space.epistemic_state.upper()}")
        
        print("\n↻ GENERATING QUESTIONS:")
        for i, q in enumerate(problem_space.generating_questions, 1):
            print(f"   {i}. {q}")
        
        print("\n⧉ ALTERNATIVE FORMULATIONS:")
        for i, alt in enumerate(problem_space.alternative_formulations, 1):
            print(f"   {i}. {alt}")
        
        print("\n⊥ HIDDEN ASSUMPTIONS:")
        for i, assume in enumerate(problem_space.hidden_assumptions, 1):
            print(f"   {i}. {assume}")
        
        print("\n◊ AGNOSTIC KEYWORDS (domain-independent structure):")
        for kw in problem_space.agnostic_keywords:
            role = kw.structural_role or "structural term"
            print(f"   • {kw.term}: {role}")
        
        print("\n⊡ DOMAIN-SPECIFIC KEYWORDS:")
        for kw in problem_space.domain_specific_keywords[:10]:  # Limit display
            print(f"   • {kw.term}")
        
        if problem_space.structural_patterns:
            print("\n∇ STRUCTURAL PATTERNS:")
            for pattern, desc in problem_space.structural_patterns.items():
                print(f"   • {pattern}: {desc}")
        
        print("\n" + "=" * 80)
    
    def compare_solutions(self, solution1: str, solution2: str):
        """Compare two solutions' problem-spaces"""
        print("\n" + "=" * 80)
        print("COMPARATIVE UNSOLUTION ANALYSIS")
        print("=" * 80)
        
        ps1 = self.un_S.apply(solution1)
        ps2 = self.un_S.apply(solution2)
        
        # Find shared agnostic keywords
        ag1_terms = {kw.term for kw in ps1.agnostic_keywords}
        ag2_terms = {kw.term for kw in ps2.agnostic_keywords}
        shared = ag1_terms & ag2_terms
        
        print(f"\n◊ SHARED AGNOSTIC STRUCTURE:")
        for term in shared:
            print(f"   • {term}")
        
        # Find shared patterns
        pat1 = set(ps1.structural_patterns.keys())
        pat2 = set(ps2.structural_patterns.keys())
        shared_patterns = pat1 & pat2
        
        if shared_patterns:
            print(f"\n∇ SHARED STRUCTURAL PATTERNS:")
            for pattern in shared_patterns:
                print(f"   • {pattern}")
        
        print("\n" + "=" * 80)
    
    def export_json(self, problem_space: ProblemSpace, filename: str):
        """Export problem-space to JSON"""
        with open(filename, 'w') as f:
            json.dump(problem_space.to_dict(), f, indent=2)
        print(f"\n✓ Exported to {filename}")


# ============================================================================
# EXAMPLE USAGE
# ============================================================================

def main():
    """Run example explorations"""
    explorer = UnsolutionManifoldExplorer()
    
    # Example 1: Consciousness
    print("\n" + "█" * 80)
    print("EXAMPLE 1: CONSCIOUSNESS")
    print("█" * 80)
    
    solution1 = """Consciousness is an emergent property arising from integrated 
    information processing in recursive neural networks that create self-referential 
    models, generating the boundary between observer and observed."""
    
    ps1 = explorer.explore(solution1)
    explorer.display(ps1)
    
    # Example 2: Dark Matter  
    print("\n" + "█" * 80)
    print("EXAMPLE 2: DARK MATTER")
    print("█" * 80)
    
    solution2 = """Dark matter is non-baryonic matter that interacts primarily through 
    gravitational forces, making up approximately 85% of the universe's matter content 
    and explaining galactic rotation curves and gravitational lensing effects."""
    
    ps2 = explorer.explore(solution2)
    explorer.display(ps2)
    
    # Example 3: Life
    print("\n" + "█" * 80)
    print("EXAMPLE 3: LIFE")
    print("█" * 80)
    
    solution3 = """Life is a self-organizing, self-replicating chemical system that 
    maintains homeostasis through metabolic processes and evolves through natural 
    selection acting on heritable variation."""
    
    ps3 = explorer.explore(solution3)
    explorer.display(ps3)
    
    # Comparative analysis
    print("\n" + "█" * 80)
    print("COMPARATIVE ANALYSIS: Consciousness vs Life")
    print("█" * 80)
    explorer.compare_solutions(solution1, solution3)
    
    # Export
    explorer.export_json(ps1, "/home/claude/consciousness_unsolution.json")


if __name__ == "__main__":
    main()