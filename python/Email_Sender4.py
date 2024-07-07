# import getpass
# import smtplib
#
# print("Loading")
# HOST = "smtp-mail.outlook.com"
# PORT = 587
# FROM_EMAIL = "ibsuleiman9@outlook.com"
# TO_EMAIL = "ibsuleiman9@gmail.com"
# # PASSWORD = getpass.getpass('Enter password: ')
# PASSWORD = input('Enter password: ')
#
# MESSAGE = """Subject: Mail sent using python
# Hi Ibrahim,
#
# This is a test message
#
# Thank,
# Test Account
# """
#
# print(f"Trying to connect to {HOST}")
# smtp = smtplib.SMTP(HOST, PORT)
# print(f"Successfully connected to {HOST}")
# status_code, response = smtp.ehlo()
# print(f"[*] Echoing the server: {status_code} {response}")
#
# status_code, response = smtp.starttls()
# print(f"[*] Starting TLS Connection: {status_code} {response}")
#
# status_code, response = smtp.login(FROM_EMAIL, PASSWORD)
# print(f"[*] Login in: {status_code} {response}")
#
# smtp.sendmail(FROM_EMAIL, TO_EMAIL, MESSAGE)
# smtp.quit()


# 2. ===================================================================

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_mail(sender_email, sender_password, recipient_email, subject, message):
    #Create a multipart message object
    global server
    msg = MIMEMultipart("alternative")
    msg["From"] = sender_email
    msg["To"] = recipient_email
    msg["Subject"] = subject

    text = "This is a sample message"
    html = f"<html><body><h2>{message}</h2></body></html>"

    # Create both plain and html versions to the email
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

    msg.attach(part1)
    msg.attach(part2)

    # SMTP server settings
    # smtp_server = "smtp-mail.outlook.com"
    smtp_server = "smtp.office365.com"
    smtp_port = 587

    try:
        # Create a secure SSL/TLS connection
        print("Connecting to email server")
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.set_debuglevel(1)
        print("Done creating secure SSL/TLS connection")
        server.starttls()
        print("Started TLS connection")

        # Login to Outlook email
        server.login(sender_email, sender_password)

        # Send email
        server.sendmail(sender_email, recipient_email, msg.as_string())
        print("Email sent successfully")
    except smtplib.SMTPException as e:
        print(f"Error sending email: {e}")
    finally:
        server.quit()


sender_email = "coolgirls@cihpng.org"
sender_password = "CihpLock@24"
recipient_email = "isuleiman@cihpng.org"
subject = "Now"
message = "Get this"

send_mail(sender_email, sender_password, recipient_email, subject, message)





