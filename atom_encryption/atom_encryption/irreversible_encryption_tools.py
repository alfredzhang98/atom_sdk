import os
import hashlib
import binascii
import bcrypt

class IrreversibleEncryptionTools:


    @staticmethod
    # support algorithm print
    def supported_algorithms():
        """
        Print the supported irreversible encryption algorithms.
        """
        print("Supported Irreversible Encryption Algorithms:")
        print("1. SHA-1 (Secure Hash Algorithm 1)")
        print("2. SHA-256 (Secure Hash Algorithm 256)")
        print("3. SHA-512 (Secure Hash Algorithm 512)")
        print("4. MD5 (Message Digest Algorithm 5)")
        print("5. bcrypt (Adaptive Password Hashing Algorithm)")


    class Hash:
        """
        Provides hashing utilities using algorithms like SHA-256, SHA-512, MD5, and bcrypt.
        """

        @staticmethod
        def hash_data(data: str, algorithm: str = 'sha256', salt: str = None) -> str:
            """
            Hash the provided data using the specified algorithm.
            """
            if not isinstance(data, str):
                raise TypeError("Data must be a string.")
            if salt and not isinstance(salt, str):
                raise TypeError("Salt must be a string if provided.")

            if algorithm in {'sha1', 'sha256', 'sha512', 'md5'}:
                if algorithm in {'md5', 'sha1'}:
                    raise ValueError(f"{algorithm} is considered insecure and should not be used.")
                hash_object = hashlib.new(algorithm)
                hash_object.update((salt + data).encode() if salt else data.encode())
                return hash_object.hexdigest()
            elif algorithm == 'bcrypt':
                if salt is None:
                    salt = bcrypt.gensalt()
                elif isinstance(salt, str) and salt.startswith("$2b$"):
                    salt = salt.encode()
                else:
                    raise ValueError("Invalid bcrypt salt. Salt must be in bcrypt format.")
                return bcrypt.hashpw(data.encode(), salt).decode()
            else:
                raise ValueError(f"Unsupported algorithm: {algorithm}")

        @staticmethod
        def generate_salt(length: int = 16) -> str:
            """
            Generate a cryptographic random salt.
            """
            return binascii.hexlify(os.urandom(length)).decode()

        @staticmethod
        def generate_bcrypt_salt(rounds: int = 12) -> str:
            """
            Generate a bcrypt-compatible salt.
            """
            return bcrypt.gensalt(rounds).decode()

        @staticmethod
        def verify_bcrypt_hash(data: str, hashed: str) -> bool:
            """
            Verify if the data matches a bcrypt hash.
            """
            if not isinstance(data, str) or not isinstance(hashed, str):
                raise TypeError("Both data and hashed must be strings.")
            return bcrypt.checkpw(data.encode(), hashed.encode())

if __name__ == "__main__":
    # include the class
    tools = IrreversibleEncryptionTools

    # test the supported algorithms
    print("Testing supported algorithms:")
    tools.supported_algorithms()

    # test data
    test_data = "HelloWorld"
    print("\nOriginal Data:", test_data)

    # test SHA-256
    print("\nTesting SHA-256:")
    sha256_hashed = tools.Hash.hash_data(test_data, algorithm="sha256")
    print("SHA-256 Hash:", sha256_hashed)

    # test SHA-512
    print("\nTesting SHA-512:")
    sha512_hashed = tools.Hash.hash_data(test_data, algorithm="sha512")
    print("SHA-512 Hash:", sha512_hashed)

    # test SHA-1 (should raise an error)
    print("\nTesting MD5 (should raise an error):")
    try:
        md5_hashed = tools.Hash.hash_data(test_data, algorithm="md5")
        print("MD5 Hash:", md5_hashed)
    except ValueError as e:
        print("Caught Exception:", e)

    # test bcrypt
    print("\nTesting Bcrypt:")
    bcrypt_salt = tools.Hash.generate_bcrypt_salt()
    bcrypt_hashed = tools.Hash.hash_data(test_data, algorithm="bcrypt", salt=bcrypt_salt)
    print("Bcrypt Hash:", bcrypt_hashed)
    print("Bcrypt Salt:", bcrypt_salt)

    # test bcrypt verification
    print("\nVerifying Bcrypt Hash:")
    is_valid = tools.Hash.verify_bcrypt_hash(test_data, bcrypt_hashed)
    print("Verification Result:", is_valid)

    # test random salt generation
    print("\nTesting Random Salt Generation:")
    random_salt = tools.Hash.generate_salt(16)
    print("Random Salt (Hex):", random_salt)

    # test SHA-256 with salt
    print("\nTesting SHA-256 with Salt:")
    sha256_with_salt = tools.Hash.hash_data(test_data, algorithm="sha256", salt=random_salt)
    print("SHA-256 Hash with Salt:", sha256_with_salt)

    # test unsupported algorithm
    print("\nTesting Unsupported Algorithm:")
    try:
        unsupported_hash = tools.Hash.hash_data(test_data, algorithm="unsupported_algo")
        print("Unsupported Hash:", unsupported_hash)
    except ValueError as e:
        print("Caught Exception:", e)
