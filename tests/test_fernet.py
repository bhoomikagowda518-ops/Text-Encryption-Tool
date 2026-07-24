import unittest
from algorithms.fernet_encrypt import fernet_encrypt
from algorithms.fernet_decrypt import fernet_decrypt
class TestFernet(unittest.TestCase):
    def test_fernet_encrypt_decrypt(self):
        message = "Hello Fernet"
        encrypted = fernet_encrypt(message)
        decrypted = fernet_decrypt(encrypted)
        self.assertEqual(decrypted, message)