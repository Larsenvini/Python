# Code for the Final Project CS50P - Vinicius Larsen Santos
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime, timedelta

import time
import threading

def main():
    print("New message")
    sender = input("From: ")
    recipient = input("To: ")
    subject = input("Subject: ")
    body = input(" ")
    send_time = datetime.now() + timedelta(seconds=10)
    email_content = subject, body
    compose_email

# function to compose email, takes as arguments(4):
# the sender, recipient, subject and body, just like an email.
def compose_email(sender, recipient, subject, body):
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    return msg.as_string()

# function to schedule mail, takes as arguments(4):
# send_time, email_content, recipient, smtp_info.
def schedule_email(send_time, email_content, recipient, smtp_info):
    delay = (send_time - datetime.now()).total_seconds()
    if delay < 0:
        raise ValueError("Scheduled time must be in the future")

    threading.Timer(delay, send_email, [email_content, recipient, smtp_info]).start()

# function to send emails, takes as arguments(3):
# email_content, recipient, smtp_info.
def send_email(email_content, recipient, smtp_info):
    try:
        with smtplib.SMTP(smtp_info['server'], smtp_info['port']) as server:
            server.starttls()
            server.login(smtp_info['username'], smtp_info['password'])
            server.sendmail(smtp_info['username'], recipient, email_content)
    except Exception as e:
        print(f"Failed to send email: {e}")

if __name__ == "__main__":
    main()
