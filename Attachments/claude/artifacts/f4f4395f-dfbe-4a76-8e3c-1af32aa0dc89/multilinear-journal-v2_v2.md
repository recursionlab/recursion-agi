---
nexus: nexus-ai-chat-importer
plugin_version: "1.3.0"
provider: claude
artifact_id: multilinear-journal-v2
version_uuid: 4590833f-72e1-4f18-a806-13cbc9b5795a
version_number: 2
command: rewrite
conversation_id: f4f4395f-dfbe-4a76-8e3c-1af32aa0dc89
create_time: 2025-09-22T22:43:32.000Z
format: jsx
aliases: [Untitled Artifact, multilinear-journal-v2_v2]
---

# Untitled Artifact (Version 2)

**Conversation:** [[Nexus/Conversations/claude/2025/09/Recursive psychic journaling tool|Recursive psychic journaling tool]]

## Content

```jsx
import React, { useState, useEffect, useReducer, useMemo, useCallback, createContext, useContext } from 'react';
import { 
  ChevronRight, ChevronDown, Brain, Eye, Heart, Users, 
  Infinity, Clock, GitBranch, Sparkles, AlertTriangle, 
  Link, Layers, Zap, Search, Filter, Plus, Edit, 
  BarChart3, Network, Map, Hash, Calendar, TrendingUp,
  Compass, Moon, Sun, Save, Download, Upload, X, Check
} from 'lucide-react';

// ============= CONTEXT & STATE MANAGEMENT =============
const JournalContext = createContext(null);

const journalReducer = (state, action) => {
  switch (action.type) {
    case 'SET_ACTIVE_ENTRY':
      return { ...state, activeEntryId: action.payload };
    case 'SET_VIEW_MODE':
      return { ...state, viewMode: action.payload };
    case 'TOGGLE_LAYER':
      return { 
        ...state, 
        activeLayers: state.activeLayers.includes(action.payload)
          ? state.activeLayers.filter(l => l !== action.payload)
          : [...state.activeLayers, action.payload]
      };
    case 'UPDATE_ENTRY':
      return {
        ...state,
        entries: state.entries.map(e => 
          e.id === action.payload.id ? { ...e, ...action.payload.updates } : e
        )
      };
    case 'ADD_INTERPRETATION':
      return {
        ...state,
        entries: state.entries.map(e => 
          e.id === action.payload.entryId 
            ? {
                ...e,
                recursiveInterpretations: [
                  ...e.recursiveInterpretations,
                  action.payload.interpretation
                ]
              }
            : e
        )
      };
    case 'SET_FILTER':
      return { ...state, filters: { ...state.filters, ...action.payload } };
    case 'SET_COMPARISON_MODE':
      return { ...state, comparisonMode: action.payload };
    case 'ADD_TAG':
      return { 
        ...state, 
        globalTags: [...new Set([...state.globalTags, action.payload])]
      };
    default:
      return state;
  }
};

// ============= REUSABLE COMPONENTS =============

const LayerCard = ({ layer, data, icon, gradient, expanded, onToggle }) => {
  const [localExpanded, setLocalExpanded] = useState(expanded);
  
  return (
    <div className={`relative overflow-hidden rounded-lg border border-gray-700 transition-all duration-300 ${
      localExpanded ? 'ring-2 ring-purple-500/30' : ''
    }`}>
      <div className={`absolute inset-0 bg-gradient-to-r ${gradient} opacity-10`} />
      <div className="relative p-4">
        <button
          onClick={() => {
            setLocalExpanded(!localExpanded);
            onToggle?.();
          }}
          className="flex items-center gap-2 w-full text-left hover:text-purple-400 transition-colors"
        >
          {localExpanded ? <ChevronDown className="w-4 h-4" /> : <ChevronRight className="w-4 h-4" />}
          {icon}
          <span className="font-semibold">{layer}</span>
        </button>
        
        {localExpanded && (
          <div className="mt-4 space-y-3 animate-in slide-in-from-top-2">
            {typeof data.data === 'string' ? (
              <p className="text-gray-200 leading-relaxed">{data.data}</p>
            ) : (
              <ul className="space-y-1">
                {data.data.map((item, i) => (
                  <li key={i} className="text-sm text-gray-300 flex items-start">
                    <span className="text-purple-400 mr-2">▸</span>
                    {item}
                  </li>
                ))}
              </ul>
            )}
            
            {data.insights && (
              <InsightBlock title="Insights" items={data.insights} color="blue" />
            )}
            
            {data.questions && (
              <InsightBlock title="Questions" items={data.questions} color="purple" prefix="?" />
            )}
            
            {data.tags && <TagCloud tags={data.tags} />}
          </div>
        )}
      </div>
    </div>
  );
};

const InsightBlock = ({ title, items, color = "gray", prefix = "→" }) => (
  <div className={`p-3 bg-${color}-900/20 rounded-lg border border-${color}-800/30`}>
    <p className={`text-xs text-${color}-400 mb-2 font-semibold`}>{title}</p>
    {items.map((item, i) => (
      <p key={i} className="text-sm text-gray-300 mb-1">
        <span className={`text-${color}-400`}>{prefix}</span> {item}
      </p>
    ))}
  </div>
);

const TagCloud = ({ tags, onTagClick }) => (
  <div className="flex flex-wrap gap-2">
    {tags.map((tag, i) => (
      <button
        key={i}
        onClick={() => onTagClick?.(tag)}
        className="px-2 py-1 bg-gray-800/50 hover:bg-purple-900/30 
                   text-xs rounded transition-colors cursor-pointer
                   hover:ring-1 hover:ring-purple-500"
      >
        #{tag}
      </button>
    ))}
  </div>
);

const EmotionalSparkline = ({ interpretations }) => {
  const maxDepth = Math.max(...interpretations.map(i => i.depth));
  const sparklineHeight = 40;
  
  return (
    <div className="relative h-10 flex items-center gap-1">
      {interpretations.map((interp, i) => {
        const height = (interp.confidence * sparklineHeight);
        const opacity = 0.3 + (interp.depth / maxDepth) * 0.7;
        
        return (
          <div
            key={i}
            className="relative flex flex-col justify-end h-full"
            style={{ width: `${100 / interpretations.length}%` }}
          >
            <div
              className="bg-gradient-to-t from-purple-600 to-pink-500 rounded-t"
              style={{ 
                height: `${height}px`,
                opacity: opacity
              }}
              title={`Depth ${interp.depth}: ${(interp.confidence * 100).toFixed(0)}% confidence`}
            />
          </div>
        );
      })}
    </div>
  );
};

const TimelineNavigator = ({ entries, activeId, onSelect }) => {
  return (
    <div className="relative">
      <div className="absolute inset-0 bg-gradient-to-r from-purple-900/20 to-blue-900/20 rounded-lg" />
      <div className="relative p-4">
        <h3 className="text-sm font-semibold text-gray-400 mb-3">Timeline Navigation</h3>
        <div className="space-y-2">
          {entries.map((entry) => (
            <button
              key={entry.id}
              onClick={() => onSelect(entry.id)}
              className={`w-full text-left p-3 rounded-lg transition-all ${
                activeId === entry.id 
                  ? 'bg-purple-900/40 border border-purple-600' 
                  : 'bg-gray-900/30 hover:bg-gray-800/50 border border-gray-800'
              }`}
            >
              <div className="flex justify-between items-start">
                <div className="flex-1">
                  <p className="font-semibold text-sm">{entry.title}</p>
                  <p className="text-xs text-gray-500 mt-1">
                    {new Date(entry.timestamp).toLocaleDateString()}
                  </p>
                </div>
                <div className="text-right">
                  <div className={`text-xs px-2 py-1 rounded ${
                    entry.emotionalIntensity > 0.7 
                      ? 'bg-red-900/30 text-red-400' 
                      : entry.emotionalIntensity > 0.4
                      ? 'bg-yellow-900/30 text-yellow-400'
                      : 'bg-green-900/30 text-green-400'
                  }`}>
                    {(entry.emotionalIntensity * 100).toFixed(0)}%
                  </div>
                </div>
              </div>
              {activeId === entry.id && (
                <EmotionalSparkline interpretations={entry.recursiveInterpretations} />
              )}
            </button>
          ))}
        </div>
      </div>
    </div>
  );
};

const PatternVisualizer = ({ entries }) => {
  const patterns = useMemo(() => {
    const patternMap = {};
    entries.forEach(entry => {
      entry.recursionPatterns?.forEach(pattern => {
        if (!patternMap[pattern]) {
          patternMap[pattern] = { count: 0, entries: [], intensity: 0 };
        }
        patternMap[pattern].count++;
        patternMap[pattern].entries.push(entry.id);
        patternMap[pattern].intensity += entry.emotionalIntensity;
      });
    });
    return Object.entries(patternMap)
      .sort(([,a], [,b]) => b.count - a.count)
      .slice(0, 8);
  }, [entries]);

  return (
    <div className="bg-gradient-to-b from-gray-900 to-gray-950 rounded-lg p-4 border border-gray-800">
      <div className="flex items-center gap-2 mb-3">
        <Network className="w-4 h-4 text-purple-400" />
        <h3 className="text-sm font-semibold text-gray-300">Recurring Patterns</h3>
      </div>
      <div className="space-y-2">
        {patterns.map(([pattern, data]) => (
          <div key={pattern} className="relative">
            <div 
              className="absolute inset-0 bg-gradient-to-r from-purple-900/30 to-transparent rounded"
              style={{ width: `${(data.count / patterns[0][1].count) * 100}%` }}
            />
            <div className="relative flex justify-between items-center p-2">
              <span className="text-xs text-gray-300">{pattern}</span>
              <div className="flex items-center gap-2">
                <span className="text-xs text-purple-400">{data.count}x</span>
                <div className={`w-2 h-2 rounded-full ${
                  data.intensity / data.count > 0.7 ? 'bg-red-500' : 
                  data.intensity / data.count > 0.4 ? 'bg-yellow-500' : 'bg-green-500'
                }`} />
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

const EntryComparison = ({ entry1, entry2 }) => {
  if (!entry1 || !entry2) return null;
  
  const findCommonPatterns = () => {
    const patterns1 = new Set(entry1.recursionPatterns || []);
    const patterns2 = new Set(entry2.recursionPatterns || []);
    return [...patterns1].filter(p => patterns2.has(p));
  };
  
  const commonPatterns = findCommonPatterns();
  
  return (
    <div className="bg-gradient-to-b from-purple-950/30 to-blue-950/30 rounded-lg p-4 border border-purple-800/50">
      <h3 className="text-sm font-semibold text-purple-300 mb-3">Entry Comparison</h3>
      <div className="grid grid-cols-2 gap-4">
        <div>
          <p className="text-xs text-gray-400 mb-1">{entry1.title}</p>
          <p className="text-xs text-gray-500">{new Date(entry1.timestamp).toLocaleDateString()}</p>
          <div className="mt-2">
            <span className="text-xs text-gray-400">Intensity:</span>
            <div className="w-full bg-gray-800 h-2 rounded-full mt-1">
              <div 
                className="h-full bg-gradient-to-r from-purple-600 to-pink-500 rounded-full"
                style={{width: `${entry1.emotionalIntensity * 100}%`}}
              />
            </div>
          </div>
        </div>
        <div>
          <p className="text-xs text-gray-400 mb-1">{entry2.title}</p>
          <p className="text-xs text-gray-500">{new Date(entry2.timestamp).toLocaleDateString()}</p>
          <div className="mt-2">
            <span className="text-xs text-gray-400">Intensity:</span>
            <div className="w-full bg-gray-800 h-2 rounded-full mt-1">
              <div 
                className="h-full bg-gradient-to-r from-blue-600 to-cyan-500 rounded-full"
                style={{width: `${entry2.emotionalIntensity * 100}%`}}
              />
            </div>
          </div>
        </div>
      </div>
      
      {commonPatterns.length > 0 && (
        <div className="mt-4 p-3 bg-purple-900/20 rounded">
          <p className="text-xs text-purple-400 mb-2">Common Patterns:</p>
          <div className="flex flex-wrap gap-1">
            {commonPatterns.map(p => (
              <span key={p} className="px-2 py-1 bg-purple-800/30 text-xs rounded">
                {p}
              </span>
            ))}
          </div>
        </div>
      )}
      
      <div className="mt-3 text-xs text-gray-400">
        Time Distance: {Math.abs(
          (new Date(entry1.timestamp) - new Date(entry2.timestamp)) / (1000 * 60 * 60 * 24)
        ).toFixed(0)} days
      </div>
    </div>
  );
};

const AICoAuthorPanel = ({ entry, onGenerate }) => {
  const [generating, setGenerating] = useState(false);
  const [mode, setMode] = useState('echo');
  
  const handleGenerate = async () => {
    setGenerating(true);
    await onGenerate(mode, entry);
    setGenerating(false);
  };
  
  return (
    <div className="bg-gradient-to-b from-blue-950/30 to-purple-950/30 rounded-lg p-4 border border-blue-800/50">
      <div className="flex items-center gap-2 mb-3">
        <Sparkles className="w-4 h-4 text-blue-400" />
        <h3 className="text-sm font-semibold text-blue-300">AI Co-Author</h3>
      </div>
      
      <select 
        value={mode} 
        onChange={(e) => setMode(e.target.value)}
        className="w-full p-2 bg-gray-900 border border-gray-700 rounded text-sm mb-3"
      >
        <option value="echo">Generate Future Echo</option>
        <option value="shadow">Reveal Shadow Timeline</option>
        <option value="interpretation">Add Deeper Interpretation</option>
        <option value="parallel">Create Parallel Outcome</option>
        <option value="pattern">Identify Hidden Pattern</option>
      </select>
      
      <button
        onClick={handleGenerate}
        disabled={generating}
        className="w-full py-2 bg-gradient-to-r from-blue-600 to-purple-600 
                   hover:from-blue-500 hover:to-purple-500 rounded text-sm
                   disabled:opacity-50 disabled:cursor-not-allowed transition-all"
      >
        {generating ? (
          <span className="flex items-center justify-center gap-2">
            <Sparkles className="w-4 h-4 animate-spin" />
            Generating...
          </span>
        ) : (
          'Generate'
        )}
      </button>
      
      {entry.aiInsights?.lastGenerated && (
        <p className="text-xs text-gray-500 mt-2">
          Last generated: {new Date(entry.aiInsights.lastGenerated).toLocaleTimeString()}
        </p>
      )}
    </div>
  );
};

// ============= MAIN JOURNAL COMPONENT =============

const MultilinearJournal = () => {
  // Initial state with sample data
  const initialState = {
    entries: [
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
            confidence: 0.3,
            timestamp: "2024-03-15T16:00:00Z"
          },
          {
            depth: 2,
            interpretation: "Second pass: Liberation disguised as loss. We were holding each other prisoner.",
            confidence: 0.6,
            timestamp: "2024-03-15T22:00:00Z"
          },
          {
            depth: 3,
            interpretation: "Deep recursion: This ending was written into our beginning. Every 'I love you' contained its own negation.",
            confidence: 0.8,
            timestamp: "2024-03-16T10:00:00Z"
          },
          {
            depth: 4,
            interpretation: "Meta-recursive: The breakup is not an event but a revelation of what always was—two parallel lines mistaking proximity for intersection.",
            confidence: 0.95,
            timestamp: "2024-03-17T14:00:00Z"
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
            certainty: 0.8,
            timeDistance: "3 years"
          },
          {
            echo: "Six months: Meeting someone at a bookstore, feeling possibility again",
            certainty: 0.6,
            timeDistance: "6 months"
          },
          {
            echo: "Ten years: Our paths cross. We smile like old soldiers who survived the same war.",
            certainty: 0.4,
            timeDistance: "10 years"
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
        
        thematicLinks: ["entry_002", "entry_003"],
        recursionPatterns: ["abandonment", "transformation", "identity-death-rebirth", "public-endings"],
        contraindications: ["Memory of 'forever' promises conflicts with current reality"],
        
        aiInsights: {
          patterns: ["Recurring theme: Endings in transitional spaces (coffee shops, airports, train stations)"],
          contradictions: ["Claims readiness for end while fighting against it somatically"],
          emergence: ["New meta-pattern: Using intellectual analysis as emotional armor"],
          suggestions: ["Explore the connection between public endings and childhood witnessed arguments"]
        }
      },
      {
        id: "entry_002",
        timestamp: "2024-01-10T09:15:00Z",
        title: "Career Metamorphosis",
        emotionalIntensity: 0.78,
        timeSignature: "divergence",
        realEvents: {
          description: "Quit the job. Ten years of climbing the wrong mountain. The resignation letter trembled in my hands.",
          sensoryMarkers: ["office AC hum", "keyboard click finality", "empty desk echo"],
          duration: "15 minutes"
        },
        recursiveInterpretations: [
          {
            depth: 1,
            interpretation: "Fear and exhilaration, mixed like oil and water",
            confidence: 0.5,
            timestamp: "2024-01-10T10:00:00Z"
          },
          {
            depth: 2,
            interpretation: "This was never about the job—it was about proving I was enough",
            confidence: 0.7,
            timestamp: "2024-01-10T20:00:00Z"
          }
        ],
        recursionPatterns: ["transformation", "identity-death-rebirth", "liberation"],
        hierarchy: {
          level1_sensory: {
            data: ["hands: steady", "voice: clear", "posture: upright"],
            tags: ["somatic", "courage"]
          },
          level2_emotional: {
            data: "Terror wrapped in excitement. Freedom tastes like vertigo.",
            valence: 0.3,
            complexity: 0.8,
            tags: ["fear", "liberation", "uncertainty"]
          }
        }
      },
      {
        id: "entry_003",
        timestamp: "2023-11-22T18:45:00Z",
        title: "Father's Ghost",
        emotionalIntensity: 0.95,
        timeSignature: "recursive",
        realEvents: {
          description: "Found his journal in the attic. His handwriting like mine. His fears like mine. His dreams—abandoned—like mine?",
          sensoryMarkers: ["dust motes in light", "leather book smell", "attic wood creak"],
          duration: "3 hours"
        },
        recursiveInterpretations: [
          {
            depth: 1,
            interpretation: "Shock at the similarity. Am I living his unlived life?",
            confidence: 0.4,
            timestamp: "2023-11-22T19:00:00Z"
          },
          {
            depth: 2,
            interpretation: "Generational patterns are prisons we build ourselves",
            confidence: 0.8,
            timestamp: "2023-11-23T10:00:00Z"
          }
        ],
        recursionPatterns: ["inheritance", "generational-trauma", "identity-death-rebirth"],
        hierarchy: {
          level1_sensory: {
            data: ["tears: unexpected", "breathing: caught", "time: suspended"],
            tags: ["somatic", "recognition"]
          },
          level5_existential: {
            data: "We are our ancestors' dreams and nightmares made flesh.",
            questions: ["Can we break the cycle or only transform it?"],
            integration_state: "processing"
          }
        }
      }
    ],
    activeEntryId: "entry_001",
    viewMode: "standard",
    activeLayers: ["level1_sensory", "level2_emotional", "level3_cognitive", "level4_social", "level5_existential"],
    filters: {
      emotionalIntensity: [0, 1],
      timeRange: null,
      patterns: [],
      tags: []
    },
    comparisonMode: false,
    comparisonEntries: [],
    globalTags: ["abandonment", "transformation", "identity-death-rebirth", "liberation", "inheritance"],
    theme: "dark"
  };

  const [state, dispatch] = useReducer(journalReducer, initialState);
  const [searchQuery, setSearchQuery] = useState("");
  const [showSidebar, setShowSidebar] = useState(true);
  const [showPatternViz, setShowPatternViz] = useState(true);
  const [expandedSections, setExpandedSections] = useState({
    realEvents: true,
    interpretations: true,
    parallelOutcomes: false,
    failedRealities: false,
    shadowTimelines: false,
    futureEchoes: false,
    hierarchy: true
  });

  const currentEntry = state.entries.find(e => e.id === state.activeEntryId);
  
  const layerConfig = {
    level1_sensory: { icon: <Eye className="w-4 h-4" />, gradient: "from-blue-900 to-blue-700" },
    level2_emotional: { icon: <Heart className="w-4 h-4" />, gradient: "from-red-900 to-pink-700" },
    level3_cognitive: { icon: <Brain className="w-4 h-4" />, gradient: "from-purple-900 to-purple-700" },
    level4_social: { icon: <Users className="w-4 h-4" />, gradient: "from-green-900 to-green-700" },
    level5_existential: { icon: <Infinity className="w-4 h-4" />, gradient: "from-gray-900 to-gray-700" }
  };

  const toggleSection = (section) => {
    setExpandedSections(prev => ({ ...prev, [section]: !prev[section] }));
  };

  const handleAIGenerate = async (mode, entry) => {
    // Simulate AI generation
    console.log(`Generating ${mode} for entry ${entry.id}`);
    // In production, this would call an AI API
    await new Promise(resolve => setTimeout(resolve, 2000));
    
    // Update entry with generated content
    dispatch({
      type: 'UPDATE_ENTRY',
      payload: {
        id: entry.id,
        updates: {
          aiInsights: {
            ...entry.aiInsights,
            lastGenerated: new Date().toISOString()
          }
        }
      }
    });
  };

  const exportData = () => {
    const dataStr = JSON.stringify(state.entries, null, 2);
    const dataUri = 'data:application/json;charset=utf-8,'+ encodeURIComponent(dataStr);
    const exportFileDefaultName = `journal-export-${new Date().toISOString().split('T')[0]}.json`;
    
    const linkElement = document.createElement('a');
    linkElement.setAttribute('href', dataUri);
    linkElement.setAttribute('download', exportFileDefaultName);
    linkElement.click();
  };

  return (
    <JournalContext.Provider value={{ state, dispatch }}>
      <div className="min-h-screen bg-black text-gray-100">
        {/* Header Bar */}
        <div className="border-b border-gray-800 bg-gray-950/50 backdrop-blur sticky top-0 z-50">
          <div className="max-w-full px-4 py-3">
            <div className="flex items-center justify-between">
              <div className="flex items-center gap-4">
                <button
                  onClick={() => setShowSidebar(!showSidebar)}
                  className="p-2 hover:bg-gray-800 rounded-lg transition-colors"
                >
                  <Layers className="w-5 h-5" />
                </button>
                <h1 className="text-xl font-bold bg-gradient-to-r from-purple-400 to-pink-400 bg-clip-text text-transparent">
                  Multilinear Recursive Journal
                </h1>
              </div>
              
              <div className="flex items-center gap-2">
                <button
                  onClick={() => setShowPatternViz(!showPatternViz)}
                  className="p-2 hover:bg-gray-800 rounded-lg transition-colors"
                  title="Toggle Pattern Visualization"
                >
                  <Network className="w-5 h-5" />
                </button>
                <button
                  onClick={exportData}
                  className="p-2 hover:bg-gray-800 rounded-lg transition-colors"
                  title="Export Data"
                >
                  <Download className="w-5 h-5" />
                </button>
                <button className="p-2 hover:bg-gray-800 rounded-lg transition-colors">
                  <Plus className="w-5 h-5" />
                </button>
              </div>
            </div>
          </div>
        </div>

        <div className="flex">
          {/* Sidebar */}
          {showSidebar && (
            <div className="w-80 border-r border-gray-800 bg-gray-950/30 h-[calc(100vh-60px)] overflow-y-auto">
              <div className="p-4 space-y-4">
                {/* Search */}
                <div className="relative">
                  <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 w-4 h-4 text-gray-500" />
                  <input
                    type="text"
                    placeholder="Search entries..."
                    value={searchQuery}
                    onChange={(e) => setSearchQuery(e.target.value)}
                    className="w-full pl-10 pr-4 py-2 bg-gray-900 border border-gray-700 rounded-lg 
                             focus:ring-2 focus:ring-purple-500 focus:border-transparent outline-none"
                  />
                </div>

                {/* Timeline Navigator */}
                <TimelineNavigator
                  entries={state.entries}
                  activeId={state.activeEntryId}
                  onSelect={(id) => dispatch({ type: 'SET_ACTIVE_ENTRY', payload: id })}
                />

                {/* Pattern Visualizer */}
                {showPatternViz && (
                  <PatternVisualizer entries={state.entries} />
                )}

                {/* Entry Comparison */}
                {state.entries.length > 1 && (
                  <EntryComparison
                    entry1={state.entries[0]}
                    entry2={state.entries[1]}
                  />
                )}
              </div>
            </div>
          )}

          {/* Main Content */}
          <div className="flex-1 overflow-y-auto h-[calc(100vh-60px)]">
            <div className="max-w-5xl mx-auto p-6">
              {currentEntry && (
                <div className="space-y-6">
                  {/* Entry Header */}
                  <div className="bg-gradient-to-r from-gray-900 to-gray-800 p-6 rounded-xl border border-gray-700">
                    <div className="flex justify-between items-start mb-4">
                      <div>
                        <h2 className="text-3xl font-bold text-white mb-2">{currentEntry.title}</h2>
                        <p className="text-gray-400">
                          {new Date(currentEntry.timestamp).toLocaleString()} • {currentEntry.timeSignature}
                        </p>
                      </div>
                      <div className="text-right">
                        <div className="text-sm text-gray-400 mb-1">Emotional Intensity</div>
                        <div className="text-3xl font-bold bg-gradient-to-r from-red-500 to-pink-500 bg-clip-text text-transparent">
                          {(currentEntry.emotionalIntensity * 100).toFixed(0)}%
                        </div>
                      </div>
                    </div>

                    {/* Emotional Sparkline */}
                    <div className="mb-4 p-3 bg-gray-950/50 rounded-lg">
                      <p className="text-xs text-gray-500 mb-2">Interpretation Confidence Over Depth</p>
                      <EmotionalSparkline interpretations={currentEntry.recursiveInterpretations} />
                    </div>

                    {/* Real Events */}
                    <div className="mb-4">
                      <button
                        onClick={() => toggleSection('realEvents')}
                        className="flex items-center gap-2 text-blue-400 hover:text-blue-300 mb-2 transition-colors"
                      >
                        {expandedSections.realEvents ? <ChevronDown className="w-4 h-4" /> : <ChevronRight className="w-4 h-4" />}
                        <Clock className="w-4 h-4" />
                        <span className="font-semibold">Real Events</span>
                      </button>
                      {expandedSections.realEvents && (
                        <div className="ml-6 p-4 bg-gray-950 rounded-lg border border-gray-800">
                          <p className="text-gray-200 mb-3 leading-relaxed">{currentEntry.realEvents.description}</p>
                          <div className="flex items-center gap-4 text-xs text-gray-500">
                            <span>Duration: {currentEntry.realEvents.duration}</span>
                            <span>•</span>
                            <span>{currentEntry.realEvents.sensoryMarkers.length} sensory markers</span>
                          </div>
                          <TagCloud tags={currentEntry.realEvents.sensoryMarkers} />
                        </div>
                      )}
                    </div>

                    {/* Recursive Interpretations */}
                    <div className="mb-4">
                      <button
                        onClick={() => toggleSection('interpretations')}
                        className="flex items-center gap-2 text-purple-400 hover:text-purple-300 mb-2 transition-colors"
                      >
                        {expandedSections.interpretations ? <ChevronDown className="w-4 h-4" /> : <ChevronRight className="w-4 h-4" />}
                        <Layers className="w-4 h-4" />
                        <span className="font-semibold">Recursive Interpretations</span>
                      </button>
                      {expandedSections.interpretations && (
                        <div className="ml-6 space-y-3">
                          {currentEntry.recursiveInterpretations.map((interp, i) => (
                            <div key={i} className="group relative">
                              <div className="absolute left-0 top-0 bottom-0 w-1 bg-gradient-to-b from-purple-600 to-purple-400 rounded-full"
                                   style={{ opacity: interp.confidence }} />
                              <div className="pl-4 p-3 bg-gradient-to-r from-purple-950/30 to-transparent rounded-lg 
                                            border border-purple-800/30 hover:border-purple-600/50 transition-all">
                                <div className="flex justify-between items-start mb-2">
                                  <span className="text-xs font-semibold text-purple-400">
                                    Depth {interp.depth} • {new Date(interp.timestamp).toLocaleTimeString()}
                                  </span>
                                  <div className="flex items-center gap-2">
                                    <span className="text-xs text-gray-500">Confidence</span>
                                    <div className="w-20 bg-gray-800 h-1.5 rounded-full">
                                      <div 
                                        className="h-full bg-gradient-to-r from-purple-600 to-pink-500 rounded-full transition-all"
                                        style={{width: `${interp.confidence * 100}%`}}
                                      />
                                    </div>
                                  </div>
                                </div>
                                <p className="text-gray-200">{interp.interpretation}</p>
                              </div>
                            </div>
                          ))}
                        </div>
                      )}
                    </div>

                    {/* Other sections with similar improvements... */}
                  </div>

                  {/* Hierarchy Grid */}
                  <div className="grid grid-cols-1 lg:grid-cols-2 gap-4">
                    {Object.entries(currentEntry.hierarchy || {}).map(([level, data]) => {
                      if (!state.activeLayers.includes(level)) return null;
                      
                      return (
                        <LayerCard
                          key={level}
                          layer={level.replace(/_/g, ' ').replace(/level\d /i, 'Level ' + level.charAt(5) + ': ')}
                          data={data}
                          icon={layerConfig[level].icon}
                          gradient={layerConfig[level].gradient}
                          expanded={true}
                          onToggle={() => dispatch({ type: 'TOGGLE_LAYER', payload: level })}
                        />
                      );
                    })}
                  </div>
                </div>
              )}
            </div>
          </div>

          {/* Right Panel - AI Assistant */}
          <div className="w-80 border-l border-gray-800 bg-gray-950/30 h-[calc(100vh-60px)] overflow-y-auto">
            <div className="p-4 space-y-4">
              <AICoAuthorPanel 
                entry={currentEntry} 
                onGenerate={handleAIGenerate}
              />
              
              {/* Layer Controls */}
              <div className="bg-gray-900 rounded-lg p-4 border border-gray-700">
                <h3 className="text-sm font-semibold text-gray-300 mb-3">Active Layers</h3>
                <div className="space-y-2">
                  {Object.entries(layerConfig).map(([layer, config]) => (
                    <label key={layer} className="flex items-center gap-2 cursor-pointer hover:text-purple-400 transition-colors">
                      <input
                        type="checkbox"
                        checked={state.activeLayers.includes(layer)}
                        onChange={() => dispatch({ type: 'TOGGLE_LAYER', payload: layer })}
                        className="rounded border-gray-600 text-purple-600 focus:ring-purple-500"
                      />
                      {config.icon}
                      <span className="text-xs">{layer.split('_').slice(1).join(' ')}</span>
                    </label>
                  ))}
                </div>
              </div>
              
              {/* Global Tags */}
              <div className="bg-gray-900 rounded-lg p-4 border border-gray-700">
                <h3 className="text-sm font-semibold text-gray-300 mb-3">Global Patterns</h3>
                <TagCloud 
                  tags={state.globalTags} 
                  onTagClick={(tag) => console.log('Filter by tag:', tag)}
                />
              </div>
            </div>
          </div>
        </div>
      </div>
    </JournalContext.Provider>
  );
};

export default MultilinearJournal;
```