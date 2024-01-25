import time
from cryptography.fernet import Fernet



# NB: The key changes on each run. Hence, only need to run once and store the generated key in a .key file, then comment out this block of code
'''
def generate_and_write_key():
    generated_key = Fernet.generate_key()
    with open("crypt_key.key", 'wb') as key_file:
        key_file.write(generated_key)
generate_and_write_key()
'''
def load_key():
    with open("crypt_key.key", 'rb') as key_file:
        key = key_file.read()
    return key

master_pswd = input("What is the master password?: ")

if master_pswd != "Admin123":
    print("Incorrect master password, can't go further. Run and try again")
    quit()

key = load_key()
cipher_suite = Fernet(key)

def add():
    name = input("Account name: ")
    pwd = input("Password: ")
    encrypt_pswd = cipher_suite.encrypt(pwd.encode()).decode()

    with open('passwords.txt', 'a') as f:
        f.write(f'{name} :-> {encrypt_pswd}\n')
    print("Account details added successfully!")


def view():
    with open('passwords.txt', 'r') as f:
        contents = f.readlines()
        for content in contents:
            # print(content.rstrip())
            # account_name = content.split(":->")[0]
            # account_pwd = content.split(":->")[1]
            account_name, account_pwd = content.split(":->")
            decrypt_pswd = cipher_suite.decrypt(account_pwd.encode()).decode()
            print(f"ACCOUNT: {str(account_name).rstrip()}, PASSWORD: {decrypt_pswd}")


while True:
    mode = input("Would you like to add a new password or view existing ones (view, add)? Press q to quit: ").casefold()
    if mode == "view".casefold():
        view()
    elif mode == "add".casefold():
        add()
    elif mode == 'q'.casefold():
        print("Quitting the process in ... ")
        for i in range(3, -1, -1):
            time.sleep(1)
            print(i)
        print("Process ended!")
        quit()
    else:
        print("Invalid mode")
        continue
