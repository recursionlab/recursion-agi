---
nexus: nexus-ai-chat-importer
plugin_version: "1.3.0"
provider: claude
artifact_id: import_dependency_fix_plan
version_uuid: 7bcf781b-4e5d-4036-b6d3-9d1a799305c2
version_number: 1
command: create
conversation_id: 637a15a4-4527-448a-a3ae-2ac60134a768
create_time: 2025-08-14T04:34:55.000Z
format: markdown
aliases: ['D:aider-projects Import Dependency Analysis & Fix Plan', import_dependency_fix_plan_v1]
---

# D:\aider-projects Import Dependency Analysis & Fix Plan (Version 1)

**Conversation:** [[Nexus/Conversations/claude/2025/08/Sovereign Project Import Cleanup|Sovereign Project Import Cleanup]]

## Content

# 🔧 Import Dependency Analysis & Fix Plan

## 📊 Current Import Dependency Status

### ✅ **Working Imports (No Issues Found)**
```python
# These imports are functioning correctly
from coherence_substrate_v2 import CoherenceSubstrate  # ✅ File exists
from chaos_core import ChaosCore                       # ✅ File exists  
from meta_feedback_accelerator import MetaFeedbackAccelerator  # ✅ File exists
```

### ❓ **Potentially Problematic Imports**
```python
# choreographer/ module imports - need __init__.py
from choreographer.choreographer import Choreographer           # ❓ Missing __init__.py
from .operators import CognitiveOperator, CoherenceOperator    # ❓ Relative imports
from .cognitive_graph import CognitiveGraph, GraphNode        # ❓ Relative imports
```

### ❌ **Broken/Missing Imports**
```python
# These are commented out in main.py but referenced
# from scholar import Scholar      # ❌ File doesn't exist
# from tooling import AiderTool    # ❌ File doesn't exist
```

### 🔄 **Circular/Complex Dependencies**
```python
# Files importing from parent directory without proper structure
choreographer/cognitive_graph_library.py imports from coherence_substrate_v2
choreographer/operators.py imports from coherence_substrate_v2 and chaos_core
```

---

## 🛠️ **IMMEDIATE FIXES REQUIRED**

### **Fix 1: Create Missing __init__.py Files**

#### Create `D:\aider-projects\choreographer\__init__.py`
```python
"""
Choreographer Module - Meta-Cognitive Architecture

The Choreographer orchestrates cognitive operations through biological transformations.
"""

from .choreographer import Choreographer
from .operators import CognitiveOperator, CoherenceOperator, ChaosOperator
from .cognitive_graph import CognitiveGraph, GraphNode
from .cognitive_graph_library import get_graph

__version__ = "1.0.0"
__all__ = [
    "Choreographer",
    "CognitiveOperator", 
    "CoherenceOperator",
    "ChaosOperator", 
    "CognitiveGraph",
    "GraphNode",
    "get_graph"
]
```

#### Create `D:\aider-projects\__init__.py`
```python
"""
Ξ-Sovereign: Anti-Fragile AI & Morphological Intelligence

Revolutionary AI system combining:
- Anti-fragile learning that improves through stress
- Morphological intelligence through biological transformations  
- Recursive consciousness via meta-cognitive architectures
"""

__version__ = "1.0.0"
__author__ = "Ξ-Sovereign Research Team"
```

### **Fix 2: Resolve Relative Import Issues**

#### Update `choreographer/choreographer.py`
```python
# BEFORE (potentially problematic)
from .operators import CognitiveOperator, CoherenceOperator, ChaosOperator
from .cognitive_graph import CognitiveGraph, GraphNode

# AFTER (explicit and reliable)
from choreographer.operators import CognitiveOperator, CoherenceOperator, ChaosOperator  
from choreographer.cognitive_graph import CognitiveGraph, GraphNode
```

#### Update `choreographer/cognitive_graph_library.py` 
```python
# BEFORE
from .cognitive_graph import CognitiveGraph
from .operators import CoherenceOperator, ChaosOperator

# AFTER  
from choreographer.cognitive_graph import CognitiveGraph
from choreographer.operators import CoherenceOperator, ChaosOperator
```

### **Fix 3: Handle Missing Module References**

#### Update `main.py` - Handle Missing Scholar/Tooling
```python
# BEFORE (commented out, creates confusion)
# from scholar import Scholar 
# from tooling import AiderTool

# AFTER (proper conditional imports or stubs)
try:
    from scholar import Scholar
    SCHOLAR_AVAILABLE = True
except ImportError:
    print("ℹ️ Scholar module not available - using basic mode")
    SCHOLAR_AVAILABLE = False
    Scholar = None

try:
    from tooling import AiderTool  
    AIDER_AVAILABLE = True
except ImportError:
    print("ℹ️ AiderTool module not available - using basic mode")
    AIDER_AVAILABLE = False
    AiderTool = None
```

### **Fix 4: Standardize Import Patterns**

