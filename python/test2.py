from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


# Example usage
if __name__ == "__main__":
    # Hash a password
    hashed_pwd = hash_password("Admin123")
    print(f"Hashed password: {hashed_pwd}")

    # Verify the password
    is_correct = verify_password("Admin123", hashed_pwd)
    print(f"Password is correct: {is_correct}")

    # Attempt to verify with a wrong password
    is_correct = verify_password("Admin1234", hashed_pwd)
    print(f"Password is correct: {is_correct}")
