from cryptography.fernet import Fernet
from algorithms.key_manager import get_fernet_key
from logger import log_info
def fernet_encrypt(message):
    key = get_fernet_key()
    fernet = Fernet(key)
    encoded_message = message.encode()
    encrypted_message = fernet.encrypt(encoded_message)
    log_info("Fernet Encryption Successful")
    return encrypted_message.decode()