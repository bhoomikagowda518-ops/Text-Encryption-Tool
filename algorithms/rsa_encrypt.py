from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from algorithms.rsa_key_manager import generate_rsa_keys
import base64
from logger import log_info
def rsa_encrypt(message):
    _, public_key = generate_rsa_keys()
    message_bytes = message.encode()
    ciphertext = public_key.encrypt(
    message_bytes,
    padding.OAEP(
        mgf=padding.MGF1(
            algorithm=hashes.SHA256()
        ),
        algorithm=hashes.SHA256(),
        label=None
    )
)
    encrypted_text = base64.b64encode(ciphertext).decode()
    log_info("RSA Encryption Successful")
    return encrypted_text