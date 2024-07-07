# import requests

# def send_multiple_attached_outlook_email(subject, to, body, display=False, attachment_paths=None):
#     data = {"to": to, "subject": subject, "message": body, "attachmentBase64": "", "attachmentFilename": ""}
#
#     # Check if there is an attachment
#     if attachment_paths:
#         path = attachment_paths[0]  # Since there is only one file, get the first element
#         print(f"ATTACHED FILE PATH: {path}")
#
#         # Get the filename from the path
#         filename = path.split("/")[-1]
#         print(f"ATTACHED FILE NAME: {filename}")
#
#         try:
#             # Read the file and encode its content to base64
#             with open(path, "rb") as file:
#                 encoded_content = base64.b64encode(file.read()).decode('utf-8')
#
#             # Set the attachmentBase64 field in the data dictionary
#             data["attachmentBase64"] = encoded_content
#
#             # Optionally, you can also set the filename in the data dictionary
#             data["attachmentFilename"] = filename
#
#             moveToArchive(path)
#
#         except Exception as e:
#             print(f"Error encoding file {path}: {e}")
#
#     # Display the data if required
#     if display:
#         print(data)
#
#     print(f"DATA: {data}")
#     # print(f"ATTACHMENT PATH: {data["attachmentFilename"]}")
#
#     url = "http://xamagos-001-site4.ctempurl.com/api/Email/send_mail_coolgirls"
#     try:
#         response = requests.post(url, json=data)
#         response.raise_for_status()  # Raise an error for bad status codes
#         print("Email sent successfully.")
#     except Exception as e:
#         print(f"Error sending email: {e}")

# =======================================

# @app.post("/login")
# async def login(email: str = Form(...), password: str = Form(...)):
#     connection = connect_to_mysql(host=dbHostName, username=dbUsername, password=dbPassword, database=databaseName)
#     cursor = connection.cursor()
#     cursor.execute(f"SELECT * FROM {login_table} WHERE email = %s AND password = %s", (email, password))
#     result = cursor.fetchone()
#     print(f"RESULT: {result}")
#     cursor.close()
#     connection.close()
#     if result:
#         return {"message": "Login successful"}
#     else:
#         raise HTTPException(status_code=401, detail="Incorrect email or password")
