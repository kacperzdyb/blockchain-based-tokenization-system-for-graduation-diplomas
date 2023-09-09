# imports
from web3 import HTTPProvider, Web3


def get_token_data_infura(infura_url, abi, contract_address, token_id):
    web3 = Web3(HTTPProvider(infura_url))

    contract = web3.eth.contract(address=contract_address, abi=abi)

    pdf_url, json_url, pdf_hash = contract.functions.getTokenData(token_id).call()

    return pdf_url, json_url, pdf_hash
