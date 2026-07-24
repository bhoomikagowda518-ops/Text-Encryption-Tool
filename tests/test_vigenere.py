import unittest
from algorithms.vigenere_encrypt import vigenere_encrypt
from algorithms.vigenere_decrypt import vigenere_decrypt
class TestVigenere(unittest.TestCase):
    def test_vigenere_encrypt(self):
        result = vigenere_encrypt("HELLO", "KEY")
        self.assertEqual(result, "RIJVS")
    def test_vigenere_decrypt(self):
        result = vigenere_decrypt("RIJVS", "KEY")
        self.assertEqual(result, "HELLO")
