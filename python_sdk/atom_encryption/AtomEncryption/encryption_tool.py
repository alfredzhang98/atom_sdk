import os
import logging
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding, ec
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
import hashlib
import binascii
import bcrypt
# pip install cryptography
# pip install bcrypt

class ReversibleEncryptionTools:

    # Symmetric encryption
    class AES:
        '''
        # AES example
        aes = ReversibleEncryptionTools.AES()
        aes.generate_key()
        key = aes.load_key()
        encrypted = aes.encrypt_data("Your data here", key)
        print(encrypted)
        decrypted = aes.decrypt_data(encrypted, key)
        print(decrypted)
        '''
        def __init__(self, key_length=256, mode='CBC', iv=None, path=None, name="AES"):
            self.key_length = key_length
            self.mode = mode
            self.iv = iv
            if path is None:
                # current_dir = os.getcwd()
                current_dir = os.path.dirname(os.path.abspath(__file__))
            else:
                current_dir = path
            self.file_path = os.path.join(current_dir, name + ".key")
            logging.basicConfig(level=logging.INFO)
            self.logger = logging.getLogger(__name__)

        def generate_key(self):
            key = os.urandom(self.key_length // 8)
            with open(self.file_path, "wb") as key_file:
                key_file.write(key)
            self.logger.info("AES key generated.")

        def load_key(self):
            if not os.path.exists(self.file_path):
                raise FileNotFoundError("Key file not found.")
            with open(self.file_path, "rb") as key_file:
                key = key_file.read()
            return key

        def _get_cipher(self, key):
            if self.mode == 'CBC':
                if self.iv is None:
                    self.iv = os.urandom(16)
                cipher = Cipher(algorithms.AES(key), modes.CBC(self.iv), backend=default_backend())
            # 其他模式可以在这里添加
            else:
                raise ValueError("Unsupported mode.")
            return cipher

        def encrypt_data(self, data, key):
            if not key:
                raise ValueError("Invalid key.")
            padder = padding.PKCS7(128).padder()
            padded_data = padder.update(data.encode()) + padder.finalize()
            cipher = self._get_cipher(key)
            encryptor = cipher.encryptor()
            encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
            return encrypted_data

        def decrypt_data(self, encrypted_data, key):
            if not key:
                raise ValueError("Invalid key.")
            cipher = self._get_cipher(key)
            decryptor = cipher.decryptor()
            try:
                padded_data = decryptor.update(encrypted_data) + decryptor.finalize()
                unpadder = padding.PKCS7(128).unpadder()
                data = unpadder.update(padded_data) + unpadder.finalize()
                return data.decode('utf-8')
            except Exception as e:
                self.logger.error(f"Error in decrypt_data: {e}")
                raise

    class TripleDES:
        '''
        # TripleDES example
        # triple_des = ReversibleEncryptionTools.TripleDES()
        # triple_des.generate_key()
        # key = triple_des.load_key()
        # encrypted = triple_des.encrypt_data("Your data here", key)
        # decrypted = triple_des.decrypt_data(encrypted, key)
        '''
        def __init__(self, key_length=192, mode='CBC', iv=None, path=None, name="TripleDES"):
            self.key_length = key_length
            self.mode = mode
            self.iv = iv
            if path is None:
                current_dir = os.path.dirname(os.path.abspath(__file__))
            else:
                current_dir = path
            self.file_path = os.path.join(current_dir, name + ".key")
            logging.basicConfig(level=logging.INFO)
            self.logger = logging.getLogger(__name__)

        def generate_key(self):
            key = os.urandom(self.key_length // 8)
            with open(self.file_path, "wb") as key_file:
                key_file.write(key)
            self.logger.info("3DES key generated.")

        def load_key(self):
            if not os.path.exists(self.file_path):
                raise FileNotFoundError("Key file not found.")
            with open(self.file_path, "rb") as key_file:
                key = key_file.read()
            return key

        def _get_cipher(self, key):
            if self.mode == 'CBC':
                if self.iv is None:
                    self.iv = os.urandom(8)  # 3DES使用8字节的IV
                cipher = Cipher(algorithms.TripleDES(key), modes.CBC(self.iv), backend=default_backend())
            else:
                raise ValueError("Unsupported mode.")
            return cipher

        def encrypt_data(self, data, key):
            if not key:
                raise ValueError("Invalid key.")
            padder = padding.PKCS7(algorithms.TripleDES.block_size).padder()
            padded_data = padder.update(data.encode()) + padder.finalize()
            cipher = self._get_cipher(key)
            encryptor = cipher.encryptor()
            encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
            return encrypted_data

        def decrypt_data(self, encrypted_data, key):
            if not key:
                raise ValueError("Invalid key.")
            cipher = self._get_cipher(key)
            decryptor = cipher.decryptor()
            try:
                padded_data = decryptor.update(encrypted_data) + decryptor.finalize()
                unpadder = padding.PKCS7(algorithms.TripleDES.block_size).unpadder()
                data = unpadder.update(padded_data) + unpadder.finalize()
                return data.decode('utf-8')
            except Exception as e:
                self.logger.error(f"Error in decrypt_data: {e}")
                raise

    class Blowfish:
        '''
        # Blowfish example
        blowfish = ReversibleEncryptionTools.Blowfish()
        blowfish.generate_key()
        key = blowfish.load_key()
        encrypted = blowfish.encrypt_data("Your data here", key)
        decrypted = blowfish.decrypt_data(encrypted, key)
        '''
        def __init__(self, key_length=128, mode='CBC', iv=None, path=None, name="Blowfish"):
            self.key_length = key_length
            self.mode = mode
            self.iv = iv
            if path is None:
                current_dir = os.path.dirname(os.path.abspath(__file__))
            else:
                current_dir = path
            self.file_path = os.path.join(current_dir, name + ".key")
            logging.basicConfig(level=logging.INFO)
            self.logger = logging.getLogger(__name__)

        def generate_key(self):
            key = os.urandom(self.key_length // 8)
            with open(self.file_path, "wb") as key_file:
                key_file.write(key)
            self.logger.info("Blowfish key generated.")

        def load_key(self):
            if not os.path.exists(self.file_path):
                raise FileNotFoundError("Key file not found.")
            with open(self.file_path, "rb") as key_file:
                key = key_file.read()
            return key

        def _get_cipher(self, key):
            if self.mode == 'CBC':
                if self.iv is None:
                    self.iv = os.urandom(8)  # Blowfish使用8字节的IV
                cipher = Cipher(algorithms.Blowfish(key), modes.CBC(self.iv), backend=default_backend())
            else:
                raise ValueError("Unsupported mode.")
            return cipher

        def encrypt_data(self, data, key):
            if not key:
                raise ValueError("Invalid key.")
            padder = padding.PKCS7(algorithms.Blowfish.block_size).padder()
            padded_data = padder.update(data.encode()) + padder.finalize()
            cipher = self._get_cipher(key)
            encryptor = cipher.encryptor()
            encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
            return encrypted_data

        def decrypt_data(self, encrypted_data, key):
            if not key:
                raise ValueError("Invalid key.")
            cipher = self._get_cipher(key)
            decryptor = cipher.decryptor()
            try:
                padded_data = decryptor.update(encrypted_data) + decryptor.finalize()
                unpadder = padding.PKCS7(algorithms.Blowfish.block_size).unpadder()
                data = unpadder.update(padded_data) + unpadder.finalize()
                return data.decode('utf-8')
            except Exception as e:
                self.logger.error(f"Error in decrypt_data: {e}")
                raise

    # Asymmetric encryption
    class RSA:
        '''
        # RSA example
        rsa = ReversibleEncryptionTools.RSA()
        rsa.generate_keys()
        private_key = rsa.load_private_key("path/to/private_key.pem")  # Optional custom path
        public_key = rsa.load_public_key("path/to/public_key.pem")     # Optional custom path
        encrypted = rsa.encrypt_data("Your data here", public_key)
        decrypted = rsa.decrypt_data(encrypted, private_key)
        '''
        def __init__(self, key_size=2048, path=None, name="RSA"):
            self.key_size = key_size
            self.default_path = os.path.dirname(os.path.abspath(__file__)) if path is None else path
            self.private_key_path = os.path.join(self.default_path, name + "_private.pem")
            self.public_key_path = os.path.join(self.default_path, name + "_public.pem")
            logging.basicConfig(level=logging.INFO)
            self.logger = logging.getLogger(__name__)

        def generate_keys(self):
            private_key = rsa.generate_private_key(
                public_exponent=65537,
                key_size=self.key_size,
                backend=default_backend()
            )
            public_key = private_key.public_key()

            with open(self.private_key_path, "wb") as priv_file:
                priv_file.write(private_key.private_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PrivateFormat.PKCS8,
                    encryption_algorithm=serialization.NoEncryption()
                ))

            with open(self.public_key_path, "wb") as pub_file:
                pub_file.write(public_key.public_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PublicFormat.SubjectPublicKeyInfo
                ))
            self.logger.info("RSA key pair generated.")

        def load_private_key(self, path=None):
            private_key_path = self.private_key_path if path is None else path
            if not os.path.exists(private_key_path):
                raise FileNotFoundError(f"Private key file not found at {private_key_path}.")
            with open(private_key_path, "rb") as key_file:
                private_key = serialization.load_pem_private_key(
                    key_file.read(),
                    password=None,
                    backend=default_backend()
                )
            return private_key

        def load_public_key(self, path=None):
            public_key_path = self.public_key_path if path is None else path
            if not os.path.exists(public_key_path):
                raise FileNotFoundError(f"Public key file not found at {public_key_path}.")
            with open(public_key_path, "rb") as key_file:
                public_key = serialization.load_pem_public_key(
                    key_file.read(),
                    backend=default_backend()
                )
            return public_key

        def encrypt_data(self, data, public_key):
            encrypted = public_key.encrypt(
                data.encode(),
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )
            return encrypted

        def decrypt_data(self, encrypted_data, private_key):
            try:
                decrypted = private_key.decrypt(
                    encrypted_data,
                    padding.OAEP(
                        mgf=padding.MGF1(algorithm=hashes.SHA256()),
                        algorithm=hashes.SHA256(),
                        label=None
                    )
                )
                return decrypted.decode('utf-8')
            except Exception as e:
                self.logger.error(f"Error in decrypt_data: {e}")
                raise

    class ECC:
        '''
        # Example 
        # Alice generates the key pair
        alice_ecc = ECC()
        alice_ecc.generate_keys()
        alice_private_key = alice_ecc.load_private_key()
        alice_public_key = alice_ecc.load_public_key()

        # Bob generates the key pair
        bob_ecc = ECC()
        bob_ecc.generate_keys()
        bob_private_key = bob_ecc.load_private_key()
        bob_public_key = bob_ecc.load_public_key()

        # Alice generates a shared key using Bob's public key and her own private key
        alice_shared_key = alice_ecc.generate_shared_key(alice_private_key, bob_public_key)

        # Bob generates shared key using Alice's public key and his own private key
        bob_shared_key = bob_ecc.generate_shared_key(bob_private_key, alice_public_key)

        # Alice encrypts a message
        encrypted_message = alice_ecc.encrypt_data("Hello Bob!", bob_public_key)

        # Bob decrypts the message
        # Note: Bob needs to decrypt the message with his own private key and Alice's public key.
        decrypted_message = bob_ecc.decrypt_data(encrypted_message, bob_private_key, alice_public_key)
        print(decrypted_message.decode()) # The output should be "Hello Bob!"
        '''
        def __init__(self, curve=ec.SECP384R1(), path=None, name="ECC"):
            self.curve = curve
            if path is None:
                current_dir = os.path.dirname(os.path.abspath(__file__))
            else:
                current_dir = path
            self.private_key_path = os.path.join(current_dir, name + "_private.pem")
            self.public_key_path = os.path.join(current_dir, name + "_public.pem")
            logging.basicConfig(level=logging.INFO)
            self.logger = logging.getLogger(__name__)

        def generate_keys(self):
            private_key = ec.generate_private_key(self.curve, default_backend())
            public_key = private_key.public_key()

            with open(self.private_key_path, "wb") as priv_file:
                priv_file.write(private_key.private_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PrivateFormat.TraditionalOpenSSL,
                    encryption_algorithm=serialization.NoEncryption()
                ))

            with open(self.public_key_path, "wb") as pub_file:
                pub_file.write(public_key.public_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PublicFormat.SubjectPublicKeyInfo
                ))
            self.logger.info("ECC key pair generated.")

        def generate_shared_key(self, private_key, peer_public_key):
                shared_key = private_key.exchange(ec.ECDH(), peer_public_key)
                derived_key = HKDF(
                    algorithm=hashes.SHA256(),
                    length=32,
                    salt=None,
                    info=b'handshake data',
                    backend=default_backend()
                ).derive(shared_key)
                return derived_key

        def load_private_key(self, path=None):
            private_key_path = self.private_key_path if path is None else path
            if not os.path.exists(private_key_path):
                raise FileNotFoundError(f"Private key file not found at {private_key_path}.")
            with open(private_key_path, "rb") as key_file:
                private_key = serialization.load_pem_private_key(
                    key_file.read(),
                    password=None,
                    backend=default_backend()
                )
            return private_key

        def load_public_key(self, path=None):
            public_key_path = self.public_key_path if path is None else path
            if not os.path.exists(public_key_path):
                raise FileNotFoundError(f"Public key file not found at {public_key_path}.")
            with open(public_key_path, "rb") as key_file:
                public_key = serialization.load_pem_public_key(
                    key_file.read(),
                    backend=default_backend()
                )
            return public_key

        def encrypt_data(self, data, public_key):
            private_key = self.load_private_key()
            shared_key = self.generate_shared_key(private_key, public_key)
            cipher = Cipher(algorithms.AES(shared_key), modes.CBC(os.urandom(16)), backend=default_backend())
            encryptor = cipher.encryptor()
            ct = encryptor.update(data.encode()) + encryptor.finalize()
            return ct

        def decrypt_data(self, encrypted_data, private_key, peer_public_key):
            shared_key = self.generate_shared_key(private_key, peer_public_key)
            cipher = Cipher(algorithms.AES(shared_key), modes.CBC(os.urandom(16)), backend=default_backend())
            decryptor = cipher.decryptor()
            return decryptor.update(encrypted_data) + decryptor.finalize()

