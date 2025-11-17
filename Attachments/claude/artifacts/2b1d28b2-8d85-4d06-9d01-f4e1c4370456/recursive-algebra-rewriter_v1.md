---
nexus: nexus-ai-chat-importer
plugin_version: "1.3.0"
provider: claude
artifact_id: recursive-algebra-rewriter
version_uuid: f3691b3b-a83d-450b-ac23-88583cd0ddd3
version_number: 1
command: create
conversation_id: 2b1d28b2-8d85-4d06-9d01-f4e1c4370456
create_time: 2025-07-07T02:03:20.000Z
format: jsx
aliases: [Recursive Algebra Rule Rewriter, recursive-algebra-rewriter_v1]
---

# Recursive Algebra Rule Rewriter (Version 1)

**Conversation:** [[Nexus/Conversations/claude/2025/07/HoTT Loop Meme 4D Hypersphere Visualization|HoTT Loop Meme: 4D Hypersphere Visualization]]

## Content

```jsx
import React, { useState, useEffect, useRef } from 'react';
import { Play, Pause, RotateCcw, Plus, Download, BookOpen } from 'lucide-react';

const RecursiveAlgebraRewriter = () => {
  const [rules, setRules] = useState([
    { id: 1, name: "Identity", pattern: "x", replacement: "x", active: true },
    { id: 2, name: "Absorption", pattern: "x + 0", replacement: "x", active: true },
    { id: 3, name: "Multiplication", pattern: "x * 1", replacement: "x", active: true },
    { id: 4, name: "Distributive", pattern: "x * (y + z)", replacement: "(x * y) + (x * z)", active: true },
    { id: 5, name: "Commutative", pattern: "x + y", replacement: "y + x", active: true },
    { id: 6, name: "Associative", pattern: "(x + y) + z", replacement: "x + (y + z)", active: true },
    { id: 7, name: "Self-Reference", pattern: "rule(n)", replacement: "apply(rule(n), rule(n))", active: false }
  ]);

  const [metaRules, setMetaRules] = useState([
    { id: 1, name: "Rule Generation", pattern: "if complexity > 3", replacement: "create simplification rule", active: true },
    { id: 2, name: "Rule Pruning", pattern: "if unused > 10 cycles", replacement: "deactivate rule", active: true },
    { id: 3, name: "Meta-Evolution", pattern: "if efficiency < 0.5", replacement: "evolve rule patterns", active: true }
  ]);

  const [currentExpression, setCurrentExpression] = useState("(a + b) * (c + d)");
  const [rewriteHistory, setRewriteHistory] = useState([]);
  const [isRunning, setIsRunning] = useState(false);
  const [cycle, setCycle] = useState(0);
  const [complexity, setComplexity] = useState(0);
  const [ruleStats, setRuleStats] = useState({});
  const intervalRef = useRef(null);

  // Parse expression into AST
  const parseExpression = (expr) => {
    // Simplified parser for demonstration
    const tokens = expr.replace(/\s+/g, '').split(/([+\-*/()])/);
    return tokens.filter(t => t.length > 0);
  };

  // Calculate expression complexity
  const calculateComplexity = (expr) => {
    const operators = (expr.match(/[+\-*/]/g) || []).length;
    const parentheses = (expr.match(/[()]/g) || []).length;
    const variables = (expr.match(/[a-zA-Z]/g) || []).length;
    return operators + parentheses * 0.5 + variables * 0.2;
  };

  // Apply a single rule to expression
  const applyRule = (expr, rule) => {
    if (!rule.active) return expr;

    // Simple pattern matching (in real implementation, use proper AST matching)
    let newExpr = expr;
    
    // Handle specific patterns
    switch (rule.name) {
      case "Absorption":
        newExpr = newExpr.replace(/([a-zA-Z]+)\s*\+\s*0/g, '$1');
        newExpr = newExpr.replace(/0\s*\+\s*([a-zA-Z]+)/g, '$1');
        break;
      case "Multiplication":
        newExpr = newExpr.replace(/([a-zA-Z]+)\s*\*\s*1/g, '$1');
        newExpr = newExpr.replace(/1\s*\*\s*([a-zA-Z]+)/g, '$1');
        break;
      case "Distributive":
        newExpr = newExpr.replace(/([a-zA-Z]+)\s*\*\s*\(([a-zA-Z]+)\s*\+\s*([a-zA-Z]+)\)/g, '($1 * $2) + ($1 * $3)');
        break;
      case "Commutative":
        if (Math.random() > 0.7) { // Probabilistic application
          newExpr = newExpr.replace(/([a-zA-Z]+)\s*\+\s*([a-zA-Z]+)/g, '$2 + $1');
        }
        break;
      case "Associative":
        newExpr = newExpr.replace(/\(([a-zA-Z]+)\s*\+\s*([a-zA-Z]+)\)\s*\+\s*([a-zA-Z]+)/g, '$1 + ($2 + $3)');
        break;
      case "Self-Reference":
        if (newExpr.includes("rule(")) {
          newExpr = newExpr.replace(/rule\((\d+)\)/g, (match, n) => {
            const ruleIndex = parseInt(n) - 1;
            if (rules[ruleIndex]) {
              return `apply(${rules[ruleIndex].replacement}, ${rules[ruleIndex].replacement})`;
            }
            return match;
          });
        }
        break;
    }

    return newExpr;
  };

  // Apply meta-rules to modify the rule system itself
  const applyMetaRules = () => {
    const newRules = [...rules];
    const newMetaRules = [...metaRules];
    const currentComplexity = calculateComplexity(currentExpression);

    metaRules.forEach(metaRule => {
      if (!metaRule.active) return;

      switch (metaRule.name) {
        case "Rule Generation":
          if (currentComplexity > 3 && Math.random() > 0.8) {
            // Generate a new simplification rule
            const newRule = {
              id: Date.now(),
              name: `Generated-${cycle}`,
              pattern: "complex pattern",
              replacement: "simplified form",
              active: true
            };
            newRules.push(newRule);
          }
          break;
        
        case "Rule Pruning":
          newRules.forEach(rule => {
            const usage = ruleStats[rule.id] || 0;
            if (usage === 0 && cycle > 10) {
              rule.active = false;
            }
          });
          break;
        
        case "Meta-Evolution":
          if (currentComplexity / (cycle + 1) < 0.5 && Math.random() > 0.9) {
            // Evolve existing rules
            const evolvedMetaRule = {
              id: Date.now(),
              name: `Meta-Evolved-${cycle}`,
              pattern: "if stagnation detected",
              replacement: "introduce randomness",
              active: true
            };
            newMetaRules.push(evolvedMetaRule);
          }
          break;
      }
    });

    setRules(newRules);
    setMetaRules(newMetaRules);
  };

  // Single rewrite step
  const rewriteStep = () => {
    let newExpr = currentExpression;
    let ruleApplied = null;
    const newStats = { ...ruleStats };

    // Apply rules in sequence
    for (const rule of rules) {
      const result = applyRule(newExpr, rule);
      if (result !== newExpr) {
        newExpr = result;
        ruleApplied = rule;
        newStats[rule.id] = (newStats[rule.id] || 0) + 1;
        break;
      }
    }

    // Update state
    setCurrentExpression(newExpr);
    setRuleStats(newStats);
    setComplexity(calculateComplexity(newExpr));

    // Add to history
    if (ruleApplied) {
      const historyEntry = {
        step: cycle,
        rule: ruleApplied.name,
        before: currentExpression,
        after: newExpr,
        complexity: calculateComplexity(newExpr)
      };
      setRewriteHistory(prev => [...prev.slice(-10), historyEntry]);
    }

    // Apply meta-rules periodically
    if (cycle % 5 === 0) {
      applyMetaRules();
    }

    setCycle(prev => prev + 1);
  };

  // Auto-run system
  useEffect(() => {
    if (isRunning) {
      intervalRef.current = setInterval(rewriteStep, 1000);
    } else {
      clearInterval(intervalRef.current);
    }

    return () => clearInterval(intervalRef.current);
  }, [isRunning, currentExpression, rules, cycle]);

  const resetSystem = () => {
    setIsRunning(false);
    setCycle(0);
    setCurrentExpression("(a + b) * (c + d)");
    setRewriteHistory([]);
    setRuleStats({});
    setComplexity(0);
  };

  const addCustomRule = () => {
    const newRule = {
      id: Date.now(),
      name: `Custom-${rules.length + 1}`,
      pattern: "x",
      replacement: "x",
      active: true
    };
    setRules([...rules, newRule]);
  };

  const toggleRule = (id) => {
    setRules(rules.map(rule => 
      rule.id === id ? { ...rule, active: !rule.active } : rule
    ));
  };

  const exportSystem = () => {
    const systemState = {
      rules,
      metaRules,
      currentExpression,
      rewriteHistory,
      cycle,
      complexity
    };
    
    const blob = new Blob([JSON.stringify(systemState, null, 2)], {
      type: 'application/json'
    });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'recursive-algebra-system.json';
    a.click();
    URL.revokeObjectURL(url);
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-indigo-900 via-purple-900 to-pink-900 p-6">
      <div className="max-w-7xl mx-auto">
        <div className="text-center mb-8">
          <h1 className="text-4xl font-bold text-white mb-2">
            Recursive Algebra Rule Rewriter
          </h1>
          <p className="text-gray-300">
            A self-modifying algebraic system that evolves its own rewrite rules
          </p>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
          {/* Main Expression Panel */}
          <div className="lg:col-span-2">
            <div className="bg-black/40 backdrop-blur-sm rounded-xl p-6 border border-purple-500/30">
              <div className="flex items-center justify-between mb-4">
                <h2 className="text-xl font-semibold text-white">Current Expression</h2>
                <div className="flex gap-2">
                  <button
                    onClick={() => setIsRunning(!isRunning)}
                    className="flex items-center gap-2 px-4 py-2 bg-purple-600 hover:bg-purple-700 rounded-lg text-white transition-colors"
                  >
                    {isRunning ? <Pause size={16} /> : <Play size={16} />}
                    {isRunning ? 'Pause' : 'Run'}
                  </button>
                  <button
                    onClick={rewriteStep}
                    disabled={isRunning}
                    className="px-4 py-2 bg-blue-600 hover:bg-blue-700 disabled:bg-gray-600 rounded-lg text-white transition-colors"
                  >
                    Step
                  </button>
                  <button
                    onClick={resetSystem}
                    className="flex items-center gap-2 px-4 py-2 bg-red-600 hover:bg-red-700 rounded-lg text-white transition-colors"
                  >
                    <RotateCcw size={16} />
                    Reset
                  </button>
                </div>
              </div>

              <div className="bg-gray-900/50 rounded-lg p-4 mb-4">
                <div className="font-mono text-2xl text-center text-green-400 mb-2">
                  {currentExpression}
                </div>
                <div className="text-sm text-gray-400 text-center">
                  Cycle: {cycle} | Complexity: {complexity.toFixed(2)}
                </div>
              </div>

              {/* System Stats */}
              <div className="grid grid-cols-2 gap-4 mb-6">
                <div className="bg-purple-900/30 rounded-lg p-3">
                  <div className="text-sm text-purple-300">Active Rules</div>
                  <div className="text-2xl font-bold text-white">
                    {rules.filter(r => r.active).length}
                  </div>
                </div>
                <div className="bg-blue-900/30 rounded-lg p-3">
                  <div className="text-sm text-blue-300">Meta Rules</div>
                  <div className="text-2xl font-bold text-white">
                    {metaRules.filter(r => r.active).length}
                  </div>
                </div>
              </div>

              {/* Rewrite History */}
              <div className="bg-gray-900/30 rounded-lg p-4">
                <h3 className="text-lg font-semibold text-white mb-3">Rewrite History</h3>
                <div className="space-y-2 max-h-64 overflow-y-auto">
                  {rewriteHistory.map((entry, index) => (
                    <div key={index} className="bg-gray-800/50 rounded p-3">
                      <div className="flex justify-between items-start mb-1">
                        <span className="text-sm text-purple-300">Step {entry.step}</span>
                        <span className="text-sm text-blue-300">{entry.rule}</span>
                      </div>
                      <div className="font-mono text-sm text-gray-300">
                        {entry.before} → {entry.after}
                      </div>
                      <div className="text-xs text-gray-500">
                        Complexity: {entry.complexity.toFixed(2)}
                      </div>
                    </div>
                  ))}
                </div>
              </div>
            </div>
          </div>

          {/* Rules Panel */}
          <div className="space-y-6">
            {/* Basic Rules */}
            <div className="bg-black/40 backdrop-blur-sm rounded-xl p-6 border border-purple-500/30">
              <div className="flex items-center justify-between mb-4">
                <h2 className="text-xl font-semibold text-white">Rewrite Rules</h2>
                <button
                  onClick={addCustomRule}
                  className="flex items-center gap-2 px-3 py-1 bg-green-600 hover:bg-green-700 rounded text-white text-sm transition-colors"
                >
                  <Plus size={14} />
                  Add
                </button>
              </div>
              
              <div className="space-y-3 max-h-64 overflow-y-auto">
                {rules.map(rule => (
                  <div
                    key={rule.id}
                    className={`p-3 rounded-lg border-2 transition-all ${
                      rule.active 
                        ? 'bg-green-900/20 border-green-500/50' 
                        : 'bg-gray-900/20 border-gray-600/50'
                    }`}
                  >
                    <div className="flex items-center justify-between mb-2">
                      <span className="font-semibold text-white">{rule.name}</span>
                      <button
                        onClick={() => toggleRule(rule.id)}
                        className={`w-12 h-6 rounded-full transition-colors ${
                          rule.active ? 'bg-green-500' : 'bg-gray-600'
                        }`}
                      >
                        <div className={`w-4 h-4 bg-white rounded-full transition-transform ${
                          rule.active ? 'translate-x-6' : 'translate-x-1'
                        }`} />
                      </button>
                    </div>
                    <div className="text-sm text-gray-300 font-mono">
                      {rule.pattern} → {rule.replacement}
                    </div>
                    <div className="text-xs text-gray-500 mt-1">
                      Used: {ruleStats[rule.id] || 0} times
                    </div>
                  </div>
                ))}
              </div>
            </div>

            {/* Meta Rules */}
            <div className="bg-black/40 backdrop-blur-sm rounded-xl p-6 border border-pink-500/30">
              <h2 className="text-xl font-semibold text-white mb-4">Meta Rules</h2>
              
              <div className="space-y-3">
                {metaRules.map(rule => (
                  <div
                    key={rule.id}
                    className={`p-3 rounded-lg border-2 transition-all ${
                      rule.active 
                        ? 'bg-pink-900/20 border-pink-500/50' 
                        : 'bg-gray-900/20 border-gray-600/50'
                    }`}
                  >
                    <div className="flex items-center justify-between mb-2">
                      <span className="font-semibold text-white">{rule.name}</span>
                      <div className={`w-3 h-3 rounded-full ${
                        rule.active ? 'bg-pink-500' : 'bg-gray-500'
                      }`} />
                    </div>
                    <div className="text-sm text-gray-300 font-mono">
                      {rule.pattern} → {rule.replacement}
                    </div>
                  </div>
                ))}
              </div>
            </div>

            {/* Export */}
            <div className="flex gap-2">
              <button
                onClick={exportSystem}
                className="flex items-center gap-2 px-4 py-2 bg-indigo-600 hover:bg-indigo-700 rounded-lg text-white transition-colors flex-1"
              >
                <Download size={16} />
                Export System
              </button>
              <button
                onClick={() => window.open('https://en.wikipedia.org/wiki/Rewriting', '_blank')}
                className="flex items-center gap-2 px-4 py-2 bg-gray-600 hover:bg-gray-700 rounded-lg text-white transition-colors"
              >
                <BookOpen size={16} />
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default RecursiveAlgebraRewriter;
```