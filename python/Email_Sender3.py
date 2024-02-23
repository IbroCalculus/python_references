# import os
# import win32com.client  #(NB: pip install pywin32, FOR THIS TO WORK)
#
# def send_email(subject, body, to):
#     outlook = win32com.client.Dispatch("Outlook.Application")
#     mail = outlook.CreateItem(0)  # 0 represents the Outlook MailItem
#
#     mail.Subject = subject
#     mail.Body = body
#     mail.To = to
#
#     # Get the absolute file path
#     file_path = os.path.abspath("email_sender.pdf")
#
#     # To attach a file, you can use the following line:
#     mail.Attachments.Add(file_path)
#
#     mail.Send()
#
# send_email("Test Subject", "Test Body", "testmail@gmail.com")




# NB: Outlook must be already installed and signed in on the computer device running this program.
# If not sending, You can open outlook to find them in outbox. Enabling metered connection setting within solved it.
# If display=True, this will open the Outlook app, rather that just sending

import os
import win32com.client   # (NB: pip install pywin32, FOR THIS TO WORK)

def send_outlook_email(subject, to, cc, body, display=False):
    ol = win32com.client.Dispatch("outlook.application")
    olmailitem = 0x0  # Size of the new email
    newmail = ol.CreateItem(olmailitem)
    newmail.Subject = subject
    newmail.To = to
    newmail.CC = cc
    newmail.Body = body

    # Get the absolute file path
    file_path = os.path.abspath("email_sender.pdf")
    newmail.Attachments.Add(file_path)

    try:
        if display:
            newmail.Display()
        else:
            newmail.Send()
        print("Email sent successfully")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
# send_outlook_email('NEW SAMPLE Mail', 'example@gmail.com', 'lomih55502@oprevolt.com', 'HELLO, this is a test email.')
send_outlook_email('NEW SAMPLE Mail', 'someone@gmail.com', 'lomih55502@oprevolt.com', 'HELLO, this is a test email.', True)
