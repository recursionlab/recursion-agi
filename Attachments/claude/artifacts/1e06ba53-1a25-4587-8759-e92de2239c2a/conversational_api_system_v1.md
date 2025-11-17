---
nexus: nexus-ai-chat-importer
plugin_version: "1.3.0"
provider: claude
artifact_id: conversational_api_system
version_uuid: c5e344d7-0f0f-4747-924b-c156c53a7d8c
version_number: 1
command: create
conversation_id: 1e06ba53-1a25-4587-8759-e92de2239c2a
create_time: 2025-07-10T16:46:53.000Z
format: jsx
aliases: [Conversational API System, conversational_api_system_v1]
---

# Conversational API System (Version 1)

**Conversation:** [[Nexus/Conversations/claude/2025/07/Knowledge Speedrunning System Design|Knowledge Speedrunning System Design]]

## Content

```jsx
import React, { useState } from 'react';
import { Send, User, Bot, Settings, Plus, Trash2 } from 'lucide-react';

const ConversationalAPISystem = () => {
  const [services, setServices] = useState([
    {
      id: 'categorizer',
      name: 'File Categorizer',
      role: 'Analyzes files and suggests folder structures',
      prompt: 'You are a file categorization service. When given file data, respond with ONLY a JSON object containing: {"categories": ["folder1", "folder2"], "files": {"filename.md": "folder1"}, "confidence": 0.85}',
      active: true
    },
    {
      id: 'connector',
      name: 'Relationship Mapper',
      role: 'Finds connections between files',
      prompt: 'You are a relationship mapping service. When given file data, respond with ONLY a JSON object containing: {"connections": [{"from": "file1.md", "to": "file2.md", "strength": 0.9}], "tags": {"file1.md": ["tag1", "tag2"]}}',
      active: true
    },
    {
      id: 'validator',
      name: 'Quality Validator',
      role: 'Reviews and validates other AI outputs',
      prompt: 'You are a quality validation service. When given AI outputs, respond with ONLY a JSON object containing: {"valid": true, "issues": ["list of problems"], "suggestions": ["list of improvements"], "score": 0.92}',
      active: true
    }
  ]);

  const [conversations, setConversations] = useState([]);
  const [currentInput, setCurrentInput] = useState('');
  const [selectedService, setSelectedService] = useState('categorizer');

  const callConversationalAPI = async (serviceId, input) => {
    const service = services.find(s => s.id === serviceId);
    if (!service) return;

    const prompt = `${service.prompt}

INPUT DATA:
${input}

