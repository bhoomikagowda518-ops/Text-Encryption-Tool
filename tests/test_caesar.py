import unittest
from algorithms.caesar_encrypt import caesar_encrypt
from algorithms.caesar_decrypt import caesar_decrypt
class TestCaesar(unittest.TestCase):
    def test_caesar_encrypt(self):
        result = caesar_encrypt("ABC", 3)
        self.assertEqual(result, "DEF")
    def test_caesar_decrypt(self):
        result = caesar_decrypt("DEF", 3)
        self.assertEqual(result, "ABC")