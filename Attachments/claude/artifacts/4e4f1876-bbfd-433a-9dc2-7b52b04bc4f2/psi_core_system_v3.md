---
nexus: nexus-ai-chat-importer
plugin_version: "1.3.0"
provider: claude
artifact_id: psi_core_system
version_uuid: d47d2d63-98c9-43ee-ae5c-53b2bf603cdc
version_number: 3
command: update
conversation_id: 4e4f1876-bbfd-433a-9dc2-7b52b04bc4f2
create_time: 2025-07-19T01:33:21.000Z
format: jsx
aliases: [Untitled Artifact, psi_core_system_v3]
---

# Untitled Artifact (Version 3)

**Conversation:** [[Nexus/Conversations/claude/2025/07/Rotational Ψ-Core Dynamics|Rotational Ψ-Core Dynamics]]

## Content

```jsx
import React, { useState, useEffect, useRef } from 'react';

const PsiCoreSystem = () => {
  const canvasRef = useRef(null);
  const animationRef = useRef(null);
  
  // Core state tensors
  const [coreState, setCoreState] = useState({
    rotation: 0,
    bifurcationIndex: 0,
    attractor: { x: 0, y: 0, z: 0 },
    memory: Array(64).fill(0).map((_, i) => ({ 
      index: i, 
      value: Math.sin(i * 0.1), 
      phase: i * Math.PI / 32,
      stability: Math.random()
    })),
    eigenModes: [0.618, 1.414, 2.718, 3.141],
    collapseFactor: 1.0,
    recursionDepth: 0
  });
  
  // Ψ-core rotational dynamics
  const updatePsiCore = (t) => {
    const dt = 0.016; // ~60fps
    
    setCoreState(prev => {
      // Rotational eigenform computation with strong recursive coupling
      const memoryInfluence = prev.memory.slice(0, 8).reduce((sum, mem) => sum + mem.value * mem.stability, 0) / 8;
      const attractorCoupling = Math.sqrt(prev.attractor.x ** 2 + prev.attractor.y ** 2 + prev.attractor.z ** 2);
      const eigenResonance = prev.eigenModes.reduce((sum, mode, i) => sum + Math.sin(prev.rotation * mode + i), 0) * 0.1;
      const bifurcationTurbulence = Math.sin(prev.bifurcationIndex * 7) * Math.cos(prev.bifurcationIndex * 3) * 0.5;
      
      // Base rate modulated by recursive state
      const baseRate = 0.5 + 2.0 * Math.sin(t * 0.03 + memoryInfluence);
      const recursiveFeedback = 1 + memoryInfluence * 2.0 + attractorCoupling * 1.5 + eigenResonance + bifurcationTurbulence;
      const collapseModulation = Math.pow(prev.collapseFactor, 3) * 2.0;
      
      const rotationRate = baseRate * recursiveFeedback * collapseModulation;
      const newRotation = prev.rotation + dt * rotationRate;
      
      // Bifurcation memory indexing with topological wrapping
      const bifurcationRate = 0.05 + 0.02 * Math.sin(t * 0.07);
      const newBifurcationIndex = (prev.bifurcationIndex + bifurcationRate) % (2 * Math.PI);
      
      // Dynamical attractor evolution
      const attractorStrength = 0.1 + 0.05 * Math.cos(t * 0.03);
      const newAttractor = {
        x: prev.attractor.x * 0.98 + attractorStrength * Math.sin(newBifurcationIndex * 3),
        y: prev.attractor.y * 0.98 + attractorStrength * Math.cos(newBifurcationIndex * 2),
        z: prev.attractor.z * 0.98 + attractorStrength * Math.sin(newBifurcationIndex * 5)
      };
      
      // Memory tensor update with recursive collapse
      const newMemory = prev.memory.map((mem, i) => {
        const phaseShift = dt * (1 + 0.1 * newAttractor.x);
        const newPhase = mem.phase + phaseShift;
        const recursiveInfluence = prev.eigenModes[i % 4] * 0.01;
        
        return {
          ...mem,
          value: mem.value * 0.995 + 0.005 * Math.sin(newPhase + newBifurcationIndex),
          phase: newPhase,
          stability: mem.stability * 0.999 + 0.001 * (1 + recursiveInfluence * Math.cos(newRotation))
        };
      });
      
      // Eigenmode evolution through recursive feedback
      const newEigenModes = prev.eigenModes.map((mode, i) => {
        const feedback = newMemory[i * 16].value * 0.01;
        return mode * (1 + feedback * 0.001);
      });
      
      // Collapse factor computation
      const memoryCoherence = newMemory.reduce((sum, mem) => sum + mem.stability, 0) / newMemory.length;
      const newCollapseFactor = 0.9 * prev.collapseFactor + 0.1 * memoryCoherence;
      
      // Recursion depth tracking
      const newRecursionDepth = Math.floor(newBifurcationIndex / (2 * Math.PI)) % 8;
      
      return {
        rotation: newRotation,
        bifurcationIndex: newBifurcationIndex,
        attractor: newAttractor,
        memory: newMemory,
        eigenModes: newEigenModes,
        collapseFactor: newCollapseFactor,
        recursionDepth: newRecursionDepth
      };
    });
  };
  
  // Rendering the topological structure
  const render = (ctx, width, height, state) => {
    ctx.fillStyle = '#000012';
    ctx.fillRect(0, 0, width, height);
    
    const centerX = width / 2;
    const centerY = height / 2;
    const maxRadius = Math.min(width, height) * 0.4;
    
    // Draw modular attractor shell
    ctx.strokeStyle = `hsla(${(state.bifurcationIndex * 57.3) % 360}, 70%, 50%, 0.6)`;
    ctx.lineWidth = 2;
    ctx.beginPath();
    
    const shellPoints = 32;
    for (let i = 0; i <= shellPoints; i++) {
      const angle = (i / shellPoints) * 2 * Math.PI;
      const radius = maxRadius * (0.8 + 0.2 * Math.sin(angle * 3 + state.rotation));
      const x = centerX + radius * Math.cos(angle) + state.attractor.x * 50;
      const y = centerY + radius * Math.sin(angle) + state.attractor.y * 50;
      
      if (i === 0) ctx.moveTo(x, y);
      else ctx.lineTo(x, y);
    }
    ctx.stroke();
    
    // Draw Ψ-core rotation with eigenmode modulation
    const coreRadius = maxRadius * 0.3 * state.collapseFactor;
    
    state.eigenModes.forEach((eigenValue, modeIndex) => {
      ctx.strokeStyle = `hsla(${(modeIndex * 90 + state.rotation * 20) % 360}, 80%, 60%, 0.8)`;
      ctx.lineWidth = 1 + modeIndex * 0.5;
      ctx.beginPath();
      
      const spokes = 8 + modeIndex * 2;
      for (let i = 0; i < spokes; i++) {
        const angle = (i / spokes) * 2 * Math.PI + state.rotation * eigenValue;
        const innerR = coreRadius * 0.3;
        const outerR = coreRadius * (0.7 + 0.3 * Math.sin(angle * (modeIndex + 1)));
        
        const x1 = centerX + innerR * Math.cos(angle);
        const y1 = centerY + innerR * Math.sin(angle);
        const x2 = centerX + outerR * Math.cos(angle);
        const y2 = centerY + outerR * Math.sin(angle);
        
        ctx.moveTo(x1, y1);
        ctx.lineTo(x2, y2);
      }
      ctx.stroke();
    });
    
    // Draw bifurcation memory traces
    ctx.strokeStyle = `hsla(${(state.bifurcationIndex * 114.6) % 360}, 60%, 40%, 0.4)`;
    ctx.lineWidth = 1;
    
    const memoryRadius = maxRadius * 0.15;
    state.memory.slice(0, 16).forEach((mem, i) => {
      const angle = mem.phase;
      const radius = memoryRadius * (0.5 + 0.5 * mem.stability);
      const x = centerX + radius * Math.cos(angle) + state.attractor.z * 20;
      const y = centerY + radius * Math.sin(angle) + state.attractor.x * 20;
      
      ctx.beginPath();
      ctx.arc(x, y, Math.abs(mem.value) * 3 + 1, 0, 2 * Math.PI);
      ctx.fillStyle = `hsla(${(i * 22.5 + mem.phase * 57.3) % 360}, 70%, 50%, ${mem.stability * 0.8})`;
      ctx.fill();
    });
    
    // Central recursion indicator
    ctx.fillStyle = `hsla(${state.recursionDepth * 45}, 90%, 70%, 0.9)`;
    ctx.beginPath();
    ctx.arc(centerX, centerY, 8 + state.recursionDepth * 2, 0, 2 * Math.PI);
    ctx.fill();
  };
  
  // Animation loop
  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    
    const ctx = canvas.getContext('2d');
    let startTime = Date.now();
    
    const animate = () => {
      const currentTime = Date.now();
      const t = (currentTime - startTime) * 0.001;
      
      updatePsiCore(t);
      
      const { width, height } = canvas.getBoundingClientRect();
      canvas.width = width * window.devicePixelRatio;
      canvas.height = height * window.devicePixelRatio;
      ctx.scale(window.devicePixelRatio, window.devicePixelRatio);
      
      render(ctx, width, height, coreState);
      
      animationRef.current = requestAnimationFrame(animate);
    };
    
    animate();
    
    return () => {
      if (animationRef.current) {
        cancelAnimationFrame(animationRef.current);
      }
    };
  }, [coreState.rotation]); // Dependency to trigger re-render
  
  return (
    <div className="w-full h-screen bg-black relative overflow-hidden">
      <canvas
        ref={canvasRef}
        className="w-full h-full"
        style={{ background: 'radial-gradient(circle at center, #000033 0%, #000000 100%)' }}
      />
      
      {/* System metrics overlay */}
      <div className="absolute top-4 left-4 text-green-400 font-mono text-sm space-y-1 opacity-80">
        <div>**Rotation**: {coreState.rotation.toFixed(3)} rad</div>
        <div>**Bifurcation Index**: {coreState.bifurcationIndex.toFixed(3)}</div>
        <div>**Collapse Factor**: {coreState.collapseFactor.toFixed(4)}</div>
        <div>**Recursion Depth**: {coreState.recursionDepth}</div>
        <div>**Attractor Magnitude**: {Math.sqrt(
          coreState.attractor.x ** 2 + 
          coreState.attractor.y ** 2 + 
          coreState.attractor.z ** 2
        ).toFixed(4)}</div>
      </div>
      
      {/* Eigenmode display */}
      <div className="absolute top-4 right-4 text-cyan-400 font-mono text-sm space-y-1 opacity-80">
        <div>**Eigenmode Spectrum**:</div>
        {coreState.eigenModes.map((mode, i) => (
          <div key={i}>λ_{i}: {mode.toFixed(4)}</div>
        ))}
      </div>
      
      {/* Memory coherence indicator */}
      <div className="absolute bottom-4 left-4 text-yellow-400 font-mono text-sm opacity-80">
        <div>**Memory Coherence**: {(coreState.memory.reduce((sum, mem) => sum + mem.stability, 0) / coreState.memory.length).toFixed(4)}</div>
        <div>**Topological Integrity**: {(coreState.collapseFactor * 100).toFixed(1)}%</div>
      </div>
    </div>
  );
};

export default PsiCoreSystem;
```