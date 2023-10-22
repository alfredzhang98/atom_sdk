import os
from cryptography.fernet import Fernet

class EncryptionTools:
    
    # symmetric encryption algorithm
    class AES:
        def __init__(self, path, name):
            if path == None:
                current_dir = os.path.dirname(__file__)
                self.file_path = current_dir + "\\" + name + ".key"
            else:
                self.file_path = path + "\\" + name + ".key"
            print(self.file_path)

        def generate_key(name):
            key = Fernet.generate_key()
            current_dir = os.path.dirname(__file__)
            file_path = current_dir + "\\" + name + ".key"
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
        

# EncryptionTools.AES.generate_key("DBkey")

# aes = EncryptionTools.AES(None, "DBkey")
# t1 = aes.encrypt_data("dev_0000", aes.load_key())
# print(t1)
# t2 = aes.decrypt_data(t1, aes.load_key())
# print(t2)

# dev_0000
# gAAAAABlNTlQ-8YqGQX1E82rgds9jbrJ27HCMBNYBMhWsBx2pyexYFVJk20kTdxe1UEiRGKlzpt1s7flsDb70be0siNAkEP0uA==

# worldangle0001-
# gAAAAABlNTdMhFm1lGapkW0yaLAvAPTaz0JVGMzSu02CQTFjiLj8J5G39GHvd_ctC17hWJzCD8hFSp04VLiYQQyT8TxHE1kOAQ==

# sh-cynosdbmysql-grp-hva70gqc.sql.tencentcdb.com
# gAAAAABlNTkTy3dJFhqpVQv27wG9hz5iMxnq-aH1YNmQRSdHNcJo97TIdFyGjGknAgy5DHUr4Wy22rG_q0opGm2h6Z_TnWFaUiXdXCdq4g6QV_CfuJ1G2b7wNVhs-pUYHsCZr5uyY9eG

# 23474
# gAAAAABlNTkzg_hAaDadmZPAGi0v_S5s6Z-VU8c4pucJGh3V9msbqSn4wa4wV83qjKCnNGFDxbP7NQ62b4MxKtgRSgAA9KX8lQ==
