import getpass
import smtplib

print("Loading")
HOST = "smtp-mail.outlook.com"
PORT = 587
FROM_EMAIL = "ibsuleiman9@outlook.com"
TO_EMAIL = "ibsuleiman9@gmail.com"
# PASSWORD = getpass.getpass('Enter password: ')
PASSWORD = input('Enter password: ')

MESSAGE = """Subject: Mail sent using python
Hi Ibrahim,

This is a test message

Thank,
Test Account
"""

print(f"Trying to connect to {HOST}")
smtp = smtplib.SMTP(HOST, PORT)
print(f"Successfully connected to {HOST}")
status_code, response = smtp.ehlo()
print(f"[*] Echoing the server: {status_code} {response}")

status_code, response = smtp.starttls()
print(f"[*] Starting TLS Connection: {status_code} {response}")

status_code, response = smtp.login(FROM_EMAIL, PASSWORD)
print(f"[*] Login in: {status_code} {response}")

smtp.sendmail(FROM_EMAIL, TO_EMAIL, MESSAGE)
smtp.quit()



