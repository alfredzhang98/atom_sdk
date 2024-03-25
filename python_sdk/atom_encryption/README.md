# read_files_SDK
This library contains two main encryption tool classes, ReversibleEncryptionTools and IrreversibleEncryptionTools, for implementing reversible and irreversible encryption operations.

ReversibleEncryptionTools: Supports major reversible encryption techniques such as AES, 3DES, Blowfish and RSA.
IrreversibleEncryptionTools: provides irreversible hash encryption with support for SHA-256, SHA-512, MD5 and bcrypt.

# Installation
To install the package, run the following command:
```bash

cd ./dist
pip install *.whl
# 一键运行
cd {project_files_path}
python setup.py bdist_wheel; pip uninstall AtomEncryption -y; pip install ./dist/AtomEncryption-0.0.1-py3-none-any.whl

```