import os
from cryptography.fernet import Fernet

class EncryptionTools:
    
    # symmetric encryption algorithm
    class AES:
        def __init__(self, path=None, name="TEST"):
            if path is None:
                current_dir = os.getcwd()
            else:
                current_dir = path
            self.file_path = os.path.join(current_dir, name + ".key")

        @staticmethod
        def generate_key(path=None, name="TEST"):
            if path is None:
                current_dir = os.getcwd()
            else:
                current_dir = path
            key = Fernet.generate_key()
            file_path = os.path.join(current_dir, name + ".key")
            with open(file_path, "wb") as key_file:
                key_file.write(key)

        def load_key(self):
            if not os.path.exists(self.file_path):
                raise FileNotFoundError("Key file not found.")
            with open(self.file_path, "rb") as key_file:
                key = key_file.read()
            return key
        
        def encrypt_data(self, data, key):
            if not key:
                raise ValueError("Invalid key.")
            f = Fernet(key)
            encrypted_data = f.encrypt(data.encode())
            return encrypted_data.decode('utf-8')
        
        def decrypt_data(self, encrypted_data, key):
            if not key:
                raise ValueError("Invalid key.")
            f = Fernet(key)
            try:
                decrypted_data = f.decrypt(encrypted_data)
                return decrypted_data.decode('utf-8')
            except cryptography.fernet.InvalidToken:
                raise ValueError("Invalid encrypted data.")

if __name__ == "__main__":
    EncryptionTools.AES.generate_key(None, "KeyTest")
    aes = EncryptionTools.AES(None, "KeyTest")
    t1 = aes.encrypt_data("Test", aes.load_key())
    print(t1)
    t2 = aes.decrypt_data(t1, aes.load_key())
    print(t2)
