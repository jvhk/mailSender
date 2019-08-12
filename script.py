from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

#Sender email structure
sender_email = "yourpassword@gmail.com"
receiver_email = "whowillreceive@hotmail.com"
message = """\
Subject: Hi there

This message is sent from a Python script."""

############


######### Server
smtp_server = "smtp.gmail.com"
port = 587  # For starttls without ssl autentication
sender_email = "yourpassword@gmail.com"
password = input("Type your password and press enter: ")

# Create a secure SSL context
#context = ssl.create_default_context()

# Try to log in to server and send email
try:
    server = smtplib.SMTP(smtp_server,port)
    server.ehlo() # Can be omitted
    server.starttls(context=context) # Secure the connection
    server.ehlo() # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
    # TODO: Send email here
except Exception as e:
    # Print any error messages to stdout
    print(e)
finally:
    server.quit()

#########

print("Sucess!!")
