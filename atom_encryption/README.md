# Atom Encryption Library

Atom Encryption is a comprehensive Python library that provides tools for both reversible and irreversible encryption methods, as well as error detection mechanisms. It includes support for algorithms like AES, Twofish, RSA, ECC, and more.

---

## Features

- **Error Detection Tools**: Implementations of BCC, CRC, Parity Check, and LRC for data integrity checks.
- **Irreversible Encryption**: Secure hashing algorithms like SHA-256, SHA-512, and bcrypt.
- **Reversible Encryption**: Symmetric and asymmetric encryption algorithms including AES, Twofish, RSA, and ECC.

---

## Installation

You can install Atom Encryption from PyPI:

```bash
pip install atom-encryption
```

Or clone the repository and install it locally:

```bash
git clone https://github.com/yourusername/atom-encryption.git
cd atom-encryption
pip install .
```

---

## Usage

### Error Detection Tools

```python
from atom_encryption.error_detection_tools import ErrorDetectionTools

# Example: BCC
bcc = ErrorDetectionTools.BCC.generate(b"123456789")
print("BCC:", bcc)
```

### Irreversible Encryption Tools

```python
from atom_encryption.irreversible_encryption_tools import IrreversibleEncryptionTools

# Example: SHA-256 Hashing
hashed_data = IrreversibleEncryptionTools.Hash.hash_data("HelloWorld", algorithm="sha256")
print("SHA-256 Hash:", hashed_data)
```

### Reversible Encryption Tools

```python
from atom_encryption.reversible_encryption_tools import ReversibleEncryptionTools

# Example: AES Encryption
aes_tool = ReversibleEncryptionTools.AES()
aes_tool.generate_key()
key = aes_tool.load_key()
encrypted = aes_tool.encrypt_data("Hello AES", key)
decrypted = aes_tool.decrypt_data(encrypted, key)
print("Decrypted:", decrypted)
```

---

## Development

### Requirements

Before you begin, ensure you have the following installed:

- Python 3.8 or higher
- pip

Install the dependencies:

```bash
pip install -r requirements.txt
```

### Running Tests

To run unit tests, use:

```bash
python -m unittest discover test
```

---

## Building and Uploading to PyPI

### Step 1: Install Build Tools

Make sure you have the required tools for building and uploading:

```bash
pip install build twine
```

### Step 2: Build the Package

Build the source distribution and wheel:

```bash
python -m build
```

This will generate the `dist/` folder containing `.tar.gz` and `.whl` files.

### Step 3: Upload to PyPI

Upload the package to PyPI using Twine:

```bash
twine upload dist/*
```

You will be prompted to enter your PyPI credentials. Once done, your package will be live on PyPI.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Contributing

Contributions are welcome! If you have ideas for improvements or new features, feel free to fork the repository and submit a pull request.

