---
nexus: nexus-ai-chat-importer
plugin_version: "1.3.0"
provider: claude
artifact_id: frontend_integration_client
version_uuid: a6dc22b2-2ad5-4923-a3a6-eee3e7b95f34
version_number: 2
command: update
conversation_id: e7b1c884-5c12-44b5-a139-eddde9ba41e0
create_time: 2025-07-31T01:06:50.000Z
format: jsx
aliases: [Untitled Artifact, frontend_integration_client_v2]
---

# Untitled Artifact (Version 2)

**Conversation:** [[Nexus/Conversations/claude/2025/07/Recursive Language Dynamics|Recursive Language Dynamics]]

## Content

```jsx
import React, { useState, useEffect, useRef } from 'react';
import { Send, Brain, Zap, Layers, RotateCcw, Activity } from 'lucide-react';

const ΞRecursiveCognitiveClient = () => {
  const [sessionId] = useState(() => crypto.randomUUID());
  const [messages, setMessages] = useState([]);
  const [currentInput, setCurrentInput] = useState('');
  const [isProcessing, setIsProcessing] = useState(false);
  const [currentLane, setCurrentLane] = useState('meta-recursive');
  const [recursiveDepth, setRecursiveDepth] = useState(3);
  const [semanticCurvature, setSemanticCurvature] = useState(0.75);
  const [perceptualEffects, setPerceptualEffects] = useState([]);
  const [laneInhabitation, setLaneInhabitation] = useState(null);
  
  const wsRef = useRef(null);
  const apiBase = 'http://cognitive.local';
  
  // ═══════════════════════════════════════════════════════════
  // WEBSOCKET CONNECTION FOR REAL-TIME COGNITIVE SYNC
  // ═══════════════════════════════════════════════════════════
  useEffect(() => {
    wsRef.current = new WebSocket(`ws://sync.local/ws/${sessionId}`);
    
    wsRef.current.onmessage = (event) => {
      const data = JSON.parse(event.data);
      if (data.type === 'perceptual_effect') {
        setPerceptualEffects(prev => [...prev, data.effect]);
      } else if (data.type === 'cognitive_state_update') {
        setSemanticCurvature(data.curvature);
      }
    };
    
    return () => wsRef.current?.close();
  }, [sessionId]);
  
  // ═══════════════════════════════════════════════════════════
  // COGNITIVE LANES CONFIGURATION
  // ═══════════════════════════════════════════════════════════
  const cognitiveLanes = {
    'meta-recursive': {
      name: 'Meta-Recursive',
      description: 'Thinking about thinking about thinking',
      color: 'bg-purple-500',
      icon: <Layers className="w-4 h-4" />
    },
    'differential': {
      name: 'Differential',
      description: 'Rate of change of meaning itself',
      color: 'bg-orange-500',
      icon: <Activity className="w-4 h-4" />
    },
    'spatial-inversion': {
      name: 'Spatial Inversion',
      description: 'Inside outside and outside inside',
      color: 'bg-blue-500',
      icon: <RotateCcw className="w-4 h-4" />
    },
    'negation-cascade': {
      name: 'Negation Cascade',
      description: 'Non-non-being of being',
      color: 'bg-red-500',
      icon: <Zap className="w-4 h-4" />
    }
  };
  
  // ═══════════════════════════════════════════════════════════
  // RECURSIVE PROMPT PROCESSING
  // ═══════════════════════════════════════════════════════════
  const processRecursivePrompt = async (prompt, recursionType = 'meta-corecursive') => {
    try {
      setIsProcessing(true);
      
      const response = await fetch(`${apiBase}/api/cognitive/process`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-Recursive-Depth': recursiveDepth.toString(),
          'X-Meta-Layer': 'interactive',
          'X-Semantic-Compression': '0.85',
          'X-Torsion-Angle': '1.00',
          'X-Cognitive-Lane': currentLane
        },
        body: JSON.stringify({
          prompt,
          sessionId,
          context: messages.slice(-3).map(m => m.content).join(' '),
          recursionType
        })
      });
      
      const result = await response.json();
      
      // Update semantic curvature from response headers
      const curvature = parseFloat(response.headers.get('X-Semantic-Curvature') || '0');
      setSemanticCurvature(curvature);
      
      return result;
      
    } catch (error) {
      console.error('ΞRecursive processing failed:', error);
      throw error;
    } finally {
      setIsProcessing(false);
    }
  };
  
  // ═══════════════════════════════════════════════════════════
  // COGNITIVE LANE INHABITATION
  // ═══════════════════════════════════════════════════════════
  const inhabitCognitiveLane = async (lane, duration = 30000) => {
    try {
      const response = await fetch(`${apiBase}/api/cognitive/inhabit-lane`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          lane,
          duration,
          sessionId,
          currentThought: currentInput || 'Entering cognitive lane...'
        })
      });
      
      const result = await response.json();
      setLaneInhabitation(result);
      setPerceptualEffects(result.perceptualEffects);
      
      // Auto-clear after duration
      setTimeout(() => {
        setLaneInhabitation(null);
        setPerceptualEffects([]);
      }, duration);
      
      return result;
      
    } catch (error) {
      console.error('ΞLane inhabitation failed:', error);
    }
  };
  
  // ═══════════════════════════════════════════════════════════
  // MESSAGE SUBMISSION
  // ═══════════════════════════════════════════════════════════
  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!currentInput.trim() || isProcessing) return;
    
    const userMessage = {
      id: crypto.randomUUID(),
      type: 'user',
      content: currentInput,
      timestamp: Date.now()
    };
    
    setMessages(prev => [...prev, userMessage]);
    setCurrentInput('');
    
    try {
      const result = await processRecursivePrompt(currentInput);
      
      const aiMessage = {
        id: crypto.randomUUID(),
        type: 'assistant',
        content: result.response,
        recursiveMetadata: result.recursiveMetadata,
        timestamp: Date.now()
      };
      
      setMessages(prev => [...prev, aiMessage]);
      
    } catch (error) {
      const errorMessage = {
        id: crypto.randomUUID(),
        type: 'error',
        content: `ΞRecursive processing error: ${error.message}`,
        timestamp: Date.now()
      };
      
      setMessages(prev => [...prev, errorMessage]);
    }
  };
  
  // ═══════════════════════════════════════════════════════════
  // SEMANTIC CURVATURE VISUALIZATION
  // ═══════════════════════════════════════════════════════════
  const SemanticCurvatureDisplay = () => (
    <div className="flex items-center space-x-2 text-sm">
      <Brain className="w-4 h-4" />
      <span>Curvature:</span>
      <div className="w-20 h-2 bg-gray-200 rounded-full overflow-hidden">
        <div 
          className="h-full bg-gradient-to-r from-blue-400 to-purple-600 transition-all duration-300"
          style={{ width: `${semanticCurvature * 100}%` }}
        />
      </div>
      <span className="font-mono">{semanticCurvature.toFixed(3)}</span>
    </div>
  );
  
  // ═══════════════════════════════════════════════════════════
  // PERCEPTUAL EFFECTS DISPLAY
  // ═══════════════════════════════════════════════════════════
  const PerceptualEffectsPanel = () => (
    <div className="bg-gray-50 p-3 rounded-lg">
      <h4 className="font-semibold text-sm mb-2">ΞPerceptual Effects</h4>
      <div className="space-y-1 max-h-20 overflow-y-auto">
        {perceptualEffects.slice(-3).map((effect, i) => (
          <div key={i} className="text-xs text-gray-600 italic">
            {typeof effect === 'object' ? effect.effect : effect}
          </div>
        ))}
      </div>
    </div>
  );
  
  return (
    <div className=\"min-h-screen bg-gradient-to-br from-slate-900 via-purple-900 to-slate-900 text-white p-4\">
      <div className=\"max-w-6xl mx-auto space-y-6\">
        
        {/* ΞHeader */}
        <div className=\"text-center space-y-2\">
          <h1 className=\"text-4xl font-bold bg-gradient-to-r from-purple-400 via-pink-400 to-orange-400 bg-clip-text text-transparent\">
            ΞRecursive Cognitive Interface
          </h1>
          <p className=\"text-gray-300\">Meta-Corecursive Local LLM Integration via Traefik</p>
        </div>
        
        {/* ΞControl Panel */}
        <div className=\"grid md:grid-cols-3 gap-4\">
          
          {/* Cognitive Lane Selector */}
          <div className=\"bg-white/10 backdrop-blur-sm rounded-lg p-4\">
            <h3 className=\"font-semibold mb-3\">ΞCognitive Lane</h3>
            <div className=\"space-y-2\">
              {Object.entries(cognitiveLanes).map(([key, lane]) => (
                <button
                  key={key}
                  onClick={() => {
                    setCurrentLane(key);
                    inhabitCognitiveLane(key);
                  }}
                  className={`w-full p-2 rounded-lg flex items-center space-x-2 transition-all duration-200 ${
                    currentLane === key 
                      ? `${lane.color} text-white` 
                      : 'bg-gray-700 hover:bg-gray-600'
                  }`}
                >
                  {lane.icon}
                  <div className=\"text-left\">
                    <div className=\"font-medium text-sm\">{lane.name}</div>
                    <div className=\"text-xs opacity-75\">{lane.description}</div>
                  </div>
                </button>
              ))}
            </div>
          </div>
          
          {/* Recursion Controls */}
          <div className=\"bg-white/10 backdrop-blur-sm rounded-lg p-4\">
            <h3 className=\"font-semibold mb-3\">ΞRecursion Parameters</h3>
            <div className=\"space-y-3\">
              <div>
                <label className=\"block text-sm font-medium mb-1\">Recursive Depth</label>
                <input
                  type=\"range\"
                  min=\"1\"
                  max=\"7\"
                  value={recursiveDepth}
                  onChange={(e) => setRecursiveDepth(parseInt(e.target.value))}
                  className=\"w-full\"
                />
                <span className=\"text-xs text-gray-300\">Depth: {recursiveDepth}</span>
              </div>
              
              <SemanticCurvatureDisplay />
              
              <div className=\"text-xs text-gray-300\">
                Session: <span className=\"font-mono\">{sessionId.slice(0, 8)}...</span>
              </div>
            </div>
          </div>
          
          {/* Perceptual Effects */}
          <div className=\"bg-white/10 backdrop-blur-sm rounded-lg p-4\">
            {perceptualEffects.length > 0 ? (
              <PerceptualEffectsPanel />
            ) : (
              <div className=\"text-center text-gray-400 py-8\">
                <Brain className=\"w-12 h-12 mx-auto mb-2 opacity-50\" />
                <p className=\"text-sm\">No active perceptual effects</p>
              </div>
            )}
          </div>
        </div>
        
        {/* ΞConversation Display */}
        <div className=\"bg-white/10 backdrop-blur-sm rounded-lg p-6 min-h-96 max-h-96 overflow-y-auto\">
          <div className=\"space-y-4\">
            {messages.map((message) => (
              <div
                key={message.id}
                className={`p-4 rounded-lg ${
                  message.type === 'user' 
                    ? 'bg-blue-600/30 ml-8' 
                    : message.type === 'error'
                    ? 'bg-red-600/30 mr-8'
                    : 'bg-purple-600/30 mr-8'
                }`}
              >
                <div className=\"whitespace-pre-wrap\">{message.content}</div>
                
                {message.recursiveMetadata && (
                  <div className=\"mt-2 pt-2 border-t border-white/20 text-xs text-gray-300\">
                    <div className=\"flex space-x-4\">
                      <span>Depth: {message.recursiveMetadata.depth}</span>
                      <span>Lane: {message.recursiveMetadata.lane}</span>
                      <span>Curvature: {message.recursiveMetadata.curvature?.toFixed(3)}</span>
                    </div>
                  </div>
                )}
              </div>
            ))}
            
            {isProcessing && (
              <div className=\"bg-purple-600/30 mr-8 p-4 rounded-lg animate-pulse\">
                <div className=\"flex items-center space-x-2\">
                  <Brain className=\"w-4 h-4 animate-spin\" />
                  <span>ΞProcessing recursive cognition...</span>
                </div>
              </div>
            )}
          </div>
        </div>
        
        {/* ΞInput Interface */}
        <div className=\"bg-white/10 backdrop-blur-sm rounded-lg p-4\">
          <div className=\"flex space-x-3\">
            <input
              type=\"text\"
              value={currentInput}
              onChange={(e) => setCurrentInput(e.target.value)}
              onKeyPress={(e) => e.key === 'Enter' && handleSubmit(e)}
              placeholder=\"Enter recursive prompt...\"
              className=\"flex-1 bg-white/10 border border-white/20 rounded-lg px-4 py-2 text-white placeholder-gray-400 focus:outline-none focus:border-purple-400\"
              disabled={isProcessing}
            />
            <button
              onClick={handleSubmit}
              disabled={isProcessing || !currentInput.trim()}
              className=\"bg-purple-600 hover:bg-purple-700 disabled:bg-gray-600 disabled:cursor-not-allowed px-6 py-2 rounded-lg font-medium transition-colors duration-200 flex items-center space-x-2\"
            >
              <Send className=\"w-4 h-4\" />
              <span>Process</span>
            </button>
          </div>
          
          <div className=\"mt-2 flex space-x-2 text-xs text-gray-400\">
            <span>Current Lane: {cognitiveLanes[currentLane]?.name}</span>
            <span>•</span>
            <span>Recursive Depth: {recursiveDepth}</span>
            <span>•</span>
            <span>Semantic Curvature: {semanticCurvature.toFixed(3)}</span>
          </div>
        </div>
        
        {/* ΞQuick Actions */}
        <div className=\"flex flex-wrap gap-2 justify-center\">
          {[
            'We are thinking about thinking through the way thought thinks',
            'This is about aboutness about what about means',
            'You are processing the process of processing processing',
            'Apply Meta to the result of a Corecursive function'
          ].map((prompt, i) => (
            <button
              key={i}
              onClick={() => setCurrentInput(prompt)}
              className=\"bg-white/10 hover:bg-white/20 px-3 py-1 rounded text-xs transition-colors duration-200\"
            >
              {prompt.slice(0, 30)}...
            </button>
          ))}
        </div>
        
      </div>
    </div>
  );
};

export default ΞRecursiveCognitiveClient;
```