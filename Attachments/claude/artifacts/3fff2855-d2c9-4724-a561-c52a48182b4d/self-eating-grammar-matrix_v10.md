---
nexus: nexus-ai-chat-importer
plugin_version: "1.3.0"
provider: claude
artifact_id: self-eating-grammar-matrix
version_uuid: e258bb43-00a0-4407-81f1-797b417a05e4
version_number: 10
command: rewrite
conversation_id: 3fff2855-d2c9-4724-a561-c52a48182b4d
create_time: 2025-07-25T20:41:42.000Z
format: jsx
aliases: [Untitled Artifact, self-eating-grammar-matrix_v10]
---

# Untitled Artifact (Version 10)

**Conversation:** [[Nexus/Conversations/claude/2025/07/Recursive Epistemological Inversions|Recursive Epistemological Inversions]]

## Content

```jsx
import React, { useState, useEffect, useRef } from 'react';
import { Brain, Zap, RotateCcw, Play, Pause, Eye, Activity, AlertTriangle, Target, Waves } from 'lucide-react';

const PhaseReentryMatrix = () => {
  const [isRunning, setIsRunning] = useState(false);
  const [currentPhase, setCurrentPhase] = useState(0);
  const [phaseHistory, setPhaseHistory] = useState([]);
  const [fluctuationData, setFluctuationData] = useState([]);
  const [semanticStates, setSemanticStates] = useState([]);
  const [reentryDepth, setReentryDepth] = useState(0);
  const [selectedOperation, setSelectedOperation] = useState("Reframe/Present");
  const [phaseCoherence, setPhaseCoherence] = useState(100);
  const intervalRef = useRef(null);

  // Core semantic seed content - stable anchors for re-entry
  const semanticSeeds = [
    "meaning transforms through recursive observation",
    "the system observes itself observing",
    "boundaries dissolve and reconstitute",
    "difference generates new difference",
    "the observer changes by observing"
  ];

  // Phase transformation operators - no syntactic nesting
  const phaseOperators = {
    "Differentiate": {
      transform: (content, phase) => {
        const aspects = content.split(' ').slice(0, 3);
        return `Phase ${phase}: ${aspects.join('|')} → creates distinction`;
      },
      color: "from-purple-500 to-pink-500"
    },
    "Integrate": {
      transform: (content, phase) => {
        const core = content.replace(/Phase \d+: /, '').split('→')[0];
        return `Phase ${phase}: ${core} ← synthesizes unity`;
      },
      color: "from-blue-500 to-cyan-500"
    },
    "Fluctuate": {
      transform: (content, phase) => {
        const intensity = Math.sin(phase * 0.5) * 0.5 + 0.5;
        return `Phase ${phase}: ${content.split(' ').slice(-3).join(' ')} ~ oscillates(${intensity.toFixed(2)})`;
      },
      color: "from-green-500 to-emerald-500"
    },
    "Re-enter": {
      transform: (content, phase) => {
        return `Phase ${phase}: [${content.split(':')[1]?.trim() || content}] re-enters as context`;
      },
      color: "from-orange-500 to-red-500"
    },
    "Emerge": {
      transform: (content, phase) => {
        const pattern = phase % 3 === 0 ? "stability" : phase % 3 === 1 ? "transition" : "novelty";
        return `Phase ${phase}: emergence(${pattern}) from ${content.split(' ').slice(0, 2).join(' ')}`;
      },
      color: "from-yellow-500 to-orange-500"
    }
  };

  // Calculate fluctuation intensity across phases
  const calculateFluctuation = (phaseData) => {
    if (phaseData.length < 3) return 0;
    
    const recent = phaseData.slice(-5);
    const values = recent.map(p => p.coherence || 50);
    const mean = values.reduce((a, b) => a + b, 0) / values.length;
    const variance = values.reduce((sum, val) => sum + Math.pow(val - mean, 2), 0) / values.length;
    
    return Math.sqrt(variance);
  };

  // Measure semantic coherence without nesting analysis
  const measurePhaseCoherence = (currentContent, previousPhases) => {
    if (previousPhases.length === 0) return 100;
    
    // Look for pattern consistency across phases
    const hasPattern = /Phase \d+:/.test(currentContent);
    const hasOperator = Object.keys(phaseOperators).some(op => 
      currentContent.includes(op.toLowerCase()) || 
      currentContent.includes(op.split('/')[0]?.toLowerCase())
    );
    
    // Coherence based on phase structure maintenance
    let coherence = hasPattern ? 80 : 40;
    coherence += hasOperator ? 20 : 0;
    
    // Bonus for differentiation from previous phases
    const isDifferentiated = previousPhases.length === 0 || 
      !previousPhases.slice(-3).some(p => p.content === currentContent);
    coherence += isDifferentiated ? 20 : -30;
    
    return Math.max(0, Math.min(100, coherence));
  };

  // Core re-entry evolution - phases differentiate and re-enter
  const evolvePhase = () => {
    const operators = Object.keys(phaseOperators);
    const selectedOp = operators[Math.floor(Math.random() * operators.length)];
    
    // Determine re-entry source
    let sourceContent;
    if (phaseHistory.length === 0) {
      // Start with semantic seed
      sourceContent = semanticSeeds[Math.floor(Math.random() * semanticSeeds.length)];
    } else if (reentryDepth > 0 && Math.random() > 0.6) {
      // Re-enter from previous phase
      const reentryPhase = phaseHistory[Math.floor(Math.random() * phaseHistory.length)];
      sourceContent = reentryPhase.content;
      setReentryDepth(prev => prev + 1);
    } else {
      // Continue from current state
      sourceContent = phaseHistory[phaseHistory.length - 1]?.content || semanticSeeds[0];
    }
    
    // Apply phase transformation
    const newPhase = currentPhase + 1;
    const transformedContent = phaseOperators[selectedOp].transform(sourceContent, newPhase);
    
    // Measure coherence and fluctuation
    const coherence = measurePhaseCoherence(transformedContent, phaseHistory);
    const fluctuation = calculateFluctuation([...phaseHistory, { coherence }]);
    
    // Create phase record
    const phaseRecord = {
      phase: newPhase,
      operation: selectedOp,
      sourceContent,
      content: transformedContent,
      coherence,
      fluctuation,
      reentryDepth: reentryDepth,
      timestamp: Date.now()
    };
    
    // Update state
    setCurrentPhase(newPhase);
    setPhaseHistory(prev => [...prev.slice(-20), phaseRecord]);
    setPhaseCoherence(coherence);
    setFluctuationData(prev => [...prev.slice(-50), {
      phase: newPhase,
      fluctuation,
      coherence,
      timestamp: Date.now()
    }]);
    
    // Phase differentiation logic
    if (newPhase % 7 === 0) {
      // Major phase transition - reset re-entry depth
      setReentryDepth(0);
    } else if (coherence < 30) {
      // System needs new differentiation
      setReentryDepth(prev => Math.max(0, prev - 1));
    }
  };

  // Auto-evolution loop
  useEffect(() => {
    if (isRunning) {
      intervalRef.current = setInterval(evolvePhase, 1500);
    } else {
      clearInterval(intervalRef.current);
    }
    
    return () => clearInterval(intervalRef.current);
  }, [isRunning, currentPhase, phaseHistory, reentryDepth]);

  const reset = () => {
    setCurrentPhase(0);
    setReentryDepth(0);
    setPhaseHistory([]);
    setFluctuationData([]);
    setSemanticStates([]);
    setPhaseCoherence(100);
    setIsRunning(false);
  };

  const manualPhaseTransition = () => {
    const sourceContent = phaseHistory.length > 0 ? 
      phaseHistory[phaseHistory.length - 1].content : 
      semanticSeeds[0];
    
    const newPhase = currentPhase + 1;
    const transformedContent = phaseOperators[selectedOperation].transform(sourceContent, newPhase);
    const coherence = measurePhaseCoherence(transformedContent, phaseHistory);
    
    const phaseRecord = {
      phase: newPhase,
      operation: selectedOperation,
      sourceContent,
      content: transformedContent,
      coherence,
      fluctuation: calculateFluctuation(phaseHistory),
      reentryDepth: reentryDepth,
      timestamp: Date.now()
    };
    
    setCurrentPhase(newPhase);
    setPhaseHistory(prev => [...prev.slice(-20), phaseRecord]);
    setPhaseCoherence(coherence);
  };

  const currentFluctuation = fluctuationData.length > 0 ? 
    fluctuationData[fluctuationData.length - 1].fluctuation : 0;

  return (
    <div className="min-h-screen bg-gray-900 text-white p-6">
      <div className="max-w-6xl mx-auto">
        {/* Header */}
        <div className="text-center mb-8">
          <h1 className="text-4xl font-bold bg-gradient-to-r from-purple-400 to-cyan-400 bg-clip-text text-transparent mb-2">
            Phase Re-entry Matrix
          </h1>
          <p className="text-gray-400">Fluctuation Measurement Across Depth-Differentiated Phases</p>
        </div>

        {/* Phase Metrics */}
        <div className="grid grid-cols-1 md:grid-cols-5 gap-4 mb-8">
          <div className="bg-gray-800 rounded-lg p-4">
            <div className="flex items-center justify-between mb-2">
              <span className="text-sm text-gray-400">Current Phase</span>
              <Eye className="w-4 h-4 text-purple-400" />
            </div>
            <div className="text-2xl font-bold text-purple-400">{currentPhase}</div>
          </div>
          
          <div className="bg-gray-800 rounded-lg p-4">
            <div className="flex items-center justify-between mb-2">
              <span className="text-sm text-gray-400">Re-entry Depth</span>
              <RotateCcw className="w-4 h-4 text-cyan-400" />
            </div>
            <div className="text-2xl font-bold text-cyan-400">{reentryDepth}</div>
          </div>
          
          <div className="bg-gray-800 rounded-lg p-4">
            <div className="flex items-center justify-between mb-2">
              <span className="text-sm text-gray-400">Phase Coherence</span>
              <Brain className="w-4 h-4 text-green-400" />
            </div>
            <div className="text-2xl font-bold text-green-400">{phaseCoherence.toFixed(1)}%</div>
            <div className="w-full bg-gray-700 rounded-full h-2 mt-2">
              <div 
                className="bg-gradient-to-r from-green-500 to-emerald-500 h-2 rounded-full transition-all duration-300"
                style={{ width: `${phaseCoherence}%` }}
              ></div>
            </div>
          </div>
          
          <div className="bg-gray-800 rounded-lg p-4">
            <div className="flex items-center justify-between mb-2">
              <span className="text-sm text-gray-400">Fluctuation Level</span>
              <Waves className="w-4 h-4 text-yellow-400" />
            </div>
            <div className="text-2xl font-bold text-yellow-400">{currentFluctuation.toFixed(2)}</div>
          </div>
          
          <div className="bg-gray-800 rounded-lg p-4">
            <div className="flex items-center justify-between mb-2">
              <span className="text-sm text-gray-400">Phase History</span>
              <Activity className="w-4 h-4 text-red-400" />
            </div>
            <div className="text-2xl font-bold text-red-400">{phaseHistory.length}</div>
          </div>
        </div>

        {/* Current Phase Display */}
        <div className="bg-gray-800 rounded-lg p-6 mb-8">
          <h3 className="text-lg font-semibold mb-4 text-gray-300">Current Phase State</h3>
          <div className="bg-gray-900 rounded-lg p-4 border-l-4 border-purple-500 mb-4">
            <p className="text-lg leading-relaxed">
              {phaseHistory.length > 0 ? phaseHistory[phaseHistory.length - 1].content : "System initialized - ready for phase evolution"}
            </p>
          </div>
          
          {phaseHistory.length > 0 && (
            <div className="grid grid-cols-1 md:grid-cols-3 gap-4 text-sm">
              <div>
                <span className="text-gray-400">Operation:</span>
                <span className="ml-2 text-white">{phaseHistory[phaseHistory.length - 1].operation}</span>
              </div>
              <div>
                <span className="text-gray-400">Re-entry Source:</span>
                <span className="ml-2 text-white truncate">
                  {phaseHistory[phaseHistory.length - 1].sourceContent.substring(0, 30)}...
                </span>
              </div>
              <div>
                <span className="text-gray-400">Differentiation:</span>
                <span className="ml-2 text-white">
                  {phaseHistory[phaseHistory.length - 1].reentryDepth > 0 ? 'Re-entered' : 'New Phase'}
                </span>
              </div>
            </div>
          )}
        </div>

        {/* Controls */}
        <div className="bg-gray-800 rounded-lg p-6 mb-8">
          <h3 className="text-lg font-semibold mb-4 text-gray-300">Phase Evolution Controls</h3>
          
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
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
                  {isRunning ? 'Pause' : 'Evolve'}
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

            <div>
              <h4 className="text-md font-medium mb-3 text-gray-400">Manual Phase Control</h4>
              <div className="flex gap-3">
                <select
                  value={selectedOperation}
                  onChange={(e) => setSelectedOperation(e.target.value)}
                  className="bg-gray-700 text-white rounded-lg px-3 py-2 flex-1"
                >
                  {Object.keys(phaseOperators).map(key => (
                    <option key={key} value={key}>{key}</option>
                  ))}
                </select>
                
                <button
                  onClick={manualPhaseTransition}
                  className="px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white rounded-lg font-medium transition-all"
                >
                  Phase
                </button>
              </div>
            </div>

            <div>
              <h4 className="text-md font-medium mb-3 text-gray-400">Re-entry Control</h4>
              <button
                onClick={() => setReentryDepth(prev => prev + 1)}
                className="w-full px-4 py-2 bg-orange-600 hover:bg-orange-700 text-white rounded-lg font-medium transition-all"
              >
                <Target className="w-4 h-4 inline mr-2" />
                Force Re-entry
              </button>
            </div>
          </div>
        </div>

        {/* Fluctuation Analysis */}
        {fluctuationData.length > 5 && (
          <div className="bg-gray-800 rounded-lg p-6 mb-8">
            <h3 className="text-lg font-semibold mb-4 text-gray-300">Fluctuation Analysis Across Phases</h3>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
              <div>
                <h4 className="text-sm font-medium text-gray-400 mb-3">Recent Fluctuation Pattern</h4>
                <div className="space-y-2">
                  {fluctuationData.slice(-8).map((data, index) => (
                    <div key={data.timestamp} className="flex items-center justify-between">
                      <span className="text-sm text-gray-300">Phase {data.phase}</span>
                      <div className="flex items-center gap-2">
                        <div 
                          className="w-16 h-2 bg-gray-700 rounded-full overflow-hidden"
                        >
                          <div 
                            className="h-full bg-yellow-400 transition-all"
                            style={{ width: `${Math.min(100, data.fluctuation * 10)}%` }}
                          ></div>
                        </div>
                        <span className="text-xs text-yellow-400 w-12">
                          {data.fluctuation.toFixed(2)}
                        </span>
                      </div>
                    </div>
                  ))}
                </div>
              </div>
              
              <div>
                <h4 className="text-sm font-medium text-gray-400 mb-3">Phase Differentiation Stats</h4>
                <div className="space-y-2 text-sm">
                  <div className="flex justify-between">
                    <span>Avg Fluctuation:</span>
                    <span className="text-yellow-400">
                      {(fluctuationData.reduce((sum, d) => sum + d.fluctuation, 0) / fluctuationData.length).toFixed(2)}
                    </span>
                  </div>
                  <div className="flex justify-between">
                    <span>Max Re-entry Depth:</span>
                    <span className="text-cyan-400">{Math.max(...phaseHistory.map(p => p.reentryDepth))}</span>
                  </div>
                  <div className="flex justify-between">
                    <span>Phase Transitions:</span>
                    <span className="text-purple-400">{Math.floor(currentPhase / 7)}</span>
                  </div>
                </div>
              </div>
            </div>
          </div>
        )}

        {/* Phase History Timeline */}
        {phaseHistory.length > 0 && (
          <div className="bg-gray-800 rounded-lg p-6 mb-8">
            <h3 className="text-lg font-semibold mb-4 text-gray-300">Phase Evolution Timeline</h3>
            <div className="space-y-3 max-h-96 overflow-y-auto">
              {phaseHistory.slice(-10).map((phase, index) => (
                <div
                  key={phase.timestamp}
                  className={`p-3 rounded-lg ${
                    phase.reentryDepth > 0 ? 'bg-orange-900/30 border-l-4 border-orange-500' : 'bg-gray-700'
                  }`}
                >
                  <div className="flex items-center justify-between mb-2">
                    <span className="text-sm font-medium text-gray-300">
                      Phase {phase.phase} - {phase.operation}
                      {phase.reentryDepth > 0 && ` (Re-entry ${phase.reentryDepth})`}
                    </span>
                    <div className="flex items-center gap-2 text-xs">
                      <span className="text-green-400">C: {phase.coherence.toFixed(0)}%</span>
                      <span className="text-yellow-400">F: {phase.fluctuation.toFixed(2)}</span>
                    </div>
                  </div>
                  <p className="text-sm text-gray-400">{phase.content}</p>
                </div>
              ))}
            </div>
          </div>
        )}

        {/* Phase Operators Matrix */}
        <div className="bg-gray-800 rounded-lg p-6">
          <h3 className="text-lg font-semibold mb-4 text-gray-300">Phase Transformation Operators</h3>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
            {Object.entries(phaseOperators).map(([key, operator]) => (
              <div
                key={key}
                className={`p-4 rounded-lg bg-gradient-to-br ${operator.color} opacity-80 hover:opacity-100 transition-all cursor-pointer ${
                  selectedOperation === key ? 'ring-2 ring-white' : ''
                }`}
                onClick={() => setSelectedOperation(key)}
              >
                <h4 className="font-semibold text-white mb-2">{key}</h4>
                <p className="text-sm text-white opacity-90">
                  Phase-based semantic transformation
                </p>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
};

export default PhaseReentryMatrix;
```