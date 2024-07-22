# Code for the Final Project CS50P - Vinicius Larsen Santos
import smtplib
from email.mime.text import MIMEtext
from email.mime.multipart import MimeMultipart
from datetime import datetime, timedelta

import time
import threading

def main():
    ...

# function to compose email, takes as arguments:
# the sender, recipient, subject and body, just like an email.
def compose_email(sender, recipient, subject, body):
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    return msg.as_string()

def store_email():
    ...

def search_email():
    ...

def send_email():
    ...

def resend_email():
    ...
