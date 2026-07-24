from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from algorithms.rsa_key_manager import generate_rsa_keys
import base64
from logger import log_info
def rsa_decrypt(encrypted_message):
    private_key, _ = generate_rsa_keys()
    encrypted_bytes = base64.b64decode(encrypted_message)
    plaintext_bytes = private_key.decrypt(
    encrypted_bytes,
    padding.OAEP(
        mgf=padding.MGF1(
            algorithm=hashes.SHA256()
        ),
        algorithm=hashes.SHA256(),
        label=None
    )
)
    log_info("RSA Decryption Successful")
    return plaintext_bytes.decode()