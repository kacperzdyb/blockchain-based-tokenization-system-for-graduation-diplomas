# DEPLOY SMART CONTRACT TO A BLOCKCHAIN NETWORK

## 1. Set up Ethereum account
*An Ethereum account is necessary for deploying the smart contract and will be the account that controls the deployed contract.*

In order to create a new Ethereum account (e-wallet) follow [the official guide](https://ethereum.org/en/guides/how-to-create-an-ethereum-account/).

After setting up an account, you will have:
1.  `PUBLIC_KEY` - Your Ethereum account public address
2.  `PRIVATE_KEY` - Your Ethereum account private key

## 2. Set up Infura account
*This Infura account will act as an access proxy to the blockchain network for an Ethereum account*

In order to sing up for an Infura account follow [the official guide](https://docs.infura.io/getting-started).

After successful setup of the Infura account you should have:
1.  `INFURA_URL` - Your Infura account URL pointing to an Ethereum network 

Both of those should be stored securely as they provide full control of your Ethereum account (prefereably as environment variables).
Those credentials will be used for every interaction with the blockchain network -> deploying contracts, minting NFTs, etc.

## 3. Prepare environment variables
*Infura credentials should be passed to the system's user as environment variables so that they are both securely stored and easily accessible to all python scripts that require access to the blockchain network*

1. `INFURA_URL` which should be accessible via `os.getenv()`
2. `PRIVATE_KEY` which should be accessible via `os.getenv()`

## 4. Deploy Smart Contract
*Deploying the Smart Contract to the blockchain network allows for generating and assigning tokens (digital representations of physical graduation diplomas) via remotely triggering its functions using python scripts*

Run `python ./deploy_smart_contract.py`.

The script can handle command line parameters via the following flags:
- `--infura-url` (optional) - Infura URL [if not passed the script will look for this value in `INFURA_URL` environment variable]
- `--private-key` (optional) - Ethereum account (e-wallet) private key [if not passed the script will look for this value in `INFURA_KEY` environment variable]
- `--contract-path` (optional) - path to the location of .sol Smart Contract [if not passed the script will assume default path `./sol/diplomaNFT.sol`]

The script will save the following as environment variables accessible via `os.getenv()`:
1.  Contract's application binary interface as `SMART_CONTRACT_ABI`
2.  Contract's blockchain network address as `SMART_CONTRACT_ADDRESS`
