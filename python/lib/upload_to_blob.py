# imports
import json
from azure.storage.blob import BlobServiceClient


def upload_pdf_to_blob(azure_connection_string, container_name, blob_name, file_path):
    connect_str = azure_connection_string

    blob_service_client = BlobServiceClient.from_connection_string(connect_str)

    blob_client = blob_service_client.get_blob_client(container_name, blob_name)

    print("\nUploading to Azure Storage as blob:\n\t" + blob_name)

    with open(file_path, "rb") as data:
        blob_client.upload_blob(data)

    blob_url = blob_client.url

    return blob_url


def upload_json_to_blob(azure_connection_string, container_name, blob_name, json_data):
    connect_str = azure_connection_string

    blob_service_client = BlobServiceClient.from_connection_string(connect_str)

    blob_client = blob_service_client.get_blob_client(container_name, blob_name)

    print("\nUploading to Azure Storage as blob:\n\t" + blob_name)

    json_string = json.dumps(json_data)

    blob_client.upload_blob(json_string)

    blob_url = blob_client.url

    return blob_url
