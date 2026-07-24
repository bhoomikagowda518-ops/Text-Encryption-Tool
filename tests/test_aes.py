import unittest
from algorithms.aes_encrypt import aes_encrypt
from algorithms.aes_decrypt import aes_decrypt
class TestAES(unittest.TestCase):
    def test_aes_encrypt_decrypt(self):
        message = "Hello AES Encryption"
        encrypted = aes_encrypt(message)
        decrypted = aes_decrypt(encrypted)
        self.assertEqual(decrypted, message)