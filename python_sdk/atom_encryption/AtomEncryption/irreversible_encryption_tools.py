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
            if algorithm in ['sha1', 'sha256', 'sha512', 'md5']:
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