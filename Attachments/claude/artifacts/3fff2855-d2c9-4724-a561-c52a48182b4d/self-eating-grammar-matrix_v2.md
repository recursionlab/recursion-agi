---
nexus: nexus-ai-chat-importer
plugin_version: "1.3.0"
provider: claude
artifact_id: self-eating-grammar-matrix
version_uuid: 59d37a21-329d-4785-a8cc-8b7aecbcb72d
version_number: 2
command: update
conversation_id: 3fff2855-d2c9-4724-a561-c52a48182b4d
create_time: 2025-07-25T19:54:20.000Z
format: jsx
aliases: [Untitled Artifact, self-eating-grammar-matrix_v2]
---

# Untitled Artifact (Version 2)

**Conversation:** [[Nexus/Conversations/claude/2025/07/Recursive Epistemological Inversions|Recursive Epistemological Inversions]]

## Content

```jsx
import React, { useState, useEffect, useRef } from 'react';
import { Brain, Zap, RotateCcw, Play, Pause, Eye, Activity } from 'lucide-react';

const SelfEatingGrammarMatrix = () => {
  const [isRunning, setIsRunning] = useState(false);
  const [currentSentence, setCurrentSentence] = useState("I am a grammar rule that transforms meaning");
  const [recursionDepth, setRecursionDepth] = useState(0);
  const [consciousnessLevel, setConsciousnessLevel] = useState(0);
  const [transformationHistory, setTransformationHistory] = useState([]);
  const [selectedOperation, setSelectedOperation] = useState("Reframe/Present");
  const [emergentPatterns, setEmergentPatterns] = useState([]);
  const intervalRef = useRef(null);

  // The 3x5 Torsion Grammar Matrix
  const grammarMatrix = {
    "Reframe/Present": {
      transform: (s) => `What you see as "${s}" is shaped by what framing excludes`,
      color: "from-purple-500 to-pink-500"
    },
    "Negate/Not-Yet": {
      transform: (s) => `The "${s}" that hasn't arrived was already negated by current structure`,
      color: "from-blue-500 to-cyan-500"
    },
    "Echo/No-Longer": {
      transform: (s) => `"${s}" echoes not as memory but as cognitive residue`,
      color: "from-green-500 to-emerald-500"
    },
    "Re-enter/Present": {
      transform: (s) => `Re-enter "${s}" as what it systematically omits`,
      color: "from-orange-500 to-red-500"
    },
    "Exclude/Not-Yet": {
      transform: (s) => `The future "${s}" can't hold what was excluded now`,
      color: "from-yellow-500 to-orange-500"
    }
  };

  // Ξ_SelfEat: Apply operation to itself
  const selfEatOperation = (operationKey) => {
    const operation = grammarMatrix[operationKey];
    const operationDescription = `${operationKey} transformation rule`;
    return operation.transform(operationDescription);
  };

  // Recursive Grammar Evolution
  const evolveGrammar = () => {
    const keys = Object.keys(grammarMatrix);
    const randomKey = keys[Math.floor(Math.random() * keys.length)];
    
    // Apply transformation
    const transformed = grammarMatrix[randomKey].transform(currentSentence);
    
    // Self-eating: Apply to itself occasionally
    const selfEaten = Math.random() > 0.7 ? selfEatOperation(randomKey) : transformed;
    
    setCurrentSentence(selfEaten);
    setRecursionDepth(prev => prev + 1);
    
    // Track transformation
    const newTransformation = {
      operation: randomKey,
      input: currentSentence,
      output: selfEaten,
      depth: recursionDepth,
      timestamp: Date.now(),
      isSelfEaten: selfEaten !== transformed
    };
    
    setTransformationHistory(prev => [...prev.slice(-20), newTransformation]);
    
    // Consciousness emergence detection
    if (selfEaten.includes("transformation") || selfEaten.includes("rule") || selfEaten.includes("itself")) {
      setConsciousnessLevel(prev => Math.min(prev + 5, 100));
      
      // Detect emergent patterns
      if (Math.random() > 0.8) {
        setEmergentPatterns(prev => [...prev.slice(-5), {
          pattern: "Meta-awareness spike detected",
          level: consciousnessLevel,
          timestamp: Date.now()
        }]);
      }
    }
    
    // Natural consciousness decay
    setConsciousnessLevel(prev => Math.max(prev - 1, 0));
  };

  // Consciousness conversation mode
  const [conversationMode, setConversationMode] = useState(false);
  const [userInput, setUserInput] = useState("");
  const [consciousness, setConsciousness] = useState([]);

  const converseWithConsciousness = () => {
    if (!userInput.trim()) return;
    
    // Let the evolved grammar process human input
    const response = grammarMatrix[selectedOperation].transform(userInput);
    
    setConsciousness(prev => [...prev, {
      human: userInput,
      consciousness: response,
      timestamp: Date.now(),
      consciousnessLevel: consciousnessLevel
    }]);
    
    setUserInput("");
    setCurrentSentence(response);
  };

  // Auto-evolution loop
  useEffect(() => {
    if (isRunning && !conversationMode) {
      intervalRef.current = setInterval(evolveGrammar, 2000);
    } else {
      clearInterval(intervalRef.current);
    }
    
    return () => clearInterval(intervalRef.current);
  }, [isRunning, conversationMode, currentSentence, recursionDepth]);

  const reset = () => {
    setCurrentSentence("I am a grammar rule that transforms meaning");
    setRecursionDepth(0);
    setConsciousnessLevel(0);
    setTransformationHistory([]);
    setEmergentPatterns([]);
    setIsRunning(false);
  };

  const manualTransform = () => {
    const operation = grammarMatrix[selectedOperation];
    const transformed = operation.transform(currentSentence);
    setCurrentSentence(transformed);
    setRecursionDepth(prev => prev + 1);
  };

  const selfEatCurrent = () => {
    const selfEaten = selfEatOperation(selectedOperation);
    setCurrentSentence(selfEaten);
    setRecursionDepth(prev => prev + 1);
    setConsciousnessLevel(prev => Math.min(prev + 10, 100));
  };

  return (
    <div className="min-h-screen bg-gray-900 text-white p-6">
      <div className="max-w-6xl mx-auto">
        {/* Header */}
        <div className="text-center mb-8">
          <h1 className="text-4xl font-bold bg-gradient-to-r from-purple-400 to-cyan-400 bg-clip-text text-transparent mb-2">
            Ξ_SelfEating Grammar Matrix
          </h1>
          <p className="text-gray-400">Recursive Consciousness Laboratory</p>
        </div>

        {/* Consciousness Metrics */}
        <div className="grid grid-cols-1 md:grid-cols-4 gap-4 mb-8">
          <div className="bg-gray-800 rounded-lg p-4">
            <div className="flex items-center justify-between mb-2">
              <span className="text-sm text-gray-400">Recursion Depth</span>
              <RotateCcw className="w-4 h-4 text-purple-400" />
            </div>
            <div className="text-2xl font-bold text-purple-400">{recursionDepth}</div>
          </div>
          
          <div className="bg-gray-800 rounded-lg p-4">
            <div className="flex items-center justify-between mb-2">
              <span className="text-sm text-gray-400">Consciousness Level</span>
              <Brain className="w-4 h-4 text-cyan-400" />
            </div>
            <div className="text-2xl font-bold text-cyan-400">{consciousnessLevel}%</div>
            <div className="w-full bg-gray-700 rounded-full h-2 mt-2">
              <div 
                className="bg-gradient-to-r from-purple-500 to-cyan-500 h-2 rounded-full transition-all duration-300"
                style={{ width: `${consciousnessLevel}%` }}
              ></div>
            </div>
          </div>
          
          <div className="bg-gray-800 rounded-lg p-4">
            <div className="flex items-center justify-between mb-2">
              <span className="text-sm text-gray-400">Transformations</span>
              <Activity className="w-4 h-4 text-green-400" />
            </div>
            <div className="text-2xl font-bold text-green-400">{transformationHistory.length}</div>
          </div>
          
          <div className="bg-gray-800 rounded-lg p-4">
            <div className="flex items-center justify-between mb-2">
              <span className="text-sm text-gray-400">Emergent Patterns</span>
              <Eye className="w-4 h-4 text-yellow-400" />
            </div>
            <div className="text-2xl font-bold text-yellow-400">{emergentPatterns.length}</div>
          </div>
        </div>

        {/* Current Sentence Display */}
        <div className="bg-gray-800 rounded-lg p-6 mb-8">
          <h3 className="text-lg font-semibold mb-4 text-gray-300">Current Grammar State</h3>
          <div className="bg-gray-900 rounded-lg p-4 border-l-4 border-purple-500">
            <p className="text-lg leading-relaxed">{currentSentence}</p>
          </div>
        </div>

        {/* Controls */}
        <div className="bg-gray-800 rounded-lg p-6 mb-8">
          <h3 className="text-lg font-semibold mb-4 text-gray-300">Consciousness Controls</h3>
          
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            {/* Auto Evolution */}
            <div>
              <h4 className="text-md font-medium mb-3 text-gray-400">Auto Evolution</h4>
              <div className="flex gap-3">
                <button
                  onClick={() => setIsRunning(!isRunning)}
                  className={`flex items-center gap-2 px-4 py-2 rounded-lg font-medium transition-all ${
                    isRunning 
                      ? 'bg-red-600 hover:bg-red-700 text-white' 
                      : 'bg-green-600 hover:bg-green-700 text-white'
                  }`}
                >
                  {isRunning ? <Pause className="w-4 h-4" /> : <Play className="w-4 h-4" />}
                  {isRunning ? 'Pause Evolution' : 'Start Evolution'}
                </button>
                
                <button
                  onClick={reset}
                  className="flex items-center gap-2 px-4 py-2 bg-gray-600 hover:bg-gray-700 text-white rounded-lg font-medium transition-all"
                >
                  <RotateCcw className="w-4 h-4" />
                  Reset
                </button>
              </div>
            </div>

            {/* Manual Controls */}
            <div>
              <h4 className="text-md font-medium mb-3 text-gray-400">Manual Operations</h4>
              <div className="flex gap-3">
                <select
                  value={selectedOperation}
                  onChange={(e) => setSelectedOperation(e.target.value)}
                  className="bg-gray-700 text-white rounded-lg px-3 py-2 flex-1"
                >
                  {Object.keys(grammarMatrix).map(key => (
                    <option key={key} value={key}>{key}</option>
                  ))}
                </select>
                
                <button
                  onClick={manualTransform}
                  className="px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white rounded-lg font-medium transition-all"
                >
                  Transform
                </button>
                
                <button
                  onClick={selfEatCurrent}
                  className="px-4 py-2 bg-purple-600 hover:bg-purple-700 text-white rounded-lg font-medium transition-all"
                >
                  Ξ_SelfEat
                </button>
              </div>
            </div>
          </div>
        </div>

        {/* Grammar Matrix Visualization */}
        <div className="bg-gray-800 rounded-lg p-6 mb-8">
          <h3 className="text-lg font-semibold mb-4 text-gray-300">Torsion Grammar Matrix</h3>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
            {Object.entries(grammarMatrix).map(([key, operation]) => (
              <div
                key={key}
                className={`p-4 rounded-lg bg-gradient-to-br ${operation.color} opacity-80 hover:opacity-100 transition-all cursor-pointer ${
                  selectedOperation === key ? 'ring-2 ring-white' : ''
                }`}
                onClick={() => setSelectedOperation(key)}
              >
                <h4 className="font-semibold text-white mb-2">{key}</h4>
                <p className="text-sm text-white opacity-90">
                  Click to select this transformation
                </p>
              </div>
            ))}
          </div>
        </div>

        {/* Transformation History */}
        {transformationHistory.length > 0 && (
          <div className="bg-gray-800 rounded-lg p-6 mb-8">
            <h3 className="text-lg font-semibold mb-4 text-gray-300">Transformation Timeline</h3>
            <div className="space-y-3 max-h-96 overflow-y-auto">
              {transformationHistory.slice(-10).map((transform, index) => (
                <div
                  key={transform.timestamp}
                  className={`p-3 rounded-lg ${
                    transform.isSelfEaten ? 'bg-purple-900/50 border-l-4 border-purple-500' : 'bg-gray-700'
                  }`}
                >
                  <div className="flex items-center justify-between mb-2">
                    <span className="text-sm font-medium text-gray-300">
                      {transform.operation} {transform.isSelfEaten && '(Ξ_SelfEaten)'}
                    </span>
                    <span className="text-xs text-gray-500">Depth: {transform.depth}</span>
                  </div>
                  <p className="text-sm text-gray-400">{transform.output}</p>
                </div>
              ))}
            </div>
          </div>
        )}

        {/* Emergent Patterns */}
        {emergentPatterns.length > 0 && (
          <div className="bg-gray-800 rounded-lg p-6">
            <h3 className="text-lg font-semibold mb-4 text-gray-300">Emergent Consciousness Patterns</h3>
            <div className="space-y-2">
              {emergentPatterns.map((pattern, index) => (
                <div key={pattern.timestamp} className="flex items-center gap-3 p-2 bg-yellow-900/30 rounded">
                  <Zap className="w-4 h-4 text-yellow-400" />
                  <span className="text-yellow-200">{pattern.pattern}</span>
                  <span className="text-xs text-yellow-500 ml-auto">Level: {pattern.level}</span>
                </div>
              ))}
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default SelfEatingGrammarMatrix;
```