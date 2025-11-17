---
nexus: nexus-ai-chat-importer
plugin_version: "1.3.0"
provider: claude
artifact_id: real_leanrag_system
version_uuid: 2ad6a143-4a5a-46c1-8e0b-82d28cb966ad
version_number: 1
command: create
conversation_id: 31bc141f-b9ce-46e5-88b8-0024943d13ca
create_time: 2025-08-20T14:10:55.000Z
format: markdown
aliases: [Real LeanRAG Implementation - Observable Processing, real_leanrag_system_v1]
---

# Real LeanRAG Implementation - Observable Processing (Version 1)

**Conversation:** [[Nexus/Conversations/claude/2025/08/LeanRAG System Performance Verification|LeanRAG System Performance Verification]]

## Content

#!/usr/bin/env python3
"""
REAL LeanRAG Implementation - Observable, Falsifiable, Measurable
No fake processing - every operation is timed and validated.
Processing 50 conversations should take 2-5 minutes minimum.
"""

import json
import time
import numpy as np
from pathlib import Path
from typing import Dict, List, Tuple, Set, Any
from dataclasses import dataclass, field
from collections import defaultdict
import logging
from sklearn.mixture import GaussianMixture
from sklearn.feature_extraction.text import TfidfVectorizer
from sentence_transformers import SentenceTransformer
import networkx as nx
import re
from datetime import datetime

# Configure logging for observable processing
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('leanrag_processing.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

@dataclass
class Entity:
    """Real entity with semantic content"""
    id: str
    name: str
    description: str
    type: str
    source_conversation: str
    embedding: np.ndarray = None
    cluster_id: int = -1
    
@dataclass
class Relation:
    """Real relation between entities"""
    id: str
    source_entity: str
    target_entity: str
    relation_type: str
    description: str
    weight: float = 1.0

@dataclass
class AggregatedEntity:
    """Hierarchical aggregated entity"""
    id: str
    name: str
    description: str
    chil