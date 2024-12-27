import unittest
from atom_encryption import IrreversibleEncryptionTools

class TestIrreversibleEncryptionTools(unittest.TestCase):

    def setUp(self):
        self.data = "HelloWorld"
        self.salt = IrreversibleEncryptionTools.Hash.generate_salt()
        self.bcrypt_salt = IrreversibleEncryptionTools.Hash.generate_bcrypt_salt()

    def test_supported_algorithms(self):
        # This test ensures the supported_algorithms method runs without error.
        try:
            IrreversibleEncryptionTools.supported_algorithms()
        except Exception as e:
            self.fail(f"supported_algorithms raised an exception: {e}")

    def test_hash_sha256(self):
        sha256_hash = IrreversibleEncryptionTools.Hash.hash_data(self.data, algorithm="sha256")
        self.assertIsInstance(sha256_hash, str)
        self.assertEqual(len(sha256_hash), 64)  # SHA-256 hash length in hex

    def test_hash_sha512(self):
        sha512_hash = IrreversibleEncryptionTools.Hash.hash_data(self.data, algorithm="sha512")
        self.assertIsInstance(sha512_hash, str)
        self.assertEqual(len(sha512_hash), 128)  # SHA-512 hash length in hex

    def test_hash_with_salt(self):
        sha256_with_salt = IrreversibleEncryptionTools.Hash.hash_data(self.data, algorithm="sha256", salt=self.salt)
        self.assertIsInstance(sha256_with_salt, str)
        self.assertEqual(len(sha256_with_salt), 64)

    def test_hash_md5_raises_error(self):
        with self.assertRaises(ValueError):
            IrreversibleEncryptionTools.Hash.hash_data(self.data, algorithm="md5")

    def test_bcrypt_hash_and_verify(self):
        bcrypt_hash = IrreversibleEncryptionTools.Hash.hash_data(self.data, algorithm="bcrypt", salt=self.bcrypt_salt)
        self.assertIsInstance(bcrypt_hash, str)
        is_valid = IrreversibleEncryptionTools.Hash.verify_bcrypt_hash(self.data, bcrypt_hash)
        self.assertTrue(is_valid)

    def test_bcrypt_invalid_verification(self):
        bcrypt_hash = IrreversibleEncryptionTools.Hash.hash_data(self.data, algorithm="bcrypt", salt=self.bcrypt_salt)
        is_valid = IrreversibleEncryptionTools.Hash.verify_bcrypt_hash("WrongData", bcrypt_hash)
        self.assertFalse(is_valid)

    def test_generate_random_salt(self):
        random_salt = IrreversibleEncryptionTools.Hash.generate_salt(16)
        self.assertIsInstance(random_salt, str)
        self.assertEqual(len(random_salt), 32)  # 16 bytes in hex

    def test_unsupported_algorithm(self):
        with self.assertRaises(ValueError):
            IrreversibleEncryptionTools.Hash.hash_data(self.data, algorithm="unsupported_algo")

if __name__ == "__main__":
    unittest.main()
