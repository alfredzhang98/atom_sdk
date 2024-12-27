import unittest
import os
from atom_encryption import ReversibleEncryptionTools

class TestReversibleEncryptionTools(unittest.TestCase):

    def setUp(self):
        self.aes_tool = ReversibleEncryptionTools.AES()
        self.twofish_tool = ReversibleEncryptionTools.Twofish()
        self.rsa_tool = ReversibleEncryptionTools.RSA()
        self.ecc_tool = ReversibleEncryptionTools.ECC()

    def tearDown(self):
        # Clean up generated key files
        if os.path.exists(self.aes_tool.file_path):
            os.remove(self.aes_tool.file_path)
        if os.path.exists(self.twofish_tool.file_path):
            os.remove(self.twofish_tool.file_path)
        if os.path.exists(self.rsa_tool.private_key_path):
            os.remove(self.rsa_tool.private_key_path)
        if os.path.exists(self.rsa_tool.public_key_path):
            os.remove(self.rsa_tool.public_key_path)
        if os.path.exists(self.ecc_tool.private_key_path):
            os.remove(self.ecc_tool.private_key_path)
        if os.path.exists(self.ecc_tool.public_key_path):
            os.remove(self.ecc_tool.public_key_path)

    def test_aes_encryption_decryption(self):
        self.aes_tool.generate_key()
        aes_key = self.aes_tool.load_key()
        plaintext = "Hello AES"
        encrypted = self.aes_tool.encrypt_data(plaintext, aes_key)
        decrypted = self.aes_tool.decrypt_data(encrypted, aes_key)
        self.assertEqual(plaintext, decrypted)

    def test_twofish_encryption_decryption(self):
        self.twofish_tool.generate_key()
        twofish_key = self.twofish_tool.load_key()
        plaintext = "Hello Twofish"
        encrypted = self.twofish_tool.encrypt_data(plaintext, twofish_key)
        decrypted = self.twofish_tool.decrypt_data(encrypted, twofish_key)
        self.assertEqual(plaintext, decrypted)

    def test_rsa_encryption_decryption(self):
        self.rsa_tool.generate_keys()
        private_key = self.rsa_tool.load_private_key()
        public_key = self.rsa_tool.load_public_key()
        plaintext = "Hello RSA"
        encrypted = self.rsa_tool.encrypt_data(plaintext, public_key)
        decrypted = self.rsa_tool.decrypt_data(encrypted, private_key)
        self.assertEqual(plaintext, decrypted)

    def test_ecc_key_generation_and_shared_key(self):
        self.ecc_tool.generate_keys()
        private_key = self.ecc_tool.load_private_key()
        public_key = self.ecc_tool.load_public_key()
        shared_key = self.ecc_tool.generate_shared_key(private_key, public_key)
        self.assertIsInstance(shared_key, bytes)
        self.assertEqual(len(shared_key), 32)  # 256-bit shared key

    def test_aes_invalid_key_load(self):
        with self.assertRaises(ValueError):
            self.aes_tool.load_key("non_existent_key_file.key")

    def test_twofish_invalid_key_load(self):
        with self.assertRaises(ValueError):
            self.twofish_tool.load_key("non_existent_key_file.key")

    def test_rsa_invalid_private_key_load(self):
        with self.assertRaises(ValueError):
            self.rsa_tool.load_private_key("non_existent_private_key.pem")

    def test_rsa_invalid_public_key_load(self):
        with self.assertRaises(ValueError):
            self.rsa_tool.load_public_key("non_existent_public_key.pem")

    def test_ecc_invalid_private_key_load(self):
        with self.assertRaises(ValueError):
            self.ecc_tool.load_private_key("non_existent_private_key.pem")

    def test_ecc_invalid_public_key_load(self):
        with self.assertRaises(ValueError):
            self.ecc_tool.load_public_key("non_existent_public_key.pem")

if __name__ == "__main__":
    unittest.main()