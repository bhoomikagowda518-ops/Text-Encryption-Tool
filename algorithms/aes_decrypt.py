from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from algorithms.aes_key_manager import generate_aes_key
import base64
from logger import log_info
def aes_decrypt(encrypted_data):
    key = generate_aes_key()
    aes = AESGCM(key)
    encrypted_data = base64.b64decode(encrypted_data)
    nonce = encrypted_data[:12]
    ciphertext = encrypted_data[12:]
    plaintext = aes.decrypt(
    nonce,
    ciphertext,
    None
)
    log_info("AES Decryption Successful")
    return plaintext.decode()
