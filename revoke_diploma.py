# imports
from web3 import Web3
import os
import argparse
import json

from python.lib.burn_diploma import burn_diploma

# Parse cl parameters
parser = argparse.ArgumentParser()

parser.add_argument(
    "--infura-url", dest="infura_url", default=os.environ.get("INFURA_URL")
)
parser.add_argument(
    "--private-key", dest="private_key", default=os.environ.get("PRIVATE_KEY")
)
parser.add_argument(
    "--sc-abi", dest="sc_abi", default=os.environ.get("SMART_CONTRACT_ABI")
)
parser.add_argument(
    "--sc-address", dest="sc_address", default=os.environ.get("SMART_CONTRACT_ADDRESS")
)
parser.add_argument("--token-id", dest="token_id")
args = parser.parse_args()

# infura credentials
INFURA_URL = args.infura_url
PRIVATE_KEY = args.private_key

# smart contract address and abi (must be deployed to a blockchain network prior to usage)
CONTRACT_ABI = json.loads(args.sc_abi)
CONTRACT_ADDRESS = args.sc_address

txn_hash = burn_diploma(
    INFURA_URL, PRIVATE_KEY, CONTRACT_ABI, CONTRACT_ADDRESS, token_id=int(args.token_id)
)

print(f"NFT {args.token_id} burned in transaction {txn_hash}")
