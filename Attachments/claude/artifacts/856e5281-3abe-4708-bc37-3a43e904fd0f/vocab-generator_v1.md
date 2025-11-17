---
nexus: nexus-ai-chat-importer
plugin_version: "1.3.0"
provider: claude
artifact_id: vocab-generator
version_uuid: 9d72868b-e2b4-4fcb-880e-d3a826059b82
version_number: 1
command: create
conversation_id: 856e5281-3abe-4708-bc37-3a43e904fd0f
create_time: 2025-07-25T03:23:35.000Z
format: jsx
aliases: [Experimental Prompt Vocabulary Generator, vocab-generator_v1]
---

# Experimental Prompt Vocabulary Generator (Version 1)

**Conversation:** [[Nexus/Conversations/claude/2025/07/Meta-Recursive Prompt Engineering|Meta-Recursive Prompt Engineering]]

## Content

```jsx
import React, { useState, useCallback } from 'react';
import { RefreshCw, Copy, Zap, Brain, Atom, Eye } from 'lucide-react';

const VocabularyGenerator = () => {
  const [generatedVocab, setGeneratedVocab] = useState({});
  const [selectedCategories, setSelectedCategories] = useState(['operations', 'concepts', 'modifiers']);

  // Core vocabulary banks
  const vocabularyBanks = {
    operations: {
      name: "Operations & Processes",
      icon: <Zap className="w-4 h-4" />,
      items: [
        "inversing", "meta-analyzing", "corecursing", "differentiating", "integrating",
        "deconstructing", "anti-constructing", "reverse-engineering", "phase-transitioning",
        "crystallizing", "liquefying", "propagating", "resonating", "interfering",
        "superposing", "entangling", "collapsing", "bifurcating", "converging",
        "mapping", "unmapping", "folding", "unfolding", "recursing", "iterating",
        "transforming", "inverting", "reflecting", "refracting", "amplifying",
        "attenuating", "modulating", "demodulating", "encoding", "decoding",
        "compressing", "expanding", "rotating", "translating", "scaling"
      ]
    },
    concepts: {
      name: "Abstract Concepts",
      icon: <Brain className="w-4 h-4" />,
      items: [
        "meta-pattern", "co-emergence", "anti-structure", "pseudo-logic", "hyper-context",
        "proto-meaning", "quasi-understanding", "neo-awareness", "ultra-coherence",
        "inter-dimensionality", "trans-temporality", "omni-directionality", "multi-layered-ness",
        "self-reference", "other-reference", "cross-reference", "deep-structure",
        "surface-tension", "semantic-gravity", "conceptual-momentum", "cognitive-inertia",
        "thought-crystallization", "idea-liquefaction", "mental-phase-space",
        "consciousness-topology", "awareness-geometry", "understanding-dynamics",
        "knowledge-thermodynamics", "wisdom-mechanics", "insight-kinetics",
        "perception-field", "cognition-wave", "reflection-matrix", "abstraction-layer"
      ]
    },
    modifiers: {
      name: "Intensifiers & Qualifiers",
      icon: <Atom className="w-4 h-4" />,
      items: [
        "meta-", "anti-", "co-", "contra-", "pseudo-", "quasi-", "neo-", "proto-",
        "hyper-", "ultra-", "mega-", "multi-", "poly-", "omni-", "trans-", "inter-",
        "intra-", "extra-", "super-", "sub-", "pre-", "post-", "non-", "semi-",
        "auto-", "self-", "cross-", "counter-", "reverse-", "inverse-", "over-",
        "under-", "re-", "de-", "un-", "anti-anti-", "meta-meta-", "co-contra-",
        "-ive", "-istic", "-ional", "-esque", "-ward", "-wise", "-like", "-oid"
      ]
    },
    contexts: {
      name: "Context Domains",
      icon: <Eye className="w-4 h-4" />,
      items: [
        "conversation-space", "universe-context", "reality-framework", "meaning-topology",
        "semantic-field", "cognitive-landscape", "conceptual-terrain", "mental-geography",
        "thought-ecosystem", "idea-biosphere", "knowledge-environment", "wisdom-climate",
        "understanding-atmosphere", "awareness-stratosphere", "consciousness-cosmos",
        "perception-dimension", "cognition-plane", "reflection-realm", "abstraction-zone",
        "interpretation-domain", "analysis-sphere", "synthesis-region", "emergence-field",
        "complexity-space", "simplicity-void", "clarity-medium", "confusion-matrix",
        "order-lattice", "chaos-cloud", "pattern-web", "structure-architecture",
        "function-mechanism", "process-pathway", "system-network", "meta-system"
      ]
    },
    connectors: {
      name: "Logical Connectors",
      icon: <RefreshCw className="w-4 h-4" />,
      items: [
        "where", "whereby", "wherein", "whereas", "whilst", "during which",
        "such that", "in that", "given that", "provided that", "assuming that",
        "through which", "by means of", "via the mechanism of", "as mediated by",
        "resulting in", "leading to", "culminating in", "manifesting as",
        "becoming", "transforming into", "evolving toward", "converging on",
        "applied to", "mapped onto", "projected into", "reflected through",
        "filtered by", "modulated via", "amplified through", "attenuated by",
        "interfacing with", "intersecting at", "parallel to", "orthogonal to",
        "in opposition to", "in harmony with", "in resonance with", "in tension with"
      ]
    }
  };

  const generateVocab = useCallback(() => {
    const result = {};
    selectedCategories.forEach(category => {
      if (vocabularyBanks[category]) {
        const items = vocabularyBanks[category].items;
        const randomItem = items[Math.floor(Math.random() * items.length)];
        result[category] = randomItem;
      }
    });
    setGeneratedVocab(result);
  }, [selectedCategories]);

  const generateMultiple = (category, count = 3) => {
    const items = vocabularyBanks[category].items;
    const selected = [];
    const used = new Set();
    
    while (selected.length < count && selected.length < items.length) {
      const randomItem = items[Math.floor(Math.random() * items.length)];
      if (!used.has(randomItem)) {
        selected.push(randomItem);
        used.add(randomItem);
      }
    }
    return selected;
  };

  const copyToClipboard = (text) => {
    navigator.clipboard.writeText(text);
  };

  const toggleCategory = (category) => {
    setSelectedCategories(prev => 
      prev.includes(category) 
        ? prev.filter(c => c !== category)
        : [...prev, category]
    );
  };

  return (
    <div className="max-w-6xl mx-auto p-6 bg-gradient-to-br from-slate-900 via-purple-900 to-slate-900 min-h-screen text-white">
      <div className="mb-8 text-center">
        <h1 className="text-4xl font-bold mb-4 bg-gradient-to-r from-cyan-400 to-purple-400 bg-clip-text text-transparent">
          Experimental Prompt Vocabulary Generator
        </h1>
        <p className="text-slate-300 text-lg">
          Generate semantic building blocks for mind-bending prompts
        </p>
      </div>

      {/* Category Selection */}
      <div className="mb-8">
        <h2 className="text-2xl font-semibold mb-4 text-cyan-300">Select Vocabulary Categories</h2>
        <div className="grid grid-cols-2 md:grid-cols-3 gap-4">
          {Object.entries(vocabularyBanks).map(([key, bank]) => (
            <button
              key={key}
              onClick={() => toggleCategory(key)}
              className={`p-4 rounded-lg border-2 transition-all duration-300 flex items-center gap-3 ${
                selectedCategories.includes(key)
                  ? 'border-cyan-400 bg-cyan-400/20 text-cyan-300'
                  : 'border-slate-600 bg-slate-800/50 text-slate-400 hover:border-slate-500'
              }`}
            >
              {bank.icon}
              <span className="font-medium">{bank.name}</span>
            </button>
          ))}
        </div>
      </div>

      {/* Quick Generate */}
      <div className="mb-8 text-center">
        <button
          onClick={generateVocab}
          className="px-8 py-4 bg-gradient-to-r from-purple-600 to-cyan-600 rounded-lg font-semibold text-lg hover:from-purple-700 hover:to-cyan-700 transition-all duration-300 flex items-center gap-3 mx-auto"
        >
          <RefreshCw className="w-5 h-5" />
          Generate Vocabulary Set
        </button>
      </div>

      {/* Generated Results */}
      {Object.keys(generatedVocab).length > 0 && (
        <div className="mb-8 p-6 bg-slate-800/50 rounded-lg border border-slate-700">
          <h3 className="text-xl font-semibold mb-4 text-cyan-300">Generated Vocabulary</h3>
          <div className="grid gap-4">
            {Object.entries(generatedVocab).map(([category, word]) => (
              <div key={category} className="flex items-center justify-between p-3 bg-slate-700/50 rounded">
                <div className="flex items-center gap-3">
                  {vocabularyBanks[category]?.icon}
                  <span className="font-medium text-purple-300">{vocabularyBanks[category]?.name}:</span>
                  <span className="text-cyan-300 font-mono text-lg">{word}</span>
                </div>
                <button
                  onClick={() => copyToClipboard(word)}
                  className="p-2 hover:bg-slate-600 rounded transition-colors"
                >
                  <Copy className="w-4 h-4" />
                </button>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* Category Browsers */}
      <div className="grid gap-8">
        {Object.entries(vocabularyBanks).map(([key, bank]) => (
          <div key={key} className="bg-slate-800/30 rounded-lg p-6 border border-slate-700">
            <div className="flex items-center gap-3 mb-4">
              {bank.icon}
              <h3 className="text-xl font-semibold text-cyan-300">{bank.name}</h3>
              <button
                onClick={() => {
                  const multiple = generateMultiple(key, 5);
                  copyToClipboard(multiple.join(', '));
                }}
                className="ml-auto px-3 py-1 bg-purple-600 hover:bg-purple-700 rounded text-sm transition-colors"
              >
                Copy Random 5
              </button>
            </div>
            <div className="flex flex-wrap gap-2">
              {bank.items.map((item, index) => (
                <button
                  key={index}
                  onClick={() => copyToClipboard(item)}
                  className="px-3 py-1 bg-slate-700 hover:bg-slate-600 rounded-full text-sm transition-all duration-200 hover:scale-105 font-mono"
                >
                  {item}
                </button>
              ))}
            </div>
          </div>
        ))}
      </div>

      {/* Usage Instructions */}
      <div className="mt-8 p-6 bg-gradient-to-r from-purple-900/30 to-cyan-900/30 rounded-lg border border-purple-500/30">
        <h3 className="text-xl font-semibold mb-4 text-purple-300">Usage Instructions</h3>
        <div className="text-slate-300 space-y-2">
          <p><strong>Basic Formula:</strong> [Operation] the [Concept] [Connector] the [Modified Context] [Operation] the [Concept]</p>
          <p><strong>Example:</strong> "Meta-analyzing the proto-meaning whereby the consciousness-topology inversing the self-reference"</p>
          <p><strong>Advanced:</strong> Chain multiple operations: "Co-recursively differentiating the hyper-context through which the anti-structure becomes the meta-pattern of observed observation"</p>
        </div>
      </div>
    </div>
  );
};

export default VocabularyGenerator;
```