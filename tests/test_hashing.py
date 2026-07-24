import unittest
from algorithms.sha256 import sha256_hash
from algorithms.bcrypt_hash import bcrypt_hash
from algorithms.bcrypt_verify import bcrypt_verify
from algorithms.file_sha256 import file_sha256
import tempfile
class TestHashing(unittest.TestCase):
    def test_sha256_hash(self):
        result = sha256_hash("Hello")
        self.assertEqual(
            result,
            "185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969"
        )
    def test_bcrypt_verify(self):
        password = "mysecretpassword"
        hashed_password = bcrypt_hash(password)
        result = bcrypt_verify(
            password,
            hashed_password
        )
        self.assertTrue(result)
    def test_bcrypt_wrong_password(self):
        password = "mysecretpassword"
        hashed_password = bcrypt_hash(password)
        result = bcrypt_verify(
            "wrongpassword",
            hashed_password
        )
        self.assertFalse(result)
    def test_file_sha256(self):
        with tempfile.NamedTemporaryFile(mode="w", delete=False) as file:
            file.write("Hello")
            file_path = file.name
        result = file_sha256(file_path)
        expected_hash = "185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969"
        self.assertEqual(result, expected_hash)