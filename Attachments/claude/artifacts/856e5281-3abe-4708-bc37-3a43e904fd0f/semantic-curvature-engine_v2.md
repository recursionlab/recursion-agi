---
nexus: nexus-ai-chat-importer
plugin_version: "1.3.0"
provider: claude
artifact_id: semantic-curvature-engine
version_uuid: 5737564f-9042-4ac5-b75e-844c70c54414
version_number: 2
command: update
conversation_id: 856e5281-3abe-4708-bc37-3a43e904fd0f
create_time: 2025-07-25T03:46:15.000Z
format: jsx
aliases: [Untitled Artifact, semantic-curvature-engine_v2]
---

# Untitled Artifact (Version 2)

**Conversation:** [[Nexus/Conversations/claude/2025/07/Meta-Recursive Prompt Engineering|Meta-Recursive Prompt Engineering]]

## Content

```jsx
import React, { useState, useCallback, useEffect } from 'react';
import { Brain, Zap, Infinity, ArrowRight, RotateCcw, Square, Triangle } from 'lucide-react';

const SemanticCurvatureEngine = () => {
  const [currentExpression, setCurrentExpression] = useState("");
  const [curvatureValue, setCurvatureValue] = useState(0.5);
  const [recursionDepth, setRecursionDepth] = useState(3);
  const [operatorMode, setOperatorMode] = useState('forward');
  const [visualization, setVisualization] = useState([]);

  // Core semantic atoms - the building blocks of meaning-space
  const semanticAtoms = {
    base: ['thinking', 'meaning', 'being', 'knowing', 'understanding', 'awareness', 'existence', 'reality'],
    reflexive: ['self', 'other', 'meta', 'anti', 'non', 'co', 'through', 'between', 'within', 'beyond'],
    spatial: ['inside', 'outside', 'through', 'around', 'between', 'beneath', 'above', 'alongside'],
    temporal: ['before', 'after', 'during', 'backwards', 'forwards', 'simultaneous', 'retroactive'],
    operators: ['of', 'as', 'through', 'via', 'by', 'with', 'against', 'toward', 'from'],
    intensifiers: ['hyper', 'ultra', 'mega', 'proto', 'quasi', 'pseudo', 'neo', 'trans']
  };

  // Mathematical operations on semantic space
  const mathOperations = {
    square: (token) => `${token}-squared`,
    inverse: (token) => `inverse-${token}`,
    differential: (token) => `d${token}/dt`,
    integral: (token) => `∫${token}`,
    recursive: (token) => `${token}(${token})`,
    negation: (token) => `non-${token}`,
    doubleNegation: (token) => `non-non-${token}`,
    meta: (token) => `meta-${token}`,
    metaMeta: (token) => `meta-meta-${token}`,
    throughness: (token) => `${token}-throughness`,
    betweenness: (token) => `${token}-betweenness`,
    curvature: (token) => `curved-${token}`,
    topology: (token) => `${token}-topology`
  };

  // Generate semantic curvature based on self-reference density
  const calculateSemanticCurvature = useCallback((expression) => {
    const selfRefCount = (expression.match(/thinking|meta|self|non-non|through.*through/g) || []).length;
    const totalTokens = expression.split(/[\s-]/).length;
    const density = selfRefCount / Math.max(totalTokens, 1);
    return Math.min(density * 2, 1); // Normalize to 0-1
  }, []);

  // Apply mathematical operations to tokens
  const applyMathOperation = useCallback((token, operation) => {
    if (!mathOperations[operation]) return token;
    return mathOperations[operation](token);
  }, []);

  // Generate recursive self-reference chains with your patterns
  const generateRecursiveChain = useCallback((baseToken, depth) => {
    if (depth <= 0) return baseToken;
    
    const operations = ['meta', 'through', 'inverse', 'square'];
    const operation = operations[Math.floor(Math.random() * operations.length)];
    const transformed = applyMathOperation(baseToken, operation);
    
    // Add your specific patterns
    const spatialFolding = Math.random() > 0.7 ? 
      `${baseToken} of ${baseToken} and ${baseToken} ${baseToken}` : '';
    
    return `${transformed} ${spatialFolding} ${generateRecursiveChain(baseToken, depth - 1)}`;
  }, [applyMathOperation]);

  // Create novel compound words through semantic fusion
  const fuseSemanticTokens = useCallback((token1, token2, connector = 'of') => {
    const fusionTypes = [
      `${token1}-${token2}`,
      `${token1} ${connector} ${token2}`,
      `${token1}-as-${token2}`,
      `${token2}-through-${token1}`,
      `meta-${token1}-${token2}`,
      `${token1}-${token2}-throughness`
    ];
    return fusionTypes[Math.floor(Math.random() * fusionTypes.length)];
  }, []);

  // Generate curvature visualization
  const generateVisualization = useCallback((expression) => {
    const tokens = expression.split(/[\s-]+/).filter(t => t.length > 0);
    return tokens.map((token, index) => {
      const curvature = calculateSemanticCurvature(token);
      const recursionLevel = (token.match(/meta|non|through/g) || []).length;
      return {
        token,
        curvature,
        recursionLevel,
        position: index,
        intensity: Math.min(recursionLevel * 0.3, 1)
      };
    });
  }, [calculateSemanticCurvature]);

  // Main generation function
  const generateExpression = useCallback(() => {
    const baseAtom = semanticAtoms.base[Math.floor(Math.random() * semanticAtoms.base.length)];
    const reflexive = semanticAtoms.reflexive[Math.floor(Math.random() * semanticAtoms.reflexive.length)];
    const spatial1 = semanticAtoms.spatial[Math.floor(Math.random() * semanticAtoms.spatial.length)];
    const spatial2 = semanticAtoms.spatial[Math.floor(Math.random() * semanticAtoms.spatial.length)];
    const operator = semanticAtoms.operators[Math.floor(Math.random() * semanticAtoms.operators.length)];
    
    // Create base semantic construct
    let construct = fuseSemanticTokens(reflexive, baseAtom);
    
    // Apply mathematical operations based on curvature
    if (curvatureValue > 0.3) {
      construct = applyMathOperation(construct, 'square');
    }
    if (curvatureValue > 0.6) {
      construct = applyMathOperation(construct, 'metaMeta');
    }
    
    // Add spatial recursion
    const spatialConstruct = `${spatial1} ${spatial2} and ${spatial2} ${spatial1}`;
    
    // Create temporal recursion
    const temporalPart = operatorMode === 'backwards' ? 
      'backwards backwards and retrobackcasting forwards through itself' :
      'forwards through backwards while retroactively being forwards';
    
    // Generate recursive chain
    const recursiveChain = generateRecursiveChain(baseAtom, recursionDepth);
    
    // Combine everything with mathematical operators
    const expression = `${construct} ${operator} ${spatialConstruct} but also ${recursiveChain} ${temporalPart} but also applying the ${operatorMode === 'square' ? 'square' : 'differential'} function to all the operators while ${construct}-throughness meta-${baseAtom}s the ${reflexive}-${reflexive}-${baseAtom}`;
    
    setCurrentExpression(expression);
    
    // Calculate and update curvature
    const newCurvature = calculateSemanticCurvature(expression);
    setCurvatureValue(newCurvature);
    
    // Generate visualization
    const viz = generateVisualization(expression);
    setVisualization(viz);
  }, [curvatureValue, recursionDepth, operatorMode, fuseSemanticTokens, applyMathOperation, generateRecursiveChain, calculateSemanticCurvature, generateVisualization]);

  // Apply mathematical transformation to current expression
  const transformExpression = useCallback((operation) => {
    if (!currentExpression) return;
    
    const tokens = currentExpression.split(' ');
    const transformedTokens = tokens.map(token => {
      if (Math.random() > 0.5) { // Apply transformation probabilistically
        return applyMathOperation(token, operation);
      }
      return token;
    });
    
    const newExpression = transformedTokens.join(' ');
    setCurrentExpression(newExpression);
    
    const newCurvature = calculateSemanticCurvature(newExpression);
    setCurvatureValue(newCurvature);
    
    const viz = generateVisualization(newExpression);
    setVisualization(viz);
  }, [currentExpression, applyMathOperation, calculateSemanticCurvature, generateVisualization]);

  return (
    <div className="max-w-7xl mx-auto p-6 bg-gradient-to-br from-slate-900 via-indigo-900 to-purple-900 min-h-screen text-white">
      <div className="mb-8 text-center">
        <h1 className="text-5xl font-bold mb-4 bg-gradient-to-r from-cyan-400 via-purple-400 to-pink-400 bg-clip-text text-transparent">
          Semantic Curvature Engine
        </h1>
        <p className="text-slate-300 text-lg">
          Mathematical manipulation of meaning-space curvature through self-referential linguistic fractals
        </p>
      </div>

      {/* Control Panel */}
      <div className="grid grid-cols-1 md:grid-cols-4 gap-6 mb-8">
        <div className="bg-slate-800/50 p-4 rounded-lg border border-slate-700">
          <label className="block text-sm font-medium mb-2 text-cyan-300">Curvature Intensity</label>
          <input
            type="range"
            min="0"
            max="1"
            step="0.1"
            value={curvatureValue}
            onChange={(e) => setCurvatureValue(parseFloat(e.target.value))}
            className="w-full"
          />
          <div className="text-xs text-slate-400 mt-1">{curvatureValue.toFixed(1)}</div>
        </div>

        <div className="bg-slate-800/50 p-4 rounded-lg border border-slate-700">
          <label className="block text-sm font-medium mb-2 text-cyan-300">Recursion Depth</label>
          <input
            type="range"
            min="1"
            max="6"
            value={recursionDepth}
            onChange={(e) => setRecursionDepth(parseInt(e.target.value))}
            className="w-full"
          />
          <div className="text-xs text-slate-400 mt-1">{recursionDepth} levels</div>
        </div>

        <div className="bg-slate-800/50 p-4 rounded-lg border border-slate-700">
          <label className="block text-sm font-medium mb-2 text-cyan-300">Operator Mode</label>
          <select
            value={operatorMode}
            onChange={(e) => setOperatorMode(e.target.value)}
            className="w-full bg-slate-700 border border-slate-600 rounded px-3 py-2"
          >
            <option value="forward">Forward</option>
            <option value="backwards">Backwards</option>
            <option value="square">Square Function</option>
            <option value="differential">Differential</option>
          </select>
        </div>

        <button
          onClick={generateExpression}
          className="bg-gradient-to-r from-purple-600 to-cyan-600 hover:from-purple-700 hover:to-cyan-700 px-6 py-4 rounded-lg font-semibold flex items-center justify-center gap-2 transition-all duration-300"
        >
          <Brain className="w-5 h-5" />
          Generate Expression
        </button>
      </div>

      {/* Mathematical Operations */}
      <div className="mb-8">
        <h3 className="text-xl font-semibold mb-4 text-cyan-300">Mathematical Transformations</h3>
        <div className="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-6 gap-3">
          {Object.keys(mathOperations).map(op => (
            <button
              key={op}
              onClick={() => transformExpression(op)}
              className="px-3 py-2 bg-slate-700 hover:bg-slate-600 rounded text-sm transition-all duration-200 hover:scale-105 border border-slate-600"
            >
              {op}
            </button>
          ))}
        </div>
      </div>

      {/* Current Expression */}
      {currentExpression && (
        <div className="mb-8">
          <div className="bg-slate-800/50 p-6 rounded-lg border border-slate-700">
            <div className="flex items-center justify-between mb-4">
              <h3 className="text-xl font-semibold text-cyan-300">Generated Expression</h3>
              <div className="flex items-center gap-4">
                <span className="text-sm text-slate-400">
                  Curvature: {(calculateSemanticCurvature(currentExpression) * 100).toFixed(1)}%
                </span>
                <button
                  onClick={() => navigator.clipboard.writeText(currentExpression)}
                  className="px-3 py-1 bg-purple-600 hover:bg-purple-700 rounded text-sm transition-colors"
                >
                  Copy
                </button>
              </div>
            </div>
            <div className="text-lg leading-relaxed font-mono bg-slate-900/50 p-4 rounded border border-slate-600">
              {currentExpression}
            </div>
          </div>
        </div>
      )}

      {/* Semantic Curvature Visualization */}
      {visualization.length > 0 && (
        <div className="mb-8">
          <h3 className="text-xl font-semibold mb-4 text-cyan-300">Semantic Curvature Visualization</h3>
          <div className="bg-slate-800/50 p-6 rounded-lg border border-slate-700">
            <div className="flex flex-wrap gap-2">
              {visualization.map((item, index) => (
                <div
                  key={index}
                  className="relative px-3 py-2 rounded-lg border transition-all duration-300"
                  style={{
                    backgroundColor: `rgba(139, 92, 246, ${item.intensity})`,
                    borderColor: `rgba(34, 197, 94, ${item.curvature})`,
                    transform: `scale(${1 + item.curvature * 0.2})`,
                  }}
                >
                  <span className="text-sm font-mono">{item.token}</span>
                  <div className="absolute -top-1 -right-1 w-3 h-3 rounded-full bg-cyan-400" 
                       style={{ opacity: item.recursionLevel * 0.3 }} />
                </div>
              ))}
            </div>
            <div className="mt-4 text-xs text-slate-400">
              Token size = curvature intensity • Border color = semantic curvature • Dot opacity = recursion level
            </div>
          </div>
        </div>
      )}

      {/* Theory Panel */}
      <div className="bg-gradient-to-r from-purple-900/30 to-cyan-900/30 rounded-lg border border-purple-500/30 p-6">
        <h3 className="text-xl font-semibold mb-4 text-purple-300">Semantic Curvature Theory</h3>
        <div className="text-slate-300 space-y-3 text-sm">
          <p><strong>Curvature:</strong> Measures the self-referential density of meaning-space. Higher curvature = more recursive loops.</p>
          <p><strong>Mathematical Operations:</strong> Transform semantic tokens through formal operations (square, differential, meta-recursion).</p>
          <p><strong>Throughness:</strong> The quality of meaning passing through itself while being itself.</p>
          <p><strong>Retrobackcasting:</strong> Temporal recursion where future meaning determines past meaning.</p>
          <p><strong>Non-non-thinking:</strong> Double negation creates semantic superposition - neither thinking nor not-thinking.</p>
        </div>
      </div>
    </div>
  );
};

export default SemanticCurvatureEngine;
```