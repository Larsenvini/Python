# Code for the Final Project CS50P - Vinicius Larsen Santos
import os
import time
import threading
import logging
import validators
from dotenv import load_dotenv
from datetime import datetime
from queue import PriorityQueue
from getpass import getpass

# Resend library
from resend import Resend

# Logging configuration
logging.basicConfig(
    filename='email_scheduler.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

load_dotenv()

# Load Resend API key from environment
RESEND_API_KEY = os.getenv("RESEND_API_KEY")
if not RESEND_API_KEY:
    raise ValueError("API key not found. Please set the RESEND_API_KEY in your environment variables.")

# Initialize Resend client
resend = Resend(api_key=RESEND_API_KEY)

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
    sender = get_email_address()
    recipient = input("To: ")
    subject = input("Subject: ")
    body = input("Body: ")
    send_time = get_send_time()

    email_content = compose_email(sender, recipient, subject, body)
    schedule_email(send_time, email_content, recipient)
    print("Your email has been scheduled!")

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
    Compose an email with the given details and return it as a dictionary.
    """
    return {
        "from": sender,
        "to": [recipient],
        "subject": subject,
        "html": f"<p>{body}</p>",  # Using HTML for email body
        "text": body  # Plain text version
    }

def schedule_email(send_time, email_content, recipient):
    """
    Schedule the email to be sent at the specified time.
    """
    email_queue.put((send_time, email_content, recipient))
    logging.info(f"Email scheduled to {recipient} at {send_time}")

def send_email(email_content):
    """
    Send an email using the Resend API.
    """
    try:
        # Use the Resend API to send the email
        response = resend.emails.send(email_content)

        logging.info(f"Email sent to {email_content['to']} with response: {response}")
        print(f"Email successfully sent to {email_content['to']}")
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
                send_time, email_content, recipient = email_queue.queue[0]

                if datetime.now() >= send_time:
                    email_queue.get()
                    send_email(email_content)
            time.sleep(5)
        except Exception as e:
            logging.error(f"Error in processing scheduled emails: {e}")
            print(f"Error in processing scheduled emails: {e}")

# Starting the scheduler
scheduler_thread = threading.Thread(target=process_scheduled_emails, daemon=True)
scheduler_thread.start()

if __name__ == "__main__":
    main()
