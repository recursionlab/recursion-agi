---
nexus: nexus-ai-chat-importer
plugin_version: "1.3.0"
provider: claude
artifact_id: operator-soup
version_uuid: 04451828-4920-44d9-b141-6115184ec673
version_number: 2
command: update
conversation_id: 263a2eb1-0da6-4fc9-b570-eb8f12cabd7d
create_time: 2025-07-05T13:50:24.000Z
format: jsx
aliases: [Untitled Artifact, operator-soup_v2]
---

# Untitled Artifact (Version 2)

**Conversation:** [[Nexus/Conversations/claude/2025/07/Want a soup of operators that.|💬 Want a soup of operators that...]]

## Content

```jsx
import React, { useState, useEffect, useCallback } from 'react';
import { Shuffle, Play, RotateCcw, Zap, Lightbulb, Copy } from 'lucide-react';

const OperatorSoup = () => {
  const [inputText, setInputText] = useState("The quick brown fox jumps over the lazy dog.");
  const [currentOperators, setCurrentOperators] = useState([]);
  const [transformedText, setTransformedText] = useState("");
  const [history, setHistory] = useState([]);
  const [isGenerating, setIsGenerating] = useState(false);

  // Base operators
  const operators = {
    'backwards': (text) => text.split('').reverse().join(''),
    'reverse': (text) => text.split(' ').reverse().join(' '),
    'inversion': (text) => text.split('').map(c => 
      c === c.toUpperCase() ? c.toLowerCase() : c.toUpperCase()
    ).join(''),
    'negation': (text) => text.replace(/\b(is|are|was|were|can|will|do|does|did)\b/gi, 
      match => `not-${match}`),
    'anti': (text) => text.replace(/\b(\w+)\b/g, '$1-anti'),
    'mirror': (text) => text + ' | ' + text.split('').reverse().join(''),
    'meta': (text) => `[${text}] about [${text}]`,
    'meta-missing': (text) => text.replace(/\b\w+\b/g, match => 
      Math.random() > 0.5 ? `absence-of-${match}` : match),
    'meta-differentiation': (text) => text.replace(/\b(\w+)\b/g, 
      '$1-differentiating-from-non-$1'),
    'counter': (text) => text.replace(/\b(\w+)\b/g, 'counter-$1'),
    'recontextualizing': (text) => `In the context of ${text.split(' ')[0]}: ${text}`,
    'undoing': (text) => text.replace(/\b(\w+)\b/g, 'un-$1'),
    'undoing-undoing': (text) => text.replace(/\bun-(\w+)\b/g, '$1').replace(/\b(\w+)\b/g, 'un-un-$1'),
    
    // New operators
    'adding': (text) => text.replace(/\b(\w+)\b/g, 'adding-$1'),
    'adding-adding': (text) => text.replace(/\b(\w+)\b/g, 'adding-adding-$1'),
    'the-add': (text) => text.replace(/\b(\w+)\b/g, 'the-add-$1'),
    'recursive-add': (text) => text.replace(/\b(\w+)\b/g, match => 
      `${match}-add-${match}-add-${match}`),
    'multiplying': (text) => text.replace(/\b(\w+)\b/g, match => 
      `${match} ${match} ${match}`),
    'fragmenting': (text) => text.replace(/\b(\w+)\b/g, match => 
      match.split('').join('-')),
    'amplifying': (text) => text.replace(/\b(\w+)\b/g, match => 
      match.toUpperCase() + '!'),
    'diminishing': (text) => text.replace(/\b(\w+)\b/g, match => 
      match.length > 3 ? match.slice(0, 3) + '...' : match),
    'quantum': (text) => text.replace(/\b(\w+)\b/g, match => 
      Math.random() > 0.5 ? `${match}|not-${match}` : match),
    'temporal': (text) => text.replace(/\b(\w+)\b/g, match => 
      `past-${match}-present-${match}-future-${match}`),
    'nesting': (text) => text.replace(/\b(\w+)\b/g, match => 
      `${match}[${match}[${match}]]`),
    'unwrapping': (text) => text.replace(/\[([^\]]+)\]/g, '$1'),
    'doubling': (text) => text.replace(/\b(\w+)\b/g, '$1-$1'),
    'halving': (text) => text.replace(/\b(\w+)\b/g, match => 
      match.slice(0, Math.ceil(match.length / 2))),
    'scrambling': (text) => text.replace(/\b(\w+)\b/g, match => 
      match.split('').sort(() => Math.random() - 0.5).join('')),
    'layering': (text) => text.replace(/\b(\w+)\b/g, match => 
      `layer1[${match}]layer2[${match}]layer3[${match}]`),
    'echo': (text) => text.replace(/\b(\w+)\b/g, match => 
      `${match}...${match}...${match}...`),
    'compressing': (text) => text.replace(/\s+/g, '').replace(/\b(\w+)\b/g, match => 
      match.slice(0, 1) + match.slice(-1)),
    'expanding': (text) => text.replace(/\b(\w+)\b/g, match => 
      match.split('').join(' ')),
    'rotating': (text) => text.replace(/\b(\w+)\b/g, match => 
      match.slice(1) + match.slice(0, 1)),
    'folding': (text) => text.replace(/\b(\w+)\b/g, match => {
      const mid = Math.floor(match.length / 2);
      return match.slice(0, mid) + '|' + match.slice(mid);
    }),
    'paradox': (text) => text.replace(/\b(\w+)\b/g, match => 
      `${match}-that-is-not-${match}`),
    'infinite': (text) => text.replace(/\b(\w+)\b/g, match => 
      `${match}-∞-${match}-∞-${match}`),
    'dimensional': (text) => text.replace(/\b(\w+)\b/g, match => 
      `${match}[x]${match}[y]${match}[z]`),
    'crystallizing': (text) => text.replace(/\b(\w+)\b/g, match => 
      `◊${match}◊`),
    'dissolving': (text) => text.replace(/\b(\w+)\b/g, match => 
      match.split('').join('~')),
    'gravitating': (text) => text.replace(/\b(\w+)\b/g, match => 
      `((${match}))`),
    'repelling': (text) => text.replace(/\b(\w+)\b/g, match => 
      `<<${match}>>`),
    'oscillating': (text) => text.replace(/\b(\w+)\b/g, match => 
      `${match}↔${match.split('').reverse().join('')}`),
    'spiraling': (text) => text.replace(/\b(\w+)\b/g, match => 
      `${match}🌀${match}🌀${match}`),
    'phase-shifting': (text) => text.replace(/\b(\w+)\b/g, match => 
      `${match}→${match.replace(/[aeiou]/g, '*')}→${match}`),
    'entangling': (text) => text.replace(/\b(\w+)\b/g, match => 
      `${match}⟷${match.split('').reverse().join('')}`),
    'superposition': (text) => text.replace(/\b(\w+)\b/g, match => 
      `⟨${match}|${match.split('').reverse().join('')}⟩`),
    'void': (text) => text.replace(/\b(\w+)\b/g, '[ ]'),
    'overflow': (text) => text.replace(/\b(\w+)\b/g, match => 
      match + match + match + '...')
  };

  // Transform text through operator chain
  const applyOperators = useCallback((text, operatorChain) => {
    return operatorChain.reduce((result, op) => {
      if (operators[op]) {
        return operators[op](result);
      }
      return result;
    }, text);
  }, []);

  // Generate random operator combination
  const generateRandomCombination = () => {
    const opNames = Object.keys(operators);
    const count = Math.floor(Math.random() * 4) + 1; // 1-4 operators
    const combination = [];
    
    for (let i = 0; i < count; i++) {
      const randomOp = opNames[Math.floor(Math.random() * opNames.length)];
      combination.push(randomOp);
    }
    
    return combination;
  };

  // Apply transformation
  const transform = () => {
    const result = applyOperators(inputText, currentOperators);
    setTransformedText(result);
    
    // Add to history
    const newEntry = {
      operators: [...currentOperators],
      input: inputText,
      output: result,
      timestamp: new Date().toLocaleTimeString()
    };
    setHistory(prev => [newEntry, ...prev.slice(0, 9)]); // Keep last 10
  };

  // Generate and apply random combination
  const randomTransform = () => {
    setIsGenerating(true);
    setTimeout(() => {
      const randomOps = generateRandomCombination();
      setCurrentOperators(randomOps);
      const result = applyOperators(inputText, randomOps);
      setTransformedText(result);
      
      const newEntry = {
        operators: [...randomOps],
        input: inputText,
        output: result,
        timestamp: new Date().toLocaleTimeString()
      };
      setHistory(prev => [newEntry, ...prev.slice(0, 9)]);
      setIsGenerating(false);
    }, 200);
  };

  // Add operator to current chain
  const addOperator = (op) => {
    setCurrentOperators(prev => [...prev, op]);
  };

  // Remove operator from chain
  const removeOperator = (index) => {
    setCurrentOperators(prev => prev.filter((_, i) => i !== index));
  };

  // Clear all operators
  const clearOperators = () => {
    setCurrentOperators([]);
    setTransformedText("");
  };

  // Load combination from history
  const loadFromHistory = (entry) => {
    setCurrentOperators(entry.operators);
    setInputText(entry.input);
    setTransformedText(entry.output);
  };

  // Copy to clipboard
  const copyToClipboard = (text) => {
    navigator.clipboard.writeText(text);
  };

  // Auto-transform when operators change
  useEffect(() => {
    if (currentOperators.length > 0) {
      transform();
    }
  }, [currentOperators, inputText]);

  return (
    <div className="max-w-6xl mx-auto p-6 bg-gradient-to-br from-purple-50 to-blue-50 min-h-screen">
      <div className="text-center mb-8">
        <h1 className="text-4xl font-bold text-gray-800 mb-2">🧪 Operator Soup</h1>
        <p className="text-gray-600">Mix and match transformation operators to discover emergent text behaviors</p>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        {/* Input Section */}
        <div className="space-y-4">
          <div className="bg-white rounded-xl shadow-lg p-6">
            <h3 className="text-lg font-semibold text-gray-800 mb-3">Input Text</h3>
            <textarea
              value={inputText}
              onChange={(e) => setInputText(e.target.value)}
              className="w-full h-24 p-3 border-2 border-gray-200 rounded-lg focus:border-purple-400 focus:outline-none"
              placeholder="Enter text to transform..."
            />
          </div>

          {/* Operator Library */}
          <div className="bg-white rounded-xl shadow-lg p-6">
            <h3 className="text-lg font-semibold text-gray-800 mb-3">Operator Library</h3>
            <div className="grid grid-cols-2 gap-2">
              {Object.keys(operators).map((op) => (
                <button
                  key={op}
                  onClick={() => addOperator(op)}
                  className="p-2 text-sm bg-gradient-to-r from-purple-100 to-blue-100 hover:from-purple-200 hover:to-blue-200 rounded-lg transition-all transform hover:scale-105"
                >
                  {op}
                </button>
              ))}
            </div>
          </div>

          {/* Random Generation */}
          <div className="bg-white rounded-xl shadow-lg p-6">
            <h3 className="text-lg font-semibold text-gray-800 mb-3">Random Discovery</h3>
            <div className="flex gap-3">
              <button
                onClick={randomTransform}
                disabled={isGenerating}
                className="flex-1 flex items-center justify-center gap-2 p-3 bg-gradient-to-r from-orange-400 to-red-400 text-white rounded-lg hover:from-orange-500 hover:to-red-500 disabled:opacity-50 transition-all"
              >
                {isGenerating ? (
                  <div className="animate-spin rounded-full h-5 w-5 border-b-2 border-white" />
                ) : (
                  <Shuffle className="w-5 h-5" />
                )}
                Random Mix
              </button>
              <button
                onClick={clearOperators}
                className="flex items-center gap-2 p-3 bg-gray-400 text-white rounded-lg hover:bg-gray-500 transition-all"
              >
                <RotateCcw className="w-5 h-5" />
                Clear
              </button>
            </div>
          </div>
        </div>

        {/* Output Section */}
        <div className="space-y-4">
          {/* Current Operator Chain */}
          <div className="bg-white rounded-xl shadow-lg p-6">
            <h3 className="text-lg font-semibold text-gray-800 mb-3">Current Operator Chain</h3>
            <div className="flex flex-wrap gap-2 mb-4">
              {currentOperators.map((op, index) => (
                <span
                  key={index}
                  onClick={() => removeOperator(index)}
                  className="px-3 py-1 bg-gradient-to-r from-purple-400 to-blue-400 text-white rounded-full cursor-pointer hover:from-purple-500 hover:to-blue-500 transition-all"
                >
                  {op} ×
                </span>
              ))}
              {currentOperators.length === 0 && (
                <span className="text-gray-400 italic">No operators selected</span>
              )}
            </div>
            <div className="text-sm text-gray-600">
              Chain: {currentOperators.join(' → ') || 'None'}
            </div>
          </div>

          {/* Transformed Output */}
          <div className="bg-white rounded-xl shadow-lg p-6">
            <div className="flex items-center justify-between mb-3">
              <h3 className="text-lg font-semibold text-gray-800">Transformed Output</h3>
              {transformedText && (
                <button
                  onClick={() => copyToClipboard(transformedText)}
                  className="flex items-center gap-1 text-sm text-gray-600 hover:text-purple-600 transition-colors"
                >
                  <Copy className="w-4 h-4" />
                  Copy
                </button>
              )}
            </div>
            <div className="p-4 bg-gradient-to-r from-purple-50 to-blue-50 rounded-lg min-h-[100px] border-2 border-purple-200">
              <p className="text-gray-800 font-mono text-sm">
                {transformedText || "Apply operators to see transformation..."}
              </p>
            </div>
          </div>

          {/* History */}
          <div className="bg-white rounded-xl shadow-lg p-6">
            <h3 className="text-lg font-semibold text-gray-800 mb-3">
              <Lightbulb className="inline w-5 h-5 mr-2" />
              Discovery History
            </h3>
            <div className="space-y-2 max-h-64 overflow-y-auto">
              {history.map((entry, index) => (
                <div
                  key={index}
                  onClick={() => loadFromHistory(entry)}
                  className="p-3 bg-gray-50 rounded-lg cursor-pointer hover:bg-gray-100 transition-colors"
                >
                  <div className="text-xs text-gray-500 mb-1">
                    {entry.timestamp} - {entry.operators.join(' → ')}
                  </div>
                  <div className="text-sm text-gray-700 truncate">
                    {entry.output}
                  </div>
                </div>
              ))}
              {history.length === 0 && (
                <div className="text-gray-400 italic text-sm">
                  No transformations yet. Try mixing some operators!
                </div>
              )}
            </div>
          </div>
        </div>
      </div>

      {/* Examples */}
      <div className="mt-8 bg-white rounded-xl shadow-lg p-6">
        <h3 className="text-lg font-semibold text-gray-800 mb-3">
          <Zap className="inline w-5 h-5 mr-2" />
          Suggested Combinations
        </h3>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          {[
            ['counter', 'negation'],
            ['meta', 'mirror', 'inversion'],
            ['anti', 'undoing', 'backwards'],
            ['recontextualizing', 'counter', 'meta-missing'],
            ['backwards', 'meta-differentiation'],
            ['counter', 'recontextualizing', 'mirror'],
            ['anti', 'meta-missing'],
            ['meta', 'undoing', 'inversion']
          ].map((combo, index) => (
            <button
              key={index}
              onClick={() => setCurrentOperators(combo)}
              className="p-3 text-left bg-gradient-to-r from-gray-100 to-gray-200 hover:from-purple-100 hover:to-blue-100 rounded-lg transition-all"
            >
              <div className="font-semibold text-sm text-gray-800">
                {combo.join(' → ')}
              </div>
            </button>
          ))}
        </div>
      </div>
    </div>
  );
};

export default OperatorSoup;
```