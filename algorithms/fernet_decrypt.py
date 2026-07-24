from cryptography.fernet import Fernet
from algorithms.key_manager import get_fernet_key
from logger import log_info
def fernet_decrypt(encrypted_message):
    key = get_fernet_key()
    fernet = Fernet(key)
    decrypted_message = fernet.decrypt(encrypted_message)
    decrypted_message = decrypted_message.decode()
    log_info("Fernet Decryption Successful")
    return decrypted_message
