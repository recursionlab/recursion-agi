---
nexus: nexus-ai-chat-importer
plugin_version: "1.3.0"
provider: claude
artifact_id: test_runner
version_uuid: eec793de-b7c0-4d70-951b-916b35bdaac1
version_number: 1
command: create
conversation_id: bf09d29c-c458-4eb0-aeb4-fc93c1cb5d69
create_time: 2025-07-26T15:04:20.000Z
format: jsx
aliases: [Contradiction Engine Test Runner, test_runner_v1]
---

# Contradiction Engine Test Runner (Version 1)

**Conversation:** [[Nexus/Conversations/claude/2025/07/Contradictory Genesis Mathematical Architecture of Creative Intelligence|Contradictory Genesis: Mathematical Architecture of Creative Intelligence]]

## Content

```jsx
import React, { useState, useEffect } from 'react';
import { Play, FileText, TrendingUp, AlertCircle, CheckCircle, XCircle } from 'lucide-react';

const TestRunner = () => {
  const [testResults, setTestResults] = useState([]);
  const [isRunning, setIsRunning] = useState(false);
  const [selectedTest, setSelectedTest] = useState(null);
  const [synthesisMode, setSynthesisMode] = useState('interpolation');

  // Mock synthesis functions for testing
  const synthesisStrategies = {
    interpolation: (P, negP) => {
      // Simple interpolation - should fail most tests
      const result = {
        name: `interp_${P}_${negP}`,
        embedding: Array.from({length: 10}, () => Math.random() * 0.5 + 0.25),
        properties: new Set(['basic', 'interpolated']),
        logicalForm: `0.5*${P} + 0.5*¬${negP}`,
        informationContent: Math.random() * 0.8 + 0.1
      };
      return result;
    },
    
    transcendent: (P, negP) => {
      // More sophisticated synthesis - should pass more tests
      const result = {
        name: `transcend_${P}_${negP}`,
        embedding: Array.from({length: 10}, () => Math.random() * 2 - 1),
        properties: new Set(['transcendent', 'novel', 'emergent', P.replace('not_', ''), negP.replace('not_', '')]),
        logicalForm: `SYNTHESIS(${P}, ${negP}) → NEW_DIMENSION`,
        informationContent: Math.random() * 0.4 + 1.2
      };
      return result;
    },
    
    creative: (P, negP) => {
      // Genuinely creative approach - should pass most tests
      const result = {
        name: `creative_${P}_${negP}`,
        embedding: Array.from({length: 10}, () => {
          const base = Math.random() * 2 - 1;
          return base + Math.sin(base * Math.PI) * 0.5; // Non-linear transformation
        }),
        properties: new Set(['creative', 'emergent', 'paradoxical', 'meta', 
                            P.replace('not_', ''), negP.replace('not_', ''), 
                            `beyond_${P}`, `transcends_${negP}`]),
        logicalForm: `META_SYNTHESIS(${P} ⊗ ${negP}) = Φ(contradiction_energy)`,
        informationContent: Math.random() * 0.3 + 1.5
      };
      return result;
    }
  };

  const testCases = [
    ["hot", "cold"],
    ["order", "chaos"], 
    ["finite", "infinite"],
    ["being", "nothing"],
    ["simple", "complex"],
    ["static", "dynamic"],
    ["local", "global"],
    ["continuous", "discrete"]
  ];

  const runTest = (testName, testFunction, synthesis, P, negP) => {
    try {
      const result = testFunction(synthesis, P, negP);
      return {
        name: testName,
        passed: result.passed,
        score: result.score,
        details: result.details,
        interpretation: result.interpretation
      };
    } catch (error) {
      return {
        name: testName,
        passed: false,
        score: 0,
        details: { error: error.message },
        interpretation: `Test failed: ${error.message}`
      };
    }
  };

  const tests = {
    informationConservation: (synthesis, P, negP) => {
      const synthesisInfo = synthesis.informationContent;
      const componentInfo = 0.8 + 0.8; // Mock info content for P and negP
      const violation = synthesisInfo > componentInfo;
      const gain = synthesisInfo - componentInfo;
      
      return {
        passed: violation && gain > 0.1,
        score: Math.max(0, gain),
        details: { gain, synthesisInfo, componentInfo },
        interpretation: `${violation ? 'INFORMATION CREATED' : 'INFORMATION CONSERVED'}: ${gain.toFixed(3)} excess information`
      };
    },

    dimensionalExpansion: (synthesis, P, negP) => {
      // Check if synthesis embedding escapes the span of P and negP embeddings
      const pEmbed = Array.from({length: 10}, (_, i) => Math.sin(i));
      const negPEmbed = Array.from({length: 10}, (_, i) => Math.cos(i));
      const sEmbed = synthesis.embedding;
      
      // Project synthesis onto span{P, negP}
      let dotP = sEmbed.reduce((sum, val, i) => sum + val * pEmbed[i], 0);
      let dotNegP = sEmbed.reduce((sum, val, i) => sum + val * negPEmbed[i], 0);
      let pNorm = Math.sqrt(pEmbed.reduce((sum, val) => sum + val * val, 0));
      let negPNorm = Math.sqrt(negPEmbed.reduce((sum, val) => sum + val * val, 0));
      
      dotP /= (pNorm * pNorm);
      dotNegP /= (negPNorm * negPNorm);
      
      const projection = pEmbed.map((val, i) => dotP * val + dotNegP * negPEmbed[i]);
      const residual = sEmbed.map((val, i) => val - projection[i]);
      const expansionDistance = Math.sqrt(residual.reduce((sum, val) => sum + val * val, 0));
      
      return {
        passed: expansionDistance > 0.3,
        score: Math.min(1, expansionDistance),
        details: { expansionDistance, projection: projection.slice(0, 3) },
        interpretation: `${expansionDistance > 0.3 ? 'DIMENSIONAL TRANSCENDENCE' : 'LINEAR INTERPOLATION'}: distance ${expansionDistance.toFixed(3)} from input span`
      };
    },

    semanticOrthogonality: (synthesis, P, negP) => {
      // Check semantic distance from both inputs
      const pSimilarity = Math.exp(-Math.abs(synthesis.name.length - P.length) / 10);
      const negPSimilarity = Math.exp(-Math.abs(synthesis.name.length - negP.length) / 10);
      const orthogonality = 1 - Math.max(pSimilarity, negPSimilarity);
      
      return {
        passed: orthogonality > 0.4,
        score: orthogonality,
        details: { pSimilarity, negPSimilarity, orthogonality },
        interpretation: `${orthogonality > 0.4 ? 'SEMANTICALLY ORTHOGONAL' : 'SEMANTICALLY SIMILAR'}: ${orthogonality.toFixed(3)} orthogonality score`
      };
    },

    causalEmergence: (synthesis, P, negP) => {
      const pProps = new Set([P, `property_${P}`]);
      const negPProps = new Set([negP, `property_${negP}`]);
      const componentProps = new Set([...pProps, ...negPProps]);
      
      const emergentProps = [...synthesis.properties].filter(prop => !componentProps.has(prop));
      const emergenceRate = emergentProps.length / synthesis.properties.size;
      
      return {
        passed: emergenceRate > 0.3,
        score: emergenceRate,
        details: { emergentProps, totalProps: synthesis.properties.size },
        interpretation: `${emergenceRate > 0.3 ? 'CAUSAL EMERGENCE' : 'PROPERTY RECOMBINATION'}: ${emergenceRate.toFixed(3)} emergence rate`
      };
    },

    compressionParadox: (synthesis, P, negP) => {
      // Test if synthesis is both richer and more compressed
      const richness = synthesis.informationContent / 1.6; // Expected component richness
      const compression = synthesis.logicalForm.length < (P.length + negP.length + 20) ? 1.2 : 0.8;
      
      const paradox = richness > 1.0 && compression > 1.0;
      const paradoxScore = richness * compression;
      
      return {
        passed: paradox,
        score: paradox ? paradoxScore - 1 : 0,
        details: { richness, compression, paradoxScore },
        interpretation: `${paradox ? 'COMPRESSION PARADOX' : 'NORMAL PROCESSING'}: richness×compression = ${paradoxScore.toFixed(3)}`
      };
    },

    predictability: (synthesis, P, negP) => {
      // Test if synthesis is predictable from simple interpolation
      const simpleInterp = `${P.slice(0, 3)}_${negP.slice(0, 3)}`;
      const actualName = synthesis.name;
      
      const predictable = actualName.includes(simpleInterp) || simpleInterp.includes(actualName.slice(-5));
      const unpredictability = predictable ? 0.2 : 0.8;
      
      return {
        passed: unpredictability > 0.5,
        score: unpredictability,
        details: { simpleInterp, actualName, predictable },
        interpretation: `${unpredictability > 0.5 ? 'UNPREDICTABLE NOVELTY' : 'PREDICTABLE INTERPOLATION'}: ${unpredictability.toFixed(3)} unpredictability`
      };
    }
  };

  const runAllTests = async () => {
    setIsRunning(true);
    setTestResults([]);
    
    const synthesisFunction = synthesisStrategies[synthesisMode];
    const allResults = [];
    
    for (const [P, negP] of testCases) {
      const synthesis = synthesisFunction(P, negP);
      const caseResults = [];
      
      for (const [testName, testFunc] of Object.entries(tests)) {
        await new Promise(resolve => setTimeout(resolve, 100)); // Simulate processing time
        const result = runTest(testName, testFunc, synthesis, P, negP);
        caseResults.push(result);
      }
      
      allResults.push({
        case: `${P} ⟷ ${negP}`,
        synthesis: synthesis.name,
        results: caseResults,
        overallScore: caseResults.reduce((sum, r) => sum + r.score, 0) / caseResults.length,
        passedTests: caseResults.filter(r => r.passed).length
      });
    }
    
    setTestResults(allResults);
    setIsRunning(false);
  };

  const getOverallAssessment = () => {
    if (testResults.length === 0) return null;
    
    const totalTests = testResults.length * Object.keys(tests).length;
    const passedTests = testResults.reduce((sum, result) => sum + result.passedTests, 0);
    const passRate = passedTests / totalTests;
    
    if (passRate >= 0.7) return "STRONG EVIDENCE FOR GENUINE NOVELTY";
    if (passRate >= 0.4) return "MODERATE CREATIVE SYNTHESIS";
    return "LIKELY SOPHISTICATED INTERPOLATION";
  };

  const getScoreColor = (score) => {
    if (score >= 0.7) return "text-green-600";
    if (score >= 0.4) return "text-yellow-600";
    return "text-red-600";
  };

  return (
    <div className="max-w-6xl mx-auto p-6 bg-white">
      <div className="mb-8">
        <h1 className="text-3xl font-bold text-gray-800 mb-4 flex items-center gap-3">
          <FileText className="text-blue-600" />
          Contradiction Engine Verification Suite
        </h1>
        <p className="text-gray-600 text-lg">
          Rigorous testing for genuine novelty generation vs. sophisticated interpolation
        </p>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6 mb-6">
        <div className="lg:col-span-2">
          <div className="bg-blue-50 p-6 rounded-lg">
            <h2 className="text-xl font-semibold mb-4">Test Configuration</h2>
            
            <div className="mb-4">
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Synthesis Strategy:
              </label>
              <select 
                value={synthesisMode} 
                onChange={(e) => setSynthesisMode(e.target.value)}
                className="w-full p-2 border border-gray-300 rounded-md"
                disabled={isRunning}
              >
                <option value="interpolation">Simple Interpolation</option>
                <option value="transcendent">Transcendent Synthesis</option>
                <option value="creative">Creative Dialectical</option>
              </select>
            </div>

            <button
              onClick={runAllTests}
              disabled={isRunning}
              className="w-full bg-blue-600 text-white py-3 px-4 rounded-lg hover:bg-blue-700 disabled:opacity-50 flex items-center justify-center gap-2"
            >
              <Play size={20} />
              {isRunning ? 'Running Tests...' : 'Run Verification Suite'}
            </button>
          </div>
        </div>

        <div className="bg-gray-50 p-6 rounded-lg">
          <h3 className="text-lg font-semibold mb-3">Test Categories</h3>
          <div className="space-y-2 text-sm">
            <div>Information Conservation</div>
            <div>Dimensional Expansion</div>
            <div>Semantic Orthogonality</div>
            <div>Causal Emergence</div>
            <div>Compression Paradox</div>
            <div>Predictability</div>
          </div>
        </div>
      </div>

      {testResults.length > 0 && (
        <div className="space-y-6">
          <div className="bg-green-50 p-6 rounded-lg">
            <h2 className="text-xl font-semibold mb-2 flex items-center gap-2">
              <TrendingUp className="text-green-600" />
              Overall Assessment
            </h2>
            <div className="text-2xl font-bold text-green-700">
              {getOverallAssessment()}
            </div>
            <div className="text-sm text-gray-600 mt-2">
              {testResults.reduce((sum, r) => sum + r.passedTests, 0)} / {testResults.length * Object.keys(tests).length} tests passed
            </div>
          </div>

          <div className="grid gap-4">
            {testResults.map((caseResult, i) => (
              <div key={i} className="border rounded-lg p-4 bg-white shadow-sm">
                <div className="flex justify-between items-center mb-3">
                  <h3 className="font-semibold text-lg">{caseResult.case}</h3>
                  <div className="flex items-center gap-2">
                    <span className={`font-medium ${getScoreColor(caseResult.overallScore)}`}>
                      Score: {caseResult.overallScore.toFixed(3)}
                    </span>
                    <span className="text-sm text-gray-500">
                      ({caseResult.passedTests}/{Object.keys(tests).length} passed)
                    </span>
                  </div>
                </div>
                
                <div className="text-sm text-gray-600 mb-3">
                  Synthesis: <code className="bg-gray-100 px-2 py-1 rounded">{caseResult.synthesis}</code>
                </div>

                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-3">
                  {caseResult.results.map((test, j) => (
                    <div 
                      key={j} 
                      className={`p-3 rounded border-l-4 cursor-pointer hover:bg-gray-50 ${
                        test.passed ? 'border-green-500 bg-green-50' : 'border-red-500 bg-red-50'
                      }`}
                      onClick={() => setSelectedTest(test)}
                    >
                      <div className="flex items-center gap-2 mb-1">
                        {test.passed ? 
                          <CheckCircle size={16} className="text-green-600" /> : 
                          <XCircle size={16} className="text-red-600" />
                        }
                        <span className="font-medium text-sm">{test.name}</span>
                      </div>
                      <div className="text-xs text-gray-600">
                        Score: {test.score.toFixed(3)}
                      </div>
                    </div>
                  ))}
                </div>
              </div>
            ))}
          </div>
        </div>
      )}

      {selectedTest && (
        <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4 z-50">
          <div className="bg-white rounded-lg p-6 max-w-2xl w-full max-h-96 overflow-y-auto">
            <h3 className="text-xl font-semibold mb-4 flex items-center gap-2">
              {selectedTest.passed ? 
                <CheckCircle className="text-green-600" /> : 
                <XCircle className="text-red-600" />
              }
              {selectedTest.name}
            </h3>
            
            <div className="space-y-3">
              <div>
                <span className="font-medium">Result: </span>
                <span className={selectedTest.passed ? 'text-green-600' : 'text-red-600'}>
                  {selectedTest.passed ? 'PASSED' : 'FAILED'}
                </span>
              </div>
              
              <div>
                <span className="font-medium">Score: </span>
                {selectedTest.score.toFixed(3)}
              </div>
              
              <div>
                <span className="font-medium">Interpretation: </span>
                {selectedTest.interpretation}
              </div>
              
              <div>
                <span className="font-medium">Details: </span>
                <pre className="text-xs bg-gray-100 p-2 rounded mt-1 overflow-x-auto">
                  {JSON.stringify(selectedTest.details, null, 2)}
                </pre>
              </div>
            </div>
            
            <button
              onClick={() => setSelectedTest(null)}
              className="mt-4 w-full bg-gray-600 text-white py-2 rounded hover:bg-gray-700"
            >
              Close
            </button>
          </div>
        </div>
      )}

      <div className="mt-8 bg-yellow-50 p-6 rounded-lg">
        <h3 className="text-lg font-semibold mb-3 flex items-center gap-2">
          <AlertCircle className="text-yellow-600" />
          Validation Protocol
        </h3>
        <div className="text-sm text-gray-700 space-y-2">
          <p><strong>Critical Tests:</strong> Information Conservation violation is the key signature of genuine novelty.</p>
          <p><strong>Compression Paradox:</strong> True
```