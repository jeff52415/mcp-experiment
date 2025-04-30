# MCP Overview

## 🧠 MCP (Model Context Protocol) Simple Overview

- **MCP** defines **how clients (like Cursor) talk to servers (tools)**.
- **It uses JSON-RPC** to structure the communication (what method to call, what params to send).
- **It is transport-agnostic** — meaning **it doesn't care** how messages move:
    - Can use **STDIO** (local input/output streams)
    - Can use **HTTP** (over network)
    - Can use **SSE** (Server-Sent Events for live updates)

## 🔧 Core Concepts

MCP servers provide three main capabilities:

1. **Tools**: Functions that can be called by the LLM
2. **Resources**: File-like data that can be read by clients
3. **Prompts**: Pre-written templates for specific tasks

### Tools
Examples:
- Mathematical operations (add, multiply)
- Time-related functions
- API calls (weather, alerts)
- Database queries
- File operations

Flow: `Model → Client → Server → Tool → Result`

### Resources
Examples:
- Greetings with dynamic content
- Mathematical constants
- Weather alerts and forecasts
- Database schemas
- File contents
- API responses

Flow: `Model → Client → Resource → Read Data`

### Prompts
Examples:
- Math assistant prompts
- Weather analysis prompts
- Text analysis prompts
- Database query prompts
- File operation prompts

Flow: `System/User → Prompt → Model → Response`

## 🌟 Server Capabilities

MCP servers can declare these capabilities during initialization:

| Capability | Feature Flag | Description |
|------------|--------------|-------------|
| prompts | listChanged | Prompt template management |
| resources | subscribelistChanged | Resource exposure and updates |
| tools | listChanged | Tool discovery and execution |
| logging | - | Server logging configuration |
| completion | - | Argument completion suggestions |


## API Architecture Terms

| Term | Description | Examples |
| --- | --- | --- |
| **API architectural style** | High-level design approach for APIs | REST, RPC, GraphQL, SOAP |
| **API protocol / spec** | Defines the format and semantics of API requests | **JSON-RPC**, XML-RPC, gRPC |
| **Communication protocol (transport)** | How messages are transported across networks | STDIO, HTTP, SSE, WebSocket |
| **Serialization format** | How data is structured in the payload | JSON |


## 🔄 Transport Options

MCP is transport-agnostic, supporting multiple communication methods:

1. **STDIO**: Local input/output streams (default for CLI tools)
2. **HTTP**: Network communication
3. **SSE**: Server-Sent Events for real-time updates
4. **ASGI**: Integration with web frameworks (via `sse_app`)

## 📦 MCP Data Flow

1. **Client (like Cursor)** wants to use a tool.
2. **Client sends a JSON-RPC request** (e.g., `"method": "send_email"`) **over a transport** (STDIO / SSE).
3. **MCP Server** receives it, understands which function/tool to call.
4. **MCP Server runs the function** (e.g., actually sends the email).
5. **Server replies** with a **JSON-RPC response** (e.g., `"result": "email sent"`).
6. **Client shows the result** to user.


## 🔑 Key Benefits

1. **Transport-agnostic**: Same JSON-RPC messages work over any transport
2. **Simple Schema**: Clear method, params, and ID structure
3. **Tool Invocation**: Easy remote function calling
4. **Lightweight**: Minimal overhead for quick tool access
5. **Flexible**: Works with any LLM or client application

