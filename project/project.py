# Code for the Final Project CS50P - Vinicius Larsen Santos
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime, timedelta

import time
import threading

def main():
    ...

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

def search_email():
    ...

def send_email():
    ...

def resend_email():
    ...