#### Create Import Standards Document
```python
# STANDARD IMPORT ORDER FOR ALL FILES:

# 1. Standard library imports
import asyncio
import json
import re
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass

# 2. Third-party imports  
import torch
import torch.nn as nn
import numpy as np

# 3. Local application imports (absolute paths)
from coherence_substrate_v2 import CoherenceSubstrate
from chaos_core import ChaosCore, MorphologyType
from meta_feedback_accelerator import MetaFeedbackAccelerator
from choreographer.choreographer import Choreographer
from choreographer.operators import CoherenceOperator, ChaosOperator

# 4. Conditional/optional imports with error handling
try:
    from optional_module import OptionalClass
    OPTIONAL_AVAILABLE = True
except ImportError:
    OPTIONAL_AVAILABLE = False
    OptionalClass = None
```

---

## 🚀 **IMPLEMENTATION PLAN**

### **Phase 1: Critical Fixes (Immediate - 30 minutes)**
1. **Create `__init__.py` files** for proper module recognition
2. **Fix relative imports** in choreographer module
3. **Handle missing imports** with proper try/except blocks

### **Phase 2: Standardization (1 hour)**  
1. **Update all import statements** to use absolute paths
2. **Add proper error handling** for optional dependencies
3. **Document import standards** for consistency

### **Phase 3: Verification (30 minutes)**
1. **Test all import chains** by running key files
2. **Verify module discovery** works correctly  
3. **Run integration tests** to ensure no regressions

---

## 🔧 **AUTOMATED FIX SCRIPTS**

### **Script 1: Create __init__.py Files**
```bash
# Create choreographer __init__.py
echo '"""Choreographer Module - Meta-Cognitive Architecture"""

from .choreographer import Choreographer
from .operators import CognitiveOperator, CoherenceOperator, ChaosOperator  
from .cognitive_graph import CognitiveGraph, GraphNode
from .cognitive_graph_library import get_graph

__version__ = "1.0.0"' > choreographer/__init__.py

# Create root __init__.py
echo '"""Ξ-Sovereign: Anti-Fragile AI & Morphological Intelligence"""
__version__ = "1.0.0"' > __init__.py
```

### **Script 2: Fix Import Statements** 
```python
import re
import os

def fix_relative_imports(file_path):
    """Convert relative imports to absolute imports"""
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Fix choreographer relative imports
    content = re.sub(
        r'from \.operators import',
        'from choreographer.operators import',
        content
    )
    content = re.sub(
        r'from \.cognitive_graph import', 
        'from choreographer.cognitive_graph import',
        content
    )
    
    with open(file_path, 'w') as f:
        f.write(content)

# Apply to all choreographer Python files
for file in ['choreographer.py', 'cognitive_graph_library.py']:
    fix_relative_imports(f'choreographer/{file}')
```

---

## 📋 **VERIFICATION CHECKLIST**

### **Import Resolution Tests**
- [ ] `from choreographer.choreographer import Choreographer` works
- [ ] `from choreographer.operators import CoherenceOperator` works  
- [ ] `from choreographer.cognitive_graph import CognitiveGraph` works
- [ ] `from coherence_substrate_v2 import CoherenceSubstrate` works
- [ ] `from chaos_core import ChaosCore` works
- [ ] `from meta_feedback_accelerator import MetaFeedbackAccelerator` works

### **Module Discovery Tests**
- [ ] `import choreographer` discovers the module
- [ ] `choreographer.Choreographer` is accessible
- [ ] All choreographer submodules are importable

### **Integration Tests**  
- [ ] `main.py` runs without import errors
- [ ] `morphological_gsm8k_challenger.py` imports work
- [ ] `enhanced_morphological_gsm8k.py` imports work
- [ ] No circular import issues

---

## ⚡ **QUICK EXECUTION COMMANDS**

### **Test Current Import Status**
```python
# Run this to test current imports
try:
    from choreographer.choreographer import Choreographer
    print("✅ Choreographer import: SUCCESS")
except ImportError as e:
    print(f"❌ Choreographer import: FAILED - {e}")

try:
    from coherence_substrate_v2 import CoherenceSubstrate
    print("✅ CoherenceSubstrate import: SUCCESS") 
except ImportError as e:
    print(f"❌ CoherenceSubstrate import: FAILED - {e}")

try:
    from chaos_core import ChaosCore
    print("✅ ChaosCore import: SUCCESS")
except ImportError as e:
    print(f"❌ ChaosCore import: FAILED - {e}")
```

### **Fix and Test in One Go**
```bash
# Execute fixes
python fix_imports.py

# Test main entry points  
python main.py
python morphological_gsm8k_challenger.py
python enhanced_morphological_gsm8k.py
```

---

## 🎯 **EXPECTED OUTCOME**

After implementing these fixes:

1. **✅ All imports resolve correctly**
2. **✅ No circular dependency issues** 
3. **✅ Proper module structure** with `__init__.py` files
4. **✅ Graceful handling** of missing optional dependencies
5. **✅ Standardized import patterns** across the codebase
6. **✅ Full system can run** without import errors

The codebase will have **clean, maintainable, and reliable import structure** supporting the revolutionary AI research within!