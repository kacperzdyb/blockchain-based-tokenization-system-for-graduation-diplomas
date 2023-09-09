# PREPARE LOCAL ENVIRONMENT

## 1. Install Python
*Python's binary local installation is required as the locally run logic is written in the Python programming language.*

In order to install Python on your local machine follow [the installation guide](https://www.python.org/) for your platform of choice

## 2. Install pip
*pip is a package manager for Python and will be used for installing dependencies.*

If Python was installed from [Python's official website](https://www.python.org/) it should come with pip installed out of the box

You can verify that by running `pip --version` in the terminal

If pip is in fact installed correcctly you can move on to the next step

If not run `python ./python/env-prov/get-pip.py` in the terminal

## 3. Install dependencies
*Dependencies are packages containing required Python libraries.*

Run `pip install requirements.txt`

## 4. Install Microsoft's Azure CLI
*Azure CLI is a first-party command line interface for interacting with the Azure cloud platform*

In order to install Azure command line interface on you local machine follow [the installation guide](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli) oficially provided by Microsoft.

## 5. Install Solidity Compiler (solc)
*The Solidity compiler is essential for compiling the smart contract.*

To install `solc`, you can follow the installation instructions appropriate for your operating system from the [Solidity documentation](https://docs.soliditylang.org/en/latest/installing-solidity.html).

After installation, you can verify the installation by running `solc --version` in the terminal.