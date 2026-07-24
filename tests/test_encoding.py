import unittest
from algorithms.base64_encode import base64_encode
from algorithms.base64_decode import base64_decode
from algorithms.hex_encode import hex_encode
from algorithms.hex_decode import hex_decode
class TestEncoding(unittest.TestCase):
    def test_base64_encode(self):
        result = base64_encode("Hello")
        self.assertEqual(result, "SGVsbG8=")
    def test_base64_decode(self):
        result = base64_decode("SGVsbG8=")
        self.assertEqual(result, "Hello")
    def test_hex_encode(self):
        result = hex_encode("Hello")
        self.assertEqual(result, "48 65 6c 6c 6f")
    def test_hex_decode(self):
        result = hex_decode("48 65 6c 6c 6f")
        self.assertEqual(result, "Hello")