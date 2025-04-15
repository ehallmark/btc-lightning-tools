# MCP Server for Bitcoin Lightning

This repository utilises https://github.com/ehallmark/btc-lightning-client for communicating with a local Lightning Network Daemon (`lnd`) and wraps it in a Model Context Protocol (MCP) server. This MCP server can be used with Agentic systems to interact with the Lightning Network.



### Prerequisites

+ Python >= 3.10
+ `uv` for package management
+ You must have a running Lightning Network Daemon (`lnd`) running on your machine. For more information on `lnd`, visit https://github.com/lightningnetwork/lnd.

### Running the MCP Server

```bash
export LIGHTNING_RPC_PORT=<lnd_port>
export LIGHTNING_CERT_PATH="/path/to/lnd/tls.cert"
export LIGHTNING_MACAROON_PATH=/path/to/bitcoin/simnet/admin.macaroon
export UVICORN_PORT=<some port>
export UVICORN_HOST=<some host>

uv run main.py
```

### Connecting to the MCP Server

This server uses SSE for transport. 

With the [LangGraph](https://www.langchain.com/langgraph) framework, you can connect to it using the following [adapter](https://github.com/langchain-ai/langchain-mcp-adapters):

```python
from contextlib import asynccontextmanager
from langchain_mcp_adapters.client import MultiServerMCPClient

@asynccontextmanager
async def make_graph():
    async with MultiServerMCPClient(
        {
            'lightning': {
                'url': 'http://localhost:8000/sse',
                'transport': 'sse',
            }
        }
    ) as lightning_mcp:
        workflow = create_workflow(user, lightning_mcp)
        graph = workflow.compile()
        yield graph
```