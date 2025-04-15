export LIGHTNING_RPC_PORT=10001
export LIGHTNING_CERT_PATH="/Users/ehallmark/Library/Application Support/Lnd/tls.cert"
export LIGHTNING_MACAROON_PATH=/Users/ehallmark/repos/lightning-ai/dev/alice/data/chain/bitcoin/simnet/admin.macaroon
export UVICORN_PORT=7098
export UVICORN_HOST=localhost

uv run main.py