---
nexus: nexus-ai-chat-importer
plugin_version: "1.3.0"
provider: claude
artifact_id: pdf-crafter
version_uuid: af6ae9f0-cf02-42d8-b389-b50e2abf23b0
version_number: 3
command: update
conversation_id: 63431f64-18ff-48ef-9624-189a352b0bb7
create_time: 2025-07-25T07:47:22.000Z
format: jsx
aliases: [Untitled Artifact, pdf-crafter_v3]
---

# Untitled Artifact (Version 3)

**Conversation:** [[Nexus/Conversations/claude/2025/07/Game-Like PDF Artifact Merging|Game-Like PDF Artifact Merging]]

## Content

```jsx
import React, { useState, useRef } from 'react';
import { Upload, Zap, Sparkles, FileText, Trash2, Download } from 'lucide-react';

const PDFCrafter = () => {
  const [artifacts, setArtifacts] = useState([]);
  const [craftingSlots, setCraftingSlots] = useState([null, null]);
  const [isCrafting, setIsCrafting] = useState(false);
  const [craftedResult, setCraftedResult] = useState(null);
  const fileInputRef = useRef(null);

  const rarityColors = {
    common: 'bg-gray-500',
    uncommon: 'bg-green-500',
    rare: 'bg-blue-500',
    epic: 'bg-purple-500',
    legendary: 'bg-orange-500'
  };

  const rarityGlow = {
    common: 'shadow-gray-400/50',
    uncommon: 'shadow-green-400/50',
    rare: 'shadow-blue-400/50',
    epic: 'shadow-purple-400/50',
    legendary: 'shadow-orange-400/50'
  };

  const getRarity = (pageCount) => {
    if (pageCount <= 5) return 'common';
    if (pageCount <= 15) return 'uncommon';
    if (pageCount <= 30) return 'rare';
    if (pageCount <= 50) return 'epic';
    return 'legendary';
  };

  const handleFileUpload = async (event) => {
    const files = Array.from(event.target.files);
    
    for (const file of files) {
      if (file.type === 'application/pdf') {
        // Simulate page count analysis (in real implementation, you'd use PDF.js)
        const pageCount = Math.floor(Math.random() * 60) + 1;
        const rarity = getRarity(pageCount);
        
        const newArtifact = {
          id: Date.now() + Math.random(),
          name: file.name.replace('.pdf', ''),
          file: file,
          pageCount,
          rarity,
          level: 1,
          power: pageCount * 10
        };
        
        setArtifacts(prev => [...prev, newArtifact]);
      }
    }
    
    // Reset file input
    event.target.value = '';
  };

  const addToCraftingSlot = (artifact, slotIndex) => {
    const newSlots = [...craftingSlots];
    newSlots[slotIndex] = artifact;
    setCraftingSlots(newSlots);
    
    // Remove from artifacts list
    setArtifacts(prev => prev.filter(a => a.id !== artifact.id));
  };

  const removeFromCraftingSlot = (slotIndex) => {
    const artifact = craftingSlots[slotIndex];
    if (artifact) {
      // Return to artifacts list
      setArtifacts(prev => [...prev, artifact]);
      
      const newSlots = [...craftingSlots];
      newSlots[slotIndex] = null;
      setCraftingSlots(newSlots);
    }
  };

  const craftArtifacts = async () => {
    if (!craftingSlots[0] || !craftingSlots[1]) return;
    
    setIsCrafting(true);
    
    // Simulate crafting delay
    await new Promise(resolve => setTimeout(resolve, 2000));
    
    const [artifact1, artifact2] = craftingSlots;
    const combinedPages = artifact1.pageCount + artifact2.pageCount;
    const newRarity = getRarity(combinedPages);
    
    // Create combined PDF blob (simulation)
    const craftedArtifact = {
      id: Date.now(),
      name: `${artifact1.name} + ${artifact2.name}`,
      pageCount: combinedPages,
      rarity: newRarity,
      level: Math.max(artifact1.level, artifact2.level) + 1,
      power: combinedPages * 15,
      isCrafted: true
    };
    
    setCraftedResult(craftedArtifact);
    setCraftingSlots([null, null]);
    setIsCrafting(false);
  };

  const collectCraftedArtifact = () => {
    setArtifacts(prev => [...prev, craftedResult]);
    setCraftedResult(null);
  };

  const ArtifactCard = ({ artifact, onClick, isSmall = false, showClickHint = false }) => (
    <div
      className={`
        ${isSmall ? 'p-3' : 'p-4'} rounded-lg border-2 transition-all duration-300
        ${rarityColors[artifact.rarity]} border-opacity-60 hover:border-opacity-100
        bg-gray-800 hover:bg-gray-700 shadow-lg hover:shadow-xl
        ${rarityGlow[artifact.rarity]} hover:shadow-2xl
        transform hover:scale-105
        ${onClick ? 'cursor-pointer' : ''}
        ${showClickHint ? 'ring-2 ring-yellow-400 animate-pulse' : ''}
      `}
      onClick={onClick}
    >
      <div className="flex items-center gap-2 mb-2">
        <FileText className={`${isSmall ? 'w-4 h-4' : 'w-5 h-5'} text-white`} />
        <span className={`font-bold text-white ${isSmall ? 'text-sm' : 'text-base'} capitalize`}>
          {artifact.rarity}
        </span>
      </div>
      <h3 className={`font-semibold text-white mb-1 ${isSmall ? 'text-sm' : 'text-base'}`}>
        {artifact.name}
      </h3>
      <div className={`text-gray-300 ${isSmall ? 'text-xs' : 'text-sm'}`}>
        <div>Pages: {artifact.pageCount}</div>
        <div>Level: {artifact.level}</div>
        <div>Power: {artifact.power}</div>
      </div>
    </div>
  );

  const CraftingSlot = ({ artifact, slotIndex, onRemove }) => (
    <div className={`
      w-48 h-32 border-4 border-dashed border-gray-600 rounded-lg
      flex items-center justify-center bg-gray-900
      ${artifact ? 'border-yellow-500 bg-yellow-900/20' : 'hover:border-gray-500'}
      transition-colors duration-200
    `}>
      {artifact ? (
        <div className="relative w-full h-full p-2">
          <ArtifactCard artifact={artifact} isSmall={true} />
          <button
            onClick={(e) => {
              e.stopPropagation();
              onRemove(slotIndex);
            }}
            className="absolute -top-2 -right-2 w-6 h-6 bg-red-500 rounded-full flex items-center justify-center hover:bg-red-600 transition-colors z-10"
          >
            <Trash2 className="w-3 h-3 text-white" />
          </button>
        </div>
      ) : (
        <div className="text-gray-500 text-center">
          <Upload className="w-8 h-8 mx-auto mb-2" />
          <div className="text-sm">Drop Artifact Here</div>
        </div>
      )}
    </div>
  );

  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-900 via-purple-900 to-gray-900 p-6">
      <div className="max-w-7xl mx-auto">
        <div className="text-center mb-8">
          <h1 className="text-4xl font-bold text-white mb-2 flex items-center justify-center gap-3">
            <Sparkles className="w-10 h-10 text-yellow-400" />
            PDF Artifact Crafter
            <Sparkles className="w-10 h-10 text-yellow-400" />
          </h1>
          <p className="text-gray-300">Combine your PDF artifacts to create more powerful documents!</p>
        </div>

        {/* Upload Section */}
        <div className="mb-8">
          <input
            ref={fileInputRef}
            type="file"
            multiple
            accept=".pdf"
            onChange={handleFileUpload}
            className="hidden"
          />
          <button
            onClick={() => fileInputRef.current?.click()}
            className="w-full p-6 border-2 border-dashed border-gray-600 rounded-lg hover:border-gray-500 transition-colors bg-gray-800/50 hover:bg-gray-800/70"
          >
            <Upload className="w-12 h-12 mx-auto mb-4 text-gray-400" />
            <div className="text-xl font-semibold text-white mb-2">Upload PDF Artifacts</div>
            <div className="text-gray-400">Click to browse or drag and drop PDF files</div>
          </button>
        </div>

        {/* Crafting Area */}
        <div className="bg-gray-800/50 rounded-lg p-6 mb-8 backdrop-blur-sm">
          <h2 className="text-2xl font-bold text-white mb-6 text-center flex items-center justify-center gap-2">
            <Zap className="w-6 h-6 text-yellow-400" />
            Crafting Forge
          </h2>
          
          <div className="flex items-center justify-center gap-8">
            <CraftingSlot 
              artifact={craftingSlots[0]} 
              slotIndex={0} 
              onRemove={removeFromCraftingSlot}
            />
            
            <div className="text-4xl text-white font-bold">+</div>
            
            <CraftingSlot 
              artifact={craftingSlots[1]} 
              slotIndex={1} 
              onRemove={removeFromCraftingSlot}
            />
            
            <div className="text-4xl text-white font-bold">=</div>
            
            {/* Result Area */}
            <div className="w-48 h-32 border-4 border-dashed border-yellow-500 rounded-lg bg-yellow-900/20 flex items-center justify-center">
              {isCrafting ? (
                <div className="text-center">
                  <div className="animate-spin w-8 h-8 border-4 border-yellow-400 border-t-transparent rounded-full mx-auto mb-2"></div>
                  <div className="text-yellow-400 text-sm">Crafting...</div>
                </div>
              ) : craftedResult ? (
                <div className="w-full h-full p-2">
                  <ArtifactCard artifact={craftedResult} isSmall={true} />
                </div>
              ) : (
                <div className="text-yellow-400 text-center">
                  <Sparkles className="w-8 h-8 mx-auto mb-2" />
                  <div className="text-sm">Result</div>
                </div>
              )}
            </div>
          </div>
          
          <div className="flex gap-4 justify-center mt-6">
            <button
              onClick={craftArtifacts}
              disabled={!craftingSlots[0] || !craftingSlots[1] || isCrafting}
              className="px-6 py-3 bg-yellow-600 hover:bg-yellow-700 disabled:bg-gray-600 disabled:cursor-not-allowed text-white font-semibold rounded-lg transition-colors flex items-center gap-2"
            >
              <Zap className="w-5 h-5" />
              {isCrafting ? 'Crafting...' : 'Craft Artifacts'}
            </button>
            
            {craftedResult && (
              <button
                onClick={collectCraftedArtifact}
                className="px-6 py-3 bg-green-600 hover:bg-green-700 text-white font-semibold rounded-lg transition-colors flex items-center gap-2"
              >
                <Download className="w-5 h-5" />
                Collect Artifact
              </button>
            )}
          </div>
        </div>

        {/* Artifacts Inventory */}
        <div>
          <h2 className="text-2xl font-bold text-white mb-6">Your Artifacts ({artifacts.length})</h2>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4">
            {artifacts.map(artifact => (
              <ArtifactCard
                key={artifact.id}
                artifact={artifact}
                onClick={() => {
                  if (!craftingSlots[0]) {
                    addToCraftingSlot(artifact, 0);
                  } else if (!craftingSlots[1]) {
                    addToCraftingSlot(artifact, 1);
                  }
                }}
              />
            ))}
          </div>
          
          {artifacts.length === 0 && (
            <div className="text-center py-12 text-gray-500">
              <FileText className="w-16 h-16 mx-auto mb-4 opacity-50" />
              <div className="text-xl">No artifacts yet</div>
              <div>Upload some PDFs to get started!</div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default PDFCrafter;
```