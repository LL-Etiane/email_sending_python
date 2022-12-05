import smtplib
import ssl #this for securing your connection
from email.message import EmailMessage

SMTP_SERVER = "smtp.gmail.com"
PORT = 465
YOUR_EMAIL = "youremail here@gmail.com" #login email of your smtp sever or gmail if you are using gmail
PASSWORD = "Your password here"

ssl_context = ssl.create_default_context() #to be used in securing the connection

receiver_email = "reciever's email"
subject = "Subject here"
message_body = """
Then message body here. Keep the above new line for proper formating
"""

emailObj = EmailMessage()
emailObj['from'] = YOUR_EMAIL 
emailObj['to'] = receiver_email
emailObj['subject'] = subject
emailObj.set_content(message_body)

with smtplib.SMTP_SSL(SMTP_SERVER,PORT, context=ssl_context) as smtp_sever:
    smtp_sever.login(YOUR_EMAIL, PASSWORD)
    smtp_sever.sendmail(YOUR_EMAIL, receiver_email, emailObj.as_string())
