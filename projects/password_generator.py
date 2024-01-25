import random
import string


def generate_password(length=12, use_digits=True, use_special_chars=True):
    characters = string.ascii_letters  # uppercase and lowercase letters

    if use_digits:
        characters += string.digits  # include digits

    if use_special_chars:
        characters += string.punctuation  # include special characters

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


# Example usage: generate a password of length 16 with digits and special characters
for i in range(5):
    password = generate_password(length=16, use_digits=True, use_special_chars=True)
    print(password)