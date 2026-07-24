from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from algorithms.aes_key_manager import generate_aes_key
from logger import log_info
def aes_file_decrypt(file_path):
    key = generate_aes_key()
    aes = AESGCM(key)
    with open(file_path, "rb") as file:
        encrypted_data = file.read()
        nonce = encrypted_data[:12]
        ciphertext = encrypted_data[12:]
        plaintext = aes.decrypt(
        nonce,
        ciphertext,
        None
        )
        output_path = file_path + ".decrypted"
        with open(output_path, "wb") as file:
            file.write(plaintext)
            log_info("AES File Decryption Successful")
        return output_path