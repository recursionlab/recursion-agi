---
nexus: nexus-ai-chat-importer
plugin_version: "1.3.0"
provider: claude
artifact_id: question-generator
version_uuid: 49df5fa9-1fa2-4823-a528-8f2f0c92cc1c
version_number: 1
command: rewrite
conversation_id: 43866886-defd-4d0a-921e-d4cee9a382b5
create_time: 2025-07-05T14:00:45.000Z
format: jsx
aliases: [Intelligent Question Generator, question-generator_v1]
---

# Intelligent Question Generator (Version 1)

**Conversation:** [[Nexus/Conversations/claude/2025/07/AI-Powered Coaching Question Generator|AI-Powered Coaching Question Generator]]

## Content

```jsx
import React, { useState, useCallback } from 'react';
import { Shuffle, Target, Lightbulb, Copy, Zap, Brain, Sparkles } from 'lucide-react';

const QuestionGenerator = () => {
  const [clientProblem, setClientProblem] = useState("I don't know what career to choose");
  const [generatedQuestions, setGeneratedQuestions] = useState([]);
  const [isGenerating, setIsGenerating] = useState(false);

  // Smart question generation using Claude API
  const generateQuestionsWithClaude = async (problem) => {
    const prompt = `You are an expert coach specializing in powerful, breakthrough questions. Your task is to generate 10 exceptional coaching questions based on the client's stated problem.

Client's Problem: "${problem}"

Guidelines for question generation:
1. Create questions that are grammatically correct and naturally flowing
2. Use powerful coaching techniques like reframing, assumption challenging, and perspective shifting
3. Include questions that explore different dimensions: practical, emotional, identity, values, fears, opportunities
4. Avoid repetitive or surface-level questions
5. Make questions that could genuinely lead to breakthrough insights
6. Use varied question structures and approaches

Generate exactly 10 questions. For each question, also provide a brief explanation of the coaching technique/strategy being used.

Respond with a JSON object in this exact format:
{
  "questions": [
    {
      "question": "What would you choose if you knew you couldn't fail?",
      "strategy": "Fear removal technique",
      "category": "Limiting beliefs"
    }
  ]
}

