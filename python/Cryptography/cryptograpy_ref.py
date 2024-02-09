# I used this module in the project 'password_manager'. CHECK its: password_manager.py
# The project includes saving and retrieving the encrypted and decrypted data respectively, in a text file.

from cryptography.fernet import Fernet

'''
key = Fernet.generate_key()             # The key changes on each run. Hence, only need to run once and store the generated key in a .key file, then comment out this block of code
print(f"Generated key: {key}")
'''

# NB: The key changes on each run. Hence, only need to run once and store the generated key in a .key file, then comment out this block of code
def generate_key():
    return Fernet.generate_key()


def encrypt_message(message, key):
    cipher_suite = Fernet(key)
    encrypted_message = cipher_suite.encrypt(message.encode())
    return encrypted_message


def decrypt_message(encrypted_message, key):
    cipher_suite = Fernet(key)
    decrypted_message = cipher_suite.decrypt(encrypted_message).decode()
    return decrypted_message


# Example usage:
# Generate a key
# NB: The key changes on each run. Hence, only need to run once and store the generated key in a .key file, then comment out this block of code
key = generate_key()

# Original message
original_message = "Hello, cryptography!"

# Encrypt the message
encrypted_message = encrypt_message(original_message, key)
print(f"Encrypted message: {encrypted_message}")

# Decrypt the message
decrypted_message = decrypt_message(encrypted_message, key)
print(f"Decrypted message: {decrypted_message}")
