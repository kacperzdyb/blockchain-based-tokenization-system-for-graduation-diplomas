# imports
import argparse
import os
import json

from python.lib.get_token_data_any import get_token_data_any as get_any
from python.lib.get_token_data_infura import get_token_data_infura as get_infura

# Parse cl parameters
parser = argparse.ArgumentParser()

parser.add_argument("--provider", dest="provider")
parser.add_argument(
    "--infura-url", dest="infura_url", default=os.environ.get("INFURA_URL")
)
parser.add_argument(
    "--any-url",
    dest="any_url",
)
parser.add_argument(
    "--sc-abi", dest="sc_abi", default=os.environ.get("SMART_CONTRACT_ABI")
)
parser.add_argument(
    "--sc-address", dest="sc_address", default=os.environ.get("SMART_CONTRACT_ADDRESS")
)
parser.add_argument("--token-id", dest="token_id")

args = parser.parse_args()

# Return the data
if args.provider == "infura":
    pdf_url_val, json_url_val, pdf_hash_val = get_infura(
        args.infura_url, json.loads(args.sc_abi), args.sc_address, int(args.token_id)
    )
elif args.provider == "any":
    pdf_url_val, json_url_val, pdf_hash_val = get_any(
        args.any_url, args.sc_abi, args.sc_address, args.token_id
    )
else:
    exit(1)

print(
    f"For the token specified with ID {args.token_id} the retrived data is as follows: \nPDF URL:\t{pdf_url_val}\nJSON URL:\t{json_url_val}\nPDF hash:\t{pdf_hash_val}\n"
)
