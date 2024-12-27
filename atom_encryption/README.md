# Atom Encryption Library

Atom Encryption is a comprehensive Python library that provides tools for both reversible and irreversible encryption methods, as well as error detection mechanisms. It includes support for algorithms like AES, Twofish, RSA, ECC, and more.

---

# CHANGELOG

## [1.2.0] - 20924/12/27
### Added
- **Type Encoding and Decoding Tools**:
  - Added `TypeEncodeDecodeTools` class with various utility methods:
    - `int_list_to_str` and `str_to_int_list`: Convert between integer lists and strings.
    - `float_to_bytes` and `bytes_to_float`: Convert between floats and bytes.
    - `hex_string_format_to_bytes` and `bytes_to_hex_string_format`: Handle hex string and byte conversions.
    - `int_to_int_list` and `int_list_to_int`: Convert integers to byte lists with MSB/LSB ordering and back.
    - Other similar encoding/decoding tools.
- Comprehensive unit tests for the new `TypeEncodeDecodeTools` in `test_type_encode_decode_tools.py`.

### Fixed
- None

---

## Features

- **Error Detection Tools**: Implementations of BCC, CRC, Parity Check, and LRC for data integrity checks.
- **Irreversible Encryption**: Secure hashing algorithms like SHA-256, SHA-512, and bcrypt.
- **Reversible Encryption**: Symmetric and asymmetric encryption algorithms including AES, Twofish, RSA, and ECC.
- **Type Encoding and Decoding**: Tools for type conversion and encoding/decoding operations, such as integer-to-string, hex-to-bytes, and more.

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

### Type Encode Decode Tools

The `TypeEncodeDecodeTools` module provides utilities for various type conversions, such as integer lists to strings, bytes to floats, and more.

```python
from atom_encryption.type_encode_decode_tools import TypeEncodeDecodeTools

tools = TypeEncodeDecodeTools()

# Example 1: Integer list to string and back
int_list = [72, 101, 108, 108, 111]
string = tools.int_list_to_str(int_list)
print("String:", string)  # Output: "Hello"
print("Back to Integer List:", tools.str_to_int_list(string))  # Output: [72, 101, 108, 108, 111]

# Example 2: Float to bytes and back
float_value = 12.34
float_bytes = tools.float_to_bytes(float_value)
print("Bytes:", float_bytes)
print("Float:", tools.bytes_to_float(float_bytes))

# Example 3: Hex string format to bytes
byte_data = b"Hello"
formatted_hex = tools.bytes_to_hex_string_format(byte_data)
print("Hex String Format:", formatted_hex)  # Output: "\x48\x65\x6c\x6c\x6f"
print("Bytes:", tools.hex_string_format_to_bytes(formatted_hex))  # Output: b"Hello"

# Example 4: Integer to integer list with MSB ordering
integer_value = 123456
int_list = tools.int_to_int_list(integer_value, specified_length=4, order="msb")
print("Integer List (MSB):", int_list)  # Output: [0, 1, 226, 64]
print("Back to Integer:", tools.int_list_to_int(int_list, "msb"))  # Output: 123456
```

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

To run the test, please clone the Github project and run the could below:
Github link: [atom_encryption](https://github.com/alfredzhang98/atom_sdk/tree/master/atom_encryption)

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

