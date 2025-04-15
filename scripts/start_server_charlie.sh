export LIGHTNING_RPC_PORT=10003
export LIGHTNING_CERT_PATH="/Users/ehallmark/Library/Application Support/Lnd/tls.cert"
export LIGHTNING_MACAROON_PATH=/Users/ehallmark/repos/lightning-ai/dev/charlie/data/chain/bitcoin/simnet/admin.macaroon
export UVICORN_PORT=7099
export UVICORN_HOST=localhost

uv run main.py