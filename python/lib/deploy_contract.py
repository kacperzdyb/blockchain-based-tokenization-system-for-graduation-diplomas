# imports
from solcx import compile_source


def deploy_contract(web3, contract_source_code, infura_private_key):
    compiled_sol = compile_source(source=contract_source_code, solc_version="0.8.1")
    contract_interface = compiled_sol["<stdin>:diplomaNFT"]

    Contract = web3.eth.contract(
        abi=contract_interface["abi"], bytecode=contract_interface["bin"]
    )

    private_key = infura_private_key

    deployer_address = web3.eth.account.from_key(private_key).address

    nonce = web3.eth.getTransactionCount(deployer_address)

    ContractConstructor = Contract.constructor()
    estimated_gas = ContractConstructor.estimateGas()
    txn = ContractConstructor.buildTransaction(
        {
            "from": deployer_address,
            "nonce": nonce,
            "gas": int(estimated_gas * 1.2),
            "gasPrice": web3.eth.gasPrice,
        }
    )

    signed_txn = web3.eth.account.sign_transaction(txn, private_key)

    tx_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)

    tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)

    return contract_interface["abi"], tx_receipt["contractAddress"]
