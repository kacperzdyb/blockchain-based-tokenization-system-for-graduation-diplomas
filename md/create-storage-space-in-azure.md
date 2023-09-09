# CREATE STORAGE SPACE IN AZURE

## 1. Log in to your Azure account
Run `az login` and follow the prompts in your web browser to complete the authentication process

## 2. Create a resource group
*This resource group will act as a high-level container for all nessesary Azure resources.*

Run `az group create --name TSFGD --location eastus`

## 3. Create storage account
*This storage account will act as a mid-level container for all nessesary storage space within Azure.*

Run `az storage account create --name TSFGDstorage --resource-group TSFGD --location eastus --sku Standard_RAGRS --kind StorageV2`

## 4. Create blob container for diploma-pdf
*This blob container will act as a low-level storage space for PDF versions of graduation diplomas.*

Run `az storage container create --name diplomas --public-access blob --account-name TSFGDstorage`

> Store container name as environment variable -> `PDF_CONTAINER_NAME`

## 5. Create blob container for diploma-json
*This blob container will act as a low level storage space for JSON versions of metadata sets of graduation diplomas.*

Run `az storage container create --name metadata --public-access blob --account-name TSFGDstorage`

> Store container name as environment variable -> `JSON_CONTAINER_NAME`

## 6. Create blob container for Smart Contract data
*This blob container will act as a low level storage space for Smart Contract's ABI (Application Binary Interface) and address*

Run `az storage container create --name smartcontract --public-access blob --account-name TSFGDstorage`

> Store container name as environment variable -> `SC_CONTAINER_NAME`

## 7. Get connection string as .tsv
*This connection string will acts as an authentication and authorization token for all interactions with the Azure storage account.*

Run `az storage account show-connection-string --name TSFGDstorage --resource-group TSFGD --query connectionString --output tsv`

> Store connection string as environment variable -> `AZURE_STORAGE_CONNECTION_STRING`


