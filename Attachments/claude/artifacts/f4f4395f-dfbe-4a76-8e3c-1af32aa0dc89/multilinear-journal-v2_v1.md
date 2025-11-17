---
nexus: nexus-ai-chat-importer
plugin_version: "1.3.0"
provider: claude
artifact_id: multilinear-journal-v2
version_uuid: e57edcf5-6b68-4dcf-96a3-cece5524eaa7
version_number: 1
command: create
conversation_id: f4f4395f-dfbe-4a76-8e3c-1af32aa0dc89
create_time: 2025-09-22T19:52:31.000Z
format: jsx
aliases: [Multilinear Recursive Journal - Psychic Tool, multilinear-journal-v2_v1]
---

# Multilinear Recursive Journal - Psychic Tool (Version 1)

**Conversation:** [[Nexus/Conversations/claude/2025/09/Recursive psychic journaling tool|Recursive psychic journaling tool]]

## Content

```jsx
import React, { useState, useEffect } from 'react';
import { ChevronRight, ChevronDown, Brain, Eye, Heart, Users, Infinity, Clock, GitBranch, Sparkles, AlertTriangle, Link, Layers, Zap } from 'lucide-react';

const MultilinearJournal = () => {
  const [activeEntry, setActiveEntry] = useState(0);
  const [activeLayer, setActiveLayer] = useState('all');
  const [timelineView, setTimelineView] = useState('actual');
  const [showAIInsights, setShowAIInsights] = useState(false);
  const [expandedSections, setExpandedSections] = useState({
    realEvents: true,
    interpretations: false,
    parallelOutcomes: false,
    failedRealities: false,
    shadowTimelines: false,
    futureEchoes: false,
    hierarchy: true
  });

  const toggleSection = (section) => {
    setExpandedSections(prev => ({
      ...prev,
      [section]: !prev[section]
    }));
  };

  // Sample journal entry with full schema implementation
  const journalEntries = [
    {
      id: "entry_001",
      timestamp: "2024-03-15T14:32:00Z",
      title: "The Dissolution",
      emotionalIntensity: 0.92,
      timeSignature: "branching_point",
      
      realEvents: {
        description: "Seven-year relationship ended. Coffee shop. 3:14 PM. Rain against windows. Her hands trembling around the ceramic mug. The words: 'I can't do this anymore.' The sound of my heartbeat louder than the espresso machine.",
        sensoryMarkers: ["rain pattern on glass", "bitter coffee taste", "fluorescent buzz", "cold metal chair"],
        duration: "47 minutes"
      },
      
      recursiveInterpretations: [
        {
          depth: 1,
          interpretation: "Surface reading: Rejection. Abandonment. Failure.",
          confidence: 0.3
        },
        {
          depth: 2,
          interpretation: "Second pass: Liberation disguised as loss. We were holding each other prisoner.",
          confidence: 0.6
        },
        {
          depth: 3,
          interpretation: "Deep recursion: This ending was written into our beginning. Every 'I love you' contained its own negation.",
          confidence: 0.8
        },
        {
          depth: 4,
          interpretation: "Meta-recursive: The breakup is not an event but a revelation of what always was—two parallel lines mistaking proximity for intersection.",
          confidence: 0.95
        }
      ],
      
      parallelOutcomes: [
        {
          timeline: "alpha",
          description: "I fight for us. Therapy. We marry in autumn. Two kids. Quiet resentment. Divorce at 45.",
          probability: 0.34,
          emotionalValence: -0.2
        },
        {
          timeline: "beta",
          description: "I leave first. She chases. Passionate reconciliation. Burn bright, burn out in 6 months.",
          probability: 0.15,
          emotionalValence: 0.4
        },
        {
          timeline: "gamma",
          description: "We become friends. Real friends. She introduces me to my future wife at her wedding.",
          probability: 0.08,
          emotionalValence: 0.7
        }
      ],
      
      failedRealities: [
        "The timeline where I proposed last Christmas—ring still in drawer",
        "The world where her depression lifted in time",
        "The reality where we were different people who could love without consuming",
        "The universe where timing aligned—met five years later, five years wiser"
      ],
      
      shadowTimelines: [
        {
          avoided: "Saying the cruel thing that would make her hate me enough to leave easily",
          reason: "Chose pain over cruelty",
          cost: 0.7
        },
        {
          avoided: "The grand gesture—showing up at her work with flowers",
          reason: "Recognized manipulation disguised as romance",
          cost: 0.3
        },
        {
          avoided: "Complete emotional collapse in public",
          reason: "Some dignities we keep for ourselves",
          cost: 0.9
        }
      ],
      
      futureEchoes: [
        {
          echo: "Three years hence: Grateful tears at 2 AM, finally understanding what she saved us from",
          certainty: 0.8
        },
        {
          echo: "Six months: Meeting someone at a bookstore, feeling possibility again",
          certainty: 0.6
        },
        {
          echo: "Ten years: Our paths cross. We smile like old soldiers who survived the same war.",
          certainty: 0.4
        }
      ],
      
      hierarchy: {
        level1_sensory: {
          data: ["rain frequency: 72 drops/min", "ambient temp: 67°F", "heart rate: 95bpm rising to 130bpm", "breathing: shallow thoracic", "pupil dilation: marked"],
          tags: ["somatic", "environmental", "physiological"]
        },
        level2_emotional: {
          data: "Grief arrives in waves—not linear but spiral. Anger flashes, subsides into numbness. Relief (guilt about relief). Love persists, transforms, doesn't end but changes state like ice to water to vapor.",
          valence: -0.7,
          complexity: 0.9,
          tags: ["grief", "liberation", "ambivalence"]
        },
        level3_cognitive: {
          data: "Pattern recognition: This is the third relationship ending in public spaces. Defense mechanism? Need witnesses to make it real? Analyzing her micro-expressions—the relief she's trying to hide. Computing alternate responses, success probabilities. Mind fragmenting into observer and participant.",
          insights: ["patterns repeat until integrated", "public endings serve as reality anchors"],
          distortions: ["catastrophizing", "mind-reading", "temporal collapse"]
        },
        level4_social: {
          data: "Friendship networks will divide like assets. Her sister unfriends me before we leave the coffee shop. My mother will blame me. Her friends already chose sides. The barista pretends not to notice crying. Social fabric tears, must be rewoven.",
          ripples: ["22 mutual friends affected", "3 planned trips cancelled", "1 wedding attendance complicated"],
          reconstruction_time: "8-12 months"
        },
        level5_existential: {
          data: "What is love but a temporary suspension of entropy? We build elaborate structures of meaning together, but time is the universal solvent. Perhaps the tragedy isn't that love ends but that we expect permanence from impermanent beings. The self I was in this relationship dies today—who emerges?",
          questions: ["Can the self survive the death of its definitions?", "Is love's impermanence its most essential quality?"],
          integration_state: "pending"
        }
      },
      
      thematicLinks: ["entry_047", "entry_108", "entry_234"],
      recursionPatterns: ["abandonment", "transformation", "identity-death-rebirth"],
      contraindications: ["Memory of 'forever' promises conflicts with current reality"],
      
      aiInsights: {
        patterns: ["Recurring theme: Endings in transitional spaces (coffee shops, airports, train stations)"],
        contradictions: ["Claims readiness for end while fighting against it somatically"],
        emergence: ["New meta-pattern: Using intellectual analysis as emotional armor"],
        suggestions: ["Explore the connection between public endings and childhood witnessed arguments"]
      }
    }
  ];

  const currentEntry = journalEntries[activeEntry];

  const layerIcons = {
    level1_sensory: <Eye className="w-4 h-4" />,
    level2_emotional: <Heart className="w-4 h-4" />,
    level3_cognitive: <Brain className="w-4 h-4" />,
    level4_social: <Users className="w-4 h-4" />,
    level5_existential: <Infinity className="w-4 h-4" />
  };

  const layerColors = {
    level1_sensory: "from-blue-900 to-blue-700",
    level2_emotional: "from-red-900 to-pink-700",
    level3_cognitive: "from-purple-900 to-purple-700",
    level4_social: "from-green-900 to-green-700",
    level5_existential: "from-gray-900 to-gray-700"
  };

  return (
    <div className="min-h-screen bg-black text-gray-100 p-4">
      <div className="max-w-7xl mx-auto">
        {/* Header */}
        <div className="mb-6 border-b border-gray-800 pb-4">
          <h1 className="text-3xl font-bold bg-gradient-to-r from-purple-400 to-pink-400 bg-clip-text text-transparent">
            Multilinear Recursive Journal
          </h1>
          <p className="text-gray-400 mt-2">Psychic Tool for Temporal Self-Analysis</p>
        </div>

        {/* Control Panel */}
        <div className="mb-6 flex flex-wrap gap-4">
          <button
            onClick={() => setTimelineView(timelineView === 'actual' ? 'parallel' : 'actual')}
            className="px-4 py-2 bg-purple-900/50 border border-purple-700 rounded-lg hover:bg-purple-800/50 transition-colors flex items-center gap-2"
          >
            <GitBranch className="w-4 h-4" />
            Timeline: {timelineView === 'actual' ? 'Actual' : 'Parallel'}
          </button>
          
          <button
            onClick={() => setShowAIInsights(!showAIInsights)}
            className="px-4 py-2 bg-blue-900/50 border border-blue-700 rounded-lg hover:bg-blue-800/50 transition-colors flex items-center gap-2"
          >
            <Sparkles className="w-4 h-4" />
            AI Insights: {showAIInsights ? 'On' : 'Off'}
          </button>
          
          <select
            value={activeLayer}
            onChange={(e) => setActiveLayer(e.target.value)}
            className="px-4 py-2 bg-gray-900 border border-gray-700 rounded-lg"
          >
            <option value="all">All Layers</option>
            <option value="level1_sensory">L1: Sensory</option>
            <option value="level2_emotional">L2: Emotional</option>
            <option value="level3_cognitive">L3: Cognitive</option>
            <option value="level4_social">L4: Social</option>
            <option value="level5_existential">L5: Existential</option>
          </select>
        </div>

        {/* Main Entry Display */}
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
          {/* Left Column - Event Data */}
          <div className="lg:col-span-2 space-y-4">
            {/* Entry Header */}
            <div className="bg-gradient-to-r from-gray-900 to-gray-800 p-6 rounded-lg border border-gray-700">
              <div className="flex justify-between items-start mb-4">
                <div>
                  <h2 className="text-2xl font-bold text-white">{currentEntry.title}</h2>
                  <p className="text-gray-400 text-sm mt-1">
                    {new Date(currentEntry.timestamp).toLocaleString()}
                  </p>
                </div>
                <div className="text-right">
                  <div className="text-sm text-gray-400">Emotional Intensity</div>
                  <div className="text-2xl font-bold text-red-400">
                    {(currentEntry.emotionalIntensity * 100).toFixed(0)}%
                  </div>
                </div>
              </div>
              
              {/* Real Events */}
              <div className="mb-4">
                <button
                  onClick={() => toggleSection('realEvents')}
                  className="flex items-center gap-2 text-blue-400 hover:text-blue-300 mb-2"
                >
                  {expandedSections.realEvents ? <ChevronDown className="w-4 h-4" /> : <ChevronRight className="w-4 h-4" />}
                  <Clock className="w-4 h-4" />
                  Real Events
                </button>
                {expandedSections.realEvents && (
                  <div className="ml-6 p-4 bg-gray-950 rounded-lg border border-gray-800">
                    <p className="text-gray-200 mb-3">{currentEntry.realEvents.description}</p>
                    <div className="flex flex-wrap gap-2">
                      {currentEntry.realEvents.sensoryMarkers.map((marker, i) => (
                        <span key={i} className="px-2 py-1 bg-blue-900/30 text-blue-300 rounded text-xs">
                          {marker}
                        </span>
                      ))}
                    </div>
                  </div>
                )}
              </div>

              {/* Recursive Interpretations */}
              <div className="mb-4">
                <button
                  onClick={() => toggleSection('interpretations')}
                  className="flex items-center gap-2 text-purple-400 hover:text-purple-300 mb-2"
                >
                  {expandedSections.interpretations ? <ChevronDown className="w-4 h-4" /> : <ChevronRight className="w-4 h-4" />}
                  <Layers className="w-4 h-4" />
                  Recursive Interpretations
                </button>
                {expandedSections.interpretations && (
                  <div className="ml-6 space-y-2">
                    {currentEntry.recursiveInterpretations.map((interp, i) => (
                      <div key={i} className="p-3 bg-gradient-to-r from-purple-950/50 to-purple-900/30 rounded-lg border border-purple-800/50">
                        <div className="flex justify-between items-start">
                          <div className="flex-1">
                            <span className="text-xs text-purple-400">Depth {interp.depth}</span>
                            <p className="text-gray-200 mt-1">{interp.interpretation}</p>
                          </div>
                          <div className="ml-4">
                            <div className="text-xs text-gray-500">Confidence</div>
                            <div className="w-16 bg-gray-800 h-2 rounded-full mt-1">
                              <div 
                                className="h-full bg-gradient-to-r from-purple-600 to-purple-400 rounded-full"
                                style={{width: `${interp.confidence * 100}%`}}
                              />
                            </div>
                          </div>
                        </div>
                      </div>
                    ))}
                  </div>
                )}
              </div>

              {/* Parallel Outcomes */}
              <div className="mb-4">
                <button
                  onClick={() => toggleSection('parallelOutcomes')}
                  className="flex items-center gap-2 text-green-400 hover:text-green-300 mb-2"
                >
                  {expandedSections.parallelOutcomes ? <ChevronDown className="w-4 h-4" /> : <ChevronRight className="w-4 h-4" />}
                  <GitBranch className="w-4 h-4" />
                  Parallel Outcomes
                </button>
                {expandedSections.parallelOutcomes && (
                  <div className="ml-6 space-y-2">
                    {currentEntry.parallelOutcomes.map((outcome, i) => (
                      <div key={i} className="p-3 bg-gradient-to-r from-green-950/50 to-green-900/30 rounded-lg border border-green-800/50">
                        <div className="flex justify-between items-start mb-2">
                          <span className="text-xs font-bold text-green-400">Timeline {outcome.timeline.toUpperCase()}</span>
                          <span className="text-xs text-gray-400">P: {(outcome.probability * 100).toFixed(0)}%</span>
                        </div>
                        <p className="text-gray-200">{outcome.description}</p>
                      </div>
                    ))}
                  </div>
                )}
              </div>

              {/* Shadow Timelines */}
              <div className="mb-4">
                <button
                  onClick={() => toggleSection('shadowTimelines')}
                  className="flex items-center gap-2 text-gray-400 hover:text-gray-300 mb-2"
                >
                  {expandedSections.shadowTimelines ? <ChevronDown className="w-4 h-4" /> : <ChevronRight className="w-4 h-4" />}
                  <Eye className="w-4 h-4" />
                  Shadow Timelines (Intentionally Avoided)
                </button>
                {expandedSections.shadowTimelines && (
                  <div className="ml-6 space-y-2">
                    {currentEntry.shadowTimelines.map((shadow, i) => (
                      <div key={i} className="p-3 bg-gray-900/50 rounded-lg border border-gray-800">
                        <p className="text-gray-300 mb-2">⊗ {shadow.avoided}</p>
                        <p className="text-gray-500 text-sm">Reason: {shadow.reason}</p>
                        <div className="mt-2">
                          <span className="text-xs text-gray-600">Emotional cost: {(shadow.cost * 100).toFixed(0)}%</span>
                        </div>
                      </div>
                    ))}
                  </div>
                )}
              </div>

              {/* Future Echoes */}
              <div>
                <button
                  onClick={() => toggleSection('futureEchoes')}
                  className="flex items-center gap-2 text-yellow-400 hover:text-yellow-300 mb-2"
                >
                  {expandedSections.futureEchoes ? <ChevronDown className="w-4 h-4" /> : <ChevronRight className="w-4 h-4" />}
                  <Zap className="w-4 h-4" />
                  Hyperstitional Future Echoes
                </button>
                {expandedSections.futureEchoes && (
                  <div className="ml-6 space-y-2">
                    {currentEntry.futureEchoes.map((echo, i) => (
                      <div key={i} className="p-3 bg-gradient-to-r from-yellow-950/30 to-orange-950/30 rounded-lg border border-yellow-800/50">
                        <p className="text-yellow-100">{echo.echo}</p>
                        <div className="mt-2">
                          <span className="text-xs text-yellow-600">Certainty: {(echo.certainty * 100).toFixed(0)}%</span>
                        </div>
                      </div>
                    ))}
                  </div>
                )}
              </div>
            </div>

            {/* Hierarchy Levels */}
            <div className="bg-gray-900 p-6 rounded-lg border border-gray-700">
              <button
                onClick={() => toggleSection('hierarchy')}
                className="flex items-center gap-2 text-white hover:text-gray-300 mb-4"
              >
                {expandedSections.hierarchy ? <ChevronDown className="w-5 h-5" /> : <ChevronRight className="w-5 h-5" />}
                <Layers className="w-5 h-5" />
                <span className="font-bold">Structural Hierarchy</span>
              </button>
              
              {expandedSections.hierarchy && (
                <div className="space-y-4">
                  {Object.entries(currentEntry.hierarchy).map(([level, data]) => {
                    if (activeLayer !== 'all' && activeLayer !== level) return null;
                    
                    return (
                      <div key={level} className={`p-4 bg-gradient-to-r ${layerColors[level]} rounded-lg border border-gray-700`}>
                        <div className="flex items-center gap-2 mb-3">
                          {layerIcons[level]}
                          <span className="font-semibold text-white">
                            {level.replace(/_/g, ' ').replace(/level\d /i, 'Level ' + level.charAt(5) + ': ')}
                          </span>
                        </div>
                        
                        <div className="text-gray-200">
                          {typeof data.data === 'string' ? (
                            <p className="mb-3">{data.data}</p>
                          ) : (
                            <ul className="mb-3 space-y-1">
                              {data.data.map((item, i) => (
                                <li key={i} className="text-sm">• {item}</li>
                              ))}
                            </ul>
                          )}
                          
                          {data.tags && (
                            <div className="flex flex-wrap gap-2 mt-3">
                              {data.tags.map((tag, i) => (
                                <span key={i} className="px-2 py-1 bg-black/30 text-xs rounded">
                                  {tag}
                                </span>
                              ))}
                            </div>
                          )}
                          
                          {data.insights && (
                            <div className="mt-3 p-3 bg-black/30 rounded">
                              <p className="text-xs text-gray-400 mb-1">Insights:</p>
                              {data.insights.map((insight, i) => (
                                <p key={i} className="text-sm">→ {insight}</p>
                              ))}
                            </div>
                          )}
                          
                          {data.questions && (
                            <div className="mt-3 p-3 bg-black/30 rounded">
                              <p className="text-xs text-gray-400 mb-1">Questions:</p>
                              {data.questions.map((q, i) => (
                                <p key={i} className="text-sm italic">? {q}</p>
                              ))}
                            </div>
                          )}
                        </div>
                      </div>
                    );
                  })}
                </div>
              )}
            </div>
          </div>

          {/* Right Column - AI Insights & Metadata */}
          <div className="space-y-4">
            {/* AI Insights */}
            {showAIInsights && (
              <div className="bg-gradient-to-b from-blue-950/50 to-purple-950/50 p-6 rounded-lg border border-blue-800">
                <div className="flex items-center gap-2 mb-4">
                  <Sparkles className="w-5 h-5 text-blue-400" />
                  <h3 className="font-bold text-white">AI Analysis</h3>
                </div>
                
                <div className="space-y-4">
                  <div>
                    <p className="text-xs text-blue-400 mb-1">Detected Patterns</p>
                    {currentEntry.aiInsights.patterns.map((pattern, i) => (
                      <p key={i} className="text-sm text-gray-300 mb-2">• {pattern}</p>
                    ))}
                  </div>
                  
                  <div>
                    <p className="text-xs text-yellow-400 mb-1">Contradictions</p>
                    {currentEntry.aiInsights.contradictions.map((con, i) => (
                      <p key={i} className="text-sm text-gray-300 mb-2">⚠ {con}</p>
                    ))}
                  </div>
                  
                  <div>
                    <p className="text-xs text-green-400 mb-1">Emerging Insights</p>
                    {currentEntry.aiInsights.emergence.map((em, i) => (
                      <p key={i} className="text-sm text-gray-300 mb-2">✦ {em}</p>
                    ))}
                  </div>
                  
                  <div>
                    <p className="text-xs text-purple-400 mb-1">Suggestions</p>
                    {currentEntry.aiInsights.suggestions.map((sug, i) => (
                      <p key={i} className="text-sm text-gray-300 mb-2">→ {sug}</p>
                    ))}
                  </div>
                </div>
              </div>
            )}
            
            {/* Metadata */}
            <div className="bg-gray-900 p-6 rounded-lg border border-gray-700">
              <h3 className="font-bold text-white mb-4">Entry Metadata</h3>
              
              <div className="space-y-3">
                <div>
                  <p className="text-xs text-gray-400">Entry ID</p>
                  <p className="text-sm font-mono text-gray-300">{currentEntry.id}</p>
                </div>
                
                <div>
                  <p className="text-xs text-gray-400">Time Signature</p>
                  <p className="text-sm text-gray-300">{currentEntry.timeSignature}</p>
                </div>
                
                <div>
                  <p className="text-xs text-gray-400">Thematic Links</p>
                  <div className="flex flex-wrap gap-2 mt-1">
                    {currentEntry.thematicLinks.map((link, i) => (
                      <span key={i} className="px-2 py-1 bg-gray-800 text-xs text-blue-400 rounded cursor-pointer hover:bg-gray-700">
                        {link}
                      </span>
                    ))}
                  </div>
                </div>
                
                <div>
                  <p className="text-xs text-gray-400">Recursion Patterns</p>
                  <div className="flex flex-wrap gap-2 mt-1">
                    {currentEntry.recursionPatterns.map((pattern, i) => (
                      <span key={i} className="px-2 py-1 bg-purple-900/30 text-xs text-purple-300 rounded">
                        {pattern}
                      </span>
                    ))}
                  </div>
                </div>
              </div>
            </div>
            
            {/* Failed Realities */}
            <div className="bg-red-950/30 p-6 rounded-lg border border-red-900/50">
              <h3 className="font-bold text-red-400 mb-4">Failed Realities</h3>
              <div className="space-y-2">
                {currentEntry.failedRealities.map((reality, i) => (
                  <p key={i} className="text-sm text-gray-300">
                    <span className="text-red-500">✕</span> {reality}
                  </p>
                ))}
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default MultilinearJournal;
```