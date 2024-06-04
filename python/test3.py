from email.message import EmailMessage
import ssl
import smtplib
import os


def send_email():
    sender_email = input("SENDER EMAIL: ")
    sender_password = input("PASSWORD: ")
    receiver_email = input("RECEIVER EMAIL: ")
    subject = input("SUBJECT: ")
    body = input("BODY: ")

    # Basic email address validation
    if not (sender_email and receiver_email):
        print("Please enter valid email addresses.")
        return

    em = EmailMessage()
    em['From'] = sender_email
    em['To'] = receiver_email
    em['Subject'] = subject
    em.set_content(body)

    # Path to the PDF file you want to attach
    pdf_file_path = input("Enter the path to the PDF file: ")

    # Check if the file exists
    if os.path.exists(pdf_file_path):
        # Open the file in binary mode and attach it to the email
        with open(pdf_file_path, 'rb') as pdf_file:
            pdf_data = pdf_file.read()
            em.add_attachment(pdf_data, maintype='application', subtype='pdf', filename=os.path.basename(pdf_file_path))
    else:
        print("The specified file does not exist.")
        return

    context = ssl.create_default_context()

    try:
        with smtplib.SMTP('smtp-mail.outlook.com', 587) as smtp:
            smtp.starttls(context=context)
            smtp.login(sender_email, sender_password)
            smtp.sendmail(sender_email, receiver_email, em.as_string())
        print("Email sent successfully")
    except Exception as e:
        print(f"An error occurred: {e}")


send_email()
