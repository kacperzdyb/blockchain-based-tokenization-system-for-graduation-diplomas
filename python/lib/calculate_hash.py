# imports
import hashlib


def calculate_pdf_hash(file_path):
    with open(file_path, "rb") as file:
        pdf_content = file.read()

    pdf_hash = hashlib.sha256(pdf_content).digest()
    pdf_hash_hex = "0x" + pdf_hash.hex()

    return pdf_hash_hex
