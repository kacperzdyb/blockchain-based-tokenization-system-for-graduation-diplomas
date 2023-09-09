# PASS ARGUMENTS TO SCRIPTS

This proof-of-concept implementation includes four user-facing scripts:
- *deploy_smart_contract.py* - used for deploying the Smart Contract to the blockchain network
- *tokenize_diploma.py* - used for minting the diploma-representing Non-Fungible Token
- *revoke_diploma.py* - used for burning the diploma-representing Non-Fungible Token
- *get_token_data.py* - used for retriving diploma-related data embeded in the token

Those scripts act as an interface for this PoC system to the outside world.

Each of those scripts by default tries to retrive nessesary data from environment variables, however it is possible to overwrite any input for any of those scripts using command line parameters.

## *deploy_smart_contract.py*

- `--infura-url`
    - *optional*
    - default value: `os.environ.get("INFURA_URL")`
    - description: *URL of the Infura account to be used to access the blockchain network from*
- `--private-key`
    - *optional*
    - default value: `os.environ.get("PRIVATE_KEY")`
    - description: *Private key of the Ethereum account (e-wallet) to be used to access the blockchain network from*
- `--contract-path`
    - *optional*
    - default value: *"./sol/diplomaNFT.sol"*
    - description: *Path to the .sol source code file of the Smart Contract to be deployed*

## *tokenize_diploma.py*

- `--infura-url`
    - *optional*
    - default value: `os.environ.get("INFURA_URL")`
    - description: *URL of the Infura account to be used to access the blockchain network from*
- `--private-key`
    - *optional*
    - default value: `os.environ.get("PRIVATE_KEY")`
    - description: *Private key of the Ethereum account (e-wallet) to be used to access the blockchain network from*
- `--sc-abi`
    - *optional*
    - default value: `os.environ.get("SMART_CONTRACT_ABI")`
    - description: *Application Binary Interface of the deployed Smart Contract to be used for tokenizing the diploma*
- `--sc-address`
    - *optional*
    - default value: `os.environ.get("SMART_CONTRACT_ADDRESS")`
    - description: *Blockchain network address of the deployed Smart Contract to be used for tokenizing the diploma*
- `--connect-str`
    - *optional*
    - default value: `os.environ.get("AZURE_STORAGE_CONNECTION_STRING")`
    - description: *Connection string used to access Azure Blob Storage cloud service*
- `--pdf-container`
    - *optional*
    - default value: `os.environ.get("PDF_CONTAINER_NAME")`
    - description: *Name of the Azure Blob storage container for storing PDF versions of the diplomas*
- `--json-container`
    - *optional*
    - default value: `os.environ.get("JSON_CONTAINER_NAME")`
    - description: *Name of the Azure Blob storage container for storing JSON defined diploma metadata*
- `--pdf-name`
    - *optional*
    - default value: *"pdf1.pdf"*
    - description: *Name of the blob-type object representing a PDF version of the diploma uploaded to Azure*
- `--pdf-path`
    - *optional*
    - default value: *"./env/example_diploma.pdf"*
    - description: *Path to the PDF file to be uploaded to the Azure cloud storage*
- `--json-name`
    - *optional*
    - default value: *"json1.json"*
    - description: *Name of the blob-type object representing a JSON defined metadata of the diploma uploaded to Azure*
- `--json-path`
    - *optional*
    - default value: *"./env/example_metadata.json"*
    - description: *Path to the JSON defined metadata to be uploaded to the Azure cloud storage*
- `--target-address`
    - *required*
    - description: *The e-wallet addresss that the newly minted NFT will be assigned ownership to*

## *revoke_diploma.py*

- `--infura-url`
    - *optional*
    - default value: `os.environ.get("INFURA_URL")`
    - description: *URL of the Infura account to be used to access the blockchain network from*
- `--private-key`
    - *optional*
    - default value: `os.environ.get("PRIVATE_KEY")`
    - description: *Private key of the Ethereum account (e-wallet) to be used to access the blockchain network from*
- `--sc-abi`
    - *optional*
    - default value: `os.environ.get("SMART_CONTRACT_ABI")`
    - description: *Application Binary Interface of the deployed Smart Contract to be used for tokenizing the diploma*
- `--sc-address`
    - *optional*
    - default value: `os.environ.get("SMART_CONTRACT_ADDRESS")`
    - description: *Blockchain network address of the deployed Smart Contract to be used for tokenizing the diploma*
- `--token-id`
    - *required*
    - description: *Identifier of a token which should be burned*

## *get_token_data.py*

- `--provider`
    - *required*
    - options: `infura` or `any`
    - description: *Provider to be used for calling the contract function to retrive diploma-related token-embeded data*
- `--infura-url`
    - *optional - only if `--provider infura`*
    - default value: `os.environ.get("INFURA_URL")`
    - description: *URL of the Infura account to be used to access the blockchain network from*
- `--any-url`
    - *optional - only if `--provider any`*
    - description: *URL of the provider of choice for blockchain network API to be used to access the network from*
- `--sc-abi`
    - *optional*
    - default value: `os.environ.get("SMART_CONTRACT_ABI")`
    - description: *Application Binary Interface of the deployed Smart Contract to be used for tokenizing the diploma*
- `--sc-address`
    - *optional*
    - default value: `os.environ.get("SMART_CONTRACT_ADDRESS")`
    - description: *Blockchain network address of the deployed Smart Contract to be used for tokenizing the diploma*
- `--token-id`
    - *required*
    - description: *Identifier of a token which data should be retrived*
