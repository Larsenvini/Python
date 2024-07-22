# Code for the Final Project CS50P - Vinicius Larsen Santos
import smtplib
import time
import threading
import logging
import validators
import os
from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime, timedelta
from getpass import getpass
from queue import PriorityQueue

logging.basicConfig(filename='email_scheduler.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

load_dotenv()

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

# priority queue to handle scheduled emails
email_queue = PriorityQueue()

def main():
    print("Welcome to RacerMail!")
    while True:
        print("1. Schedule a new email")
        print("2. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            schedule_new_email()
        elif choice == "2":
            print("Exiting RacerMail. Goodbye!")
            break
        else:
            print("Invalid choice")

def schedule_new_email():
    provider = get_provider_choice()
    print("Ok! Please login: ")
    sender = get_email_address()
    password = getpass("Password: ")
    recipient = input("To: ")
    subject = input("Subject: ")
    body = input("Body: ")
    send_time = get_send_time()
    smtp_info = get_smtp_info(provider, sender, password)
    email_content = compose_email(sender, recipient, subject, body)
    schedule_email(send_time, email_content, recipient, smtp_info)
    print("Email Sent!")

def get_email_address():
    while True:

        email = input("Email address: ")
        if validators.email(email) == True:
            print("Valid")
            return email
        else:
            print("Invalid, try again.")


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

def get_send_time():
    while True:
        try:
            send_time_str = input("Enter the send time (YYYY-MM-DD HH:MM:SS): ")
            send_time = datetime.strptime(send_time_str, '%Y-%m-%d %H:%M:%S')
            if send_time <= datetime.now():
                print("The send time must be in the future.")
            else:
                return send_time
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD HH:MM:SS.")
# function to send emails, takes as arguments(3):
# email_content, recipient, smtp_info.
def send_email(email_content, recipient, smtp_info):
    try:
        with smtplib.SMTP(smtp_info['server'], smtp_info['port']) as server:
            server.starttls()
            server.login(smtp_info['username'], smtp_info['password'])
            server.sendmail(smtp_info['username'], recipient, email_content)
        logging.info(f"Email sent to {recipient} from {smtp_info['username']}")

    except smtplib.SMTPAuthenticationError:
        logging.error(f"Authentication failed for {smtp_info['username']}")
        print("Authentication failed. Please check your email and password.")
    except smtplib.SMTPConnectError:
        logging.error(f"Failed to connect to the SMTP server {smtp_info['server']}")
        print("Failed to connect to the SMTP server. Please check your network connection.")
    except smtplib.SMTPServerDisconnected:
        logging.error("Disconnected from the SMTP server unexpectedly")
        print("Disconnected from the SMTP server. Please try again.")
    except smtplib.SMTPException as e:
        logging.error(f"SMTP error occurred: {e}")
        print(f"An error occurred while sending the email: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