class IrreversibleEncryptionTools:

    class Hash:
        '''
        hasher = IrreversibleEncryptionTools.Hash()
        salt = hasher.generate_salt()
        hashed_data_sha256 = hasher.hash_data("your_password_here", 'sha256', salt)
        hashed_data_bcrypt = hasher.hash_data("your_password_here", 'bcrypt')
        print(hashed_data_sha256)
        print(hashed_data_bcrypt)
        verification_result = hasher.verify_bcrypt_hash("your_password_here", hashed_data_bcrypt)
        print(verification_result)
        '''
        @staticmethod
        def hash_data(data, algorithm='sha256', salt=None):
            """
            Hash the data with specified algorithm and an optional salt.
            Supported algorithms: 'sha256', 'sha512', 'md5', 'bcrypt'.
            """
            if algorithm in ['sha256', 'sha512', 'md5']:
                hash_object = hashlib.new(algorithm)
                if salt:
                    hash_object.update(salt.encode() + data.encode())
                else:
                    hash_object.update(data.encode())
                return hash_object.hexdigest()
            elif algorithm == 'bcrypt':
                if salt is None:
                    salt = bcrypt.gensalt()
                return bcrypt.hashpw(data.encode(), salt).decode()
            else:
                raise ValueError(f"Unsupported algorithm: {algorithm}")

        @staticmethod
        def generate_salt(length=16):
            """
            Generate a random salt of specified length.
            """
            salt = os.urandom(length)
            return binascii.hexlify(salt).decode()

        @staticmethod
        def verify_bcrypt_hash(data, hashed):
            """
            Verify if the data matches the hashed value using bcrypt.
            """
            return bcrypt.checkpw(data.encode(), hashed.encode())