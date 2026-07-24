import unittest
from algorithms.rsa_encrypt import rsa_encrypt
from algorithms.rsa_decrypt import rsa_decrypt
class TestRSA(unittest.TestCase):
    def test_rsa_encrypt_decrypt(self):
        message = "Hello RSA Encryption"
        encrypted = rsa_encrypt(message)
        decrypted = rsa_decrypt(encrypted)
        self.assertEqual(decrypted, message)