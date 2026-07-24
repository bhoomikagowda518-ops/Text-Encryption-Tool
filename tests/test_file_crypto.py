import unittest
import tempfile
import os
from algorithms.file_encrypt import file_encrypt
from algorithms.file_decrypt import file_decrypt
class TestFileCrypto(unittest.TestCase):
    def test_file_encrypt_decrypt(self):
        original_content = "Hello File Encryption"
        try:
            with tempfile.NamedTemporaryFile(delete=False) as file:
                file.write(original_content.encode())
                file_path = file.name
            encrypted_file = file_encrypt(file_path)
            decrypted_file = file_decrypt(encrypted_file)
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