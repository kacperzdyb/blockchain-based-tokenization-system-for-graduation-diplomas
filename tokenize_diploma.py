# imports
from web3 import Web3
from solcx import compile_source
import os
import argparse

import json
import python.lib.upload_to_blob as upload_to_blob
from python.lib.mint_diploma import mint_nft
from python.lib.calculate_hash import calculate_pdf_hash as calculate_hash

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
parser.add_argument(
    "--connect-str",
    dest="connection_string",
    default=os.environ.get("AZURE_STORAGE_CONNECTION_STRING"),
)
parser.add_argument(
    "--pdf-container",
    dest="pdf_container",
    default=os.environ.get("PDF_CONTAINER_NAME"),
)
parser.add_argument(
    "--json-container",
    dest="json_container",
    default=os.environ.get("JSON_CONTAINER_NAME"),
)
parser.add_argument("--pdf-name", dest="pdf_name", default="pdf1.pdf")
parser.add_argument("--pdf-path", dest="pdf_path", default="./env/example_diploma.pdf")
parser.add_argument("--json-name", dest="json_name", default="json1.json")
parser.add_argument(
    "--json-path", dest="json_path", default="./env/example_metadata.json"
)

parser.add_argument("--target-address", dest="target_address")

args = parser.parse_args()


# infura credentials
INFURA_URL = args.infura_url
PRIVATE_KEY = args.private_key

# smart contract address and abi (must be deployed to a blockchain network prior to usage)
CONTRACT_ABI = json.loads(args.sc_abi)
CONTRACT_ADDRESS = args.sc_address

# azure storage connection string and container name
CONNECTION_STRING = args.connection_string
PDF_CONTAINER_NAME = args.pdf_container
JSON_CONTAINER_NAME = args.json_container

# desired owner's destination e-wallet address
TARGET_ADDRESS = args.target_address

# pdf
PDF_NAME = args.pdf_name
PDF_PATH = args.pdf_path

# json
JSON_NAME = args.json_name
JSON_PATH = args.json_path

# Upload the PDF file and get the URL
pdf_blob_url = upload_to_blob.upload_pdf_to_blob(
    CONNECTION_STRING, PDF_CONTAINER_NAME, PDF_NAME, PDF_PATH
)


# Calculate the hash of the PDF
pdf_hash_value = calculate_hash(PDF_PATH)

# Read JSON file
with open(JSON_PATH, "r") as f:
    json_data = json.load(f)

# Upload the JSON file and get the URL
json_blob_url = upload_to_blob.upload_json_to_blob(
    CONNECTION_STRING, JSON_CONTAINER_NAME, JSON_NAME, json_data
)


# Mint the NFT and get the transaction hash
txn_hash, token_id = mint_nft(
    INFURA_URL,
    PRIVATE_KEY,
    CONTRACT_ABI,
    CONTRACT_ADDRESS,
    TARGET_ADDRESS,
    pdf_blob_url,
    json_blob_url,
    pdf_hash_value,
)

print(f"NFT {token_id} minted in transaction {txn_hash}")
