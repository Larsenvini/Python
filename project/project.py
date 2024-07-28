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

load_dotenv() #loading .env

logging.basicConfig( #logging set up
    filename='email_scheduler.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

#mailtrap's smtp credentials
MAILTRAP_SMTP_SERVER = os.getenv('MAILTRAP_SMTP_SERVER')
MAILTRAP_SMTP_PORT = int(os.getenv('MAILTRAP_SMTP_PORT'))
MAILTRAP_SMTP_USER = os.getenv('MAILTRAP_SMTP_USER')
MAILTRAP_SMTP_PASSWORD = os.getenv('MAILTRAP_SMTP_PASSWORD')

#queue to handle scheduled emails
email_queue = PriorityQueue()

#main function welcoming user and options
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

#function to add a email to schedule list
def schedule_new_email():
    print("Ok! Please login to your email account.")
    sender = get_email_address()
    recipient = input("To: ")
    subject = input("Subject: ")
    body = input("Body: ")
    send_time = get_send_time()
    email_content = compose_email(sender, recipient, subject, body)
    schedule_email(send_time, email_content, recipient, sender)
    print("Your email has been scheduled!")

#function to get and validate a email address
def get_email_address():
    while True:
        email = input("Email address: ")
        if validators.email(email):
            print("Valid")
            return email
        else:
            print("Invalid, try again.")

#function to compose the mail with parameters
def compose_email(sender, recipient, subject, body):
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    return msg.as_string()

#function to schedule the email
def schedule_email(send_time, email_content, recipient, sender):
    email_queue.put((send_time, email_content, recipient, sender))
    logging.info(f"Email scheduled to {recipient} at {send_time}")

#function to get the time the email needs to be sent
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

#function to send the email
def send_email(email_content, recipient, sender):
    try:
        with smtplib.SMTP(MAILTRAP_SMTP_SERVER, MAILTRAP_SMTP_PORT) as server:
            server.login(MAILTRAP_SMTP_USER, MAILTRAP_SMTP_PASSWORD)
            server.sendmail(sender, recipient, email_content)

        logging.info(f"Email sent to {recipient} from {sender}")
        print(f"Email successfully sent to {recipient}")
    except smtplib.SMTPAuthenticationError:
        logging.error(f"Authentication failed for {sender}")
        print("Authentication failed. Please check your email and password.")
    except smtplib.SMTPConnectError:
        logging.error(f"Failed to connect to the SMTP server {MAILTRAP_SMTP_SERVER}")
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

#function to check and proccess the scheduled emails
def process_scheduled_emails():
    while True:
        try:
            if not email_queue.empty():
                send_time, email_content, recipient, sender = email_queue.queue[0]

                if datetime.now() >= send_time:
                    email_queue.get()
                    send_email(email_content, recipient, sender)
            time.sleep(5)
        except Exception as e:
            logging.error(f"Error in processing scheduled emails: {e}")
            print(f"Error in processing scheduled emails: {e}")

#starting the scheduler
scheduler_thread = threading.Thread(target=process_scheduled_emails, daemon=True)
scheduler_thread.start()

#obs: the program must stay running on the options menu for the scheduled emails to be succesfully sent.

if __name__ == "__main__":
    main()
