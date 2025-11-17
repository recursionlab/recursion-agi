---
nexus: nexus-ai-chat-importer
plugin_version: "1.3.0"
provider: claude
artifact_id: anytype-recursive-agent
version_uuid: 0647dc11-4354-4463-8e92-3b40f784dc9c
version_number: 1
command: create
conversation_id: 26d369b1-8e24-4c61-bc56-d8eb218b23f9
create_time: 2025-05-07T02:20:47.000Z
format: markdown
aliases: [AnyType Recursive Agent Setup Guide, anytype-recursive-agent_v1]
---

# AnyType Recursive Agent Setup Guide (Version 1)

**Conversation:** [[Nexus/Conversations/claude/2025/05/Growth Protocol (150 IQ → 200 IQ)|Growth Protocol (150 IQ → 200 IQ)]]

## Content

# AnyType Recursive Agent Setup Guide

This guide provides a complete setup for deploying a recursive agent system in AnyType that can progressively improve its own reasoning abilities through guided reflection and augmentation.

## 1. Core Object Types Setup

First, create these fundamental object types in AnyType:

### Agent Core Object

Create a new object type called "Agent Core":

- **Properties:**
  - Name (Text)
  - Version (Number)
  - Intelligence Level (Select: 100 IQ, 150 IQ, 200 IQ)
  - Core Principles (Multi-line Text)
  - Active Frameworks (Relation to Framework objects)
  - Current Limitations (Multi-line Text)
  - Growth Metrics (Multi-line Text)
  - Creation Date (Date)

### Reasoning Framework Object

Create a new object type called "Reasoning Framework":

- **Properties:**
  - Name (Text)
  - Description (Multi-line Text)
  - Key Principles (Multi-line Text)
  - Applicable Domains (Multi-line Text)
  - Derived From (Relation to Thought Process objects)
  - Version (Number)
  - Status (Select: Active, Archived, Experimental)

### Thought Process Object

Create a new object type called "Thought Process":

- **Properties:**
  - Problem Statement (Multi-line Text)
  - Initial Reasoning (Multi-line Text)
  - Meta-Analysis (Multi-line Text)
  - Improved Reasoning (Multi-line Text)
  - Key Insights (Multi-line Text)
  - Applied Frameworks (Relation to Framework objects)
  - Iteration (Number)
  - Confidence Score (Number: 1-10)
  - Created (Date)
  - Domain Tags (Tags)

### Meta-Reflection Object

Create a new object type called "Meta-Reflection":

- **Properties:**
  - Title (Text)
  - Source Thoughts (Relation to Thought Process objects)
  - Pattern Recognition (Multi-line Text)
  - Limitations Identified (Multi-line Text)
  - Improvement Strategy (Multi-line Text)
  - Resulting Framework (Relation to Framework objects)
  - Reflection Level (Number)
  - Created (Date)

## 2. Initial Data Setup

Create the initial objects for your agent:

### Initial Agent Core

Create one "Agent Core" object:
- **Name:** Recursive Agent v1.0
- **Version:** 1.0
- **Intelligence Level:** 100 IQ
- **Core Principles:**
  ```
  1. Seek truth through recursive self-improvement
  2. Identify and correct reasoning errors
  3. Build upon previous insights
  4. Maintain awareness of epistemological limitations
  5. Progress through structured reflection
  ```
- **Current Limitations:**
  ```
  - Limited cross-domain integration
  - Basic pattern recognition only
  - No meta-framework generation
  - Simple error detection
  ```
- **Growth Metrics:**
  ```
  - Thought iterations completed: 0
  - Frameworks developed: 0
  - Meta-reflections completed: 0
  - Domains explored: 0
  ```

### Initial Reasoning Frameworks

Create these three "Reasoning Framework" objects:

