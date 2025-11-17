---
nexus: nexus-ai-chat-importer
plugin_version: "1.3.0"
provider: claude
artifact_id: multilinear_journal
version_uuid: 3137690b-b6b2-43ea-a675-6996cedb2a13
version_number: 1
command: create
conversation_id: be3e0849-4c3b-44df-b21e-365455699ba8
create_time: 2025-09-22T19:44:35.000Z
format: jsx
aliases: ['Multilinear Journal: Alternate Reality Reflection', multilinear_journal_v1]
---

# Multilinear Journal: Alternate Reality Reflection (Version 1)

**Conversation:** [[Nexus/Conversations/claude/2025/09/Starting from scratch|Starting from scratch]]

## Content

```jsx
import React, { useState, useEffect } from 'react';

const MultilinearJournal = () => {
  const [selectedEntry, setSelectedEntry] = useState(null);
  const [activeReality, setActiveReality] = useState('happened');
  const [journalEntries, setJournalEntries] = useState([
    {
      id: "entry-1",
      date: "2025-09-22",
      title: "Team Meeting Presentation",
      realities: {
        happened: {
          content: "Presented the quarterly report to the team. My hands were shaking and I stumbled over the financial projections slide. The team was supportive but I could see some confused looks. Sarah asked clarifying questions that helped, but I felt like I didn't demonstrate the expertise I wanted to show.",
          mood: "nervous",
          outcomes: ["Presentation completed", "Received supportive feedback", "Identified areas for improvement"],
          emotions: ["anxious", "disappointed", "grateful"],
          insights: "I need to practice more before big presentations"
        },
        couldHave: {
          content: "If I had practiced the presentation just one more time the night before, I would have caught the error in the financial slide. I could have spoken more confidently about the metrics since I know them well. Maybe I could have included that additional market analysis that showed our competitive advantage more clearly.",
          mood: "confident",
          outcomes: ["Smooth presentation delivery", "Clear communication of key points", "Team fully aligned on metrics"],
          emotions: ["prepared", "articulate", "professional"],
          insights: "Preparation time directly correlates with confidence"
        },
        wished: {
          content: "I wish I had been the kind of presenter who could think on their feet and turn the moment into an engaging discussion. I wish I had the natural charisma to make financial data exciting and had everyone leaving the room energized about our progress. I wish I felt as comfortable speaking to my team as I do analyzing the data.",
          mood: "aspirational",
          outcomes: ["Inspired team engagement", "Created enthusiasm for goals", "Demonstrated natural leadership"],
          emotions: ["charismatic", "inspiring", "authentic"],
          insights: "My ideal self is more collaborative and naturally engaging"
        }
      },
      metadata: {
        created: "2025-09-22T18:30:00Z",
        tags: ["work", "presentation", "growth"],
        reflectionDepth: 4
      }
    },
    {
      id: "entry-2",
      date: "2025-09-21",
      title: "Weekend Plans Cancelled",
      realities: {
        happened: {
          content: "My weekend hiking trip got cancelled because of the storm warning. I ended up staying home, ordering takeout, and binge-watching that documentary series about ocean exploration. It was actually quite relaxing, though I felt a bit guilty about not being more productive. I did finally organize my digital photos from the summer.",
          mood: "content",
          outcomes: ["Restful weekend", "Caught up on documentary", "Organized photos"],
          emotions: ["relaxed", "slightly guilty", "satisfied"],
          insights: "Sometimes forced rest is exactly what I need"
        },
        couldHave: {
          content: "If the weather had held, I would have gone on that mountain trail I've been wanting to try for months. The views would have been incredible after all the recent rain, and I probably would have taken some amazing photos. I might have run into other hikers and made some new connections with fellow outdoor enthusiasts.",
          mood: "adventurous",
          outcomes: ["Completed challenging hike", "Captured beautiful photos", "Met new people"],
          emotions: ["accomplished", "energized", "connected"],
          insights: "I thrive on outdoor challenges and new experiences"
        },
        wished: {
          content: "I wish I was the type of person who could make any day an adventure, rain or shine. I wish I had indoor hobbies that excited me as much as hiking does. Maybe I could have used the rainy day to work on that creative writing project I keep putting off, or to finally learn that musical instrument that's been gathering dust.",
          mood: "creative",
          outcomes: ["Pursued creative passion", "Developed new skills", "Felt artistically fulfilled"],
          emotions: ["creative", "motivated", "purposeful"],
          insights: "I want to cultivate indoor passions that match my outdoor energy"
        }
      },
      metadata: {
        created: "2025-09-21T21:45:00Z",
        tags: ["leisure", "reflection", "weather"],
        reflectionDepth: 3
      }
    },
    {
      id: "entry-3",
      date: "2025-09-20",
      title: "Coffee with an Old Friend",
      realities: {
        happened: {
          content: "Had coffee with Jamie for the first time in two years. We talked about our career changes and how different our lives have become. There were some awkward silences where we both realized how much we've grown apart. It was nice to catch up, but also bittersweet realizing that we're not as close as we used to be.",
          mood: "bittersweet",
          outcomes: ["Reconnected with old friend", "Acknowledged growing apart", "Shared life updates"],
          emotions: ["nostalgic", "sad", "accepting"],
          insights: "Some friendships naturally evolve as people change"
        },
        couldHave: {
          content: "If I had been more intentional about staying in touch over the past two years, we could have maintained that easy rapport we used to have. We could have supported each other through our various life changes instead of feeling like strangers catching up. The conversation could have flowed naturally without those uncomfortable pauses.",
          mood: "connected",
          outcomes: ["Maintained close friendship", "Provided mutual support", "Easy, flowing conversation"],
          emotions: ["connected", "supported", "familiar"],
          insights: "Consistent effort is required to maintain meaningful relationships"
        },
        wished: {
          content: "I wish I had the kind of friendship magic that could instantly bridge any gap, no matter how much time has passed. I wish we could have picked up exactly where we left off, with inside jokes and shared understanding intact. I wish I was better at nurturing long-distance friendships and making people feel valued even when life gets busy.",
          mood: "warm",
          outcomes: ["Effortless reconnection", "Renewed close bond", "Plans for regular contact"],
          emotions: ["warm", "skilled", "nurturing"],
          insights: "I aspire to be more intentional and skilled at maintaining relationships"
        }
      },
      metadata: {
        created: "2025-09-20T19:20:00Z",
        tags: ["friendship", "connection", "growth"],
        reflectionDepth: 5
      }
    }
  ]);

  const RealityTimeline = ({ entry, activeReality, onRealityChange }) => {
    const realities = ['happened', 'couldHave', 'wished'];
    const realityLabels = {
      happened: 'What Happened',
      couldHave: 'What Could\'ve Happened',
      wished: 'What I Wish Had Happened'
    };
    
    const realityColors = {
      happened: '#6366f1',
      couldHave: '#059669', 
      wished: '#dc2626'
    };

    return (
      <div className="mb-6">
        <div className="flex gap-2 mb-4">
          {realities.map(reality => (
            <button
              key={reality}
              onClick={() => onRealityChange(reality)}
              className={`px-4 py-2 rounded-lg font-medium transition-all ${
                activeReality === reality 
                  ? 'text-white shadow-lg' 
                  : 'text-gray-600 bg-gray-100 hover:bg-gray-200'
              }`}
              style={{
                backgroundColor: activeReality === reality ? realityColors[reality] : undefined
              }}
            >
              {realityLabels[reality]}
            </button>
          ))}
        </div>

        <div className="relative">
          <div className="flex justify-between mb-2">
            {realities.map((reality, index) => (
              <div
                key={reality}
                className="flex-1 text-center relative"
              >
                <div
                  className={`w-4 h-4 rounded-full mx-auto transition-all ${
                    activeReality === reality ? 'scale-125 shadow-lg' : ''
                  }`}
                  style={{ backgroundColor: realityColors[reality] }}
                ></div>
                {index < realities.length - 1 && (
                  <div className="absolute top-2 left-1/2 w-1/2 h-0.5 bg-gray-300"></div>
                )}
              </div>
            ))}
          </div>
          <div className="flex justify-between text-xs text-gray-500">
            <span>Reality</span>
            <span>Possibility</span>
            <span>Aspiration</span>
          </div>
        </div>
      </div>
    );
  };

  const RealityCard = ({ reality, content, isActive }) => {
    const realityColors = {
      happened: '#6366f1',
      couldHave: '#059669',
      wished: '#dc2626'
    };

    return (
      <div className={`transition-all duration-300 ${isActive ? 'opacity-100' : 'opacity-40'}`}>
        <div
          className="bg-white rounded-lg shadow-lg p-6 border-l-4"
          style={{ borderColor: realityColors[reality] }}
        >
          <div className="space-y-4">
            <div>
              <h4 className="font-semibold text-gray-700 mb-2">Experience</h4>
              <p className="text-gray-800 leading-relaxed">{content.content}</p>
            </div>

            <div className="grid md:grid-cols-2 gap-4">
              <div>
                <h5 className="font-medium text-gray-600 mb-2">Emotions</h5>
                <div className="flex flex-wrap gap-1">
                  {content.emotions.map(emotion => (
                    <span
                      key={emotion}
                      className="px-2 py-1 text-xs rounded-full text-white"
                      style={{ backgroundColor: realityColors[reality] + '80' }}
                    >
                      {emotion}
                    </span>
                  ))}
                </div>
              </div>

              <div>
                <h5 className="font-medium text-gray-600 mb-2">Outcomes</h5>
                <ul className="text-sm text-gray-700">
                  {content.outcomes.map((outcome, idx) => (
                    <li key={idx} className="flex items-start gap-2">
                      <span className="text-xs mt-1">•</span>
                      <span>{outcome}</span>
                    </li>
                  ))}
                </ul>
              </div>
            </div>

            <div className="border-t pt-3">
              <h5 className="font-medium text-gray-600 mb-1">Insight</h5>
              <p className="text-sm italic text-gray-700">{content.insights}</p>
            </div>
          </div>
        </div>
      </div>
    );
  };

  const ComparisonView = ({ entry }) => {
    const realities = ['happened', 'couldHave', 'wished'];
    const realityLabels = {
      happened: 'Reality',
      couldHave: 'Possibility', 
      wished: 'Aspiration'
    };
    
    const realityColors = {
      happened: '#6366f1',
      couldHave: '#059669',
      wished: '#dc2626'
    };

    return (
      <div className="grid lg:grid-cols-3 gap-6">
        {realities.map(reality => (
          <div key={reality} className="space-y-3">
            <h3 
              className="text-lg font-semibold text-center p-3 rounded-lg text-white"
              style={{ backgroundColor: realityColors[reality] }}
            >
              {realityLabels[reality]}
            </h3>
            <RealityCard
              reality={reality}
              content={entry.realities[reality]}
              isActive={true}
            />
          </div>
        ))}
      </div>
    );
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-purple-50 to-indigo-100 p-4">
      <div className="max-w-6xl mx-auto">
        {/* Header */}
        <div className="text-center mb-8">
          <h1 className="text-3xl font-bold text-gray-800 mb-2">Multilinear Journal</h1>
          <p className="text-gray-600">Explore alternate realities of your experiences</p>
        </div>

        {/* Journal Entries List */}
        <div className="grid md:grid-cols-3 gap-4 mb-8">
          {journalEntries.map(entry => (
            <div
              key={entry.id}
              onClick={() => setSelectedEntry(entry)}
              className={`bg-white rounded-lg shadow-md p-4 cursor-pointer transition-all hover:shadow-lg ${
                selectedEntry?.id === entry.id ? 'ring-2 ring-indigo-400' : ''
              }`}
            >
              <div className="flex justify-between items-start mb-2">
                <h3 className="font-semibold text-gray-800">{entry.title}</h3>
                <span className="text-xs text-gray-500">{entry.date}</span>
              </div>
              <p className="text-sm text-gray-600 line-clamp-2">
                {entry.realities.happened.content.substring(0, 100)}...
              </p>
              <div className="flex gap-2 mt-3">
                {entry.metadata.tags.map(tag => (
                  <span key={tag} className="px-2 py-1 bg-gray-100 text-xs rounded">
                    {tag}
                  </span>
                ))}
              </div>
            </div>
          ))}
        </div>

        {/* Selected Entry Details */}
        {selectedEntry && (
          <div className="bg-white rounded-lg shadow-xl p-6 mb-6">
            <div className="flex justify-between items-start mb-6">
              <div>
                <h2 className="text-2xl font-bold text-gray-800">{selectedEntry.title}</h2>
                <p className="text-gray-600">{selectedEntry.date}</p>
              </div>
              <div className="flex gap-2">
                <button
                  onClick={() => setActiveReality('comparison')}
                  className={`px-4 py-2 rounded-lg text-sm ${
                    activeReality === 'comparison' 
                      ? 'bg-purple-600 text-white' 
                      : 'bg-gray-200 text-gray-700'
                  }`}
                >
                  Compare All
                </button>
              </div>
            </div>

            {activeReality === 'comparison' ? (
              <ComparisonView entry={selectedEntry} />
            ) : (
              <>
                <RealityTimeline 
                  entry={selectedEntry}
                  activeReality={activeReality}
                  onRealityChange={setActiveReality}
                />
                <RealityCard
                  reality={activeReality}
                  content={selectedEntry.realities[activeReality]}
                  isActive={true}
                />
              </>
            )}
          </div>
        )}

        {/* Insights Panel */}
        {selectedEntry && (
          <div className="bg-white rounded-lg shadow-lg p-6">
            <h3 className="text-lg font-semibold mb-4">Cross-Reality Insights</h3>
            <div className="grid md:grid-cols-2 gap-6">
              <div>
                <h4 className="font-medium text-gray-700 mb-2">Patterns Across Realities</h4>
                <ul className="text-sm text-gray-600 space-y-1">
                  <li>• Common themes: {selectedEntry.metadata.tags.join(', ')}</li>
                  <li>• Reflection depth: {selectedEntry.metadata.reflectionDepth}/5</li>
                  <li>• Growth areas identified across all versions</li>
                </ul>
              </div>
              <div>
                <h4 className="font-medium text-gray-700 mb-2">Future Applications</h4>
                <ul className="text-sm text-gray-600 space-y-1">
                  <li>• Use "Could've" insights for future preparation</li>
                  <li>• Apply "Wished" aspirations to goal setting</li>
                  <li>• Integrate learnings from actual experience</li>
                </ul>
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default MultilinearJournal;
```