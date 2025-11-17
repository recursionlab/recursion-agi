---
nexus: nexus-ai-chat-importer
plugin_version: "1.3.0"
provider: claude
artifact_id: multi_ai_workflow
version_uuid: 81056b86-2634-4468-abae-032f5468a166
version_number: 1
command: create
conversation_id: 1e06ba53-1a25-4587-8759-e92de2239c2a
create_time: 2025-07-10T16:42:01.000Z
format: markdown
aliases: [Multi-AI Knowledge Organization Workflow, multi_ai_workflow_v1]
---

# Multi-AI Knowledge Organization Workflow (Version 1)

**Conversation:** [[Nexus/Conversations/claude/2025/07/Knowledge Speedrunning System Design|Knowledge Speedrunning System Design]]

## Content

# Multi-AI Knowledge Organization Workflow

## Overview
Use 4 free AI windows to collaboratively organize 1000 Obsidian files through structured handoffs.

## Batch Processing Strategy
- Process files in batches of 50-100 to avoid context limits
- Use standardized templates for consistent AI handoffs
- Aggregate results at the end

---

## WINDOW 1: DATA EXTRACTION & PREP

### Input Template
```
BATCH: [X] of [Y] 
FILES: [List 50-100 filenames]

TASK: Extract key information from these files
OUTPUT FORMAT:
FILE: filename.md
TOPICS: [3-5 main topics]
TYPE: [note/article/reference/project/other]
KEYWORDS: [important terms, proper nouns]
CONNECTIONS: [mentions of other files/topics]
---
```

### Sample Output Format
```
FILE: machine_learning_basics.md
TOPICS: artificial intelligence, neural networks, supervised learning
TYPE: reference
KEYWORDS: gradient descent, backpropagation, training data
CONNECTIONS: mentions deep_learning.md, references AI_ethics.md
---
```

---

## WINDOW 2: CATEGORIZATION SPECIALIST

### Input Template
```
EXTRACTED DATA FROM WINDOW 1:
[Paste all extracted file data]

TASK: Create folder structure and categorize files
FOCUS: Group similar content, create logical hierarchy
OUTPUT FORMAT:
FOLDER_STRUCTURE:
- Main_Category/
  - Subcategory/
    - filename1.md
    - filename2.md
    
RATIONALE: [Why this structure makes sense]
```

### Sample Output Format
```
FOLDER_STRUCTURE:
- Technology/
  - AI_ML/
    - machine_learning_basics.md
    - deep_learning.md
  - Programming/
    - python_tutorials.md
    
RATIONALE: Groups related technical content while maintaining clear hierarchy
```

---

## WINDOW 3: RELATIONSHIP MAPPER

### Input Template
```
EXTRACTED DATA FROM WINDOW 1:
[Same data as Window 2]

TASK: Identify connections and suggest linking
FOCUS: Find related files, missing connections, potential tags
OUTPUT FORMAT:
CONNECTIONS:
- file1.md → RELATED_TO → [file2.md, file3.md]
- file2.md → SHOULD_LINK_TO → [file4.md]

TAGS_SUGGESTED:
- #ai #machine-learning → [list of relevant files]
- #philosophy #ethics → [list of relevant files]

MISSING_CONNECTIONS:
- Files about X should reference Y
```

### Sample Output Format
```
CONNECTIONS:
- machine_learning_basics.md → RELATED_TO → [deep_learning.md, ai_ethics.md]
- ai_ethics.md → SHOULD_LINK_TO → [philosophy_of_mind.md]

TAGS_SUGGESTED:
- #ai #machine-learning → [machine_learning_basics.md, deep_learning.md]
- #ethics #philosophy → [ai_ethics.md, philosophy_of_mind.md]

MISSING_CONNECTIONS:
- AI technical files should reference ethical considerations
```

---

## WINDOW 4: QUALITY REVIEWER & SYNTHESIZER

### Input Template
```
CATEGORIZATION RESULTS (Window 2):
[Paste folder structure]

RELATIONSHIP MAPPING (Window 3):
[Paste connections and tags]

TASK: Review both approaches and create final recommendations
FOCUS: Resolve conflicts, optimize structure, ensure completeness
OUTPUT FORMAT:
FINAL_STRUCTURE:
[Optimized folder structure]

IMPLEMENTATION_PLAN:
1. [Step by step actions]
2. [...]

CONFLICTS_RESOLVED:
- Issue: [description]
- Solution: [resolution]
```

---

## AGGREGATION WORKFLOW

### After Processing All Batches:

1. **Collect All Results**
   - Gather folder structures from all Window 2 sessions
   - Collect connection maps from all Window 3 sessions
   - Review all Window 4 recommendations

2. **Master Synthesis Template**
```
BATCH_RESULTS_SUMMARY:
Batch 1: [50 files] → [main categories found]
Batch 2: [50 files] → [main categories found]
...

RECURRING_PATTERNS:
- Categories that appear in multiple batches
- Common connection types
- Frequent tags

FINAL_MASTER_STRUCTURE:
[Consolidated folder structure for all 1000 files]

IMPLEMENTATION_SCRIPT:
[Specific file moves and actions needed]
```

---

## HANDOFF CHECKLIST

### Before Starting Each Window:
- [ ] Clear, specific task definition
- [ ] Standardized input format
- [ ] Expected output format specified
- [ ] Batch number and context provided

### Between Windows:
- [ ] Copy exact output format
- [ ] Maintain consistent file references
- [ ] Include batch context
- [ ] Verify data integrity

### After Each Batch:
- [ ] Save results in consistent format
- [ ] Note any anomalies or edge cases
- [ ] Prepare input for next batch
- [ ] Track progress (X of Y batches complete)

---

## OPTIMIZATION TIPS

1. **Batch Size**: Start with 50 files, increase if context allows
2. **Consistency**: Use identical prompts across same-type windows
3. **Error Handling**: If context maxes out, split batch further
4. **Progress Tracking**: Number batches and track completion
5. **Quality Control**: Spot-check results before proceeding

---

## EMERGENCY PROCEDURES

### If Context Limit Hit:
1. Reduce batch size to 25 files
2. Simplify output format
3. Focus on essential information only

### If Results Don't Match:
1. Use Window 4 to resolve conflicts
2. Prioritize most frequent patterns
3. When in doubt, choose simpler structure

### If Process Breaks Down:
1. Save current progress
2. Restart with smaller batches
3. Focus on high-value files first