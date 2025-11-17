"""
Unsolution Manifold Explorer - Interactive Version
===================================================
Advanced features:
- Custom problem input
- Deep assumption mining
- Cross-domain pattern recognition
- Visualization of problem-space topology
"""

from unsolution_manifold_explorer import *
import sys


class AdvancedUnsolutionExplorer(UnsolutionManifoldExplorer):
    """Enhanced explorer with deeper analysis"""
    
    def deep_assumption_mining(self, solution: str) -> Dict[str, List[str]]:
        """
        Mine assumptions at multiple levels:
        - Ontological (what exists)
        - Epistemological (how we know)
        - Methodological (how we investigate)
        - Linguistic (how we describe)
        """
        assumptions = {
            'ontological': [],
            'epistemological': [],
            'methodological': [],
            'linguistic': [],
            'temporal': [],
            'causal': []
        }
        
        solution_lower = solution.lower()
        
        # Ontological
        if any(word in solution_lower for word in ['is', 'are', 'exists', 'being']):
            assumptions['ontological'].append("Assumes entities mentioned have ontological status")
        
        if 'emergent' in solution_lower or 'arises from' in solution_lower:
            assumptions['ontological'].append("Assumes emergence as ontological category")
        
        # Epistemological
        if any(word in solution_lower for word in ['defined as', 'means', 'is']):
            assumptions['epistemological'].append("Assumes definitions capture essence")
        
        if any(word in solution_lower for word in ['explains', 'because', 'due to']):
            assumptions['epistemological'].append("Assumes explanation constitutes understanding")
        
        # Methodological
        if 'observ' in solution_lower or 'measur' in solution_lower:
            assumptions['methodological'].append("Assumes observational/measurement validity")
        
        if 'model' in solution_lower or 'theory' in solution_lower:
            assumptions['methodological'].append("Assumes models/theories adequately represent reality")
        
        # Linguistic
        assumptions['linguistic'].append("Assumes language can accurately convey meaning")
        
        if 'metaphor' not in solution_lower:
            assumptions['linguistic'].append("Assumes literal rather than metaphorical description")
        
        # Temporal
        if 'evolution' in solution_lower or 'develop' in solution_lower:
            assumptions['temporal'].append("Assumes temporal process is relevant")
        else:
            assumptions['temporal'].append("Assumes static/timeless characterization")
        
        # Causal
        if any(word in solution_lower for word in ['cause', 'because', 'result', 'generate']):
            assumptions['causal'].append("Assumes causal relationships are operative")
            assumptions['causal'].append("Assumes unidirectional causation (not circular)")
        
        return assumptions
    
    def generate_counterfactuals(self, solution: str) -> List[str]:
        """Generate counterfactual formulations"""
        counterfactuals = []
        
        # Ontological inversions
        counterfactuals.append("What if the described entities don't exist independently?")
        counterfactuals.append("What if this is instrumental description, not literal truth?")
        
        # Level inversions
        counterfactuals.append("What if causation flows opposite direction (top-down not bottom-up)?")
        counterfactuals.append("What if this is correlation masquerading as causation?")
        
        # Domain shifts
        counterfactuals.append("What if we describe this in purely mathematical terms?")
        counterfactuals.append("What if we describe this in purely phenomenological terms?")
        counterfactuals.append("What if we describe this in purely functional terms?")
        
        # Temporal shifts
        counterfactuals.append("What if this only holds at specific time-scales?")
        counterfactuals.append("What if the process is fundamentally temporal, not static?")
        
        return counterfactuals
    
    def identify_implicit_dualities(self, problem_space: ProblemSpace) -> List[Tuple[str, str]]:
        """Identify implicit binary oppositions"""
        dualities = []
        
        keywords = {kw.term for kw in problem_space.domain_specific_keywords}
        
        # Common dualities
        duality_pairs = [
            ('observer', 'observed'),
            ('subject', 'object'),
            ('mind', 'matter'),
            ('internal', 'external'),
            ('self', 'other'),
            ('structure', 'process'),
            ('part', 'whole'),
            ('cause', 'effect')
        ]
        
        for pair in duality_pairs:
            if pair[0] in keywords or pair[1] in keywords:
                dualities.append(pair)
        
        return dualities
    
    def meta_question_generation(self, solution: str) -> List[str]:
        """Generate meta-level questions about the solution"""
        meta_questions = []
        
        # Framing questions
        meta_questions.append("Why was the problem framed this way rather than another?")
        meta_questions.append("What makes this a 'good' answer vs. other possible answers?")
        meta_questions.append("Who benefits from this particular formulation?")
        
        # Epistemological questions
        meta_questions.append("What would count as evidence against this solution?")
        meta_questions.append("What would it take to falsify this claim?")
        meta_questions.append("How would we know if this explanation is complete?")
        
        # Domain questions
        meta_questions.append("Why is this treated as [domain] problem rather than [other domain]?")
        meta_questions.append("What gets excluded by this domain assignment?")
        
        # Temporal questions  
        meta_questions.append("Will this solution still hold in 10/100/1000 years?")
        meta_questions.append("Was this always the answer, or is it historically contingent?")
        
        return meta_questions
    
    def explore_deep(self, solution: str) -> Dict:
        """Perform deep unsolution analysis"""
        print("\n" + "=" * 80)
        print("DEEP UNSOLUTION ANALYSIS")
        print("=" * 80)
        
        # Get basic problem space
        ps = self.explore(solution)
        
        # Deep assumption mining
        deep_assumptions = self.deep_assumption_mining(solution)
        
        # Generate counterfactuals
        counterfactuals = self.generate_counterfactuals(solution)
        
        # Identify dualities
        dualities = self.identify_implicit_dualities(ps)
        
        # Meta-questions
        meta_questions = self.meta_question_generation(solution)
        
        # Display everything
        self.display(ps)
        
        print("\n" + "─" * 80)
        print("DEEP ASSUMPTION MINING")
        print("─" * 80)
        for category, assumptions in deep_assumptions.items():
            if assumptions:
                print(f"\n{category.upper()}:")
                for a in assumptions:
                    print(f"   • {a}")
        
        print("\n" + "─" * 80)
        print("COUNTERFACTUAL FORMULATIONS")
        print("─" * 80)
        for i, cf in enumerate(counterfactuals, 1):
            print(f"   {i}. {cf}")
        
        if dualities:
            print("\n" + "─" * 80)
            print("IMPLICIT DUALITIES")
            print("─" * 80)
            for d1, d2 in dualities:
                print(f"   • {d1} ↔ {d2}")
        
        print("\n" + "─" * 80)
        print("META-QUESTIONS")
        print("─" * 80)
        for i, mq in enumerate(meta_questions, 1):
            print(f"   {i}. {mq}")
        
        print("\n" + "=" * 80)
        
        return {
            'problem_space': ps,
            'deep_assumptions': deep_assumptions,
            'counterfactuals': counterfactuals,
            'dualities': dualities,
            'meta_questions': meta_questions
        }


