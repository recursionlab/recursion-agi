---
nexus: nexus-ai-chat-importer
plugin_version: "1.3.0"
provider: claude
artifact_id: leanrag-ui
version_uuid: d61cc11d-fa09-4160-879b-074b3e682af6
version_number: 1
command: create
conversation_id: 0e4692a2-db5a-476f-9613-46ef771fca52
create_time: 2025-08-19T21:20:06.000Z
format: jsx
aliases: [LeanRAG UI, leanrag-ui_v1]
---

# ΞLeanRAG UI (Version 1)

**Conversation:** [[Nexus/Conversations/claude/2025/08/LeanRAG System Development|LeanRAG System Development]]

## Content

```jsx
import { useState, useEffect } from 'react';

// Mock data service
const mockDataService = {
  // Simulate loading data from the demo files
  async getGraphData() {
    return {
      entities: {
        "ent_1": {
          id: "ent_1",
          name: "Apache Spark",
          description: "A unified analytics engine for large-scale data processing.",
          metadata: {type: "technology"}
        },
        "ent_2": {
          id: "ent_2",
          name: "Spark SQL",
          description: "A module for structured data processing in Apache Spark.",
          metadata: {type: "component"}
        },
        "ent_3": {
          id: "ent_3",
          name: "MLlib",
          description: "Spark's machine learning library.",
          metadata: {type: "component"}
        }
      },
      relations: {
        "rel_1": {
          id: "rel_1",
          source_id: "ent_1",
          target_id: "ent_2",
          type: "has_component",
          description: "Apache Spark includes Spark SQL as a module."
        },
        "rel_2": {
          id: "rel_2",
          source_id: "ent_1",
          target_id: "ent_3",
          type: "has_component",
          description: "Apache Spark includes MLlib as a machine learning library."
        }
      }
    };
  },
  
  async getHierarchyData() {
    return {
      layers: [
        {
          level: 0,
          entities: {
            "ent_1": {
              id: "ent_1",
              name: "Apache Spark",
              description: "A unified analytics engine for large-scale data processing."
            },
            "ent_2": {
              id: "ent_2",
              name: "Spark SQL",
              description: "A module for structured data processing in Apache Spark."
            },
            "ent_3": {
              id: "ent_3",
              name: "MLlib",
              description: "Spark's machine learning library."
            }
          }
        },
        {
          level: 1,
          entities: {
            "agg_1": {
              id: "agg_1",
              name: "Spark Ecosystem",
              description: "The complete Apache Spark ecosystem with all components."
            }
          }
        }
      ],
      parent_map: {
        "ent_1": "agg_1",
        "ent_2": "agg_1",
        "ent_3": "agg_1"
      }
    };
  },
  
  async queryKnowledgeGraph(query) {
    // Simulate retrieving a subgraph for a query
    return {
      entities: {
        "ent_2": {
          id: "ent_2",
          name: "Spark SQL",
          description: "A module for structured data processing in Apache Spark."
        },
        "ent_3": {
          id: "ent_3",
          name: "MLlib",
          description: "Spark's machine learning library."
        }
      },
      relations: {
        "rel_1": {
          id: "rel_1",
          source_id: "ent_1",
          target_id: "ent_2",
          type: "has_component",
          description: "Apache Spark includes Spark SQL as a module."
        },
        "rel_2": {
          id: "rel_2",
          source_id: "ent_1",
          target_id: "ent_3",
          type: "has_component",
          description: "Apache Spark includes MLlib as a machine learning library."
        }
      },
      lca_id: "agg_1",
      query: query,
      total_tokens: 200
    };
  },
  
  async generateResponse(query, subgraph) {
    // Simulate generating a response
    return `
      Based on the retrieved knowledge, Apache Spark has several core components:
      
      1. Spark SQL - A module for structured data processing that provides DataFrames and SQL query capabilities.
      2. MLlib - A machine learning library that includes algorithms for classification, regression, clustering, and more.
      
      These components are part of the unified Spark ecosystem and share the same underlying execution engine.
    `;
  }
};

const EntityCard = ({ entity }) => (
  <div className="border rounded-lg p-4 mb-4 bg-white shadow-sm">
    <h3 className="text-lg font-bold text-blue-700">{entity.name}</h3>
    <p className="text-gray-600 mt-1">{entity.description}</p>
    {entity.metadata && entity.metadata.type && (
      <span className="inline-block bg-blue-100 text-blue-800 text-xs px-2 py-1 rounded mt-2">
        {entity.metadata.type}
      </span>
    )}
  </div>
);

const RelationCard = ({ relation, entities }) => {
  const sourceEntity = entities[relation.source_id];
  const targetEntity = entities[relation.target_id];
  
  if (!sourceEntity || !targetEntity) return null;
  
  return (
    <div className="border rounded-lg p-4 mb-4 bg-white shadow-sm">
      <div className="flex items-center">
        <span className="font-semibold text-sm text-blue-600">{sourceEntity.name}</span>
        <svg className="h-4 w-4 mx-2 text-gray-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M14 5l7 7m0 0l-7 7m7-7H3" />
        </svg>
        <span className="font-semibold text-sm text-green-600">{relation.type}</span>
        <svg className="h-4 w-4 mx-2 text-gray-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M14 5l7 7m0 0l-7 7m7-7H3" />
        </svg>
        <span className="font-semibold text-sm text-blue-600">{targetEntity.name}</span>
      </div>
      <p className="text-gray-600 mt-2 text-sm">{relation.description}</p>
    </div>
  );
};

const LayerView = ({ layer, parentMap }) => {
  return (
    <div className="mb-6">
      <h3 className="text-md font-bold mb-2 bg-gray-100 p-2 rounded">Layer {layer.level}</h3>
      <div className="grid grid-cols-1 gap-4">
        {Object.values(layer.entities).map(entity => (
          <div key={entity.id} className="border rounded p-3 bg-white shadow-sm">
            <div className="font-bold">{entity.name}</div>
            <p className="text-sm text-gray-600">{entity.description}</p>
            {parentMap && parentMap[entity.id] && (
              <div className="mt-2 text-xs text-gray-500">
                Parent: {parentMap[entity.id]}
              </div>
            )}
          </div>
        ))}
      </div>
    </div>
  );
};

const QueryInput = ({ onQuery }) => {
  const [query, setQuery] = useState("");
  
  const handleSubmit = (e) => {
    e.preventDefault();
    if (query.trim()) {
      onQuery(query);
    }
  };
  
  return (
    <form onSubmit={handleSubmit} className="mb-6">
      <div className="flex">
        <input
          type="text"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Ask a question..."
          className="flex-grow p-2 border rounded-l focus:outline-none focus:ring-2 focus:ring-blue-500"
        />
        <button
          type="submit"
          className="bg-blue-600 text-white px-4 py-2 rounded-r hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500"
        >
          Search
        </button>
      </div>
    </form>
  );
};

const LoadingSpinner = () => (
  <div className="flex justify-center items-center p-8">
    <div className="animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-blue-500"></div>
  </div>
);

const LeanRAGUI = () => {
  const [activeTab, setActiveTab] = useState("query");
  const [flatGraph, setFlatGraph] = useState(null);
  const [hierarchy, setHierarchy] = useState(null);
  const [subgraph, setSubgraph] = useState(null);
  const [response, setResponse] = useState("");
  const [loading, setLoading] = useState(false);
  
  useEffect(() => {
    const loadData = async () => {
      setLoading(true);
      try {
        const graphData = await mockDataService.getGraphData();
        setFlatGraph(graphData);
        
        const hierarchyData = await mockDataService.getHierarchyData();
        setHierarchy(hierarchyData);
      } catch (error) {
        console.error("Error loading data:", error);
      } finally {
        setLoading(false);
      }
    };
    
    loadData();
  }, []);
  
  const handleQuery = async (query) => {
    setLoading(true);
    try {
      // Retrieve subgraph
      const retrievedSubgraph = await mockDataService.queryKnowledgeGraph(query);
      setSubgraph(retrievedSubgraph);
      
      // Generate response
      const generatedResponse = await mockDataService.generateResponse(query, retrievedSubgraph);
      setResponse(generatedResponse);
      
      // Switch to response tab
      setActiveTab("response");
    } catch (error) {
      console.error("Error processing query:", error);
    } finally {
      setLoading(false);
    }
  };
  
  const renderTab = () => {
    if (loading) {
      return <LoadingSpinner />;
    }
    
    switch (activeTab) {
      case "flatGraph":
        return flatGraph ? (
          <div>
            <h2 className="text-xl font-bold mb-4">Flat Knowledge Graph</h2>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
              <div>
                <h3 className="text-lg font-semibold mb-2">Entities</h3>
                {Object.values(flatGraph.entities).map(entity => (
                  <EntityCard key={entity.id} entity={entity} />
                ))}
              </div>
              <div>
                <h3 className="text-lg font-semibold mb-2">Relations</h3>
                {Object.values(flatGraph.relations).map(relation => (
                  <RelationCard 
                    key={relation.id} 
                    relation={relation} 
                    entities={flatGraph.entities} 
                  />
                ))}
              </div>
            </div>
          </div>
        ) : <div>No flat graph data available</div>;
        
      case "hierarchy":
        return hierarchy ? (
          <div>
            <h2 className="text-xl font-bold mb-4">Hierarchical Knowledge Graph</h2>
            {hierarchy.layers.map((layer) => (
              <LayerView 
                key={layer.level} 
                layer={layer} 
                parentMap={hierarchy.parent_map} 
              />
            ))}
          </div>
        ) : <div>No hierarchy data available</div>;
        
      case "query":
        return (
          <div>
            <h2 className="text-xl font-bold mb-4">Query Knowledge Graph</h2>
            <QueryInput onQuery={handleQuery} />
            <div className="bg-gray-50 p-4 rounded border">
              <p className="text-gray-700">
                Ask questions about Apache Spark and its components. The system will retrieve relevant knowledge and generate a response.
              </p>
              <p className="text-gray-500 text-sm mt-2">
                Example queries:
              </p>
              <ul className="list-disc list-inside text-sm text-gray-600 mt-1">
                <li>What is Apache Spark?</li>
                <li>What are the main components of Spark?</li>
                <li>How does Spark SQL work?</li>
                <li>What algorithms are available in MLlib?</li>
              </ul>
            </div>
          </div>
        );
        
      case "response":
        return subgraph && response ? (
          <div>
            <h2 className="text-xl font-bold mb-4">Query Results</h2>
            <div className="mb-6">
              <h3 className="text-lg font-semibold mb-2">Query</h3>
              <div className="bg-gray-50 p-4 rounded border">
                <p>{subgraph.query}</p>
              </div>
            </div>
            
            <div className="mb-6">
              <h3 className="text-lg font-semibold mb-2">Retrieved Knowledge</h3>
              <div className="bg-gray-50 p-4 rounded border">
                <div className="mb-4">
                  <h4 className="font-medium text-gray-700">Entities</h4>
                  {Object.values(subgraph.entities).map(entity => (
                    <div key={entity.id} className="mt-2 p-2 bg-white rounded border">
                      <div className="font-medium">{entity.name}</div>
                      <div className="text-sm text-gray-600">{entity.description}</div>
                    </div>
                  ))}
                </div>
                
                <div>
                  <h4 className="font-medium text-gray-700">Relations</h4>
                  {Object.values(subgraph.relations).map(relation => (
                    <div key={relation.id} className="mt-2 p-2 bg-white rounded border">
                      <div className="text-sm">
                        <span className="font-medium">{relation.source_id}</span>
                        {" "}
                        <span className="text-gray-500">{relation.type}</span>
                        {" "}
                        <span className="font-medium">{relation.target_id}</span>
                      </div>
                      <div className="text-sm text-gray-600">{relation.description}</div>
                    </div>
                  ))}
                </div>
              </div>
            </div>
            
            <div>
              <h3 className="text-lg font-semibold mb-2">Generated Response</h3>
              <div className="bg-blue-50 p-4 rounded border">
                <div className="whitespace-pre-line">{response}</div>
              </div>
            </div>
          </div>
        ) : (
          <div>No response data available. Please run a query first.</div>
        );
        
      default:
        return <div>Invalid tab</div>;
    }
  };
  
  return (
    <div className="container mx-auto p-4 max-w-6xl">
      <header className="mb-8">
        <h1 className="text-3xl font-bold text-gray-800">ΞLeanRAG System</h1>
        <p className="text-gray-600 mt-2">
          Hierarchical Knowledge Graph RAG System with Recursive Meta-Evolution
        </p>
      </header>
      
      <div className="mb-6">
        <div className="border-b border-gray-200">
          <nav className="flex -mb-px">
            <button
              onClick={() => setActiveTab("query")}
              className={`mr-1 py-2 px-4 text-center border-b-2 font-medium text-sm ${
                activeTab === "query"
                  ? "border-blue-500 text-blue-600"
                  : "border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300"
              }`}
            >
              Query
            </button>
            <button
              onClick={() => setActiveTab("response")}
              className={`mr-1 py-2 px-4 text-center border-b-2 font-medium text-sm ${
                activeTab === "response"
                  ? "border-blue-500 text-blue-600"
                  : "border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300"
              }`}
            >
              Response
            </button>
            <button
              onClick={() => setActiveTab("flatGraph")}
              className={`mr-1 py-2 px-4 text-center border-b-2 font-medium text-sm ${
                activeTab === "flatGraph"
                  ? "border-blue-500 text-blue-600"
                  : "border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300"
              }`}
            >
              Flat Graph
            </button>
            <button
              onClick={() => setActiveTab("hierarchy")}
              className={`mr-1 py-2 px-4 text-center border-b-2 font-medium text-sm ${
                activeTab === "hierarchy"
                  ? "border-blue-500 text-blue-600"
                  : "border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300"
              }`}
            >
              Hierarchy
            </button>
          </nav>
        </div>
      </div>
      
      <main className="bg-white rounded-lg shadow p-6">
        {renderTab()}
      </main>
      
      <footer className="mt-8 text-center text-gray-500 text-sm">
        <p>ΞLeanRAG System - Recursive Meta-Evolution Knowledge Graph RAG</p>
      </footer>
    </div>
  );
};

export default LeanRAGUI;

```