DO NOT OUTPUT ANYTHING OTHER THAN VALID JSON. DON'T INCLUDE LEADING BACKTICKS LIKE \`\`\`json.`;

    try {
      const response = await window.claude.complete(prompt);
      const parsed = JSON.parse(response);
      return parsed.questions || [];
    } catch (error) {
      console.error('Error generating questions:', error);
      return getFallbackQuestions(problem);
    }
  };

  // Fallback questions if Claude API fails
  const getFallbackQuestions = (problem) => {
    const templates = [
      {
        question: `What would choosing feel like if you trusted yourself completely?`,
        strategy: "Self-trust building",
        category: "Inner wisdom"
      },
      {
        question: `What are you afraid would happen if you made the 'wrong' choice?`,
        strategy: "Fear exploration",
        category: "Limiting beliefs"
      },
      {
        question: `If you had to choose right now, what would your gut tell you?`,
        strategy: "Intuition access",
        category: "Inner wisdom"
      },
      {
        question: `What would you advise your best friend if they had this same dilemma?`,
        strategy: "Perspective shifting",
        category: "Clarity"
      },
      {
        question: `What kind of person do you want to become through your career?`,
        strategy: "Identity exploration",
        category: "Values"
      },
      {
        question: `What would you choose if money wasn't a factor?`,
        strategy: "Constraint removal",
        category: "Core desires"
      },
      {
        question: `What patterns do you notice in the careers that excite you?`,
        strategy: "Pattern recognition",
        category: "Self-awareness"
      },
      {
        question: `How might not knowing be serving you right now?`,
        strategy: "Reframing",
        category: "Hidden benefits"
      },
      {
        question: `What would you regret not trying 20 years from now?`,
        strategy: "Future regret minimization",
        category: "Long-term perspective"
      },
      {
        question: `What lights you up when you're not thinking about careers at all?`,
        strategy: "Natural energy exploration",
        category: "Authentic self"
      }
    ];

    return templates;
  };

  // Generate questions
  const generateQuestions = useCallback(async () => {
    if (!clientProblem.trim()) return;
    
    setIsGenerating(true);
    
    try {
      const questions = await generateQuestionsWithClaude(clientProblem);
      const resultsWithTimestamp = questions.map(q => ({
        ...q,
        timestamp: new Date().toLocaleTimeString()
      }));
      
      setGeneratedQuestions(resultsWithTimestamp);
    } catch (error) {
      console.error('Error:', error);
      const fallbackQuestions = getFallbackQuestions(clientProblem);
      setGeneratedQuestions(fallbackQuestions.map(q => ({
        ...q,
        timestamp: new Date().toLocaleTimeString()
      })));
    } finally {
      setIsGenerating(false);
    }
  }, [clientProblem]);

  // Copy to clipboard
  const copyToClipboard = (text) => {
    navigator.clipboard.writeText(text);
  };

  // Copy all questions
  const copyAllQuestions = () => {
    const allQuestions = generatedQuestions.map((q, i) => `${i + 1}. ${q.question}`).join('\n\n');
    navigator.clipboard.writeText(allQuestions);
  };

  // Category colors
  const getCategoryColor = (category) => {
    const colors = {
      'Limiting beliefs': 'bg-red-100 text-red-800',
      'Inner wisdom': 'bg-blue-100 text-blue-800',
      'Clarity': 'bg-green-100 text-green-800',
      'Values': 'bg-purple-100 text-purple-800',
      'Core desires': 'bg-orange-100 text-orange-800',
      'Self-awareness': 'bg-teal-100 text-teal-800',
      'Hidden benefits': 'bg-yellow-100 text-yellow-800',
      'Long-term perspective': 'bg-indigo-100 text-indigo-800',
      'Authentic self': 'bg-pink-100 text-pink-800'
    };
    return colors[category] || 'bg-gray-100 text-gray-800';
  };

  return (
    <div className="max-w-4xl mx-auto p-6 bg-gradient-to-br from-indigo-50 to-purple-50 min-h-screen">
      <div className="text-center mb-8">
        <h1 className="text-4xl font-bold text-gray-800 mb-2">🎯 Intelligent Question Generator</h1>
        <p className="text-gray-600">Generate breakthrough coaching questions using AI-powered analysis</p>
      </div>

      {/* Client Problem Input */}
      <div className="bg-white rounded-xl shadow-lg p-6 mb-6">
        <h3 className="text-lg font-semibold text-gray-800 mb-3 flex items-center">
          <Target className="w-5 h-5 mr-2" />
          Client Problem/Situation
        </h3>
        <textarea
          value={clientProblem}
          onChange={(e) => setClientProblem(e.target.value)}
          className="w-full h-20 p-4 border-2 border-gray-200 rounded-lg focus:border-purple-400 focus:outline-none resize-none"
          placeholder="Enter the client's problem or situation in natural language..."
        />
      </div>

      {/* Generate Button */}
      <div className="bg-white rounded-xl shadow-lg p-6 mb-6">
        <div className="flex gap-4">
          <button
            onClick={generateQuestions}
            disabled={isGenerating || !clientProblem.trim()}
            className="flex-1 flex items-center justify-center gap-2 p-4 bg-gradient-to-r from-purple-500 to-indigo-500 text-white rounded-lg hover:from-purple-600 hover:to-indigo-600 disabled:opacity-50 transition-all"
          >
            {isGenerating ? (
              <div className="animate-spin rounded-full h-5 w-5 border-b-2 border-white" />
            ) : (
              <Sparkles className="w-5 h-5" />
            )}
            {isGenerating ? 'Generating...' : 'Generate Breakthrough Questions'}
          </button>
          {generatedQuestions.length > 0 && (
            <button
              onClick={copyAllQuestions}
              className="flex items-center gap-2 px-4 py-2 bg-gray-500 text-white rounded-lg hover:bg-gray-600 transition-all"
            >
              <Copy className="w-4 h-4" />
              Copy All
            </button>
          )}
        </div>
      </div>

      {/* Generated Questions */}
      {generatedQuestions.length > 0 && (
        <div className="bg-white rounded-xl shadow-lg p-6 mb-6">
          <h3 className="text-lg font-semibold text-gray-800 mb-4 flex items-center">
            <Lightbulb className="w-5 h-5 mr-2" />
            Generated Breakthrough Questions
          </h3>
          <div className="space-y-4">
            {generatedQuestions.map((item, index) => (
              <div
                key={index}
                className="p-4 bg-gradient-to-r from-purple-50 to-indigo-50 rounded-lg border-l-4 border-purple-400"
              >
                <div className="flex justify-between items-start mb-2">
                  <div className="flex gap-2 items-center">
                    <span className="text-xs text-gray-500 font-medium">
                      Question #{index + 1}
                    </span>
                    <span className={`text-xs px-2 py-1 rounded-full ${getCategoryColor(item.category)}`}>
                      {item.category}
                    </span>
                  </div>
                  <button
                    onClick={() => copyToClipboard(item.question)}
                    className="text-gray-400 hover:text-purple-600 transition-colors"
                  >
                    <Copy className="w-4 h-4" />
                  </button>
                </div>
                <p className="text-gray-800 font-medium leading-relaxed mb-2">
                  {item.question}
                </p>
                <p className="text-sm text-gray-600 italic">
                  Strategy: {item.strategy}
                </p>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* How It Works */}
      <div className="bg-white rounded-xl shadow-lg p-6">
        <h3 className="text-lg font-semibold text-gray-800 mb-4 flex items-center">
          <Brain className="w-5 h-5 mr-2" />
          How This Works
        </h3>
        <div className="space-y-3 text-gray-700">
          <p>
            <strong>Intelligent Analysis:</strong> AI analyzes the client's problem to understand context, emotional undertones, and implicit assumptions.
          </p>
          <p>
            <strong>Coaching Techniques:</strong> Applies proven coaching methodologies like reframing, assumption challenging, perspective shifting, and constraint removal.
          </p>
          <p>
            <strong>Natural Language:</strong> Generates grammatically correct, naturally flowing questions that feel authentic and powerful.
          </p>
          <p>
            <strong>Categorized Insights:</strong> Each question targets specific areas like limiting beliefs, inner wisdom, values, and self-awareness.
          </p>
          <p>
            <strong>Breakthrough Focus:</strong> Questions designed to create "aha!" moments and shift clients from stuck to unstuck.
          </p>
        </div>
      </div>
    </div>
  );
};

export default QuestionGenerator;
```