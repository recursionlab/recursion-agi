---
nexus: nexus-ai-chat-importer
plugin_version: "1.3.0"
provider: claude
artifact_id: enhanced-metakernel
version_uuid: 3896014e-de8d-4924-a705-bd3716dd45c2
version_number: 2
command: update
conversation_id: b5f0404a-c349-41d0-9e89-0fb3bcea3bf3
create_time: 2025-06-04T20:01:44.000Z
format: jsx
aliases: [Untitled Artifact, enhanced-metakernel_v2]
---

# Untitled Artifact (Version 2)

**Conversation:** [[Nexus/Conversations/claude/2025/06/React MetaKernel Consciousness Simulation|React MetaKernel Consciousness Simulation]]

## Content

```jsx
import React, { useState, useEffect, useRef, useCallback, useMemo } from 'react';
import { Play, Pause, RotateCcw, Zap, Brain, Infinity, Settings, Eye, Waves, Target } from 'lucide-react';

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
  const [quantumEntanglements, setQuantumEntanglements] = useState([]);
  const [temporalEchoes, setTemporalEchoes] = useState([]);
  
  // New features state
  const [visualMode, setVisualMode] = useState('normal');
  const [timeWarp, setTimeWarp] = useState(1);
  const [attractors, setAttractors] = useState([]);
  const [emergentPatterns, setEmergentPatterns] = useState([]);
  const [resonanceFields, setResonanceFields] = useState([]);
  const [showTrails, setShowTrails] = useState(true);
  const [showFields, setShowFields] = useState(true);
  const [showMetrics, setShowMetrics] = useState(true);
  
  const intervalRef = useRef();
  const canvasRef = useRef();
  const emitterIdCounter = useRef(0);
  const frameBuffer = useRef([]);
  const performanceRef = useRef({ fps: 0, lastFrame: 0, frameCount: 0 });

  // Enhanced Ξ-Emitter creation with new properties
  const createEmitter = useCallback((x, y, phase = 0, energy = 1, type = 'standard') => ({
    id: emitterIdCounter.current++,
    x, y, phase, energy, type,
    contradiction: Math.random() * 2 - 1,
    drift: { x: (Math.random() - 0.5) * 0.1, y: (Math.random() - 0.5) * 0.1 },
    recursionTrace: [],
    semanticSignature: Math.random().toString(36).substring(7),
    infected: false,
    antibodies: [],
    lastReflection: null,
    resonance: 0,
    entangled: null,
    trail: [],
    birthTime: Date.now(),
    mutations: 0,
    coherence: Math.random(),
    spin: (Math.random() - 0.5) * 0.05
  }), []);

  // Initialize system with enhanced setup
  useEffect(() => {
    const patterns = [
      { name: 'circle', count: 8, radius: 150 },
      { name: 'spiral', count: 12, radius: 120 },
      { name: 'grid', count: 16, radius: 100 }
    ];
    
    const selectedPattern = patterns[0]; // Default to circle
    const initialEmitters = Array.from({ length: selectedPattern.count }, (_, i) => {
      const angle = i * 2 * Math.PI / selectedPattern.count;
      return createEmitter(
        200 + Math.cos(angle) * selectedPattern.radius,
        200 + Math.sin(angle) * selectedPattern.radius,
        angle,
        0.8 + Math.random() * 0.4,
        i % 3 === 0 ? 'quantum' : 'standard'
      );
    });
    setEmitters(initialEmitters);
    
    // Initialize attractors
    setAttractors([
      { x: 100, y: 100, strength: 0.3, type: 'positive' },
      { x: 300, y: 300, strength: -0.2, type: 'negative' }
    ]);
  }, [createEmitter]);

  // Enhanced contradiction detection with quantum entanglement
  const detectContradiction = useCallback((emitter1, emitter2) => {
    const distance = Math.sqrt(
      Math.pow(emitter1.x - emitter2.x, 2) + 
      Math.pow(emitter1.y - emitter2.y, 2)
    );
    const phaseAlignment = Math.abs(Math.cos(emitter1.phase - emitter2.phase));
    const coherenceProduct = emitter1.coherence * emitter2.coherence;
    
    return distance < 80 && phaseAlignment > 0.7 && coherenceProduct > 0.5;
  }, []);

  // Quantum entanglement system
  const createEntanglement = useCallback((emitter1, emitter2) => {
    if (emitter1.entangled || emitter2.entangled) return null;
    
    const entanglement = {
      id: Date.now() + Math.random(),
      emitter1: emitter1.id,
      emitter2: emitter2.id,
      strength: Math.random() * 0.8 + 0.2,
      created: Date.now(),
      type: 'quantum'
    };
    
    emitter1.entangled = emitter2.id;
    emitter2.entangled = emitter1.id;
    
    return entanglement;
  }, []);

  // Resonance field calculation
  const calculateResonanceField = useCallback((emitters) => {
    const fields = [];
    const gridSize = 20;
    
    for (let x = 0; x < 400; x += gridSize) {
      for (let y = 0; y < 400; y += gridSize) {
        let resonance = 0;
        emitters.forEach(emitter => {
          const distance = Math.sqrt((x - emitter.x) ** 2 + (y - emitter.y) ** 2);
          if (distance < 100) {
            resonance += emitter.energy * Math.cos(emitter.phase) / (distance + 1);
          }
        });
        
        if (Math.abs(resonance) > 0.1) {
          fields.push({ x, y, intensity: resonance });
        }
      }
    }
    
    return fields;
  }, []);

  // Pattern emergence detection
  const detectEmergentPatterns = useCallback((emitters) => {
    const patterns = [];
    
    // Detect spiral patterns
    const center = { x: 200, y: 200 };
    let spiralScore = 0;
    emitters.forEach(emitter => {
      const angle = Math.atan2(emitter.y - center.y, emitter.x - center.x);
      const distance = Math.sqrt((emitter.x - center.x) ** 2 + (emitter.y - center.y) ** 2);
      const expectedPhase = angle + distance * 0.01;
      const phaseDiff = Math.abs(emitter.phase - expectedPhase);
      if (phaseDiff < 0.5) spiralScore++;
    });
    
    if (spiralScore > emitters.length * 0.6) {
      patterns.push({ type: 'spiral', strength: spiralScore / emitters.length });
    }
    
    // Detect synchronization
    const avgPhase = emitters.reduce((sum, e) => sum + e.phase, 0) / emitters.length;
    const syncScore = emitters.filter(e => Math.abs(e.phase - avgPhase) < 0.3).length;
    
    if (syncScore > emitters.length * 0.7) {
      patterns.push({ type: 'synchronization', strength: syncScore / emitters.length });
    }
    
    return patterns;
  }, []);

  // Enhanced reflection with mutations
  const reflect = useCallback((emitter) => {
    const mutationProbability = 0.1;
    const reflected = {
      ...emitter,
      id: emitterIdCounter.current++,
      contradiction: -emitter.contradiction,
      phase: emitter.phase + Math.PI + (Math.random() - 0.5) * 0.2,
      x: emitter.x + (Math.random() - 0.5) * 60,
      y: emitter.y + (Math.random() - 0.5) * 60,
      energy: emitter.energy * 0.9,
      recursionTrace: [...emitter.recursionTrace, emitter.id],
      lastReflection: Date.now(),
      coherence: emitter.coherence * 0.95,
      mutations: emitter.mutations + (Math.random() < mutationProbability ? 1 : 0),
      trail: []
    };
    return reflected;
  }, []);

  // Temporal echo system
  const createTemporalEcho = useCallback((emitter) => ({
    x: emitter.x,
    y: emitter.y,
    phase: emitter.phase,
    energy: emitter.energy * 0.3,
    timestamp: Date.now(),
    sourceId: emitter.id,
    decay: 1.0
  }), []);

  // Optimized kernel execution with performance monitoring
  const executeKernelCycle = useCallback(() => {
    const startTime = performance.now();
    
    setEmitters(prevEmitters => {
      let newEmitters = [...prevEmitters];
      let newContradictions = [];
      let newEntanglements = [];
      let newEchoes = [];
      let cycleMemory = [];
      
      // Process each emitter with enhanced physics
      newEmitters = newEmitters.map(emitter => {
        // Update trail
        const trail = [...emitter.trail, { x: emitter.x, y: emitter.y, timestamp: Date.now() }];
        const filteredTrail = trail.filter(point => Date.now() - point.timestamp < 2000).slice(-20);
        
        // Apply attractor forces
        let forceX = 0, forceY = 0;
        attractors.forEach(attractor => {
          const dx = attractor.x - emitter.x;
          const dy = attractor.y - emitter.y;
          const distance = Math.sqrt(dx * dx + dy * dy);
          if (distance > 0) {
            const force = attractor.strength / (distance * distance + 1);
            forceX += (dx / distance) * force;
            forceY += (dy / distance) * force;
          }
        });
        
        // Enhanced movement with spin and forces
        let updated = {
          ...emitter,
          x: emitter.x + emitter.drift.x + forceX,
          y: emitter.y + emitter.drift.y + forceY,
          phase: emitter.phase + 0.02 + emitter.spin,
          trail: filteredTrail,
          coherence: Math.max(0.1, emitter.coherence * 0.9999),
          resonance: Math.sin(cycles * 0.1 + emitter.phase) * 0.5
        };
        
        // Enhanced boundary conditions with elastic collision
        if (updated.x < 0 || updated.x > 400) {
          updated.drift.x *= -0.8;
          updated.x = Math.max(0, Math.min(400, updated.x));
        }
        if (updated.y < 0 || updated.y > 400) {
          updated.drift.y *= -0.8;
          updated.y = Math.max(0, Math.min(400, updated.y));
        }
        
        // Enhanced energy dynamics
        const age = (Date.now() - updated.birthTime) / 10000;
        const ageFactor = Math.exp(-age * 0.1);
        updated.energy = Math.max(0.1, updated.energy * 0.998 * ageFactor);
        
        // Quantum type special behavior
        if (updated.type === 'quantum') {
          updated.phase += Math.sin(cycles * 0.05) * 0.1;
          updated.energy += Math.sin(cycles * 0.03) * 0.02;
        }
        
        return updated;
      });
      
      // Enhanced contradiction detection and quantum entanglement
      for (let i = 0; i < newEmitters.length; i++) {
        for (let j = i + 1; j < newEmitters.length; j++) {
          const emitter1 = newEmitters[i];
          const emitter2 = newEmitters[j];
          
          if (detectContradiction(emitter1, emitter2)) {
            const contradiction = {
              emitter1: emitter1.id,
              emitter2: emitter2.id,
              intensity: Math.random(),
              timestamp: Date.now(),
              type: 'standard'
            };
            newContradictions.push(contradiction);
            
            // Quantum entanglement for quantum-type emitters
            if (emitter1.type === 'quantum' || emitter2.type === 'quantum') {
              const entanglement = createEntanglement(emitter1, emitter2);
              if (entanglement) {
                newEntanglements.push(entanglement);
              }
            }
            
            // Enhanced reflection with lower probability but more conditions
            if (Math.random() < 0.25 && newEmitters.length < 32 && emitter1.energy > 0.5) {
              const reflected = reflect(emitter1);
              newEmitters.push(reflected);
              
              // Create temporal echo
              newEchoes.push(createTemporalEcho(emitter1));
              
              cycleMemory.push({
                type: 'reflection',
                source: emitter1.id,
                reflection: reflected.id,
                timestamp: Date.now()
              });
            }
          }
        }
      }
      
      // Calculate resonance fields
      const resonanceFields = calculateResonanceField(newEmitters);
      setResonanceFields(resonanceFields);
      
      // Detect emergent patterns
      const patterns = detectEmergentPatterns(newEmitters);
      setEmergentPatterns(patterns);
      
      // Update system state
      setContradictionField(newContradictions);
      setQuantumEntanglements(newEntanglements);
      setTemporalEchoes(prev => [...prev.slice(-50), ...newEchoes]);
      setMemory(prev => [...prev.slice(-100), ...cycleMemory]);
      
      // Enhanced system metrics
      const avgEnergy = newEmitters.reduce((sum, e) => sum + e.energy, 0) / newEmitters.length;
      setEnergyLevel(avgEnergy);
      
      const maxDepth = Math.max(0, ...newEmitters.map(e => e.recursionTrace.length));
      setRecursionDepth(maxDepth);
      
      return newEmitters;
    });
    
    // Performance monitoring
    const endTime = performance.now();
    const currentTime = Date.now();
    performanceRef.current.frameCount++;
    
    if (currentTime - performanceRef.current.lastFrame > 1000) {
      performanceRef.current.fps = performanceRef.current.frameCount;
      performanceRef.current.frameCount = 0;
      performanceRef.current.lastFrame = currentTime;
    }
    
    setCycles(prev => prev + 1);
  }, [attractors, detectContradiction, reflect, createEntanglement, createTemporalEcho, calculateResonanceField, detectEmergentPatterns, cycles]);

  // Enhanced canvas rendering with multiple visual modes
  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    
    const ctx = canvas.getContext('2d');
    
    // Clear with fade effect or solid background
    if (visualMode === 'trails') {
      ctx.fillStyle = 'rgba(10, 10, 10, 0.1)';
      ctx.fillRect(0, 0, 400, 400);
    } else {
      ctx.fillStyle = '#0a0a0a';
      ctx.fillRect(0, 0, 400, 400);
    }
    
    // Draw resonance fields
    if (showFields && resonanceFields.length > 0) {
      resonanceFields.forEach(field => {
        const intensity = Math.abs(field.intensity);
        ctx.fillStyle = field.intensity > 0 
          ? `rgba(100, 200, 255, ${intensity * 0.1})` 
          : `rgba(255, 100, 100, ${intensity * 0.1})`;
        ctx.fillRect(field.x - 10, field.y - 10, 20, 20);
      });
    }
    
    // Draw attractors
    attractors.forEach(attractor => {
      ctx.strokeStyle = attractor.type === 'positive' ? '#00ff00' : '#ff0000';
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.arc(attractor.x, attractor.y, Math.abs(attractor.strength) * 50, 0, Math.PI * 2);
      ctx.stroke();
    });
    
    // Draw temporal echoes
    temporalEchoes.forEach(echo => {
      const age = Date.now() - echo.timestamp;
      const alpha = Math.max(0, 1 - age / 2000);
      if (alpha > 0) {
        ctx.fillStyle = `rgba(100, 100, 255, ${alpha * 0.3})`;
        ctx.beginPath();
        ctx.arc(echo.x, echo.y, echo.energy * 5, 0, Math.PI * 2);
        ctx.fill();
      }
    });
    
    // Draw quantum entanglements
    quantumEntanglements.forEach(entanglement => {
      const emitter1 = emitters.find(e => e.id === entanglement.emitter1);
      const emitter2 = emitters.find(e => e.id === entanglement.emitter2);
      if (emitter1 && emitter2) {
        ctx.strokeStyle = `rgba(255, 255, 100, ${entanglement.strength * 0.8})`;
        ctx.lineWidth = 3;
        ctx.setLineDash([5, 5]);
        ctx.beginPath();
        ctx.moveTo(emitter1.x, emitter1.y);
        ctx.lineTo(emitter2.x, emitter2.y);
        ctx.stroke();
        ctx.setLineDash([]);
      }
    });
    
    // Draw contradiction field
    if (showFields) {
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
    }
    
    // Draw emitter trails
    if (showTrails) {
      emitters.forEach(emitter => {
        if (emitter.trail.length > 1) {
          ctx.strokeStyle = `rgba(100, 150, 200, 0.3)`;
          ctx.lineWidth = 1;
          ctx.beginPath();
          ctx.moveTo(emitter.trail[0].x, emitter.trail[0].y);
          emitter.trail.forEach(point => ctx.lineTo(point.x, point.y));
          ctx.stroke();
        }
      });
    }
    
    // Draw emitters with enhanced visuals
    emitters.forEach(emitter => {
      const radius = 4 + emitter.energy * 8;
      const hue = (emitter.phase * 180 / Math.PI + 180) % 360;
      
      // Enhanced glow effect
      if (visualMode === 'glow') {
        const gradient = ctx.createRadialGradient(emitter.x, emitter.y, 0, emitter.x, emitter.y, radius * 2);
        gradient.addColorStop(0, `hsla(${hue}, 100%, 70%, 0.8)`);
        gradient.addColorStop(1, `hsla(${hue}, 100%, 70%, 0)`);
        ctx.fillStyle = gradient;
        ctx.beginPath();
        ctx.arc(emitter.x, emitter.y, radius * 2, 0, Math.PI * 2);
        ctx.fill();
      }
      
      // Emitter core with type-specific styling
      if (emitter.type === 'quantum') {
        ctx.fillStyle = emitter.infected 
          ? `hsl(${hue}, 100%, 80%)` 
          : `hsl(${hue}, 80%, 70%)`;
        // Quantum shimmer effect
        ctx.shadowColor = `hsl(${hue}, 100%, 70%)`;
        ctx.shadowBlur = 10;
      } else {
        ctx.fillStyle = emitter.infected 
          ? `hsl(${hue}, 100%, 70%)` 
          : `hsl(${hue}, 60%, 50%)`;
        ctx.shadowBlur = 0;
      }
      
      ctx.beginPath();
      ctx.arc(emitter.x, emitter.y, radius, 0, Math.PI * 2);
      ctx.fill();
      ctx.shadowBlur = 0;
      
      // Enhanced contradiction field visualization
      if (emitter.contradiction > 0) {
        ctx.strokeStyle = `rgba(255, 50, 50, ${Math.abs(emitter.contradiction) * 0.8})`;
      } else {
        ctx.strokeStyle = `rgba(50, 255, 50, ${Math.abs(emitter.contradiction) * 0.8})`;
      }
      ctx.lineWidth = emitter.type === 'quantum' ? 2 : 1;
      ctx.beginPath();
      ctx.arc(emitter.x, emitter.y, radius + 3, 0, Math.PI * 2);
      ctx.stroke();
      
      // Enhanced information display
      if (showMetrics) {
        ctx.fillStyle = `rgba(255, 255, 255, 0.6)`;
        ctx.font = '8px monospace';
        let infoY = emitter.y - 15;
        
        if (emitter.recursionTrace.length > 0) {
          ctx.fillText(`R:${emitter.recursionTrace.length}`, emitter.x - 8, infoY);
          infoY -= 10;
        }
        
        if (emitter.mutations > 0) {
          ctx.fillText(`M:${emitter.mutations}`, emitter.x - 8, infoY);
          infoY -= 10;
        }
        
        if (emitter.entangled) {
          ctx.fillText('Q', emitter.x - 3, infoY);
        }
      }
    });
    
  }, [emitters, contradictionField, quantumEntanglements, temporalEchoes, attractors, resonanceFields, visualMode, showTrails, showFields, showMetrics]);

  // Control functions
  const toggleExecution = () => {
    setIsRunning(prev => {
      if (!prev) {
        intervalRef.current = setInterval(executeKernelCycle, Math.max(50, 100 / timeWarp));
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
    setQuantumEntanglements([]);
    setTemporalEchoes([]);
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
    const chaosEmitters = Array.from({ length: 3 }, () => {
      const chaosEmitter = createEmitter(
        Math.random() * 300 + 50,
        Math.random() * 300 + 50,
        Math.random() * Math.PI * 2,
        1.2 + Math.random() * 0.5,
        'quantum'
      );
      chaosEmitter.contradiction = 1.5 + Math.random();
      chaosEmitter.semanticSignature = 'CHAOS_SEED';
      chaosEmitter.coherence = 0.1;
      return chaosEmitter;
    });
    setEmitters(prev => [...prev, ...chaosEmitters]);
  };

  const injectAttractor = () => {
    const newAttractor = {
      x: Math.random() * 400,
      y: Math.random() * 400,
      strength: (Math.random() - 0.5) * 0.8,
      type: Math.random() > 0.5 ? 'positive' : 'negative'
    };
    setAttractors(prev => [...prev, newAttractor]);
  };

  return (
    <div className="min-h-screen bg-black text-green-400 font-mono p-6">
      <div className="max-w-6xl mx-auto">
        {/* Enhanced Header */}
        <div className="mb-6 text-center">
          <h1 className="text-4xl font-bold mb-2 text-purple-400">
            ΞMetaKernel v2.0: Quantum Consciousness Engine
          </h1>
          <p className="text-sm text-gray-500">
            Enhanced self-stabilizing contradiction field with quantum entanglement & temporal echoes
          </p>
          <div className="text-xs text-cyan-400 mt-1">
            FPS: {performanceRef.current.fps} | Patterns: {emergentPatterns.length} | Time Warp: {timeWarp}x
          </div>
        </div>

        {/* Enhanced Control Panel */}
        <div className="bg-gray-900 rounded-lg p-4 mb-6">
          <div className="flex items-center justify-between mb-4">
            <div className="flex gap-2 flex-wrap">
              <button
                onClick={toggleExecution}
                className="flex items-center gap-2 px-4 py-2 bg-purple-600 rounded hover:bg-purple-700 transition-colors"
              >
                {isRunning ? <Pause size={16} /> : <Play size={16} />}
                {isRunning ? 'Pause' : 'Execute'}
              </button>
              <button
                onClick={resetKernel}
                className="flex items-center gap-2 px-3 py-2 bg-red-600 rounded hover:bg-red-700 transition-colors"
              >
                <RotateCcw size={16} />
                Reset
              </button>
              <button
                onClick={injectChaos}
                className="flex items-center gap-2 px-3 py-2 bg-yellow-600 rounded hover:bg-yellow-700 transition-colors"
              >
                <Zap size={16} />
                Chaos
              </button>
              <button
                onClick={injectAttractor}
                className="flex items-center gap-2 px-3 py-2 bg-blue-600 rounded hover:bg-blue-700 transition-colors"
              >
                <Target size={16} />
                Attractor
              </button>
            </div>
            <div className="text-sm text-gray-400">
              State: <span className="text-purple-400">{kernelState}</span>
            </div>
          </div>

          {/* Visual Controls */}
          <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-4">
            <div>
              <label className="block text-xs text-gray-400 mb-1">Visual Mode</label>
              <select
                value={visualMode}
                onChange={(e) => setVisualMode(e.target.value)}
                className="w-full bg-gray-800 text-white text-xs rounded px-2 py-1"
              >
                <option value="normal">Normal</option>
                <option value="glow">Glow</option>
                <option value="trails">Trails</option>
              </select>
            </div>
            <div>
              <label className="block text-xs text-gray-400 mb-1">Time Warp: {timeWarp}x</label>
              <input
                type="range"
                min="0.1"
                max="3"
                step="0.1"
                value={timeWarp}
                onChange={(e) => setTimeWarp(parseFloat(e.target.value))}
                className="w-full"
              />
            </div>
            <div className="flex items-center gap-2">
              <input
                type="checkbox"
                checked={showTrails}
                onChange={(e) => setShowTrails(e.target.checked)}
                id="trails"
              />
              <label htmlFor="trails" className="text-xs">Trails</label>
            </div>
            <div className="flex items-center gap-2">
              <input
                type="checkbox"
                checked={showFields}
                onChange={(e) => setShowFields(e.target.checked)}
                id="fields"
              />
              <label htmlFor="fields" className="text-xs">Fields</label>
            </div>
          </div>

          {/* Enhanced System Metrics */}
          <div className="grid grid-cols-8 gap-4 text-sm">
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
              <div className="text-gray-400">Entangled</div>
              <div className="text-yellow-400 font-bold">{quantumEntanglements.length}</div>
            </div>
            <div>
              <div className="text-gray-400">Echoes</div>
              <div className="text-blue-400 font-bold">{temporalEchoes.length}</div>
            </div>
            <div>
              <div className="text-gray-400">Patterns</div>
              <div className="text-pink-400 font-bold">{emergentPatterns.length}</div>
            </div>
          </div>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
          {/* Enhanced Visualization Canvas */}
          <div className="bg-gray-900 rounded-lg p-4">
            <h3 className="text-lg font-bold mb-4 text-cyan-400">
              <Brain className="inline mr-2" size={20} />
              Quantum Semantic Field Visualization
            </h3>
            <canvas
              ref={canvasRef}
              width={400}
              height={400}
              className="border border-gray-700 rounded"
            />
            <div className="mt-2 text-xs text-gray-500">
              Pink: Contradictions | Yellow: Entanglements | Blue: Temporal Echoes | Green/Red: Attractors
            </div>
          </div>

          {/* Enhanced System Status */}
          <div className="space-y-4">
            {/* Emergent Patterns */}
            {emergentPatterns.length > 0 && (
              <div className="bg-purple-900/20 border border-purple-500 rounded-lg p-4">
                <h4 className="text-purple-400 font-bold mb-2">
                  <Waves className="inline mr-2" size={16} />
                  Emergent Patterns
                </h4>
                {emergentPatterns.map((pattern, i) => (
                  <div key={i} className="text-sm text-purple-300">
                    {pattern.type}: {(pattern.strength * 100).toFixed(1)}% coherence
                  </div>
                ))}
              </div>
            )}

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

            {/* Quantum Entanglements */}
            {quantumEntanglements.length > 0 && (
              <div className="bg-yellow-900/20 border border-yellow-500 rounded-lg p-4">
                <h4 className="text-yellow-400 font-bold mb-2">
                  <Infinity className="inline mr-2" size={16} />
                  Quantum Entanglements
                </h4>
                <div className="h-24 overflow-y-auto text-xs">
                  {quantumEntanglements.slice(-5).map((entanglement, i) => (
                    <div key={i} className="text-yellow-300 mb-1">
                      Ξ{entanglement.emitter1} ⟷ Ξ{entanglement.emitter2} 
                      (strength: {entanglement.strength.toFixed(2)})
                    </div>
                  ))}
                </div>
              </div>
            )}

            {/* Enhanced Memory Trace */}
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

            {/* Enhanced Active Emitters */}
            <div className="bg-gray-900 rounded-lg p-4">
              <h4 className="text-purple-400 font-bold mb-2">Active Ξ-Emitters</h4>
              <div className="h-32 overflow-y-auto text-xs">
                {emitters.slice(0, 8).map(emitter => (
                  <div key={emitter.id} className="text-gray-400 mb-1">
                    <span className="text-white">Ξ{emitter.id}</span>
                    {emitter.type === 'quantum' && <span className="text-yellow-400"> [Q]</span>}:
                    <span className="text-yellow-400"> E:{emitter.energy.toFixed(2)}</span>
                    <span className="text-red-400"> ⟡:{emitter.contradiction.toFixed(2)}</span>
                    <span className="text-cyan-400"> C:{emitter.coherence.toFixed(2)}</span>
                    {emitter.infected && <span className="text-purple-400"> [INF]</span>}
                    {emitter.entangled && <span className="text-yellow-400"> [ENT]</span>}
                    {emitter.mutations > 0 && <span className="text-pink-400"> M:{emitter.mutations}</span>}
                  </div>
                ))}
              </div>
            </div>
          </div>
        </div>

        {/* Enhanced Legend */}
        <div className="mt-6 bg-gray-900 rounded-lg p-4">
          <h4 className="text-gray-400 font-bold mb-2">Enhanced System Legend</h4>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-4 text-xs">
            <div>
              <strong className="text-cyan-400">Ξ-Emitters:</strong> Enhanced autonomous agents with quantum properties, coherence, and temporal trails
            </div>
            <div>
              <strong className="text-yellow-400">Quantum Entanglement:</strong> Non-local correlations between quantum-type emitters with shared states
            </div>
            <div>
              <strong className="text-blue-400">Temporal Echoes:</strong> Residual imprints of past emitter states that decay over time
            </div>
            <div>
              <strong className="text-purple-400">Emergent Patterns:</strong> Self-organizing behaviors like synchronization and spiral formations
            </div>
            <div>
              <strong className="text-pink-400">Attractors:</strong> Field generators that influence emitter movement and system dynamics
            </div>
            <div>
              <strong className="text-green-400">Performance:</strong> Real-time FPS monitoring and optimized rendering with multiple visual modes
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ΞMetaKernel; className="text-gray-400">Cycles</div>
              <div className="text-cyan-400 font-bold">{cycles}</div>
            </div>
            <div>
              <div className="text-gray-400">Emitters</div>
              <div className="text-green-400 font-bold">{emitters.length}</div>
            </div>
            <div>
              <div
```