---
nexus: nexus-ai-chat-importer
plugin_version: "1.3.0"
provider: claude
artifact_id: ai-opportunity-finder
version_uuid: 0f5c32c6-aa17-4b10-8f2e-ca19fd1749f2
version_number: 2
command: update
conversation_id: fb5b91f7-a93c-4fd6-a66f-7b73c4bf40b0
create_time: 2025-07-04T06:01:25.000Z
format: jsx
aliases: [Untitled Artifact, ai-opportunity-finder_v2]
---

# Untitled Artifact (Version 2)

**Conversation:** [[Nexus/Conversations/claude/2025/07/AI Integration Strategies|AI Integration Strategies]]

## Content

```jsx
import React, { useState } from 'react';
import { MessageCircle, Lightbulb, ArrowRight, RotateCcw } from 'lucide-react';

const AIOpportunityFinder = () => {
  const [currentStep, setCurrentStep] = useState(0);
  const [responses, setResponses] = useState({});
  const [currentResponse, setCurrentResponse] = useState('');
  const [isAnalyzing, setIsAnalyzing] = useState(false);
  const [recommendations, setRecommendations] = useState([]);

  const questions = [
    {
      id: 'role',
      question: "What's your current role or main area of work?",
      placeholder: "e.g., Marketing manager, small business owner, student, freelancer..."
    },
    {
      id: 'tasks',
      question: "What tasks do you spend the most time on in a typical week?",
      placeholder: "e.g., Writing emails, analyzing data, creating content, managing schedules..."
    },
    {
      id: 'pain_points',
      question: "What's your biggest frustration or time-waster in your work?",
      placeholder: "e.g., Repetitive tasks, information overload, manual data entry..."
    },
    {
      id: 'goals',
      question: "What would you like to achieve or improve in the next 6 months?",
      placeholder: "e.g., Save time, increase productivity, learn new skills, grow business..."
    },
    {
      id: 'tech_comfort',
      question: "How comfortable are you with technology? Any tools you already use?",
      placeholder: "e.g., Very comfortable, use APIs; Moderate, use Excel; Prefer simple tools..."
    },
    {
      id: 'resources',
      question: "What's your situation regarding time and budget for new tools?",
      placeholder: "e.g., Limited budget but time to learn; Budget available but need quick wins..."
    }
  ];

  const handleNext = async () => {
    if (currentResponse.trim()) {
      const newResponses = { ...responses, [questions[currentStep].id]: currentResponse };
      setResponses(newResponses);
      setCurrentResponse('');

      if (currentStep < questions.length - 1) {
        setCurrentStep(currentStep + 1);
      } else {
        // All questions answered, analyze
        setIsAnalyzing(true);
        await analyzeAndRecommend(newResponses);
      }
    }
  };

  const analyzeAndRecommend = async (userResponses) => {
    try {
      const prompt = `Based on this person's responses, suggest 4-5 specific AI applications they could implement. Be practical and actionable.

Role: ${userResponses.role}
Main tasks: ${userResponses.tasks}
Pain points: ${userResponses.pain_points}
Goals: ${userResponses.goals}
Tech comfort: ${userResponses.tech_comfort}
Resources: ${userResponses.resources}

For each recommendation, provide:
1. A clear title
2. What it does (2-3 sentences)
3. How to get started (specific next steps)
4. Difficulty level (Beginner/Intermediate/Advanced)
5. Estimated time to implement

Respond with a JSON object containing an array of recommendations:
{
  "recommendations": [
    {
      "title": "Recommendation Title",
      "description": "What this does and why it helps",
      "howToStart": "Specific steps to begin",
      "difficulty": "Beginner/Intermediate/Advanced",
      "timeToImplement": "e.g., 1-2 hours, 1 week, etc."
    }
  ]
}

