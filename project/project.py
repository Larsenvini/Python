# Code for the Final Project CS50P - Vinicius Larsen Santos
import smtplib
import time
import threading
import logging
import validators
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime, timedelta
from getpass import getpass

logging.basicConfig(filename='email_scheduler.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')



SMTP_PROVIDERS = {
    'gmail': {
        'server': 'smtp.gmail.com',
        'port': 587
    },
    'icloud': {
        'server': 'smtp.mail.me.com',
        'port': 587
    },
    'outlook': {
        'server': 'smtp-mail.outlook.com',
        'port': 587
    },
    'yahoo': {
        'server': 'smtp.mail.yahoo.com',
        'port': 587
    }
}

def main():
    print("Welcome to RacerMail!")
    provider = get_provider_choice()
    print("Ok! Please login: ")
    sender = 
    password = getpass("Password: ")
    recipient = input("To: ")
    subject = input("Subject: ")
    body = input(" ")
    send_time = datetime.now() + timedelta(seconds=10)
    smtp_info = get_smtp_info(provider, sender, password)
    email_content = compose_email(sender, recipient, subject, body)
    schedule_email(send_time, email_content, recipient, smtp_info)

def get_provider_choice():

     provider_map = {
        '1': 'gmail',
        '2': 'icloud',
        '3': 'outlook',
        '4': 'yahoo'
     }

     while True:
        print("Select your email provider: ")
        print("1. Gmail")
        print("2. iCloud")
        print("3. Outlook/Hotmail")
        print("4. Yahoo")
        provider_choice = input("Enter the number of your provider: ")

        if provider_choice in provider_map:
            return provider_map[provider_choice]
        else:
            print("Invalid choice. Please try again.")

def get_smtp_info(provider, email, password):
    if provider not in SMTP_PROVIDERS:
        raise ValueError("Unsupported email provider.\n Supported: Gmail, Icloud, Outlook/ Hotmail & Yahoo.")
    smtp_details = SMTP_PROVIDERS[provider]
    return {
        'server': smtp_details['server'],
        'port': smtp_details['port'],
        'username': email,
        'password': password
    }
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
        logging.info(f"Email sent to {recipient} from {smtp_info['username']}")
    except Exception as e:
        logging.error(f"Failed to send email to {recipient}: {e}")

        print(f"Failed to send email: {e}")

if __name__ == "__main__":
    main()
