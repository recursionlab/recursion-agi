---
nexus: nexus-ai-chat-importer
plugin_version: "1.3.0"
provider: claude
artifact_id: memory_machine_prototype
version_uuid: c26f9485-a9a7-4054-908e-bd51eac66f48
version_number: 1
command: create
conversation_id: be3e0849-4c3b-44df-b21e-365455699ba8
create_time: 2025-09-22T19:44:35.000Z
format: jsx
aliases: ['Memory Machine: Recursive StickyNotes', memory_machine_prototype_v1]
---

# Memory Machine: Recursive StickyNotes (Version 1)

**Conversation:** [[Nexus/Conversations/claude/2025/09/Starting from scratch|Starting from scratch]]

## Content

```jsx
import React, { useState, useRef, useEffect } from 'react';

const MemoryMachine = () => {
  const [currentLevel, setCurrentLevel] = useState(0);
  const [selectedNote, setSelectedNote] = useState(null);
  const [viewMode, setViewMode] = useState('spatial'); // spatial, list, tree

  // Sample hierarchical data
  const [noteSystem] = useState({
    "root-1": {
      id: "root-1",
      title: "Project Planning",
      content: "High-level project strategy and goals",
      abstractionLevel: 0,
      position: { x: 200, y: 150 },
      metadata: {
        created: "2025-09-22T10:00:00Z",
        tags: ["work", "planning"],
        color: "#6366f1",
        priority: 4
      },
      connections: {
        children: ["child-1-1", "child-1-2", "child-1-3"]
      },
      content_layers: {
        summary: "Plan project execution",
        detailed: "Define scope, timeline, resources, and deliverables for Q4 project",
        examples: ["Similar to Q2 migration", "Use Agile methodology"]
      },
      viewState: { isExpanded: false, isVisible: true, scale: 1.0 }
    },
    "child-1-1": {
      id: "child-1-1",
      title: "Timeline & Milestones",
      content: "Break down project into phases with specific deadlines",
      abstractionLevel: 1,
      position: { x: 100, y: 80 },
      metadata: {
        created: "2025-09-22T10:15:00Z",
        tags: ["timeline", "milestones"],
        color: "#059669",
        priority: 5
      },
      connections: {
        parent: "root-1",
        children: ["child-2-1", "child-2-2"]
      },
      content_layers: {
        summary: "Project timeline",
        detailed: "Phase 1: Research (2 weeks), Phase 2: Development (6 weeks), Phase 3: Testing (2 weeks)",
        examples: ["Use Gantt charts", "Weekly check-ins"]
      },
      viewState: { isExpanded: false, isVisible: true, scale: 1.0 }
    },
    "child-1-2": {
      id: "child-1-2",
      title: "Resource Allocation",
      content: "Assign team members and budget to different work streams",
      abstractionLevel: 1,
      position: { x: 300, y: 80 },
      metadata: {
        created: "2025-09-22T10:20:00Z",
        tags: ["resources", "team"],
        color: "#dc2626",
        priority: 4
      },
      connections: {
        parent: "root-1",
        children: ["child-2-3"]
      },
      content_layers: {
        summary: "Team & budget planning",
        detailed: "3 developers, 1 designer, 1 PM. Budget: $50k. Tools: Figma, GitHub, Slack",
        examples: ["Previous project staffing", "Industry benchmarks"]
      },
      viewState: { isExpanded: false, isVisible: true, scale: 1.0 }
    },
    "child-1-3": {
      id: "child-1-3",
      title: "Risk Assessment",
      content: "Identify potential blockers and mitigation strategies",
      abstractionLevel: 1,
      position: { x: 400, y: 200 },
      metadata: {
        created: "2025-09-22T10:25:00Z",
        tags: ["risk", "planning"],
        color: "#f59e0b",
        priority: 3
      },
      connections: {
        parent: "root-1",
        children: []
      },
      content_layers: {
        summary: "Risk planning",
        detailed: "Technical risks: API changes, dependency issues. Timeline risks: scope creep, resource conflicts",
        examples: ["Previous project issues", "Industry common risks"]
      },
      viewState: { isExpanded: false, isVisible: true, scale: 1.0 }
    },
    "child-2-1": {
      id: "child-2-1",
      title: "Sprint Planning",
      content: "Detailed sprint breakdown with story points and dependencies",
      abstractionLevel: 2,
      position: { x: 50, y: 50 },
      metadata: {
        created: "2025-09-22T11:00:00Z",
        tags: ["sprint", "agile"],
        color: "#059669",
        priority: 5
      },
      connections: {
        parent: "child-1-1",
        children: []
      },
      content_layers: {
        summary: "Sprint details",
        detailed: "2-week sprints, 40 story points capacity, daily standups at 9am",
        examples: ["Sprint 1: Setup & Research", "Sprint 2: Core Features"]
      },
      viewState: { isExpanded: false, isVisible: true, scale: 1.0 }
    },
    "child-2-2": {
      id: "child-2-2",
      title: "Deliverables Checklist",
      content: "Specific outputs and acceptance criteria for each milestone",
      abstractionLevel: 2,
      position: { x: 150, y: 50 },
      metadata: {
        created: "2025-09-22T11:10:00Z",
        tags: ["deliverables", "checklist"],
        color: "#059669",
        priority: 4
      },
      connections: {
        parent: "child-1-1",
        children: []
      },
      content_layers: {
        summary: "Delivery checklist",
        detailed: "✓ Technical specs, ✓ Design mockups, ✓ Test cases, ✓ Documentation",
        examples: ["Previous project deliverables", "Client requirements"]
      },
      viewState: { isExpanded: false, isVisible: true, scale: 1.0 }
    },
    "child-2-3": {
      id: "child-2-3",
      title: "Budget Breakdown",
      content: "Detailed cost allocation across team, tools, and infrastructure",
      abstractionLevel: 2,
      position: { x: 300, y: 50 },
      metadata: {
        created: "2025-09-22T11:15:00Z",
        tags: ["budget", "finance"],
        color: "#dc2626",
        priority: 3
      },
      connections: {
        parent: "child-1-2",
        children: []
      },
      content_layers: {
        summary: "Cost breakdown",
        detailed: "Salaries: $35k, Tools: $5k, Infrastructure: $8k, Contingency: $2k",
        examples: ["Q3 project costs", "Market rate benchmarks"]
      },
      viewState: { isExpanded: false, isVisible: true, scale: 1.0 }
    }
  });

  const getNotesAtLevel = (level) => {
    return Object.values(noteSystem).filter(note => note.abstractionLevel === level);
  };

  const getChildNotes = (parentId) => {
    const parent = noteSystem[parentId];
    if (!parent || !parent.connections.children) return [];
    return parent.connections.children.map(id => noteSystem[id]).filter(Boolean);
  };

  const handleNoteClick = (note) => {
    setSelectedNote(note);
    if (note.connections.children && note.connections.children.length > 0) {
      setCurrentLevel(note.abstractionLevel + 1);
    }
  };

  const handleLevelUp = () => {
    if (currentLevel > 0) {
      setCurrentLevel(currentLevel - 1);
      // Find parent of current selected note
      if (selectedNote && selectedNote.connections.parent) {
        setSelectedNote(noteSystem[selectedNote.connections.parent]);
      }
    }
  };

  const StickyNote = ({ note, isSelected, onClick }) => {
    const [isHovered, setIsHovered] = useState(false);
    
    return (
      <div
        className={`
          absolute cursor-pointer transition-all duration-300 transform
          ${isSelected ? 'scale-110 z-20' : 'z-10'}
          ${isHovered ? 'scale-105' : ''}
        `}
        style={{
          left: note.position.x,
          top: note.position.y,
          transform: `scale(${note.viewState.scale})`
        }}
        onClick={() => onClick(note)}
        onMouseEnter={() => setIsHovered(true)}
        onMouseLeave={() => setIsHovered(false)}
      >
        <div
          className={`
            w-48 min-h-32 p-4 rounded-lg shadow-lg border-2 transition-all duration-200
            ${isSelected ? 'ring-4 ring-blue-300' : ''}
            ${isHovered ? 'shadow-xl' : ''}
          `}
          style={{
            backgroundColor: note.metadata.color + '20',
            borderColor: note.metadata.color,
            borderLeftWidth: '6px'
          }}
        >
          <div className="flex justify-between items-start mb-2">
            <h3 className="font-bold text-sm text-gray-800 leading-tight">
              {note.title}
            </h3>
            <div className="flex gap-1">
              {note.connections.children && note.connections.children.length > 0 && (
                <div className="w-2 h-2 rounded-full bg-blue-500" title="Has children"></div>
              )}
              <div 
                className="w-2 h-2 rounded-full" 
                style={{ backgroundColor: note.metadata.color }}
                title={`Level ${note.abstractionLevel}`}
              ></div>
            </div>
          </div>
          
          <p className="text-xs text-gray-600 mb-3 line-clamp-3">
            {note.content_layers.summary}
          </p>
          
          <div className="flex justify-between items-center">
            <div className="flex gap-1">
              {note.metadata.tags.slice(0, 2).map(tag => (
                <span key={tag} className="px-1 py-0.5 bg-gray-200 text-xs rounded">
                  {tag}
                </span>
              ))}
            </div>
            <div className="text-xs text-gray-500">
              L{note.abstractionLevel}
            </div>
          </div>
        </div>
      </div>
    );
  };

  const currentNotes = getNotesAtLevel(currentLevel);

  return (
    <div className="w-full h-screen bg-gradient-to-br from-slate-50 to-blue-50 overflow-hidden">
      {/* Header */}
      <div className="absolute top-0 left-0 right-0 z-30 bg-white/90 backdrop-blur-sm border-b border-gray-200 p-4">
        <div className="flex justify-between items-center">
          <div className="flex items-center gap-4">
            <h1 className="text-xl font-bold text-gray-800">Memory Machine</h1>
            <div className="flex items-center gap-2">
              <button
                onClick={handleLevelUp}
                disabled={currentLevel === 0}
                className="px-3 py-1 bg-blue-500 text-white rounded disabled:bg-gray-300 text-sm"
              >
                ↑ Float Up
              </button>
              <span className="text-sm text-gray-600">Level {currentLevel}</span>
            </div>
          </div>
          
          <div className="flex gap-2">
            <button
              onClick={() => setViewMode('spatial')}
              className={`px-3 py-1 rounded text-sm ${viewMode === 'spatial' ? 'bg-blue-500 text-white' : 'bg-gray-200'}`}
            >
              Spatial
            </button>
            <button
              onClick={() => setViewMode('tree')}
              className={`px-3 py-1 rounded text-sm ${viewMode === 'tree' ? 'bg-blue-500 text-white' : 'bg-gray-200'}`}
            >
              Tree
            </button>
          </div>
        </div>
      </div>

      {/* Main Canvas */}
      <div className="relative w-full h-full pt-20 pb-4">
        {viewMode === 'spatial' && (
          <div className="relative w-full h-full">
            {currentNotes.map(note => (
              <StickyNote
                key={note.id}
                note={note}
                isSelected={selectedNote?.id === note.id}
                onClick={handleNoteClick}
              />
            ))}
          </div>
        )}

        {viewMode === 'tree' && selectedNote && (
          <div className="p-8 max-w-4xl mx-auto">
            <div className="bg-white rounded-lg shadow-lg p-6 mb-6">
              <h2 className="text-xl font-bold mb-4" style={{ color: selectedNote.metadata.color }}>
                {selectedNote.title}
              </h2>
              <div className="grid md:grid-cols-2 gap-4">
                <div>
                  <h4 className="font-semibold text-gray-700 mb-2">Summary</h4>
                  <p className="text-gray-600">{selectedNote.content_layers.summary}</p>
                </div>
                <div>
                  <h4 className="font-semibold text-gray-700 mb-2">Detailed</h4>
                  <p className="text-gray-600">{selectedNote.content_layers.detailed}</p>
                </div>
              </div>
              {selectedNote.content_layers.examples && (
                <div className="mt-4">
                  <h4 className="font-semibold text-gray-700 mb-2">Examples</h4>
                  <ul className="list-disc list-inside text-gray-600">
                    {selectedNote.content_layers.examples.map((example, idx) => (
                      <li key={idx}>{example}</li>
                    ))}
                  </ul>
                </div>
              )}
            </div>

            {selectedNote.connections.children && selectedNote.connections.children.length > 0 && (
              <div className="bg-white rounded-lg shadow-lg p-6">
                <h3 className="text-lg font-semibold mb-4">Child Notes</h3>
                <div className="grid gap-3">
                  {getChildNotes(selectedNote.id).map(child => (
                    <div
                      key={child.id}
                      className="p-3 border-l-4 bg-gray-50 cursor-pointer hover:bg-gray-100 transition-colors"
                      style={{ borderColor: child.metadata.color }}
                      onClick={() => handleNoteClick(child)}
                    >
                      <h4 className="font-medium">{child.title}</h4>
                      <p className="text-sm text-gray-600">{child.content_layers.summary}</p>
                    </div>
                  ))}
                </div>
              </div>
            )}
          </div>
        )}
      </div>

      {/* Status Bar */}
      <div className="absolute bottom-0 left-0 right-0 bg-gray-800 text-white p-2 text-xs">
        <div className="flex justify-between">
          <span>{currentNotes.length} notes at level {currentLevel}</span>
          {selectedNote && (
            <span>Selected: {selectedNote.title} | Children: {selectedNote.connections.children?.length || 0}</span>
          )}
        </div>
      </div>
    </div>
  );
};

export default MemoryMachine;
```