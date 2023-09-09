# imports
import json
import os
import argparse
from web3 import Web3
from python.lib.deploy_contract import deploy_contract

# Parse cl paramaters
parser = argparse.ArgumentParser()

parser.add_argument(
    "--infura-url", dest="infura_url", default=os.environ.get("INFURA_URL")
)
parser.add_argument(
    "--private-key", dest="private_key", default=os.environ.get("PRIVATE_KEY")
)
parser.add_argument(
    "--contract-path", dest="contract_path", default="./sol/diplomaNFT.sol"
)
args = parser.parse_args()

# Infura credentials
INFURA_URL = args.infura_url
PRIVATE_KEY = args.private_key

# Read contract source code from the file
with open(args.contract_path, "r") as file:
    contract_source_code = file.read()

infura_url = INFURA_URL
web3 = Web3(Web3.HTTPProvider(infura_url))

abi, contract_address = deploy_contract(web3, contract_source_code, PRIVATE_KEY)

print(f"\nABI: {str(abi)}\n")
print(f"\nAddress: {str(contract_address)}\n")

abi_json = json.dumps(abi)

shell_profile = os.path.expanduser("~/.zshrc")

with open(shell_profile, "a") as f:
    f.write(f"\nexport SMART_CONTRACT_ABI='{abi_json}'")
    f.write(f"\nexport SMART_CONTRACT_ADDRESS='{contract_address}'")
