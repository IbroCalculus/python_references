# For OUTLOOK using SMTP

# NOTE: I wanted something similar to Email.Sender.py, but this did not work. Rather, Check Email_Sender3.py


from email.message import EmailMessage
import ssl
import smtplib
import os

# def send_email():
#     sender_email = input("SENDER EMAIL: ")
#     sender_password = input("PASSWORD: ")
#     receiver_email = input("RECEIVER EMAIL: ")
#     subject = input("SUBJECT: ")
#     body = input("BODY: ")
#
#     # Basic email address validation
#     if not (sender_email and receiver_email):
#         print("Please enter valid email addresses.")
#         return
#
#     em = EmailMessage()
#     em['From'] = sender_email
#     em['To'] = receiver_email
#     em['Subject'] = subject
#     em.set_content(body)
#
#     # Path to the PDF file you want to attach
#     pdf_file_path = input("Enter the path to the PDF file: ")       # email_sender.pdf
#
#     # Check if the file exists
#     if os.path.exists(pdf_file_path):
#         # Open the file in binary mode and attach it to the email
#         with open(pdf_file_path, 'rb') as pdf_file:
#             pdf_data = pdf_file.read()
#             em.add_attachment(pdf_data, maintype='application', subtype='pdf', filename=os.path.basename(pdf_file_path))
#     else:
#         print("The specified file does not exist.")
#         return
#
#     context = ssl.create_default_context()
#
#     try:
#         # SMTP server and port for Microsoft Outlook
#         with smtplib.SMTP('smtp.office365.com', 587) as smtp:
#             smtp.starttls(context=context)
#             smtp.login(sender_email, sender_password)
#             smtp.send_message(em)
#         print("Email sent successfully")
#     except smtplib.SMTPAuthenticationError:
#         print("Authentication failed. Make sure your email and password are correct, and that access for less secure apps is enabled.")
#     except smtplib.SMTPException as e:
#         print(f"An error occurred while sending the email: {e}")
#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")

# send_email()


# smtp-mail.outlook.com

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

username = "coolgirls@cihpng.org"
password = "CihpLock@24"
mail_from = "coolgirls@cihpng.org"
mail_to = "ibsuleiman9@gmail.com"
mail_subject = "Test Subject"
mail_body = "This is a test message"

mimemsg = MIMEMultipart()
mimemsg['From']=mail_from
mimemsg['To']=mail_to
mimemsg['Subject']=mail_subject
mimemsg.attach(MIMEText(mail_body, 'plain'))
connection = smtplib.SMTP(host='smtp-mail.outlook.com', port=587)
connection.starttls()
connection.login(username,password)
connection.send_message(mimemsg)
connection.quit()