Remember: Respond ONLY with the specified JSON format. No additional text.`;

    try {
      const response = await window.claude.complete(prompt);
      return response;
    } catch (error) {
      return `{"error": "Service unavailable: ${error.message}"}`;
    }
  };

  const handleSendMessage = async () => {
    if (!currentInput.trim()) return;

    const userMessage = {
      id: Date.now(),
      type: 'user',
      service: selectedService,
      content: currentInput,
      timestamp: new Date().toLocaleTimeString()
    };

    setConversations(prev => [...prev, userMessage]);
    setCurrentInput('');

    // Call the conversational API
    const response = await callConversationalAPI(selectedService, currentInput);
    
    const apiResponse = {
      id: Date.now() + 1,
      type: 'service',
      service: selectedService,
      content: response,
      timestamp: new Date().toLocaleTimeString()
    };

    setConversations(prev => [...prev, apiResponse]);
  };

  const chainServices = async (input) => {
    const results = {};
    
    for (const service of services.filter(s => s.active)) {
      const response = await callConversationalAPI(service.id, input);
      results[service.id] = response;
      
      const chainMessage = {
        id: Date.now() + Math.random(),
        type: 'chain',
        service: service.id,
        content: response,
        timestamp: new Date().toLocaleTimeString()
      };
      
      setConversations(prev => [...prev, chainMessage]);
    }
    
    return results;
  };

  const handleChainExecution = async () => {
    if (!currentInput.trim()) return;

    const chainStart = {
      id: Date.now(),
      type: 'chain-start',
      content: `Executing chain with input: ${currentInput}`,
      timestamp: new Date().toLocaleTimeString()
    };

    setConversations(prev => [...prev, chainStart]);
    setCurrentInput('');

    await chainServices(currentInput);
  };

  const addService = () => {
    const newService = {
      id: `service_${Date.now()}`,
      name: 'New Service',
      role: 'Custom AI service',
      prompt: 'You are a custom AI service. Respond with JSON format.',
      active: true
    };
    setServices(prev => [...prev, newService]);
  };

  const updateService = (id, field, value) => {
    setServices(prev => prev.map(service => 
      service.id === id ? { ...service, [field]: value } : service
    ));
  };

  const deleteService = (id) => {
    setServices(prev => prev.filter(service => service.id !== id));
  };

  const formatResponse = (content) => {
    try {
      const parsed = JSON.parse(content);
      return JSON.stringify(parsed, null, 2);
    } catch {
      return content;
    }
  };

  return (
    <div className="max-w-6xl mx-auto p-6 bg-gray-50 min-h-screen">
      <div className="mb-8">
        <h1 className="text-3xl font-bold text-gray-900 mb-2">Conversational API System</h1>
        <p className="text-gray-600">Create AI services that respond like APIs through natural conversation</p>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Service Configuration */}
        <div className="bg-white rounded-lg shadow-md p-6">
          <div className="flex items-center justify-between mb-4">
            <h2 className="text-xl font-semibold flex items-center gap-2">
              <Settings className="w-5 h-5" />
              AI Services
            </h2>
            <button
              onClick={addService}
              className="bg-blue-500 text-white px-3 py-1 rounded-md hover:bg-blue-600 flex items-center gap-1"
            >
              <Plus className="w-4 h-4" />
              Add
            </button>
          </div>

          <div className="space-y-4">
            {services.map(service => (
              <div key={service.id} className="border rounded-lg p-4">
                <div className="flex items-center justify-between mb-2">
                  <input
                    type="text"
                    value={service.name}
                    onChange={(e) => updateService(service.id, 'name', e.target.value)}
                    className="font-medium bg-transparent border-none text-sm focus:outline-none"
                  />
                  <div className="flex items-center gap-2">
                    <input
                      type="checkbox"
                      checked={service.active}
                      onChange={(e) => updateService(service.id, 'active', e.target.checked)}
                      className="w-4 h-4"
                    />
                    <button
                      onClick={() => deleteService(service.id)}
                      className="text-red-500 hover:text-red-700"
                    >
                      <Trash2 className="w-4 h-4" />
                    </button>
                  </div>
                </div>
                
                <input
                  type="text"
                  value={service.role}
                  onChange={(e) => updateService(service.id, 'role', e.target.value)}
                  className="w-full text-xs text-gray-600 bg-transparent border-none mb-2 focus:outline-none"
                  placeholder="Service description"
                />
                
                <textarea
                  value={service.prompt}
                  onChange={(e) => updateService(service.id, 'prompt', e.target.value)}
                  className="w-full text-xs bg-gray-50 border rounded p-2 h-20 resize-none focus:outline-none focus:ring-2 focus:ring-blue-500"
                  placeholder="System prompt for this service..."
                />
              </div>
            ))}
          </div>
        </div>

        {/* Conversation Interface */}
        <div className="lg:col-span-2 bg-white rounded-lg shadow-md flex flex-col h-96">
          <div className="p-4 border-b">
            <h2 className="text-xl font-semibold mb-2">API Conversation</h2>
            <div className="flex gap-2">
              <select
                value={selectedService}
                onChange={(e) => setSelectedService(e.target.value)}
                className="border rounded px-3 py-1 text-sm"
              >
                {services.filter(s => s.active).map(service => (
                  <option key={service.id} value={service.id}>{service.name}</option>
                ))}
              </select>
              <button
                onClick={handleChainExecution}
                className="bg-purple-500 text-white px-4 py-1 rounded hover:bg-purple-600 text-sm"
              >
                Chain All Services
              </button>
            </div>
          </div>

          <div className="flex-1 overflow-y-auto p-4 space-y-4">
            {conversations.map(msg => (
              <div key={msg.id} className={`flex gap-3 ${msg.type === 'user' ? 'justify-end' : 'justify-start'}`}>
                <div className={`max-w-xs lg:max-w-md px-4 py-2 rounded-lg ${
                  msg.type === 'user' 
                    ? 'bg-blue-500 text-white' 
                    : msg.type === 'chain-start'
                    ? 'bg-purple-100 text-purple-800 border border-purple-300'
                    : msg.type === 'chain'
                    ? 'bg-green-100 text-green-800 border border-green-300'
                    : 'bg-gray-100 text-gray-800'
                }`}>
                  <div className="flex items-center gap-2 mb-1">
                    {msg.type === 'user' ? <User className="w-4 h-4" /> : <Bot className="w-4 h-4" />}
                    <span className="text-xs font-medium">
                      {msg.type === 'user' ? 'User' : 
                       msg.type === 'chain-start' ? 'Chain Executor' :
                       msg.type === 'chain' ? `Chain: ${services.find(s => s.id === msg.service)?.name}` :
                       services.find(s => s.id === msg.service)?.name}
                    </span>
                    <span className="text-xs opacity-75">{msg.timestamp}</span>
                  </div>
                  <div className="text-sm">
                    {msg.type === 'service' || msg.type === 'chain' ? (
                      <pre className="whitespace-pre-wrap font-mono text-xs">
                        {formatResponse(msg.content)}
                      </pre>
                    ) : (
                      msg.content
                    )}
                  </div>
                </div>
              </div>
            ))}
          </div>

          <div className="p-4 border-t">
            <div className="flex gap-2">
              <input
                type="text"
                value={currentInput}
                onChange={(e) => setCurrentInput(e.target.value)}
                onKeyPress={(e) => e.key === 'Enter' && handleSendMessage()}
                placeholder="Enter data to process..."
                className="flex-1 border rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500"
              />
              <button
                onClick={handleSendMessage}
                className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600 flex items-center gap-2"
              >
                <Send className="w-4 h-4" />
                Send
              </button>
            </div>
          </div>
        </div>
      </div>

      {/* API Documentation */}
      <div className="mt-8 bg-white rounded-lg shadow-md p-6">
        <h3 className="text-lg font-semibold mb-4">How Conversational APIs Work</h3>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div>
            <h4 className="font-medium mb-2">1. Define Service Behavior</h4>
            <p className="text-sm text-gray-600 mb-4">
              Each AI service has a specific role and responds in a structured format (JSON). 
              The system prompt defines exactly how the AI should behave.
            </p>
            
            <h4 className="font-medium mb-2">2. Send Requests</h4>
            <p className="text-sm text-gray-600 mb-4">
              Send natural language requests to any service. The AI processes your input 
              and responds with structured data.
            </p>
          </div>
          
          <div>
            <h4 className="font-medium mb-2">3. Chain Services</h4>
            <p className="text-sm text-gray-600 mb-4">
              Use "Chain All Services" to send the same input to multiple AI services 
              simultaneously, creating a processing pipeline.
            </p>
            
            <h4 className="font-medium mb-2">4. Customize & Extend</h4>
            <p className="text-sm text-gray-600">
              Add new services with custom prompts and behaviors. Each service can be 
              designed for specific tasks like categorization, analysis, or validation.
            </p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ConversationalAPISystem;
```