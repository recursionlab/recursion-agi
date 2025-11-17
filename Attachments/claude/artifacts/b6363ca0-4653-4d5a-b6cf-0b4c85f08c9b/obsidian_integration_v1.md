---
nexus: nexus-ai-chat-importer
plugin_version: "1.3.0"
provider: claude
artifact_id: obsidian_integration
version_uuid: 263b46b1-14b9-4e79-977a-c8ba3d5724b8
version_number: 1
command: create
conversation_id: b6363ca0-4653-4d5a-b6cf-0b4c85f08c9b
create_time: 2025-07-13T17:26:04.000Z
format: jsx
aliases: [Obsidian Recursive Intelligence Extractor, obsidian_integration_v1]
---

# Obsidian Recursive Intelligence Extractor (Version 1)

**Conversation:** [[Nexus/Conversations/claude/2025/07/Strategic Micro-Action Codegen Optimization|Strategic Micro-Action Codegen Optimization]]

## Content

```jsx
import React, { useState, useRef } from 'react';
import { Upload, Brain, Zap, FileText, Network, Target } from 'lucide-react';

const ObsidianIntegrator = () => {
  const [vaultFiles, setVaultFiles] = useState([]);
  const [analysis, setAnalysis] = useState(null);
  const [processing, setProcessing] = useState(false);
  const [frameworks, setFrameworks] = useState(null);
  const fileInputRef = useRef(null);

  const handleVaultUpload = async (event) => {
    const files = Array.from(event.target.files);
    setVaultFiles(files);
    
    // Auto-start processing
    await processVault(files);
  };

  const processVault = async (files) => {
    setProcessing(true);
    
    try {
      // Read all markdown files
      const markdownFiles = files.filter(file => file.name.endsWith('.md'));
      const noteContents = await Promise.all(
        markdownFiles.map(async (file) => {
          const content = await file.text();
          return {
            name: file.name,
            content: content,
            path: file.webkitRelativePath || file.name
          };
        })
      );

      // Extract cognitive patterns
      const patterns = extractCognitivePatterns(noteContents);
      
      // Generate frameworks
      const generatedFrameworks = await generateFrameworks(patterns);
      
      setAnalysis(patterns);
      setFrameworks(generatedFrameworks);
      
    } catch (error) {
      console.error('Processing error:', error);
    } finally {
      setProcessing(false);
    }
  };

  const extractCognitivePatterns = (notes) => {
    const patterns = {
      conceptLinks: new Set(),
      recursiveLoops: [],
      paradoxes: [],
      lacunae: [],
      morphisms: [],
      thoughtMoves: {
        expand: [],
        collapse: [],
        invert: [],
        weave: [],
        recurse: []
      }
    };

    notes.forEach(note => {
      const content = note.content;
      
      // Extract [[links]] - concept connections
      const links = content.match(/\[\[([^\]]+)\]\]/g);
      if (links) {
        links.forEach(link => {
          const concept = link.slice(2, -2);
          patterns.conceptLinks.add(concept);
        });
      }

      // Detect recursive patterns
      const recursiveMarkers = [
        'this reminds me of',
        'similar to what I said about',
        'connects back to',
        'like we discussed'
      ];
      
      recursiveMarkers.forEach(marker => {
        if (content.toLowerCase().includes(marker)) {
          patterns.recursiveLoops.push({
            note: note.name,
            context: extractContext(content, marker),
            marker: marker
          });
        }
      });

      // Detect paradoxes and contradictions
      const paradoxMarkers = [
        'but also',
        'contradicts',
        'paradox',
        'both true and false',
        'simultaneously'
      ];
      
      paradoxMarkers.forEach(marker => {
        if (content.toLowerCase().includes(marker)) {
          patterns.paradoxes.push({
            note: note.name,
            context: extractContext(content, marker),
            type: 'paradox'
          });
        }
      });

      // Detect lacunae (productive gaps)
      const lacunaMarkers = [
        'I don\'t know',
        'not sure',
        'unclear',
        'missing',
        'gap in understanding',
        'what if',
        'maybe'
      ];
      
      lacunaMarkers.forEach(marker => {
        if (content.toLowerCase().includes(marker)) {
          patterns.lacunae.push({
            note: note.name,
            context: extractContext(content, marker),
            type: 'lacuna'
          });
        }
      });

      // Detect thought moves
      const expandMarkers = ['expand', 'broaden', 'zoom out', 'bigger picture'];
      const collapseMarkers = ['focus', 'narrow', 'zoom in', 'specific'];
      const invertMarkers = ['opposite', 'reverse', 'flip', 'invert'];
      const weaveMarkers = ['connect', 'combine', 'integrate', 'synthesize'];
      const recurseMarkers = ['self-reference', 'meta', 'recursive', 'self-similar'];

      [
        [expandMarkers, 'expand'],
        [collapseMarkers, 'collapse'],
        [invertMarkers, 'invert'],
        [weaveMarkers, 'weave'],
        [recurseMarkers, 'recurse']
      ].forEach(([markers, moveType]) => {
        markers.forEach(marker => {
          if (content.toLowerCase().includes(marker)) {
            patterns.thoughtMoves[moveType].push({
              note: note.name,
              context: extractContext(content, marker),
              move: moveType
            });
          }
        });
      });
    });

    return patterns;
  };

  const extractContext = (content, marker) => {
    const index = content.toLowerCase().indexOf(marker.toLowerCase());
    if (index === -1) return '';
    
    const start = Math.max(0, index - 100);
    const end = Math.min(content.length, index + marker.length + 100);
    return content.slice(start, end);
  };

  const generateFrameworks = async (patterns) => {
    // Generate executable frameworks from patterns
    const frameworks = {
      conceptMap: Array.from(patterns.conceptLinks),
      recursiveLoops: patterns.recursiveLoops.length,
      paradoxUtilization: patterns.paradoxes.length,
      lacunaFields: patterns.lacunae.length,
      cognitiveMovements: Object.entries(patterns.thoughtMoves).map(([move, instances]) => ({
        move,
        frequency: instances.length,
        examples: instances.slice(0, 3)
      }))
    };

    return frameworks;
  };

  const triggerVaultUpload = () => {
    fileInputRef.current?.click();
  };

  return (
    <div className="max-w-4xl mx-auto p-6 bg-gray-50 min-h-screen">
      <div className="bg-white rounded-lg shadow-lg p-8">
        <div className="text-center mb-8">
          <Brain className="mx-auto h-16 w-16 text-purple-600 mb-4" />
          <h1 className="text-3xl font-bold text-gray-900 mb-2">
            Obsidian Recursive Intelligence Extractor
          </h1>
          <p className="text-gray-600">
            Transform your conversational notes into executable cognitive frameworks
          </p>
        </div>

        {/* Upload Section */}
        <div className="mb-8">
          <div 
            onClick={triggerVaultUpload}
            className="border-2 border-dashed border-purple-300 rounded-lg p-8 text-center cursor-pointer hover:border-purple-400 hover:bg-purple-50 transition-colors"
          >
            <Upload className="mx-auto h-12 w-12 text-purple-400 mb-4" />
            <p className="text-lg font-medium text-gray-700 mb-2">
              Upload Your Obsidian Vault
            </p>
            <p className="text-gray-500">
              Select your entire vault folder - all .md files will be processed
            </p>
          </div>
          
          <input
            ref={fileInputRef}
            type="file"
            multiple
            webkitdirectory="true"
            directory="true"
            onChange={handleVaultUpload}
            className="hidden"
            accept=".md"
          />
        </div>

        {/* Processing Status */}
        {processing && (
          <div className="mb-8 p-4 bg-blue-50 border border-blue-200 rounded-lg">
            <div className="flex items-center">
              <Zap className="h-5 w-5 text-blue-600 mr-2 animate-spin" />
              <span className="text-blue-800">Processing vault and extracting cognitive patterns...</span>
            </div>
          </div>
        )}

        {/* Results */}
        {analysis && (
          <div className="space-y-6">
            <div className="bg-gradient-to-r from-purple-500 to-blue-600 text-white p-6 rounded-lg">
              <h2 className="text-2xl font-bold mb-4 flex items-center">
                <Target className="mr-2" />
                Cognitive Pattern Analysis
              </h2>
              <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
                <div className="text-center">
                  <div className="text-3xl font-bold">{analysis.conceptLinks.size}</div>
                  <div className="text-sm opacity-90">Concept Links</div>
                </div>
                <div className="text-center">
                  <div className="text-3xl font-bold">{analysis.recursiveLoops.length}</div>
                  <div className="text-sm opacity-90">Recursive Loops</div>
                </div>
                <div className="text-center">
                  <div className="text-3xl font-bold">{analysis.paradoxes.length}</div>
                  <div className="text-sm opacity-90">Paradoxes</div>
                </div>
                <div className="text-center">
                  <div className="text-3xl font-bold">{analysis.lacunae.length}</div>
                  <div className="text-sm opacity-90">Lacuna Fields</div>
                </div>
              </div>
            </div>

            {/* Thought Moves Analysis */}
            <div className="bg-white border border-gray-200 rounded-lg p-6">
              <h3 className="text-xl font-bold mb-4 flex items-center">
                <Network className="mr-2 text-green-600" />
                Cognitive Movement Patterns
              </h3>
              <div className="space-y-3">
                {frameworks?.cognitiveMovements.map((movement, idx) => (
                  <div key={idx} className="flex items-center justify-between p-3 bg-gray-50 rounded">
                    <div className="flex items-center">
                      <div className="w-3 h-3 bg-green-500 rounded-full mr-3"></div>
                      <span className="font-medium capitalize">{movement.move}</span>
                    </div>
                    <span className="text-gray-600">{movement.frequency} instances</span>
                  </div>
                ))}
              </div>
            </div>

            {/* Recursive Loops */}
            {analysis.recursiveLoops.length > 0 && (
              <div className="bg-white border border-gray-200 rounded-lg p-6">
                <h3 className="text-xl font-bold mb-4 flex items-center">
                  <FileText className="mr-2 text-blue-600" />
                  Recursive Thinking Patterns
                </h3>
                <div className="space-y-3">
                  {analysis.recursiveLoops.slice(0, 5).map((loop, idx) => (
                    <div key={idx} className="p-3 bg-blue-50 rounded">
                      <div className="font-medium text-blue-800">{loop.note}</div>
                      <div className="text-sm text-gray-600 mt-1">
                        "{loop.context.slice(0, 120)}..."
                      </div>
                    </div>
                  ))}
                </div>
              </div>
            )}

            {/* Paradoxes */}
            {analysis.paradoxes.length > 0 && (
              <div className="bg-white border border-gray-200 rounded-lg p-6">
                <h3 className="text-xl font-bold mb-4 flex items-center">
                  <Zap className="mr-2 text-orange-600" />
                  Paradox Navigation Points
                </h3>
                <div className="space-y-3">
                  {analysis.paradoxes.slice(0, 5).map((paradox, idx) => (
                    <div key={idx} className="p-3 bg-orange-50 rounded">
                      <div className="font-medium text-orange-800">{paradox.note}</div>
                      <div className="text-sm text-gray-600 mt-1">
                        "{paradox.context.slice(0, 120)}..."
                      </div>
                    </div>
                  ))}
                </div>
              </div>
            )}

            {/* Action Items */}
            <div className="bg-gradient-to-r from-green-500 to-teal-600 text-white p-6 rounded-lg">
              <h3 className="text-xl font-bold mb-4">Next Steps: Framework Integration</h3>
              <div className="space-y-2">
                <div className="flex items-center">
                  <div className="w-2 h-2 bg-white rounded-full mr-3"></div>
                  <span>Extract {analysis.conceptLinks.size} concepts into recursive knowledge graph</span>
                </div>
                <div className="flex items-center">
                  <div className="w-2 h-2 bg-white rounded-full mr-3"></div>
                  <span>Convert {analysis.paradoxes.length} paradoxes into productive cognitive tensions</span>
                </div>
                <div className="flex items-center">
                  <div className="w-2 h-2 bg-white rounded-full mr-3"></div>
                  <span>Transform {analysis.lacunae.length} gaps into generative lacuna fields</span>
                </div>
                <div className="flex items-center">
                  <div className="w-2 h-2 bg-white rounded-full mr-3"></div>
                  <span>Amplify {analysis.recursiveLoops.length} recursive patterns into meta-cognitive tools</span>
                </div>
              </div>
            </div>
          </div>
        )}

        {vaultFiles.length === 0 && (
          <div className="text-center py-8">
            <p className="text-gray-500">
              Upload your Obsidian vault to begin extracting cognitive patterns
            </p>
          </div>
        )}
      </div>
    </div>
  );
};

export default ObsidianIntegrator;
```