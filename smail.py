import smtplib
import ssl #this for securing your connection

SMTP_SERVER = "smtp.gmail.com"
PORT = 465
YOUR_EMAIL = "youremail here@gmail.com" #login email of your smtp sever or gmail if you are using gmail
PASSWORD = "Your password here"

ssl_context = ssl.create_default_context() #to be used in securing the connection

receiver_email = "reciever's email"
message = """\
Subject: Your subject here

Then message body here. Keep the above new line for proper formating
"""
try:
    print("Connecting to server")
    server = smtplib.SMTP_SSL(SMTP_SERVER,PORT, context=ssl_context)

    print("Logining in")
    server.login(YOUR_EMAIL, PASSWORD)

    print("sending email")

    #send email
    server.sendmail(YOUR_EMAIL, receiver_email, message)

except Exception as e:
    print(e)
    