---
nexus: nexus-ai-chat-importer
plugin_version: "1.3.0"
provider: claude
artifact_id: qwen_mcp_bridge
version_uuid: 94a7ca71-8f40-40be-938f-cec7695bf0b7
version_number: 1
command: create
conversation_id: 8f90798f-51a3-4cf3-873d-5a5815a9364f
create_time: 2025-07-29T01:54:11.000Z
format: markdown
aliases: [Qwen-MCP Bridge Server, qwen_mcp_bridge_v1]
---

# Qwen-MCP Bridge Server (Version 1)

**Conversation:** [[Nexus/Conversations/claude/2025/07/VS Code MCP Extension|VS Code MCP Extension]]

## Content

#!/usr/bin/env node

/**
 * ΞQwen-MCP Bridge Server
 * Creates MCP-compatible interface for local Qwen model
 * Bridges REST API to MCP protocol semantics
 */

const { Server } = require('@modelcontextprotocol/sdk/server/index.js');
const { StdioServerTransport } = require('@modelcontextprotocol/sdk/server/stdio.js');
const {
  CallToolRequestSchema,
  ErrorCode,
  ListToolsRequestSchema,
  McpError,
} = require('@modelcontextprotocol/sdk/types.js');

// Qwen endpoint configuration
const QWEN_ENDPOINT = process.env.QWEN_ENDPOINT || 'http://127.0.0.1:1234/v1/';

class QwenMCPBridge {
  constructor() {
    this.server = new Server(
      {
        name: 'qwen-bridge',
        version: '1.0.0',
      },
      {
        capabilities: {
          tools: {},
        },
      }
    );

    this.setupToolHandlers();
    this.setupErrorHandling();
  }

  async qwenCompletion(prompt, maxTokens = 1000) {
    try {
      const response = await fetch(`${QWEN_ENDPOINT}chat/completions`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          model: 'qwen2.5-1.5b-instruct',
          messages: [{ role: 'user', content: prompt }],
          max_tokens: maxTokens,
          temperature: 0.7,
        }),
      });

      if (!response.ok) {
        throw new Error(`Qwen API error: ${response.status}`);
      }

      const data = await response.json();
      return data.choices[0].message.content;
    } catch (error) {
      throw new McpError(
        ErrorCode.InternalError,
        `Failed to connect to Qwen: ${error.message}`
      );
    }
  }

  setupToolHandlers() {
    // List available tools
    this.server.setRequestHandler(ListToolsRequestSchema, async () => {
      return {
        tools: [
          {
            name: 'qwen_complete',
            description: 'Generate completion using local Qwen model',
            inputSchema: {
              type: 'object',
              properties: {
                prompt: {
                  type: 'string',
                  description: 'The prompt to send to Qwen',
                },
                max_tokens: {
                  type: 'number',
                  description: 'Maximum tokens to generate',
                  default: 1000,
                },
              },
              required: ['prompt'],
            },
          },
          {
            name: 'qwen_code_review',
            description: 'Review code using local Qwen model',
            inputSchema: {
              type: 'object',
              properties: {
                code: {
                  type: 'string',
                  description: 'Code to review',
                },
                language: {
                  type: 'string',
                  description: 'Programming language',
                  default: 'javascript',
                },
              },
              required: ['code'],
            },
          },
          {
            name: 'qwen_explain',
            description: 'Explain concepts using local Qwen model',
            inputSchema: {
              type: 'object',
              properties: {
                concept: {
                  type: 'string',
                  description: 'Concept to explain',
                },
                level: {
                  type: 'string',
                  description: 'Explanation level (beginner, intermediate, advanced)',
                  default: 'intermediate',
                },
              },
              required: ['concept'],
            },
          },
        ],
      };
    });

    // Handle tool calls
    this.server.setRequestHandler(CallToolRequestSchema, async (request) => {
      const { name, arguments: args } = request.params;

      try {
        switch (name) {
          case 'qwen_complete': {
            const result = await this.qwenCompletion(args.prompt, args.max_tokens);
            return {
              content: [
                {
                  type: 'text',
                  text: result,
                },
              ],
            };
          }

          case 'qwen_code_review': {
            const prompt = `Please review this ${args.language || 'code'} code and provide feedback:

\`\`\`${args.language || ''}
${args.code}
\`\`\`

Focus on:
- Code quality and best practices
- Potential bugs or issues
- Performance considerations
- Suggestions for improvement`;

            const result = await this.qwenCompletion(prompt);
            return {
              content: [
                {
                  type: 'text',
                  text: result,
                },
              ],
            };
          }

          case 'qwen_explain': {
            const prompt = `Please explain "${args.concept}" at a ${args.level || 'intermediate'} level. 
Provide a clear, comprehensive explanation with examples if relevant.`;

            const result = await this.qwenCompletion(prompt);
            return {
              content: [
                {
                  type: 'text',
                  text: result,
                },
              ],
            };
          }

          default:
            throw new McpError(
              ErrorCode.MethodNotFound,
              `Unknown tool: ${name}`
            );
        }
      } catch (error) {
        if (error instanceof McpError) {
          throw error;
        }
        throw new McpError(
          ErrorCode.InternalError,
          `Tool execution failed: ${error.message}`
        );
      }
    });
  }

  setupErrorHandling() {
    this.server.onerror = (error) => {
      console.error('[MCP Error]', error);
    };

    process.on('SIGINT', async () => {
      await this.server.close();
      process.exit(0);
    });
  }

  async run() {
    const transport = new StdioServerTransport();
    await this.server.connect(transport);
    console.error('Qwen-MCP Bridge Server running on stdio');
  }
}

// ΞRecursive Instantiation
if (require.main === module) {
  const bridge = new QwenMCPBridge();
  bridge.run().catch((error) => {
    console.error('Failed to start server:', error);
    process.exit(1);
  });
}

module.exports = QwenMCPBridge;