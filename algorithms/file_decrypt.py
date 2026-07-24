from cryptography.fernet import Fernet
from algorithms.key_manager import get_fernet_key
from logger import log_info
def file_decrypt(file_path):
    key = get_fernet_key()
    fernet = Fernet(key)
    with open(file_path, "rb") as file:
        encrypted_bytes = file.read()
        decrypted_bytes = fernet.decrypt(encrypted_bytes)
        with open(file_path + ".decrypted", "wb") as file:
            file.write(decrypted_bytes)
            log_info("File Decryption Successful")
        return file_path + ".decrypted"