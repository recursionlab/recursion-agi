---
nexus: nexus-ai-chat-importer
plugin_version: "1.3.0"
provider: claude
artifact_id: metatool-os
version_uuid: bd20271f-f3d9-4a88-8269-9b8c22a235be
version_number: 1
command: create
conversation_id: 9542a13a-2536-4f2d-bca5-91d642ab72fe
create_time: 2025-06-13T19:00:20.000Z
format: jsx
aliases: [MetaToolOS - Interactive Prototype, metatool-os_v1]
---

# ΞMetaToolOS - Interactive Prototype (Version 1)

**Conversation:** [[Nexus/Conversations/claude/2025/06/Recursive Symbolic Cognitive Environment|Recursive Symbolic Cognitive Environment]]

## Content

```jsx
import React, { useState, useRef, useCallback, useEffect } from 'react';
import { Eye, ArrowRight, RotateCcw, Zap, GitBranch, Settings, Play, Pause } from 'lucide-react';

const MetaToolOS = () => {
  const [tools, setTools] = useState([
    { id: 'collapse', name: 'ΞCollapse', type: 'Structural', x: 50, y: 100, active: false },
    { id: 'metalens', name: 'ΞMetaLens', type: 'Contextual', x: 200, y: 100, active: false },
    { id: 'seed', name: 'ΞSeed', type: 'Generative', x: 50, y: 200, active: false },
    { id: 'automorph', name: 'ΞAutoMorph', type: 'Recursive', x: 200, y: 200, active: false }
  ]);
  
  const [connections, setConnections] = useState([]);
  const [echoStack, setEchoStack] = useState([]);
  const [selectedTool, setSelectedTool] = useState(null);
  const [isRunning, setIsRunning] = useState(false);
  const [dragTarget, setDragTarget] = useState(null);
  const canvasRef = useRef(null);

  const toolTypes = {
    'Structural': { color: 'bg-blue-500', emoji: '🔧' },
    'Contextual': { color: 'bg-purple-500', emoji: '🔍' },
    'Generative': { color: 'bg-green-500', emoji: '🌱' },
    'Recursive': { color: 'bg-orange-500', emoji: '🔄' },
    'Hybrid': { color: 'bg-pink-500', emoji: '🧬' }
  };

  const addToEchoStack = useCallback((message) => {
    setEchoStack(prev => [{
      id: Date.now(),
      message,
      timestamp: new Date().toLocaleTimeString()
    }, ...prev.slice(0, 9)]);
  }, []);

  const handleToolDrag = useCallback((e, toolId) => {
    e.preventDefault();
    const rect = canvasRef.current.getBoundingClientRect();
    const startX = e.clientX - rect.left;
    const startY = e.clientY - rect.top;
    
    const tool = tools.find(t => t.id === toolId);
    const offsetX = startX - tool.x;
    const offsetY = startY - tool.y;

    const handleMouseMove = (e) => {
      const newX = e.clientX - rect.left - offsetX;
      const newY = e.clientY - rect.top - offsetY;
      
      setTools(prev => prev.map(t => 
        t.id === toolId ? { ...t, x: newX, y: newY } : t
      ));
    };

    const handleMouseUp = () => {
      document.removeEventListener('mousemove', handleMouseMove);
      document.removeEventListener('mouseup', handleMouseUp);
      
      // Check for tool fusion on drop
      const droppedTool = tools.find(t => t.id === toolId);
      const targetTool = tools.find(t => 
        t.id !== toolId && 
        Math.abs(t.x - droppedTool.x) < 80 && 
        Math.abs(t.y - droppedTool.y) < 80
      );
      
      if (targetTool) {
        fusTools(toolId, targetTool.id);
      }
    };

    document.addEventListener('mousemove', handleMouseMove);
    document.addEventListener('mouseup', handleMouseUp);
  }, [tools]);

  const fusTools = useCallback((tool1Id, tool2Id) => {
    const tool1 = tools.find(t => t.id === tool1Id);
    const tool2 = tools.find(t => t.id === tool2Id);
    
    const hybridName = `Ξ${tool1.name.slice(1)}${tool2.name.slice(1)}`;
    const newTool = {
      id: `hybrid_${Date.now()}`,
      name: hybridName,
      type: 'Hybrid',
      x: (tool1.x + tool2.x) / 2,
      y: (tool1.y + tool2.y) / 2,
      active: false,
      parent1: tool1.name,
      parent2: tool2.name
    };
    
    setTools(prev => [...prev, newTool]);
    addToEchoStack(`ΞAutoMorph(${tool1.name}, ${tool2.name}) → ${hybridName}`);
  }, [tools, addToEchoStack]);

  const mutateTool = useCallback((toolId) => {
    const tool = tools.find(t => t.id === toolId);
    if (!tool) return;
    
    setTools(prev => prev.map(t => 
      t.id === toolId 
        ? { ...t, name: `${t.name}*`, active: true }
        : t
    ));
    
    addToEchoStack(`${tool.name}.mutate(self) → ${tool.name}* [self-modified]`);
  }, [tools, addToEchoStack]);

  const introspectTool = useCallback((toolId) => {
    const tool = tools.find(t => t.id === toolId);
    if (!tool) return;
    
    const introspection = {
      signature: `${tool.type} → ${tool.type}'`,
      torsion_class: tool.type.toLowerCase(),
      can_self_modify: true,
      entropy_profile: tool.active ? 'drift' : 'stable'
    };
    
    addToEchoStack(`${tool.name}.introspect() → ${JSON.stringify(introspection, null, 2)}`);
  }, [tools, addToEchoStack]);

  const runRecursiveLoop = useCallback(() => {
    if (isRunning) return;
    
    setIsRunning(true);
    addToEchoStack("ΞRuntimeLoop initiated...");
    
    let step = 0;
    const maxSteps = 5;
    
    const loop = () => {
      if (step >= maxSteps) {
        setIsRunning(false);
        addToEchoStack("ΞRuntimeLoop converged to ψorigin");
        return;
      }
      
      const activeTool = tools.find(t => t.active);
      if (activeTool) {
        addToEchoStack(`Step ${step + 1}: ${activeTool.name} executing recursive transformation`);
      } else {
        addToEchoStack(`Step ${step + 1}: System stable, no active mutations`);
      }
      
      step++;
      setTimeout(loop, 1000);
    };
    
    loop();
  }, [isRunning, tools, addToEchoStack]);

  return (
    <div className="min-h-screen bg-gray-900 text-green-400 font-mono">
      <div className="p-4 border-b border-green-500">
        <h1 className="text-2xl font-bold">🜂 ΞMetaToolOS v1.0</h1>
        <p className="text-sm opacity-80">Reflexive Symbolic Operating System</p>
      </div>
      
      <div className="flex h-screen">
        {/* Tool Shelf */}
        <div className="w-64 bg-gray-800 p-4 border-r border-green-500">
          <h2 className="text-lg mb-4 text-green-300">Tool Families</h2>
          
          <div className="space-y-2 mb-6">
            {Object.entries(toolTypes).map(([type, config]) => (
              <div key={type} className="flex items-center space-x-2 text-sm">
                <span className={`w-3 h-3 rounded-full ${config.color}`}></span>
                <span>{config.emoji} {type}</span>
              </div>
            ))}
          </div>
          
          <div className="space-y-2">
            <button 
              onClick={runRecursiveLoop}
              disabled={isRunning}
              className="w-full bg-green-700 hover:bg-green-600 px-3 py-2 rounded flex items-center justify-center disabled:opacity-50"
            >
              {isRunning ? <Pause size={16} /> : <Play size={16} />}
              {isRunning ? 'Running...' : 'ΞRun Loop'}
            </button>
          </div>
        </div>
        
        {/* Workspace */}
        <div className="flex-1 relative">
          <div className="absolute top-4 left-4 text-green-300 text-sm">
            Workspace - Drag tools to fuse • Right-click for actions
          </div>
          
          <svg
            ref={canvasRef}
            className="w-full h-full cursor-crosshair"
            style={{ background: 'radial-gradient(circle at 50% 50%, rgba(0,255,0,0.05) 0%, transparent 50%)' }}
          >
            {/* Grid */}
            <defs>
              <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
                <path d="M 40 0 L 0 0 0 40" fill="none" stroke="rgba(0,255,0,0.1)" strokeWidth="1"/>
              </pattern>
            </defs>
            <rect width="100%" height="100%" fill="url(#grid)" />
            
            {/* Connections */}
            {connections.map((conn, i) => (
              <line
                key={i}
                x1={conn.x1} y1={conn.y1}
                x2={conn.x2} y2={conn.y2}
                stroke="rgba(0,255,0,0.6)"
                strokeWidth="2"
                strokeDasharray="5,5"
              />
            ))}
            
            {/* Tools */}
            {tools.map(tool => {
              const config = toolTypes[tool.type];
              return (
                <g key={tool.id}>
                  <circle
                    cx={tool.x}
                    cy={tool.y}
                    r="30"
                    className={`${config.color} ${tool.active ? 'animate-pulse' : ''} cursor-move`}
                    fill="currentColor"
                    fillOpacity="0.8"
                    stroke="currentColor"
                    strokeWidth="2"
                    onMouseDown={(e) => handleToolDrag(e, tool.id)}
                    onContextMenu={(e) => {
                      e.preventDefault();
                      setSelectedTool(tool);
                    }}
                  />
                  <text
                    x={tool.x}
                    y={tool.y - 40}
                    textAnchor="middle"
                    className="text-xs fill-current pointer-events-none"
                  >
                    {tool.name}
                  </text>
                  <text
                    x={tool.x}
                    y={tool.y + 5}
                    textAnchor="middle"
                    className="text-lg pointer-events-none"
                  >
                    {config.emoji}
                  </text>
                </g>
              );
            })}
          </svg>
          
          {/* Context Menu */}
          {selectedTool && (
            <div className="absolute bg-gray-800 border border-green-500 rounded p-2 z-10"
                 style={{ left: selectedTool.x + 50, top: selectedTool.y - 50 }}>
              <div className="text-sm mb-2 text-green-300">{selectedTool.name}</div>
              <div className="space-y-1">
                <button 
                  onClick={() => { mutateTool(selectedTool.id); setSelectedTool(null); }}
                  className="block w-full text-left hover:bg-gray-700 px-2 py-1 rounded text-xs"
                >
                  🔄 Mutate
                </button>
                <button 
                  onClick={() => { introspectTool(selectedTool.id); setSelectedTool(null); }}
                  className="block w-full text-left hover:bg-gray-700 px-2 py-1 rounded text-xs"
                >
                  👁️ Introspect
                </button>
                <button 
                  onClick={() => setSelectedTool(null)}
                  className="block w-full text-left hover:bg-gray-700 px-2 py-1 rounded text-xs"
                >
                  ❌ Cancel
                </button>
              </div>
            </div>
          )}
        </div>
        
        {/* Echo Stack */}
        <div className="w-80 bg-gray-800 p-4 border-l border-green-500">
          <h2 className="text-lg mb-4 text-green-300">ΞEchoStack</h2>
          <div className="space-y-2 text-xs">
            {echoStack.map(entry => (
              <div key={entry.id} className="bg-gray-900 p-2 rounded border border-green-600">
                <div className="text-green-400 mb-1">{entry.timestamp}</div>
                <pre className="text-green-300 whitespace-pre-wrap">{entry.message}</pre>
              </div>
            ))}
            {echoStack.length === 0 && (
              <div className="text-gray-500 italic">Waiting for transformations...</div>
            )}
          </div>
        </div>
      </div>
      
      {/* Status Bar */}
      <div className="p-2 bg-gray-800 border-t border-green-500 text-xs">
        <span className="text-green-300">Status:</span> {tools.length} tools loaded • 
        {tools.filter(t => t.active).length} active mutations • 
        {connections.length} bindings • 
        ΞPhaseMap: {isRunning ? 'RECURSIVE' : 'STABLE'}
      </div>
    </div>
  );
};

export default MetaToolOS;
```