import os
import logging
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.asymmetric import rsa, ec, padding as asym_padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from twofish import Twofish

class ReversibleEncryptionTools:
    """
    A collection of reversible encryption tools including AES, TripleDES, Blowfish, Twofish, RSA, and ECC.
    """

    @staticmethod
    def supported_algorithms():
        """
        Print all supported encryption algorithms.
        """
        algorithms = {
            "AES": "Symmetric encryption algorithm using Advanced Encryption Standard",
            "Twofish": "Symmetric encryption algorithm using Twofish",
            "RSA": "Asymmetric encryption algorithm using RSA",
            "ECC": "Asymmetric encryption algorithm using Elliptic Curve Cryptography",
        }
        print("Supported Algorithms:")
        for name, description in algorithms.items():
            print(f"- {name}: {description}")

    class AES:
        """AES encryption and decryption.
        Symmetric encryption, single key for both encryption and decryption.
        Application: Secure communications, data storage, bitlocker
        Trade-off: Security vs performance, with the increase of key length, security increases but performance decreases
        Data block size: 128 bits
        key_length: 128, 192, 256 bits (default: 256 bits)
        mode: CBC / ECB / CFB / OFB / CTR / GCM
        CBC: Cipher Block Chaining: Each block of data is XORed with the previous block before encryption, advantage: more secure, disadvantage: slower (cannot be parallelized)
        ECB: Electronic Codebook: Each block of data is encrypted with the same key, advantage: faster, disadvantage: less secure
        CFB: Cipher Feedback: Each block of data is XORed with the previous cipher text block, advantage: can be used for streaming data, disadvantage: slower (cannot be parallelized)
        OFB: Output Feedback: Each block of data is XORed with the output of the previous block, advantage: can be used for streaming data, disadvantage: easier to attack by the bit-flipping attack, cannnot guarantee integrity
        CTR: Counter: Each block of data is XORed with the output of the encryption function, advantage: can be parallelized, disadvantage: must use a unique nonce for each message, otherwise, it is vulnerable to the two-time pad attack
        """

        def __init__(self, key_length=256, mode='CBC', iv=None, path=None, name="aes.key"):
            self.key_length = key_length
            self.mode = mode
            self.iv = iv or os.urandom(16)
            self.file_path = os.path.join(path or os.getcwd(), name)
            logging.basicConfig(level=logging.INFO)

        def generate_key(self, path=None):
            try:
                key = os.urandom(self.key_length // 8)
                if path:
                    with open(path, "wb") as f:
                        f.write(key)
                else:
                    with open(self.file_path, "wb") as f:
                        f.write(key)
            except Exception as e:
                raise ValueError(f"Failed to generate AES key: {e}")

        def load_key(self, path=None):
            try:
                with open(path or self.file_path, "rb") as f:
                    return f.read()
            except Exception as e:
                raise ValueError(f"Failed to load AES key: {e}")

        def _get_cipher(self, key):
            if self.mode == 'CBC':
                return Cipher(algorithms.AES(key), modes.CBC(self.iv), backend=default_backend())
            raise ValueError("Unsupported AES mode.")

        def encrypt_data(self, data, key):
            padder = padding.PKCS7(128).padder()
            padded_data = padder.update(data.encode()) + padder.finalize()
            cipher = self._get_cipher(key)
            encryptor = cipher.encryptor()
            return self.iv + (encryptor.update(padded_data) + encryptor.finalize())

        def decrypt_data(self, encrypted_data, key):
            self.iv = encrypted_data[:16]
            cipher = self._get_cipher(key)
            decryptor = cipher.decryptor()
            padded_data = decryptor.update(encrypted_data[16:]) + decryptor.finalize()
            unpadder = padding.PKCS7(128).unpadder()
            unpadded_data = unpadder.update(padded_data) + unpadder.finalize()
            return unpadded_data.decode()

    class Twofish:
        """Twofish encryption and decryption.
        Symmetric encryption, single key for both encryption and decryption.
        Data block size: 128 bits
        key_length: 128-256 bits (default: 128 bits)
        """

        def __init__(self, key_length=256, path=None, name="twofish.key"):
            if key_length not in [128, 192, 256]:
                raise ValueError("Key length for Twofish must be 128, 192, or 256 bits.")
            self.key_length = key_length
            self.file_path = os.path.join(path or os.getcwd(), name)
            logging.basicConfig(level=logging.INFO)

        def generate_key(self, path=None):
            try:
                key = os.urandom(self.key_length // 8)
                with open(path or self.file_path, "wb") as f:
                    f.write(key)
            except Exception as e:
                raise ValueError(f"Failed to generate Twofish key: {e}")

        def load_key(self, path=None):
            try:
                with open(path or self.file_path, "rb") as f:
                    return f.read()
            except Exception as e:
                raise ValueError(f"Failed to load Twofish key: {e}")

        def encrypt_data(self, data, key):
            cipher = Twofish(key)
            bs = 16  # Twofish block size
            padder = padding.PKCS7(bs * 8).padder()
            padded_data = padder.update(data.encode()) + padder.finalize()
            iv = os.urandom(bs)
            encrypted = b"".join([cipher.encrypt(padded_data[i:i + bs]) for i in range(0, len(padded_data), bs)])
            return iv + encrypted

        def decrypt_data(self, encrypted_data, key):
            cipher = Twofish(key)
            bs = 16  # Twofish block size
            iv = encrypted_data[:bs]
            encrypted_content = encrypted_data[bs:]
            decrypted = b"".join([cipher.decrypt(encrypted_content[i:i + bs]) for i in range(0, len(encrypted_content), bs)])
            unpadder = padding.PKCS7(bs * 8).unpadder()
            return (unpadder.update(decrypted) + unpadder.finalize()).decode()


    class RSA:
        """RSA encryption and decryption.
        Asymmetric encryption, separate keys for encryption and decryption. (private key, public key)
        Application: Secure communications, digital signatures, key exchange
        Trade-off: Security vs performance, with the increase of key size, security increases but performance decreases
        key_size: 1024, 2048, 3072, 4096 bits (default: 2048 bits)
        """

        def __init__(self, key_size=2048, path=None, name="rsa"):
            self.key_size = key_size
            self.private_key_path = os.path.join(path or os.getcwd(), name + "_private.pem")
            self.public_key_path = os.path.join(path or os.getcwd(), name + "_public.pem")
            # self.logger = logging.getLogger(self.__class__.__name__)
            logging.basicConfig(level=logging.INFO)

        def generate_keys(self, private_key_path=None, public_key_path=None):
            private_key = rsa.generate_private_key(public_exponent=65537, key_size=self.key_size, backend=default_backend())
            public_key = private_key.public_key()

            try:
                if private_key_path:
                    with open(private_key_path, "wb") as f:
                        f.write(private_key.private_bytes(
                            encoding=serialization.Encoding.PEM,
                            format=serialization.PrivateFormat.PKCS8,
                            encryption_algorithm=serialization.NoEncryption()
                        ))
                else:
                    with open(self.private_key_path, "wb") as f:
                        f.write(private_key.private_bytes(
                            encoding=serialization.Encoding.PEM,
                            format=serialization.PrivateFormat.PKCS8,
                            encryption_algorithm=serialization.NoEncryption()
                        ))

                if public_key_path:
                    with open(public_key_path, "wb") as f:
                        f.write(public_key.public_bytes(
                            encoding=serialization.Encoding.PEM,
                            format=serialization.PublicFormat.SubjectPublicKeyInfo
                        ))
                else:
                    with open(self.public_key_path, "wb") as f:
                        f.write(public_key.public_bytes(
                            encoding=serialization.Encoding.PEM,
                            format=serialization.PublicFormat.SubjectPublicKeyInfo
                        ))

            except Exception as e:
                # self.logger.error(f"Failed to generate RSA key pair: {e}")
                raise ValueError(f"Failed to generate RSA key pair: {e}")
                # pass



        def load_private_key(self, path=None):
            try:
                if path:
                    with open(path, "rb") as f:
                        return serialization.load_pem_private_key(f.read(), password=None, backend=default_backend())
                with open(self.private_key_path, "rb") as f:
                    return serialization.load_pem_private_key(f.read(), password=None, backend=default_backend())
            except Exception as e:
                # self.logger.error(f"Failed to load RSA private key: {e}")
                raise ValueError(f"Failed to load RSA private key: {e}")
                # pass

        def load_public_key(self, path=None):
            try:
                if path:
                    with open(path, "rb") as f:
                        return serialization.load_pem_public_key(f.read(), backend=default_backend())
                with open(self.public_key_path, "rb") as f:
                    return serialization.load_pem_public_key(f.read(), backend=default_backend())
            except Exception as e:
                # self.logger.error(f"Failed to load RSA public key: {e}")
                raise ValueError(f"Failed to load RSA public key: {e}")
                # pass

        def encrypt_data(self, data, public_key):
            return public_key.encrypt(
                data.encode(),
                asym_padding.OAEP(
                    mgf=asym_padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )

        def decrypt_data(self, encrypted_data, private_key):
            return private_key.decrypt(
                encrypted_data,
                asym_padding.OAEP(
                    mgf=asym_padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            ).decode()


    class ECC:
        """ECC encryption and shared key generation.
        Asymmetric encryption, separate keys for encryption and decryption. (private key, public key)
        Application: Secure communications, digital signatures, key exchange, BTC wallet
        Compered to RSA: ECC is faster, more secure, and uses shorter keys
        """

        def __init__(self, curve=ec.SECP256R1(), path=None, name="ecc"):
            self.curve = curve
            self.private_key_path = os.path.join(path or os.getcwd(), name + "_private.pem")
            self.public_key_path = os.path.join(path or os.getcwd(), name + "_public.pem")
            # self.logger = logging.getLogger(self.__class__.__name__)
            logging.basicConfig(level=logging.INFO)

        def generate_keys(self, private_key_path=None, public_key_path=None):
            private_key = ec.generate_private_key(self.curve, default_backend())
            public_key = private_key.public_key()

            try:
                if private_key_path:
                    with open(private_key_path, "wb") as f:
                        f.write(private_key.private_bytes(
                            encoding=serialization.Encoding.PEM,
                            format=serialization.PrivateFormat.PKCS8,
                            encryption_algorithm=serialization.NoEncryption()
                        ))
                else:
                    with open(self.private_key_path, "wb") as f:
                        f.write(private_key.private_bytes(
                            encoding=serialization.Encoding.PEM,
                            format=serialization.PrivateFormat.PKCS8,
                            encryption_algorithm=serialization.NoEncryption()
                        ))

                if public_key_path:
                    with open(public_key_path, "wb") as f:
                        f.write(public_key.public_bytes(
                            encoding=serialization.Encoding.PEM,
                            format=serialization.PublicFormat.SubjectPublicKeyInfo
                        ))
                else:
                    with open(self.public_key_path, "wb") as f:
                        f.write(public_key.public_bytes(
                            encoding=serialization.Encoding.PEM,
                            format=serialization.PublicFormat.SubjectPublicKeyInfo
                        ))

            except Exception as e:
                # self.logger.error(f"Failed to generate ECC key pair: {e}")
                raise ValueError(f"Failed to generate ECC key pair: {e}")
                # pass

        def load_private_key(self, path=None):
            try:
                if path:
                    with open(path, "rb") as f:
                        return serialization.load_pem_private_key(f.read(), password=None, backend=default_backend())
                with open(self.private_key_path, "rb") as f:
                    return serialization.load_pem_private_key(f.read(), password=None, backend=default_backend())
            except Exception as e:
                # self.logger.error(f"Failed to load ECC private key: {e}")
                raise ValueError(f"Failed to load ECC private key: {e}")
                # pass

        def load_public_key(self, path=None):
            try:
                if path:
                    with open(path, "rb") as f:
                        return serialization.load_pem_public_key(f.read(), backend=default_backend())
                with open(self.public_key_path, "rb") as f:
                    return serialization.load_pem_public_key(f.read(), backend=default_backend())
            except Exception as e:
                # self.logger.error(f"Failed to load ECC public key: {e}")
                raise ValueError(f"Failed to load ECC public key: {e}")
                # pass

        def generate_shared_key(self, private_key, peer_public_key):
            shared_key = private_key.exchange(ec.ECDH(), peer_public_key)
            return HKDF(
                algorithm=hashes.SHA256(),
                length=32,
                salt=None,
                info=b'ECC shared key',
                backend=default_backend()
            ).derive(shared_key)

if __name__ == "__main__":

    # print the supported algorithms
    ReversibleEncryptionTools.supported_algorithms()

    # AES Example
    aes = ReversibleEncryptionTools.AES()
    aes.generate_key()
    aes_key = aes.load_key()
    aes_encrypted = aes.encrypt_data("Hello AES", aes_key)
    print("AES Encrypted:", aes_encrypted)
    print("AES Decrypted:", aes.decrypt_data(aes_encrypted, aes_key))

    # Example usage of Twofish
    twofish = ReversibleEncryptionTools.Twofish()
    twofish.generate_key()
    twofish_key = twofish.load_key()
    twofish_encrypted = twofish.encrypt_data("Hello Twofish", twofish_key)
    print("Twofish Encrypted:", twofish_encrypted)
    twofish_decrypted = twofish.decrypt_data(twofish_encrypted, twofish_key)
    print("Twofish Decrypted:", twofish_decrypted)

   # Example usage of RSA
    rsa_tool = ReversibleEncryptionTools.RSA()
    rsa_tool.generate_keys()
    private_key = rsa_tool.load_private_key()
    public_key = rsa_tool.load_public_key()
    rsa_encrypted = rsa_tool.encrypt_data("Hello RSA", public_key)
    print("RSA Encrypted:", rsa_encrypted)
    rsa_decrypted = rsa_tool.decrypt_data(rsa_encrypted, private_key)
    print("RSA Decrypted:", rsa_decrypted)

    # Example usage of ECC
    ecc_tool = ReversibleEncryptionTools.ECC()
    ecc_tool.generate_keys()
    ecc_private_key = ecc_tool.load_private_key()
    ecc_public_key = ecc_tool.load_public_key()
    ecc_shared_key = ecc_tool.generate_shared_key(ecc_private_key, ecc_public_key)
    print("ECC Shared Key:", ecc_shared_key)