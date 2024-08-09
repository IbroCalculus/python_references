
import secrets  # This is needed for the generate secret key function


# OAUTH2 requires a username and password

def generate_secret_key():
    return secrets.token_hex(32)


secret_key = generate_secret_key()
print(f'SECRET_KEY GENERATED: {secret_key}')