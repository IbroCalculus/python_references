# pip install python-dotenv
# create a .env file (just .env, no title)

# os.getenv() allows for a default value in case the environment variable isn't set.
# os.environ[] does not allow a default value, and if the environment variable doesn't exist, it will raise a KeyError

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

username = os.getenv('username', 'default username')       # NB: 'username' is a keyword for the computer's username.
password = os.getenv('password', 'Default password')

username2 = os.environ['username2']
password2 = os.environ['password2']

print(f'USERNAME: {username}, and PASSWORD: {password}')
print(f'USERNAME2: {username2}, and PASSWORD2: {password2}')


# Print all environment variables
print("\nList of all environment variables:")
for key, value in os.environ.items():
    print(f"{key}: {value}")