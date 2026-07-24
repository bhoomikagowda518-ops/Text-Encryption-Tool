import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
KEY_PATH = "keys/aes.key"
def generate_aes_key():
    if not os.path.exists(KEY_PATH):
       key = AESGCM.generate_key(bit_length=256)
       with open(KEY_PATH, "wb") as file:
        file.write(key)
       return key
    else:
       with open(KEY_PATH, "rb") as file:
        key = file.read()
       return key