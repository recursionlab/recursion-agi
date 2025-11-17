---
nexus: nexus-ai-chat-importer
plugin_version: "1.3.0"
provider: claude
artifact_id: search_interface
version_uuid: a4d9ab3c-eea6-4509-bb2a-8f436ad48a55
version_number: 1
command: create
conversation_id: 9fbbf9fd-0fc7-4cb5-9e1d-9c2c1f119f9a
create_time: 2025-07-12T17:22:38.000Z
format: html
aliases: [Conversation Search Interface, search_interface_v1]
---

# Conversation Search Interface (Version 1)

**Conversation:** [[Nexus/Conversations/claude/2025/07/Knowledge Representation Topology|Knowledge Representation Topology]]

## Content

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Conversation Search</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background: #f5f5f5;
        }
        .container {
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        .search-box {
            display: flex;
            gap: 10px;
            margin-bottom: 30px;
        }
        #searchInput {
            flex: 1;
            padding: 12px;
            border: 2px solid #ddd;
            border-radius: 5px;
            font-size: 16px;
        }
        #searchButton {
            padding: 12px 24px;
            background: #007bff;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
        }
        #searchButton:hover {
            background: #0056b3;
        }
        .result {
            border: 1px solid #ddd;
            border-radius: 5px;
            padding: 20px;
            margin-bottom: 15px;
            background: #fafafa;
        }
        .result-title {
            font-weight: bold;
            font-size: 18px;
            margin-bottom: 10px;
            color: #333;
        }
        .result-content {
            color: #666;
            line-height: 1.6;
            margin-bottom: 10px;
        }
        .result-tags {
            display: flex;
            gap: 5px;
            flex-wrap: wrap;
        }
        .tag {
            background: #007bff;
            color: white;
            padding: 3px 8px;
            border-radius: 3px;
            font-size: 12px;
        }
        .similarity-score {
            float: right;
            background: #28a745;
            color: white;
            padding: 3px 8px;
            border-radius: 3px;
            font-size: 12px;
        }
        .no-results {
            text-align: center;
            color: #666;
            font-style: italic;
            padding: 40px;
        }
        .loading {
            text-align: center;
            padding: 40px;
        }
        .stats {
            background: #e9ecef;
            padding: 15px;
            border-radius: 5px;
            margin-bottom: 20px;
            text-align: center;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Conversation Search</h1>
        
        <div class="stats">
            <div id="statsDisplay">Database not loaded</div>
            <button onclick="loadStats()" style="margin-left: 10px; padding: 5px 10px; background: #6c757d; color: white; border: none; border-radius: 3px; cursor: pointer;">Refresh Stats</button>
        </div>
        
        <div class="search-box">
            <input type="text" id="searchInput" placeholder="Search your conversations..." />
            <button id="searchButton" onclick="searchConversations()">Search</button>
        </div>
        
        <div id="results"></div>
    </div>

    <script>
        // Mock backend - in real implementation, this would connect to your Python backend
        let mockDatabase = [];
        
        // Initialize
        document.addEventListener('DOMContentLoaded', function() {
            loadMockData();
            loadStats();
            
            // Enable Enter key search
            document.getElementById('searchInput').addEventListener('keypress', function(e) {
                if (e.key === 'Enter') {
                    searchConversations();
                }
            });
        });
        
        function loadMockData() {
            // This would be replaced with actual API calls to your Python backend
            mockDatabase = [
                {
                    id: '1',
                    title: 'Machine Learning Discussion',
                    content: 'We talked about neural networks, deep learning, and how to implement gradient descent algorithms...',
                    tags: ['machine learning', 'neural networks', 'algorithms'],
                    similarity: 0.95
                },
                {
                    id: '2',
                    title: 'Python Programming Tips',
                    content: 'Discussion about Python best practices, including list comprehensions, decorators, and async programming...',
                    tags: ['python', 'programming', 'best practices'],
                    similarity: 0.87
                },
                {
                    id: '3',
                    title: 'Database Design Concepts',
                    content: 'We explored database normalization, indexing strategies, and query optimization techniques...',
                    tags: ['databases', 'sql', 'optimization'],
                    similarity: 0.76
                }
            ];
        }
        
        function loadStats() {
            // Mock stats - replace with actual backend call
            document.getElementById('statsDisplay').innerHTML = 
                `Total Conversations: ${mockDatabase.length} | Last Updated: ${new Date().toLocaleString()}`;
        }
        
        function searchConversations() {
            const query = document.getElementById('searchInput').value.trim();
            const resultsDiv = document.getElementById('results');
            
            if (!query) {
                resultsDiv.innerHTML = '<div class="no-results">Please enter a search term</div>';
                return;
            }
            
            resultsDiv.innerHTML = '<div class="loading">Searching...</div>';
            
            // Mock search - replace with actual API call
            setTimeout(() => {
                const results = mockDatabase.filter(conv => 
                    conv.content.toLowerCase().includes(query.toLowerCase()) ||
                    conv.title.toLowerCase().includes(query.toLowerCase()) ||
                    conv.tags.some(tag => tag.toLowerCase().includes(query.toLowerCase()))
                );
                
                displayResults(results);
            }, 500);
        }
        
        function displayResults(results) {
            const resultsDiv = document.getElementById('results');
            
            if (results.length === 0) {
                resultsDiv.innerHTML = '<div class="no-results">No conversations found matching your search</div>';
                return;
            }
            
            let html = '';
            results.forEach(result => {
                html += `
                    <div class="result">
                        <div class="result-title">
                            ${result.title}
                            <span class="similarity-score">${(result.similarity * 100).toFixed(1)}%</span>
                        </div>
                        <div class="result-content">${result.content}</div>
                        <div class="result-tags">
                            ${result.tags.map(tag => `<span class="tag">${tag}</span>`).join('')}
                        </div>
                    </div>
                `;
            });
            
            resultsDiv.innerHTML = html;
        }
        
        // Real implementation would include these functions:
        
        async function realSearchConversations(query) {
            try {
                const response = await fetch('/api/search', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ query: query })
                });
                
                const results = await response.json();
                return results;
            } catch (error) {
                console.error('Search error:', error);
                return [];
            }
        }
        
        async function realLoadStats() {
            try {
                const response = await fetch('/api/stats');
                const stats = await response.json();
                document.getElementById('statsDisplay').innerHTML = 
                    `Total Conversations: ${stats.total} | Last Updated: ${stats.lastUpdated}`;
            } catch (error) {
                console.error('Stats error:', error);
            }
        }
    </script>
</body>
</html>
```