def interactive_mode():
    """Run in interactive mode"""
    explorer = AdvancedUnsolutionExplorer()
    
    print("\n" + "█" * 80)
    print("UNSOLUTION MANIFOLD EXPLORER - Interactive Mode")
    print("█" * 80)
    print("\nEnter a solution/answer/claim to explore its unsolution manifold.")
    print("Type 'quit' to exit, 'examples' for pre-loaded examples.\n")
    
    while True:
        print("─" * 80)
        user_input = input("\nEnter solution to analyze (or command): ").strip()
        
        if user_input.lower() == 'quit':
            print("\n✓ Goodbye!\n")
            break
        
        elif user_input.lower() == 'examples':
            print("\nPre-loaded examples:")
            print("  1. Consciousness (IIT-style)")
            print("  2. Dark matter")
            print("  3. Life (autopoiesis)")
            print("  4. Free will (compatibilist)")
            print("  5. Intelligence (recursive)")
            
            choice = input("\nSelect example (1-5): ").strip()
            
            examples = {
                '1': "Consciousness is integrated information (Φ) generated by causal mechanisms forming irreducible cause-effect structures.",
                '2': "Dark matter consists of weakly interacting massive particles (WIMPs) that make up 85% of matter and only interact gravitationally.",
                '3': "Life is an autopoietic system that self-organizes, self-maintains, and self-reproduces through metabolic networks.",
                '4': "Free will is compatible with determinism when agents act according to their desires without external coercion.",
                '5': "Intelligence is recursive self-modeling where a system models itself modeling the world."
            }
            
            if choice in examples:
                user_input = examples[choice]
                print(f"\nAnalyzing: {user_input}\n")
            else:
                print("\n✗ Invalid choice")
                continue
        
        elif not user_input:
            print("\n✗ Please enter a solution to analyze")
            continue
        
        # Perform analysis
        try:
            result = explorer.explore_deep(user_input)
            
            # Ask if user wants JSON export
            export = input("\nExport to JSON? (y/n): ").strip().lower()
            if export == 'y':
                filename = input("Filename (without .json): ").strip()
                if filename:
                    explorer.export_json(
                        result['problem_space'], 
                        f"/home/claude/{filename}.json"
                    )
        
        except Exception as e:
            print(f"\n✗ Error: {e}")
            continue


