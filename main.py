from server import create_server
from mcp.server.fastmcp import FastMCP
import os
from lightning_client import LightningClient

mcp = FastMCP("lightning-tools", host=os.environ['UVICORN_HOST'], port=int(os.environ['UVICORN_PORT']))

client = LightningClient(
    rpc_port=int(os.environ['LIGHTNING_RPC_PORT']),
    cert_path=os.environ['LIGHTNING_CERT_PATH'],
    macaroon_path=os.environ['LIGHTNING_MACAROON_PATH']
)

create_server(mcp, client)

if __name__ == "__main__":
    mcp.run(transport="sse")
