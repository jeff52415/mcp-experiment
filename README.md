# MCP Examples

Personal experiments with Model Control Protocol (MCP) server.


## Setup

```bash
# Install uv (if not already installed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install dependencies from requirements.txt
uv sync
```



## Server Example

```bash
# Run server examples
mcp dev server_examples/server.py    # SSE transport
mcp dev server_examples/weather.py   # stdio transport
```



## Client Example

_Not yet implemented. (To be added soon!)_


## To-Do

- [x] Server examples (`server_examples/server.py`, `server_examples/weather.py`)
- [ ] Client example
- [ ] More documentation/examples as needed


## Configuration

- `configs/config.json` is provided as an example of how to configure MCP hosts (e.g., Claude, Cursor). It is not intended for direct use.
- The default examples use SSE (server.py) and stdio (weather.py).
