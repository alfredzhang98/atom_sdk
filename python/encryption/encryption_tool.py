import os
from cryptography.fernet import Fernet

class EncryptionTools:
    
    # symmetric encryption algorithm
    class AES:
        def __init__(self, path, name):
            self.file_path = path + "\\" + name + ".key"
            print(self.file_path)

        def generate_key(path, name):
            key = Fernet.generate_key()
            file_path = path + "\\" + name + ".key"
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
    # EncryptionTools.AES.generate_key("DBkey")

    aes = EncryptionTools.AES(None, "DBkey")
    t1 = aes.encrypt_data("3306", aes.load_key())
    print(t1)
    t2 = aes.decrypt_data(t1, aes.load_key())
    print(t2)

    #### remote
    # user
    # gAAAAABlNTlQ-8YqGQX1E82rgds9jbrJ27HCMBNYBMhWsBx2pyexYFVJk20kTdxe1UEiRGKlzpt1s7flsDb70be0siNAkEP0uA==

    # password
    # gAAAAABlNTdMhFm1lGapkW0yaLAvAPTaz0JVGMzSu02CQTFjiLj8J5G39GHvd_ctC17hWJzCD8hFSp04VLiYQQyT8TxHE1kOAQ==

    # host
    # gAAAAABlNTkTy3dJFhqpVQv27wG9hz5iMxnq-aH1YNmQRSdHNcJo97TIdFyGjGknAgy5DHUr4Wy22rG_q0opGm2h6Z_TnWFaUiXdXCdq4g6QV_CfuJ1G2b7wNVhs-pUYHsCZr5uyY9eG

    # port
    # gAAAAABlNTkzg_hAaDadmZPAGi0v_S5s6Z-VU8c4pucJGh3V9msbqSn4wa4wV83qjKCnNGFDxbP7NQ62b4MxKtgRSgAA9KX8lQ==

    #### local
    # user
    # gAAAAABlNdp6dyZKaGsQipeayIbm5ep4P3WEDd4pQbk7NIKWFgpVssLR83u2S7IJLdJkCVamjHb54spRYx-NJLYm2j66oIbG8A==

    # passward
    # gAAAAABlNdppwjD4oAG6zcbW7DelDiES0wNU7oZ8HuUiXsAn7X1yIbqHkzxHLSbV1CzCr0mbgnGvQXYBEJSWIo8QF_0FSqTsqw==

    # host
    # gAAAAABlNdqZ5BhbXS3kUuncVxcmNeJTsUc8MijHSpXWaH-qLgRC8ezzHIryLsFUzevGhdV8nJaIS9FvEHEnO-Y91V913JEovA==

    # port
    # gAAAAABlNdqooNbpLQ2NocLNpsFt8mLb59czsA6oZ24HOu45QV04MItzvcLBYG8Ss98TpoMvb4bi2YGbE1VcLQURY0sNHfUoSQ==