# imports
from web3 import Web3


def get_token_data_any(provider_url, abi, contract_address, token_id):
    web3 = Web3(Web3.HTTPProvider(provider_url))

    contract = web3.eth.contract(address=contract_address, abi=abi)

    pdf_url, json_url, pdf_hash = contract.functions.getTokenData(token_id).call()

    return {
        "pdf_url": pdf_url,
        "json_url": json_url,
        "pdf_hash": pdf_hash,
    }