IMPORTANT: Your entire response must be valid JSON only. Do not include any text outside the JSON structure.`;

      const response = await window.claude.complete(prompt);
      
      // Clean the response by removing markdown code blocks if present
      let cleanedResponse = response.trim();
      if (cleanedResponse.startsWith('```json')) {
        cleanedResponse = cleanedResponse.replace(/^```json\n?/, '').replace(/\n?```$/, '');
      } else if (cleanedResponse.startsWith('```')) {
        cleanedResponse = cleanedResponse.replace(/^```\n?/, '').replace(/\n?```$/, '');
      }
      
      const parsed = JSON.parse(cleanedResponse);
      setRecommendations(parsed.recommendations);
    } catch (error) {
      console.error('Error analyzing responses:', error);
      setRecommendations([{
        title: "Analysis Error",
        description: "There was an issue analyzing your responses. This might be due to a temporary issue - please try restarting the questionnaire.",
        howToStart: "Click 'Start Over' below to try again",
        difficulty: "N/A",
        timeToImplement: "N/A"
      }]);
    }
    setIsAnalyzing(false);
  };

  const restart = () => {
    setCurrentStep(0);
    setResponses({});
    setCurrentResponse('');
    setRecommendations([]);
    setIsAnalyzing(false);
  };

  const getDifficultyColor = (difficulty) => {
    switch(difficulty) {
      case 'Beginner': return 'bg-green-100 text-green-800';
      case 'Intermediate': return 'bg-yellow-100 text-yellow-800';
      case 'Advanced': return 'bg-red-100 text-red-800';
      default: return 'bg-gray-100 text-gray-800';
    }
  };

  if (isAnalyzing) {
    return (
      <div className="max-w-2xl mx-auto p-6 bg-white rounded-lg shadow-lg">
        <div className="text-center">
          <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-500 mx-auto mb-4"></div>
          <h2 className="text-xl font-semibold mb-2">Analyzing Your Responses</h2>
          <p className="text-gray-600">Finding the best AI opportunities for your situation...</p>
        </div>
      </div>
    );
  }

  if (recommendations.length > 0) {
    return (
      <div className="max-w-4xl mx-auto p-6 bg-white rounded-lg shadow-lg">
        <div className="text-center mb-8">
          <Lightbulb className="w-12 h-12 text-yellow-500 mx-auto mb-4" />
          <h2 className="text-2xl font-bold mb-2">Your AI Opportunities</h2>
          <p className="text-gray-600">Here are personalized recommendations based on your responses</p>
        </div>

        <div className="space-y-6">
          {recommendations.map((rec, index) => (
            <div key={index} className="border rounded-lg p-6 hover:shadow-md transition-shadow">
              <div className="flex justify-between items-start mb-3">
                <h3 className="text-xl font-semibold text-gray-900">{rec.title}</h3>
                <div className="flex gap-2">
                  <span className={`px-2 py-1 rounded-full text-xs font-medium ${getDifficultyColor(rec.difficulty)}`}>
                    {rec.difficulty}
                  </span>
                  <span className="px-2 py-1 rounded-full text-xs font-medium bg-blue-100 text-blue-800">
                    {rec.timeToImplement}
                  </span>
                </div>
              </div>
              
              <p className="text-gray-700 mb-4">{rec.description}</p>
              
              <div className="bg-gray-50 p-4 rounded-lg">
                <h4 className="font-medium text-gray-900 mb-2">How to get started:</h4>
                <p className="text-gray-700">{rec.howToStart}</p>
              </div>
            </div>
          ))}
        </div>

        <div className="text-center mt-8">
          <button
            onClick={restart}
            className="flex items-center gap-2 mx-auto px-6 py-3 bg-blue-500 text-white rounded-lg hover:bg-blue-600 transition-colors"
          >
            <RotateCcw className="w-4 h-4" />
            Start Over
          </button>
        </div>
      </div>
    );
  }

  return (
    <div className="max-w-2xl mx-auto p-6 bg-white rounded-lg shadow-lg">
      <div className="text-center mb-8">
        <MessageCircle className="w-12 h-12 text-blue-500 mx-auto mb-4" />
        <h2 className="text-2xl font-bold mb-2">AI Opportunity Finder</h2>
        <p className="text-gray-600">I'll ask you some questions to discover the best AI applications for your situation</p>
      </div>

      <div className="mb-6">
        <div className="flex justify-between items-center mb-4">
          <span className="text-sm font-medium text-gray-500">Question {currentStep + 1} of {questions.length}</span>
          <div className="w-32 bg-gray-200 rounded-full h-2">
            <div 
              className="bg-blue-500 h-2 rounded-full transition-all duration-300"
              style={{ width: `${((currentStep + 1) / questions.length) * 100}%` }}
            ></div>
          </div>
        </div>
        
        <h3 className="text-lg font-semibold mb-4">{questions[currentStep].question}</h3>
        
        <textarea
          value={currentResponse}
          onChange={(e) => setCurrentResponse(e.target.value)}
          placeholder={questions[currentStep].placeholder}
          className="w-full p-4 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent resize-none"
          rows="4"
        />
      </div>

      <div className="flex justify-between">
        <button
          onClick={() => setCurrentStep(Math.max(0, currentStep - 1))}
          disabled={currentStep === 0}
          className="px-4 py-2 text-gray-500 hover:text-gray-700 disabled:opacity-50 disabled:cursor-not-allowed"
        >
          Previous
        </button>
        
        <button
          onClick={handleNext}
          disabled={!currentResponse.trim()}
          className="flex items-center gap-2 px-6 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
        >
          {currentStep === questions.length - 1 ? 'Get Recommendations' : 'Next'}
          <ArrowRight className="w-4 h-4" />
        </button>
      </div>
    </div>
  );
};

export default AIOpportunityFinder;
```