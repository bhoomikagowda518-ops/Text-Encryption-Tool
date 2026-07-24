import os
from cryptography.fernet import Fernet
KEYS_FOLDER = "keys"
FERNET_KEY_FILE = os.path.join(KEYS_FOLDER, "fernet.key")
def get_fernet_key():
    if not os.path.exists(KEYS_FOLDER):
        os.makedirs(KEYS_FOLDER)
    if os.path.exists(FERNET_KEY_FILE):
        with open(FERNET_KEY_FILE, "rb") as file:
            return file.read()
    key = Fernet.generate_key()
    with open(FERNET_KEY_FILE, "wb") as file:
        file.write(key)
    return key
    