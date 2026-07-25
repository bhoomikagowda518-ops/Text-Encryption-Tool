import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

KEY_DIR = "keys"
KEY_PATH = os.path.join(KEY_DIR, "aes.key")


def generate_aes_key():
    os.makedirs(KEY_DIR, exist_ok=True)

    if not os.path.exists(KEY_PATH):
        key = AESGCM.generate_key(bit_length=256)

        with open(KEY_PATH, "wb") as file:
            file.write(key)

        return key

    with open(KEY_PATH, "rb") as file:
        return file.read()