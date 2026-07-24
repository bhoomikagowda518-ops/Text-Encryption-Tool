import unittest
import tempfile
import os
from algorithms.aes_file_encrypt import aes_file_encrypt
from algorithms.aes_file_decrypt import aes_file_decrypt
class TestAESFile(unittest.TestCase):
    import unittest
import tempfile
import os

from algorithms.aes_file_encrypt import aes_file_encrypt
from algorithms.aes_file_decrypt import aes_file_decrypt
class TestAESFile(unittest.TestCase):
    def test_aes_file_encrypt_decrypt(self):
        original_content = "Hello AES File Encryption"
        file_path = None
        encrypted_file = None
        decrypted_file = None
        try:
            with tempfile.NamedTemporaryFile(delete=False) as file:
                file.write(original_content.encode())
                file_path = file.name
            encrypted_file = aes_file_encrypt(file_path)
            decrypted_file = aes_file_decrypt(encrypted_file)
            with open(decrypted_file, "rb") as file:
                result = file.read().decode()
            self.assertEqual(result, original_content)
        finally:
            if file_path:
                os.remove(file_path)
            if encrypted_file:
                os.remove(encrypted_file)
            if decrypted_file:
                os.remove(decrypted_file)