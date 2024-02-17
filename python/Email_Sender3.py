import win32com.client

def send_email(subject, body, to):
    outlook = win32com.client.Dispatch("Outlook.Application")
    mail = outlook.CreateItem(0)  # 0 represents the Outlook MailItem

    mail.Subject = subject
    mail.Body = body
    mail.To = to

    # To attach a file, you can use the following line:
    # mail.Attachments.Add("C:\\path\\to\\file.txt")

    mail.Send()

send_email("Test Subject", "Test Body", "recipient@example.com")
