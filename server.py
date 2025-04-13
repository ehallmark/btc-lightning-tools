# server.py
from mcp.server.fastmcp import FastMCP
from lightning_client import LightningClient
from google.protobuf.json_format import MessageToJson
import sys
import base64


# Create an MCP server
def create_server(client: LightningClient):
    mcp = FastMCP("lightning-tools")

    @mcp.tool()
    def pay_invoice(payment_request: str) -> dict:
        """Pay a payment request."""
        return MessageToJson(client.SendPaymentSync(client.SendRequest(payment_request=payment_request)))

    @mcp.tool()
    def create_invoice(amount: int) -> dict:
        """Create an invoice for the given amount and return the invoice payment request."""
        return MessageToJson(client.AddInvoice(client.Invoice(
            value=amount,
            private=False,
            expiry=3600,
        )))

    @mcp.tool()
    def check_invoice_is_settled(r_hash: bytes) -> bool:
        """Check if an invoice is settled."""
        if len(r_hash) != 32:
            r_hash = base64.b64decode(r_hash)
        return client.LookupInvoice(client.PaymentHash(r_hash=r_hash)).settled

    @mcp.tool()
    def check_wallet_balance() -> int:
        """Check my wallet balance."""
        return client.WalletBalance(client.WalletBalanceRequest()).total_balance

    @mcp.tool()
    def get_public_info() -> str:
        """GetInfo returns general information concerning the lightning node
         including its identity pubkey, alias, the chains it is connected to,
         and information concerning the number of open+pending channels."""
        return MessageToJson(client.GetInfo(client.GetInfoRequest()))

    return mcp


if __name__ == "__main__":
    # Initialize and run the server
    if len(sys.argv) > 3:
        client = LightningClient(
            rpc_port=int(sys.argv[1]),
            cert_path=sys.argv[2],
            macaroon_path=sys.argv[3]
        )

    else:
        raise RuntimeError("Usage: python server.py <rpc_port> <cert_path> <macaroon_path>")

    app = create_server(client)
    app.run(transport='stdio')
