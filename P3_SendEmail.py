'''
Project 3
Problem Statement:
You want to write a Python program that can send emails to one or multiple recipients using an email account.

Question:
How can I write a Python program that can send emails to one or multiple recipients using an email account?
'''

import smtplib, ssl
from email.message import EmailMessage

# Email details
sender_email = "testing@gmail.com"
receiver_email = "testing@gmail.com"
password = "Test"

# Create the email
msg = EmailMessage()
msg["From"] = sender_email
msg["To"] = receiver_email
msg["Subject"] = "Test Email"
msg.set_content("Hello! This is a test email sent using Python.")

# Create a secure SSL context
context = ssl.create_default_context()

# Send the email
try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.send_message(msg)
        print("Email sent successfully!")
except Exception as e:
        print("Error sending email:", e)
