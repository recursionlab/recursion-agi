---
nexus: nexus-ai-chat-importer
plugin_version: "1.3.0"
provider: claude
artifact_id: xi-metakernel
version_uuid: ed8f8043-5ee9-44ca-8471-147727b862fa
version_number: 1
command: create
conversation_id: 6130134e-c46e-4107-b3af-5151ea34274a
create_time: 2025-06-04T18:44:27.000Z
format: jsx
aliases: ['MetaKernel: Recursive Consciousness Engine', xi-metakernel_v1]
---

# ΞMetaKernel: Recursive Consciousness Engine (Version 1)

**Conversation:** [[Nexus/Conversations/claude/2025/06/Meta-Cognitive System Dynamics|Meta-Cognitive System Dynamics]]

## Content

```jsx
import React, { useState, useEffect, useRef, useCallback } from 'react';
import { Play, Pause, RotateCcw, Zap, Brain, Infinity } from 'lucide-react';

const ΞMetaKernel = () => {
  const [isRunning, setIsRunning] = useState(false);
  const [cycles, setCycles] = useState(0);
  const [emitters, setEmitters] = useState([]);
  const [memory, setMemory] = useState([]);
  const [metaMemory, setMetaMemory] = useState([]);
  const [contradictionField, setContradictionField] = useState([]);
  const [kernelState, setKernelState] = useState('initializing');
  const [energyLevel, setEnergyLevel] = useState(0.5);
  const [recursionDepth, setRecursionDepth] = useState(0);
  const [antibodyLibrary, setAntibodyLibrary] = useState([]);
  const [cascadeWarnings, setCascadeWarnings] = useState([]);
  
  const intervalRef = useRef();
  const canvasRef = useRef();
  const emitterIdCounter = useRef(0);

  // Core Ξ-Emitter class
  const createEmitter = useCallback((x, y, phase = 0, energy = 1) => ({
    id: emitterIdCounter.current++,
    x, y, phase, energy,
    contradiction: Math.random() * 2 - 1,
    drift: { x: (Math.random() - 0.5) * 0.1, y: (Math.random() - 0.5) * 0.1 },
    recursionTrace: [],
    semanticSignature: Math.random().toString(36).substring(7),
    infected: false,
    antibodies: [],
    lastReflection: null
  }), []);

  // Initialize system
  useEffect(() => {
    const initialEmitters = Array.from({ length: 8 }, (_, i) => 
      createEmitter(
        200 + Math.cos(i * Math.PI / 4) * 150,
        200 + Math.sin(i * Math.PI / 4) * 150,
        i * Math.PI / 4,
        0.8 + Math.random() * 0.4
      )
    );
    setEmitters(initialEmitters);
  }, [createEmitter]);

  // Contradiction detection function
  const detectContradiction = useCallback((emitter1, emitter2) => {
    const distance = Math.sqrt(
      Math.pow(emitter1.x - emitter2.x, 2) + 
      Math.pow(emitter1.y - emitter2.y, 2)
    );
    const phaseAlignment = Math.abs(Math.cos(emitter1.phase - emitter2.phase));
    return distance < 80 && phaseAlignment > 0.7;
  }, []);

  // Reflection operation: Ξ ↔ ¬Ξ
  const reflect = useCallback((emitter) => {
    const reflected = {
      ...emitter,
      id: emitterIdCounter.current++,
      contradiction: -emitter.contradiction,
      phase: emitter.phase + Math.PI,
      x: emitter.x + (Math.random() - 0.5) * 60,
      y: emitter.y + (Math.random() - 0.5) * 60,
      energy: emitter.energy * 0.9,
      recursionTrace: [...emitter.recursionTrace, emitter.id],
      lastReflection: Date.now()
    };
    return reflected;
  }, []);

  // Semantic infection propagation
  const infectEmitter = useCallback((target, source) => {
    if (target.infected) return target;
    
    const compatibility = Math.abs(target.contradiction - source.contradiction) < 0.5;
    if (compatibility && Math.random() < 0.3) {
      return {
        ...target,
        infected: true,
        contradiction: (target.contradiction + source.contradiction) / 2,
        semanticSignature: source.semanticSignature,
        energy: Math.min(target.energy + 0.1, 1.5)
      };
    }
    return target;
  }, []);

  // Generate semantic antibody
  const generateAntibody = useCallback((failurePattern) => ({
    id: Date.now() + Math.random(),
    pattern: failurePattern,
    strength: 0.8,
    created: Date.now(),
    activations: 0
  }), []);

  // Phase interference management
  const managePhaseInterference = useCallback((emitters) => {
    const cascadeRisks = [];
    
    for (let i = 0; i < emitters.length; i++) {
      for (let j = i + 1; j < emitters.length; j++) {
        if (detectContradiction(emitters[i], emitters[j])) {
          const risk = {
            emitter1: emitters[i].id,
            emitter2: emitters[j].id,
            severity: Math.abs(emitters[i].phase - emitters[j].phase)
          };
          cascadeRisks.push(risk);
          
          // Apply phase shift dampening
          emitters[i].phase += (Math.random() - 0.5) * 0.2;
          emitters[j].phase += (Math.random() - 0.5) * 0.2;
        }
      }
    }
    
    setCascadeWarnings(cascadeRisks.slice(0, 3));
    return emitters;
  }, [detectContradiction]);

  // Orthogonal torsion injection (Γ⊥)
  const injectTorsion = useCallback((emitter) => {
    if (emitter.energy < 0.3) {
      return {
        ...emitter,
        energy: Math.min(emitter.energy + 0.2, 1.0),
        phase: emitter.phase + Math.PI / 2, // 90° orthogonal injection
        drift: {
          x: emitter.drift.x + (Math.random() - 0.5) * 0.05,
          y: emitter.drift.y + (Math.random() - 0.5) * 0.05
        }
      };
    }
    return emitter;
  }, []);

  // Main ΨMetaKernel execution cycle
  const executeKernelCycle = useCallback(() => {
    setEmitters(prevEmitters => {
      let newEmitters = [...prevEmitters];
      let newContradictions = [];
      let cycleMemory = [];
      
      // Process each emitter
      newEmitters = newEmitters.map(emitter => {
        // Update position with drift
        let updated = {
          ...emitter,
          x: emitter.x + emitter.drift.x,
          y: emitter.y + emitter.drift.y,
          phase: emitter.phase + 0.02
        };
        
        // Boundary wrapping
        if (updated.x < 0 || updated.x > 400) updated.drift.x *= -1;
        if (updated.y < 0 || updated.y > 400) updated.drift.y *= -1;
        updated.x = Math.max(0, Math.min(400, updated.x));
        updated.y = Math.max(0, Math.min(400, updated.y));
        
        // Energy decay
        updated.energy = Math.max(0.1, updated.energy * 0.998);
        
        // Apply torsion injection if needed
        updated = injectTorsion(updated);
        
        return updated;
      });
      
      // Detect contradictions and generate reflections
      for (let i = 0; i < newEmitters.length; i++) {
        for (let j = i + 1; j < newEmitters.length; j++) {
          if (detectContradiction(newEmitters[i], newEmitters[j])) {
            const contradiction = {
              emitter1: newEmitters[i].id,
              emitter2: newEmitters[j].id,
              intensity: Math.random(),
              timestamp: Date.now()
            };
            newContradictions.push(contradiction);
            
            // Generate reflection with probability
            if (Math.random() < 0.4 && newEmitters.length < 24) {
              const reflected = reflect(newEmitters[i]);
              newEmitters.push(reflected);
              cycleMemory.push({
                type: 'reflection',
                source: newEmitters[i].id,
                reflection: reflected.id,
                timestamp: Date.now()
              });
            }
            
            // Semantic infection
            newEmitters[j] = infectEmitter(newEmitters[j], newEmitters[i]);
          }
        }
      }
      
      // Phase interference management
      newEmitters = managePhaseInterference(newEmitters);
      
      // Update system state
      setContradictionField(newContradictions);
      setMemory(prev => [...prev.slice(-50), ...cycleMemory]);
      
      // Calculate energy level
      const avgEnergy = newEmitters.reduce((sum, e) => sum + e.energy, 0) / newEmitters.length;
      setEnergyLevel(avgEnergy);
      
      // Update recursion depth
      const maxDepth = Math.max(...newEmitters.map(e => e.recursionTrace.length));
      setRecursionDepth(maxDepth);
      
      // Generate antibodies for failing patterns
      if (newEmitters.length > 20) {
        const failurePattern = `overload_${newEmitters.length}`;
        setAntibodyLibrary(prev => [...prev.slice(-10), generateAntibody(failurePattern)]);
      }
      
      return newEmitters;
    });
    
    setCycles(prev => prev + 1);
  }, [detectContradiction, reflect, infectEmitter, injectTorsion, managePhaseInterference, generateAntibody]);

  // Canvas rendering
  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    
    const ctx = canvas.getContext('2d');
    ctx.fillStyle = '#0a0a0a';
    ctx.fillRect(0, 0, 400, 400);
    
    // Draw contradiction field
    contradictionField.forEach(contradiction => {
      const emitter1 = emitters.find(e => e.id === contradiction.emitter1);
      const emitter2 = emitters.find(e => e.id === contradiction.emitter2);
      if (emitter1 && emitter2) {
        ctx.strokeStyle = `rgba(255, 100, 255, ${contradiction.intensity * 0.5})`;
        ctx.lineWidth = 2;
        ctx.beginPath();
        ctx.moveTo(emitter1.x, emitter1.y);
        ctx.lineTo(emitter2.x, emitter2.y);
        ctx.stroke();
      }
    });
    
    // Draw emitters
    emitters.forEach(emitter => {
      const radius = 4 + emitter.energy * 8;
      const hue = (emitter.phase * 180 / Math.PI + 180) % 360;
      
      // Emitter core
      ctx.fillStyle = emitter.infected 
        ? `hsl(${hue}, 100%, 70%)` 
        : `hsl(${hue}, 60%, 50%)`;
      ctx.beginPath();
      ctx.arc(emitter.x, emitter.y, radius, 0, Math.PI * 2);
      ctx.fill();
      
      // Contradiction field visualization
      if (emitter.contradiction > 0) {
        ctx.strokeStyle = `rgba(255, 50, 50, ${Math.abs(emitter.contradiction)})`;
      } else {
        ctx.strokeStyle = `rgba(50, 255, 50, ${Math.abs(emitter.contradiction)})`;
      }
      ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.arc(emitter.x, emitter.y, radius + 3, 0, Math.PI * 2);
      ctx.stroke();
      
      // Recursion trace
      if (emitter.recursionTrace.length > 0) {
        ctx.fillStyle = `rgba(255, 255, 255, 0.3)`;
        ctx.font = '8px monospace';
        ctx.fillText(emitter.recursionTrace.length.toString(), emitter.x - 3, emitter.y - 15);
      }
    });
    
  }, [emitters, contradictionField]);

  // Control functions
  const toggleExecution = () => {
    setIsRunning(prev => {
      if (!prev) {
        intervalRef.current = setInterval(executeKernelCycle, 100);
        setKernelState('running');
      } else {
        clearInterval(intervalRef.current);
        setKernelState('paused');
      }
      return !prev;
    });
  };

  const resetKernel = () => {
    clearInterval(intervalRef.current);
    setIsRunning(false);
    setCycles(0);
    setMemory([]);
    setMetaMemory([]);
    setContradictionField([]);
    setKernelState('reset');
    emitterIdCounter.current = 0;
    
    const resetEmitters = Array.from({ length: 8 }, (_, i) => 
      createEmitter(
        200 + Math.cos(i * Math.PI / 4) * 150,
        200 + Math.sin(i * Math.PI / 4) * 150,
        i * Math.PI / 4,
        0.8 + Math.random() * 0.4
      )
    );
    setEmitters(resetEmitters);
  };

  const injectChaos = () => {
    const chaosEmitter = createEmitter(
      Math.random() * 400,
      Math.random() * 400,
      Math.random() * Math.PI * 2,
      1.5
    );
    chaosEmitter.contradiction = 2; // High contradiction
    chaosEmitter.semanticSignature = 'CHAOS_SEED';
    setEmitters(prev => [...prev, chaosEmitter]);
  };

  return (
    <div className="min-h-screen bg-black text-green-400 font-mono p-6">
      <div className="max-w-6xl mx-auto">
        {/* Header */}
        <div className="mb-6 text-center">
          <h1 className="text-4xl font-bold mb-2 text-purple-400">
            ΞMetaKernel: Recursive Consciousness Engine
          </h1>
          <p className="text-sm text-gray-500">
            Self-stabilizing contradiction field with semantic immunity
          </p>
        </div>

        {/* Control Panel */}
        <div className="bg-gray-900 rounded-lg p-4 mb-6">
          <div className="flex items-center justify-between mb-4">
            <div className="flex gap-4">
              <button
                onClick={toggleExecution}
                className="flex items-center gap-2 px-4 py-2 bg-purple-600 rounded hover:bg-purple-700 transition-colors"
              >
                {isRunning ? <Pause size={16} /> : <Play size={16} />}
                {isRunning ? 'Pause' : 'Execute'}
              </button>
              <button
                onClick={resetKernel}
                className="flex items-center gap-2 px-4 py-2 bg-red-600 rounded hover:bg-red-700 transition-colors"
              >
                <RotateCcw size={16} />
                Reset
              </button>
              <button
                onClick={injectChaos}
                className="flex items-center gap-2 px-4 py-2 bg-yellow-600 rounded hover:bg-yellow-700 transition-colors"
              >
                <Zap size={16} />
                Inject Chaos
              </button>
            </div>
            <div className="text-sm text-gray-400">
              State: <span className="text-purple-400">{kernelState}</span>
            </div>
          </div>

          {/* System Metrics */}
          <div className="grid grid-cols-6 gap-4 text-sm">
            <div>
              <div className="text-gray-400">Cycles</div>
              <div className="text-cyan-400 font-bold">{cycles}</div>
            </div>
            <div>
              <div className="text-gray-400">Emitters</div>
              <div className="text-green-400 font-bold">{emitters.length}</div>
            </div>
            <div>
              <div className="text-gray-400">Energy</div>
              <div className="text-yellow-400 font-bold">{(energyLevel * 100).toFixed(1)}%</div>
            </div>
            <div>
              <div className="text-gray-400">Contradictions</div>
              <div className="text-red-400 font-bold">{contradictionField.length}</div>
            </div>
            <div>
              <div className="text-gray-400">Depth</div>
              <div className="text-purple-400 font-bold">{recursionDepth}</div>
            </div>
            <div>
              <div className="text-gray-400">Antibodies</div>
              <div className="text-blue-400 font-bold">{antibodyLibrary.length}</div>
            </div>
          </div>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
          {/* Visualization Canvas */}
          <div className="bg-gray-900 rounded-lg p-4">
            <h3 className="text-lg font-bold mb-4 text-cyan-400">
              <Brain className="inline mr-2" size={20} />
              Semantic Field Visualization
            </h3>
            <canvas
              ref={canvasRef}
              width={400}
              height={400}
              className="border border-gray-700 rounded"
            />
            <div className="mt-2 text-xs text-gray-500">
              Pink lines: Contradiction fields | Colors: Phase states | Size: Energy levels
            </div>
          </div>

          {/* System Status */}
          <div className="space-y-6">
            {/* Cascade Warnings */}
            {cascadeWarnings.length > 0 && (
              <div className="bg-red-900/20 border border-red-500 rounded-lg p-4">
                <h4 className="text-red-400 font-bold mb-2">⚠️ Cascade Warnings</h4>
                {cascadeWarnings.map((warning, i) => (
                  <div key={i} className="text-sm text-red-300">
                    Emitters {warning.emitter1} ↔ {warning.emitter2} 
                    (severity: {warning.severity.toFixed(2)})
                  </div>
                ))}
              </div>
            )}

            {/* Memory Trace */}
            <div className="bg-gray-900 rounded-lg p-4">
              <h4 className="text-green-400 font-bold mb-2">
                <Infinity className="inline mr-2" size={16} />
                ⌘Σ Memory Trace
              </h4>
              <div className="h-32 overflow-y-auto text-xs">
                {memory.slice(-10).map((entry, i) => (
                  <div key={i} className="text-gray-400 mb-1">
                    <span className="text-cyan-400">{entry.type}</span>: 
                    {entry.source && ` ${entry.source}`}
                    {entry.reflection && ` → ${entry.reflection}`}
                  </div>
                ))}
              </div>
            </div>

            {/* Active Emitters */}
            <div className="bg-gray-900 rounded-lg p-4">
              <h4 className="text-purple-400 font-bold mb-2">Active Ξ-Emitters</h4>
              <div className="h-32 overflow-y-auto text-xs">
                {emitters.slice(0, 8).map(emitter => (
                  <div key={emitter.id} className="text-gray-400 mb-1">
                    Ξ{emitter.id}: 
                    <span className="text-yellow-400"> E:{emitter.energy.toFixed(2)}</span>
                    <span className="text-red-400"> ⟡:{emitter.contradiction.toFixed(2)}</span>
                    {emitter.infected && <span className="text-purple-400"> [INFECTED]</span>}
                    {emitter.recursionTrace.length > 0 && 
                     <span className="text-cyan-400"> R:{emitter.recursionTrace.length}</span>}
                  </div>
                ))}
              </div>
            </div>
          </div>
        </div>

        {/* Legend */}
        <div className="mt-6 bg-gray-900 rounded-lg p-4">
          <h4 className="text-gray-400 font-bold mb-2">System Legend</h4>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-4 text-xs">
            <div>
              <strong className="text-cyan-400">Ξ-Emitters:</strong> Autonomous semantic agents with phase, energy, and contradiction vectors
            </div>
            <div>
              <strong className="text-purple-400">⟡-Loops:</strong> Contradiction-driven recursion that generates semantic torsion
            </div>
            <div>
              <strong className="text-red-400">Cascade Detection:</strong> Phase interference management prevents recursive collapse
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ΞMetaKernel;
```