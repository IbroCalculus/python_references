import uuid

# THIS FILE/FUNCTION IS SIMPLY USED TO GENERATE THE PASSWORD HASH, AND UUID BASED ON USER EMAIL
# THEN INPUTTED INTO DATABASE RESPECTIVE FIELDS MANUALLY

from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


hashed_pwd = hash_password("Admin1234")
print(f"Hashed password: {hashed_pwd}")

# Verify the password
is_correct = verify_password("Admin123", hashed_pwd)
print(f"Password is correct: {is_correct}")

# Attempt to verify with a wrong password
is_correct = verify_password("Admin1234", hashed_pwd)
print(f"Password is correct: {is_correct}")


def generate_uuid_based_on_value(value):
    # Use a predefined namespace UUID (e.g., UUID for DNS)
    namespace = uuid.UUID('6ba7b810-9dad-11d1-80b4-00c04fd430c8')

    # Generate a UUID based on the passed value
    generated_uuid = uuid.uuid5(namespace, str(value))
    str_value_generated_uuid = str(generated_uuid)
    return str_value_generated_uuid


print(f"UUID 1: {generate_uuid_based_on_value('cihphr@cihpng.org')}")
print(f"UUID 2: {generate_uuid_based_on_value('cihphr2@cihpng.org')}")
