import os
from cryptography.fernet import Fernet

class EncryptionTools:
    
    # symmetric encryption algorithm
    class AES:
        def __init__(self, path, name):
            if path is None:
                current_dir = os.path.dirname(__file__).replace('\\','/') #let win and mac could play
            else:
                current_dir = path
            self.file_path = current_dir + "/" + name + ".key"

        def generate_key(path, name):
            if path is None:
                current_dir = os.path.dirname(__file__).replace('\\','/') #let win and mac could play
            else:
                current_dir = path
            key = Fernet.generate_key()
            file_path = current_dir + "/" + name + ".key"
            with open(file_path, "wb") as key_file:
                key_file.write(key)

        def load_key(self):
            with open(self.file_path, "rb") as key_file:
                key = key_file.read()
            return key
        
        def encrypt_data(self, data, key):
            f = Fernet(key)
            encrypted_data = f.encrypt(data.encode())
            return encrypted_data.decode('utf-8')
        
        def decrypt_data(self, encrypted_data, key):
            f = Fernet(key)
            decrypted_data = f.decrypt(encrypted_data)
            return decrypted_data.decode('utf-8')


if __name__ == "__main__":
    EncryptionTools.AES.generate_key(None, "KeyTest")
    aes = EncryptionTools.AES(None, "KeyTest")
    t1 = aes.encrypt_data("Test", aes.load_key())
    print(t1)
    t2 = aes.decrypt_data(t1, aes.load_key())
    print(t2)