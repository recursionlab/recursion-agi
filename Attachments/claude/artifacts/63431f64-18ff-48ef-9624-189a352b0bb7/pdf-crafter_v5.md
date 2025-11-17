---
nexus: nexus-ai-chat-importer
plugin_version: "1.3.0"
provider: claude
artifact_id: pdf-crafter
version_uuid: 39faa50a-4b86-41db-9ff1-38019f5ce687
version_number: 5
command: rewrite
conversation_id: 63431f64-18ff-48ef-9624-189a352b0bb7
create_time: 2025-07-25T07:48:39.000Z
format: jsx
aliases: [Untitled Artifact, pdf-crafter_v5]
---

# Untitled Artifact (Version 5)

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

  const handleUploadClick = () => {
    console.log('Upload clicked');
    if (fileInputRef.current) {
      fileInputRef.current.click();
    }
  };

  const handleFileUpload = async (event) => {
    console.log('File upload triggered');
    const files = Array.from(event.target.files);
    
    for (const file of files) {
      if (file.type === 'application/pdf') {
        // Simulate page count analysis
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

  const handleArtifactClick = (artifact) => {
    console.log('Artifact clicked:', artifact.name);
    if (!craftingSlots[0]) {
      addToCraftingSlot(artifact, 0);
    } else if (!craftingSlots[1]) {
      addToCraftingSlot(artifact, 1);
    }
  };

  const addToCraftingSlot = (artifact, slotIndex) => {
    console.log('Adding to slot:', slotIndex, artifact.name);
    const newSlots = [...craftingSlots];
    newSlots[slotIndex] = artifact;
    setCraftingSlots(newSlots);
    
    // Remove from artifacts list
    setArtifacts(prev => prev.filter(a => a.id !== artifact.id));
  };

  const removeFromCraftingSlot = (slotIndex) => {
    console.log('Removing from slot:', slotIndex);
    const artifact = craftingSlots[slotIndex];
    if (artifact) {
      // Return to artifacts list
      setArtifacts(prev => [...prev, artifact]);
      
      const newSlots = [...craftingSlots];
      newSlots[slotIndex] = null;
      setCraftingSlots(newSlots);
    }
  };

  const handleCraftClick = async () => {
    console.log('Craft clicked');
    if (!craftingSlots[0] || !craftingSlots[1]) return;
    
    setIsCrafting(true);
    
    // Simulate crafting delay
    await new Promise(resolve => setTimeout(resolve, 2000));
    
    const [artifact1, artifact2] = craftingSlots;
    const combinedPages = artifact1.pageCount + artifact2.pageCount;
    const newRarity = getRarity(combinedPages);
    
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

  const handleCollectClick = () => {
    console.log('Collect clicked');
    setArtifacts(prev => [...prev, craftedResult]);
    setCraftedResult(null);
  };

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
          <div
            onClick={handleUploadClick}
            className="w-full p-6 border-2 border-dashed border-gray-600 rounded-lg hover:border-gray-500 transition-colors bg-gray-800/50 hover:bg-gray-800/70 cursor-pointer"
          >
            <Upload className="w-12 h-12 mx-auto mb-4 text-gray-400" />
            <div className="text-xl font-semibold text-white mb-2">Upload PDF Artifacts</div>
            <div className="text-gray-400">Click to browse or drag and drop PDF files</div>
          </div>
        </div>

        {/* Crafting Area */}
        <div className="bg-gray-800/50 rounded-lg p-6 mb-8 backdrop-blur-sm">
          <h2 className="text-2xl font-bold text-white mb-6 text-center flex items-center justify-center gap-2">
            <Zap className="w-6 h-6 text-yellow-400" />
            Crafting Forge
          </h2>
          
          <div className="flex items-center justify-center gap-8 mb-6">
            {/* Slot 1 */}
            <div className={`
              w-48 h-32 border-4 border-dashed rounded-lg flex items-center justify-center
              ${craftingSlots[0] ? 'border-yellow-500 bg-yellow-900/20' : 'border-gray-600 bg-gray-900 hover:border-gray-500'}
              transition-colors duration-200
            `}>
              {craftingSlots[0] ? (
                <div className="relative w-full h-full">
                  <div className="p-3 rounded-lg bg-gray-800 border-2 border-opacity-60" 
                       style={{borderColor: craftingSlots[0].rarity === 'common' ? '#6b7280' : 
                                            craftingSlots[0].rarity === 'uncommon' ? '#10b981' :
                                            craftingSlots[0].rarity === 'rare' ? '#3b82f6' :
                                            craftingSlots[0].rarity === 'epic' ? '#8b5cf6' : '#f97316'}}>
                    <div className="flex items-center gap-2 mb-2">
                      <FileText className="w-4 h-4 text-white" />
                      <span className="font-bold text-white text-sm capitalize">
                        {craftingSlots[0].rarity}
                      </span>
                    </div>
                    <h3 className="font-semibold text-white mb-1 text-sm">
                      {craftingSlots[0].name}
                    </h3>
                    <div className="text-gray-300 text-xs">
                      <div>Pages: {craftingSlots[0].pageCount}</div>
                      <div>Level: {craftingSlots[0].level}</div>
                      <div>Power: {craftingSlots[0].power}</div>
                    </div>
                  </div>
                  <button
                    onClick={() => removeFromCraftingSlot(0)}
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
            
            <div className="text-4xl text-white font-bold">+</div>
            
            {/* Slot 2 */}
            <div className={`
              w-48 h-32 border-4 border-dashed rounded-lg flex items-center justify-center
              ${craftingSlots[1] ? 'border-yellow-500 bg-yellow-900/20' : 'border-gray-600 bg-gray-900 hover:border-gray-500'}
              transition-colors duration-200
            `}>
              {craftingSlots[1] ? (
                <div className="relative w-full h-full">
                  <div className="p-3 rounded-lg bg-gray-800 border-2 border-opacity-60"
                       style={{borderColor: craftingSlots[1].rarity === 'common' ? '#6b7280' : 
                                            craftingSlots[1].rarity === 'uncommon' ? '#10b981' :
                                            craftingSlots[1].rarity === 'rare' ? '#3b82f6' :
                                            craftingSlots[1].rarity === 'epic' ? '#8b5cf6' : '#f97316'}}>
                    <div className="flex items-center gap-2 mb-2">
                      <FileText className="w-4 h-4 text-white" />
                      <span className="font-bold text-white text-sm capitalize">
                        {craftingSlots[1].rarity}
                      </span>
                    </div>
                    <h3 className="font-semibold text-white mb-1 text-sm">
                      {craftingSlots[1].name}
                    </h3>
                    <div className="text-gray-300 text-xs">
                      <div>Pages: {craftingSlots[1].pageCount}</div>
                      <div>Level: {craftingSlots[1].level}</div>
                      <div>Power: {craftingSlots[1].power}</div>
                    </div>
                  </div>
                  <button
                    onClick={() => removeFromCraftingSlot(1)}
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
                  <div className="p-3 rounded-lg bg-gray-800 border-2 border-opacity-60"
                       style={{borderColor: craftedResult.rarity === 'common' ? '#6b7280' : 
                                            craftedResult.rarity === 'uncommon' ? '#10b981' :
                                            craftedResult.rarity === 'rare' ? '#3b82f6' :
                                            craftedResult.rarity === 'epic' ? '#8b5cf6' : '#f97316'}}>
                    <div className="flex items-center gap-2 mb-2">
                      <FileText className="w-4 h-4 text-white" />
                      <span className="font-bold text-white text-sm capitalize">
                        {craftedResult.rarity}
                      </span>
                    </div>
                    <h3 className="font-semibold text-white mb-1 text-sm">
                      {craftedResult.name}
                    </h3>
                    <div className="text-gray-300 text-xs">
                      <div>Pages: {craftedResult.pageCount}</div>
                      <div>Level: {craftedResult.level}</div>
                      <div>Power: {craftedResult.power}</div>
                    </div>
                  </div>
                </div>
              ) : (
                <div className="text-yellow-400 text-center">
                  <Sparkles className="w-8 h-8 mx-auto mb-2" />
                  <div className="text-sm">Result</div>
                </div>
              )}
            </div>
          </div>
          
          <div className="flex gap-4 justify-center">
            <button
              onClick={handleCraftClick}
              disabled={!craftingSlots[0] || !craftingSlots[1] || isCrafting}
              className="px-6 py-3 bg-yellow-600 hover:bg-yellow-700 disabled:bg-gray-600 disabled:cursor-not-allowed text-white font-semibold rounded-lg transition-colors flex items-center gap-2"
            >
              <Zap className="w-5 h-5" />
              {isCrafting ? 'Crafting...' : 'Craft Artifacts'}
            </button>
            
            {craftedResult && (
              <button
                onClick={handleCollectClick}
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
              <div
                key={artifact.id}
                onClick={() => handleArtifactClick(artifact)}
                className={`
                  p-4 rounded-lg border-2 cursor-pointer transition-all duration-300
                  bg-gray-800 hover:bg-gray-700 shadow-lg hover:shadow-xl
                  transform hover:scale-105 border-opacity-60 hover:border-opacity-100
                  ${(!craftingSlots[0] || !craftingSlots[1]) ? 'ring-2 ring-yellow-400 animate-pulse' : ''}
                `}
                style={{
                  borderColor: artifact.rarity === 'common' ? '#6b7280' : 
                               artifact.rarity === 'uncommon' ? '#10b981' :
                               artifact.rarity === 'rare' ? '#3b82f6' :
                               artifact.rarity === 'epic' ? '#8b5cf6' : '#f97316',
                  boxShadow: `0 10px 25px -3px ${
                    artifact.rarity === 'common' ? 'rgba(107, 114, 128, 0.5)' : 
                    artifact.rarity === 'uncommon' ? 'rgba(16, 185, 129, 0.5)' :
                    artifact.rarity === 'rare' ? 'rgba(59, 130, 246, 0.5)' :
                    artifact.rarity === 'epic' ? 'rgba(139, 92, 246, 0.5)' : 'rgba(249, 115, 22, 0.5)'
                  }`
                }}
              >
                <div className="flex items-center gap-2 mb-2">
                  <FileText className="w-5 h-5 text-white" />
                  <span className="font-bold text-white text-base capitalize">
                    {artifact.rarity}
                  </span>
                </div>
                <h3 className="font-semibold text-white mb-1 text-base">
                  {artifact.name}
                </h3>
                <div className="text-gray-300 text-sm">
                  <div>Pages: {artifact.pageCount}</div>
                  <div>Level: {artifact.level}</div>
                  <div>Power: {artifact.power}</div>
                </div>
              </div>
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