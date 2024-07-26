import os
import base64
import time
import threading
import logging
import validators
from dotenv import load_dotenv
from datetime import datetime
from queue import PriorityQueue
from getpass import getpass
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Google API client libraries
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Logging configuration
logging.basicConfig(
    filename='email_scheduler.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

load_dotenv()

# Constants
SCOPES = ['https://www.googleapis.com/auth/gmail.send']

# Priority queue to handle scheduled emails
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
    print("Ok! Please login to your Google account.")
    service = authenticate_gmail()

    sender = get_email_address()
    recipient = input("To: ")
    subject = input("Subject: ")
    body = input("Body: ")
    send_time = get_send_time()

    email_content = compose_email(sender, recipient, subject, body)
    schedule_email(send_time, email_content, recipient, service)
    print("Your email has been scheduled!")

def authenticate_gmail():
    """
    Authenticate the user via OAuth 2.0 and return a Gmail API service object.
    """
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    return build('gmail', 'v1', credentials=creds)

def get_email_address():
    while True:
        email = input("Email address: ")
        if validators.email(email):
            print("Valid")
            return email
        else:
            print("Invalid, try again.")

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

def compose_email(sender, recipient, subject, body):
    """
    Compose an email with the given details and return it as a MIMEText object.
    """
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    return msg

def schedule_email(send_time, email_content, recipient, service):
    """
    Schedule the email to be sent at the specified time.
    """
    email_queue.put((send_time, email_content, recipient, service))
    logging.info(f"Email scheduled to {recipient} at {send_time}")

def send_email(service, sender, recipient, email_content):
    """
    Send an email using the Gmail API.
    """
    try:
        raw = base64.urlsafe_b64encode(email_content.as_bytes()).decode('utf-8')
        message = {'raw': raw}

        # Use the Gmail API to send the email
        message = (service.users().messages().send(userId=sender, body=message).execute())

        logging.info(f"Email sent to {recipient} from {sender} with Message ID: {message['id']}")
        print(f"Email successfully sent to {recipient}")
    except Exception as e:
        logging.error(f"An error occurred while sending the email: {e}")
        print(f"An error occurred while sending the email: {e}")

def process_scheduled_emails():
    """
    Continuously check the email queue and send emails at the scheduled time.
    """
    while True:
        try:
            if not email_queue.empty():
                send_time, email_content, recipient, service = email_queue.queue[0]

                if datetime.now() >= send_time:
                    email_queue.get()
                    sender = email_content['From']
                    send_email(service, sender, recipient, email_content)
            time.sleep(5)
        except Exception as e:
            logging.error(f"Error in processing scheduled emails: {e}")
            print(f"Error in processing scheduled emails: {e}")

# Starting the scheduler
scheduler_thread = threading.Thread(target=process_scheduled_emails, daemon=True)
scheduler_thread.start()

if __name__ == "__main__":
    main()
