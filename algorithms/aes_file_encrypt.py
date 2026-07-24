import os
import base64
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from algorithms.aes_key_manager import generate_aes_key
from logger import log_info
def aes_file_encrypt(file_path):
    key = generate_aes_key()
    aes = AESGCM(key)
    with open(file_path, "rb") as file:
        data = file.read()
        nonce = os.urandom(12)
        ciphertext = aes.encrypt(
    nonce,
    data,
    None
)
        encrypted_data = nonce + ciphertext
        output_path = file_path + ".encrypted"
        with open(output_path, "wb") as file:
            file.write(encrypted_data)
            log_info("AES File Encryption Successful")
        return output_path