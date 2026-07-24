from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from algorithms.aes_key_manager import generate_aes_key
import os
import base64
from logger import log_info
def aes_encrypt(message):
    key = generate_aes_key()
    aes = AESGCM(key)
    message_bytes = message.encode()
    nonce = os.urandom(12)
    ciphertext = aes.encrypt(
    nonce,
    message_bytes,
    None
)
    encrypted_data = nonce + ciphertext
    encoded_data = base64.b64encode(encrypted_data)
    log_info("AES Encryption Successful")
    return encoded_data.decode()