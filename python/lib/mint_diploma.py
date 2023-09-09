# imports
from web3 import Web3, HTTPProvider


def mint_nft(
    infura_url,
    infura_private_key,
    abi,
    contract_address,
    to_address,
    pdf_url,
    json_url,
    pdf_hash,
):
    web3 = Web3(HTTPProvider(infura_url))

    contract = web3.eth.contract(address=contract_address, abi=abi)

    account = web3.eth.account.privateKeyToAccount(infura_private_key)

    function_data = contract.functions.mintDiploma(
        to_address, pdf_url, json_url, pdf_hash
    )

    gas_estimate = function_data.estimateGas()

    transaction = {
        "from": account.address,
        "to": contract_address,
        "data": function_data.buildTransaction({"gas": gas_estimate})["data"],
        "nonce": web3.eth.getTransactionCount(account.address),
        "gas": int(gas_estimate * 1.2),
        "gasPrice": web3.eth.gasPrice,
    }

    transaction["data"] = contract.functions.mintDiploma(
        to_address, pdf_url, json_url, pdf_hash
    ).buildTransaction({"nonce": transaction["nonce"]})["data"]

    signed_tx = web3.eth.account.signTransaction(transaction, infura_private_key)

    tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    print(f"Transaction hash: {tx_hash.hex()}")

    token_id = contract.functions.tokenId().call()

    return tx_hash.hex(), token_id