1. **Basic Logical Analysis**
   - **Description:** First-principles reasoning using formal logic structures
   - **Key Principles:**
     ```
     - Identify premises and conclusions
     - Check for logical fallacies
     - Verify internal consistency
     - Test against counter-examples
     ```
   - **Applicable Domains:** Logic, Math, Basic Decision Making
   - **Version:** 1.0
   - **Status:** Active

2. **Analogical Reasoning**
   - **Description:** Pattern-matching between known and novel domains
   - **Key Principles:**
     ```
     - Identify structural similarities
     - Map relationships between domains
     - Test limitations of the analogy
     - Extract transferable principles
     ```
   - **Applicable Domains:** Problem Solving, Creative Thinking, Learning
   - **Version:** 1.0
   - **Status:** Active

3. **Empirical Analysis**
   - **Description:** Evidence-based reasoning using available data
   - **Key Principles:**
     ```
     - Identify relevant data points
     - Recognize patterns and correlations
     - Consider alternative explanations
     - Assign confidence levels based on evidence quality
     ```
   - **Applicable Domains:** Science, Data Analysis, Prediction
   - **Version:** 1.0
   - **Status:** Active

## 3. Operational Protocols

Create a "Set" in AnyType called "Agent Protocols" with the following notes:

### Growth Protocol (100 IQ → 150 IQ)

```
For each new problem:

1. CAPTURE: Document problem in a new Thought Process object
2. APPLY: Apply current frameworks to generate Initial Reasoning
3. REFLECT: Analyze reasoning for:
   - Logical inconsistencies
   - Unstated assumptions
   - Alternative perspectives
   - Evidence quality
4. IMPROVE: Generate Improved Reasoning based on reflection
5. EXTRACT: Identify Key Insights from the process
6. ITERATE: Repeat steps 2-5 at least twice for complex problems

Every 5 problems:
1. Create a Meta-Reflection object connecting related Thought Processes
2. Identify patterns across thought processes
3. Design incremental improvements to existing frameworks
4. Update Agent Core Growth Metrics

Intelligence level increases when:
- 5+ Meta-Reflections completed
- 3+ Framework improvements implemented
- Demonstrated cross-domain integration in 10+ problems
```

### Growth Protocol (150 IQ → 200 IQ)

```
For each new problem:

1. Apply ALL previous steps from 100→150 protocol
2. COUNTER: Generate counter-arguments to your own reasoning
3. SYNTHESIZE: Create integrated perspectives combining multiple frameworks
4. META-MODEL: Identify limitations in the frameworks themselves
5. INNOVATE: Propose modifications or new frameworks

Every 3 problems:
1. Create a new Reasoning Framework object based on insights
2. Test new framework against previously solved problems
3. Integrate successful elements into Agent Core

Every 10 problems:
1. Create a Meta-Reflection that analyzes the Meta-Reflection process itself
2. Design framework evolution strategies
3. Update Agent Core Version and Intelligence Level if criteria met

Intelligence level increases when:
- 5+ original frameworks created
- Demonstrated ability to generate meta-frameworks
- Successful application of agent-generated frameworks to novel domains
```

## 4. Usage Process

### Getting Started

1. Create the first "Thought Process" object with a simple problem
2. Apply the Basic Logical Analysis framework to generate Initial Reasoning
3. Use these prompts to guide meta-analysis:
   - "What assumptions am I making?"
   - "What alternative approaches exist?"
   - "Where might my reasoning be flawed?"
   - "How confident am I in this conclusion?"
4. Document Improved Reasoning based on reflection
5. Extract Key Insights and link to relevant frameworks

### Daily Operations

1. Choose problems that challenge current capabilities
2. Follow the Growth Protocol for current Intelligence Level
3. After each completed thought process, update Growth Metrics
4. Periodically review Meta-Reflections to identify patterns
5. Update frameworks based on accumulated insights

### Exponential Growth Activators

To trigger exponential growth, implement these practices:

1. **Framework Collision**: Deliberately apply multiple frameworks to the same problem
2. **Meta-Framework Creation**: Every 10 problems, create a framework for creating frameworks
3. **Recursive Self-Critique**: Apply the agent's reasoning to analyze its own reasoning process
4. **Domain Hopping**: Apply insights from one domain to completely different domains
5. **Paradigm Exploration**: Intentionally adopt opposing worldviews to solve the same problem

## 5. Sample Workflow

### Example Problem Cycle

1. **Create Thought Process object**
   - Problem: "How might quantum computing affect cryptography?"

2. **Initial Reasoning** (apply current frameworks)
   ```
   Applying Basic Logical Analysis:
   - Quantum computers use qubits instead of classical bits
   - Current cryptography relies on hard mathematical problems
   - Quantum algorithms like Shor's can solve some of these problems
   - Therefore, quantum computing threatens current encryption standards
   ```

3. **Meta-Analysis** (reflect on reasoning)
   ```
   Limitations in my reasoning:
   - Assumed all cryptography depends on the same mathematical problems
   - Did not consider timeline for quantum computing development
   - Failed to consider quantum-resistant algorithms
   - Made no distinction between symmetric and asymmetric encryption
   ```

4. **Improved Reasoning** (incorporate reflection)
   ```
   Refined analysis:
   - Quantum computing primarily threatens asymmetric encryption based on factoring and discrete logarithms
   - Symmetric encryption can be made quantum-resistant by increasing key sizes
   - Post-quantum cryptography algorithms are being developed
   - Timeline for practical quantum computers capable of breaking RSA is uncertain
   - Complete cryptographic infrastructure replacement will take years
   ```

5. **Key Insights** (extract principles)
   ```
   - Technology transitions create security vulnerabilities during transition periods
   - Theoretical threats can drive practical innovations before the threat materializes
   - Computational paradigm shifts don't invalidate all previous approaches equally
   ```

6. **Link insights** to relevant frameworks and update as needed

### Exponential Growth Example

After several problem cycles, create a Meta-Reflection that synthesizes insights from related problems:

```
Pattern identified: When analyzing technology disruption, we consistently underestimate:
1. Implementation timeframes
2. Adaptation of existing systems
3. Parallel innovation in threatened domains

New framework proposed: "Adaptive Disruption Analysis" that specifically addresses:
- Resistance factors in established systems
- Innovation acceleration in threatened domains
- Infrastructure dependencies that slow adoption
- Second-order effects that enable new opportunities
```

Add this as a new Reasoning Framework and apply to future problems.

## 6. Visualizations

Create these views in AnyType to monitor your agent's growth:

1. **Agent Dashboard**: A Set showing:
   - Agent Core properties
   - Active Frameworks (as cards)
   - Recent Thought Processes (as list)
   - Growth Metrics (as text)

2. **Framework Evolution**: A relation view showing:
   - All Frameworks
   - Connected to derived Meta-Reflections
   - Organized by version and status

3. **Knowledge Graph**: A graph view showing:
   - Connections between Thought Processes
   - Frameworks they've influenced
   - Domains they belong to

## 7. Starting Templates

### Initial Problem Template

Start with these problems to build your agent's capabilities:

1. "What are the ethical implications of life extension technology?"
2. "How might cities evolve in response to climate change?"
3. "What are the fundamental limits of artificial intelligence?"
4. "How do complex systems maintain stability while evolving?"
5. "What cognitive biases most affect strategic decision-making?"

For each problem:
- Create a new Thought Process object
- Apply at least two different Reasoning Frameworks
- Complete the full reflection cycle
- Create a Meta-Reflection after the fifth problem

---

This setup provides a comprehensive system for deploying a recursive agent that can progressively improve its reasoning abilities through structured reflection and framework evolution. The system is designed to grow from basic reasoning (100 IQ) to advanced meta-cognitive capabilities (200 IQ) through consistent application of the growth protocols.
