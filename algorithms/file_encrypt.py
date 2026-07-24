from cryptography.fernet import Fernet
from algorithms.key_manager import get_fernet_key
from logger import log_info
def file_encrypt(file_path):
    key = get_fernet_key()
    fernet = Fernet(key)
    with open(file_path, "rb") as file:
        file_bytes = file.read()
        encrypted_bytes = fernet.encrypt(file_bytes)
        with open(file_path + ".encrypted", "wb") as file:
            file.write(encrypted_bytes)
            log_info("File Encryption Successful")
        return file_path + ".encrypted"