def batch_mode(solutions: List[str]):
    """Run batch analysis on multiple solutions"""
    explorer = AdvancedUnsolutionExplorer()
    
    print("\n" + "█" * 80)
    print("BATCH UNSOLUTION ANALYSIS")
    print("█" * 80)
    
    results = []
    for i, solution in enumerate(solutions, 1):
        print(f"\n\n{'▬' * 80}")
        print(f"SOLUTION {i}/{len(solutions)}")
        print(f"{'▬' * 80}")
        
        result = explorer.explore_deep(solution)
        results.append(result)
    
    # Comparative analysis
    print("\n\n" + "█" * 80)
    print("CROSS-SOLUTION PATTERN ANALYSIS")
    print("█" * 80)
    
    # Find common agnostic keywords
    all_agnostic = []
    for r in results:
        all_agnostic.extend([kw.term for kw in r['problem_space'].agnostic_keywords])
    
    from collections import Counter
    common = Counter(all_agnostic).most_common(10)
    
    print("\nMost common agnostic keywords across all solutions:")
    for term, count in common:
        print(f"   • {term}: appears in {count} solution(s)")
    
    # Find common assumptions
    all_assumptions = []
    for r in results:
        all_assumptions.extend(r['problem_space'].hidden_assumptions)
    
    common_assumptions = Counter(all_assumptions).most_common(5)
    
    print("\nMost common hidden assumptions:")
    for assumption, count in common_assumptions:
        print(f"   • {assumption}")
        print(f"     (appears in {count} solution(s))")
    
    return results


def main():
    """Main entry point"""
    if len(sys.argv) > 1:
        if sys.argv[1] == '--interactive' or sys.argv[1] == '-i':
            interactive_mode()
        elif sys.argv[1] == '--help' or sys.argv[1] == '-h':
            print("""
Unsolution Manifold Explorer - Usage:

  python unsolution_explorer_interactive.py              # Run examples
  python unsolution_explorer_interactive.py -i           # Interactive mode
  python unsolution_explorer_interactive.py "solution"   # Analyze one solution
  python unsolution_explorer_interactive.py -h           # Show this help

Examples:
  python unsolution_explorer_interactive.py -i
  python unsolution_explorer_interactive.py "Consciousness is integrated information"
            """)
        else:
            # Analyze provided solution
            explorer = AdvancedUnsolutionExplorer()
            solution = sys.argv[1]
            explorer.explore_deep(solution)
    else:
        # Run examples in batch
        solutions = [
            "Consciousness is integrated information (Φ) generated by causal mechanisms.",
            "Life is autopoietic organization that maintains itself through metabolism.",
            "Intelligence emerges from recursive self-modeling and meta-cognition."
        ]
        batch_mode(solutions)


if __name__ == "__main__":
    main()