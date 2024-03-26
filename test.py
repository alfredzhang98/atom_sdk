from AtomEncryption import atom_Hash

hasher = atom_Hash()
salt = hasher.generate_salt()
print(hasher.hash_data("your_password_here", 'sha256', salt))
print(hasher.hash_data("123", 'sha256', salt))