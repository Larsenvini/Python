# RACER MAIL

#### Video Demo:  <URL HERE>

#### Description:

RacerMail is a simple email scheduling application, developed as part of the CS50P final project by Vinicius Larsen Santos. It allows users to schedule emails to be sent at a specified time using Mailtrap as a testing service. The program provides a command-line interface (CLI) for scheduling emails and handles sending emails at the scheduled time using Python's smtplib library and threading for scheduling.

#### Project Structure:

Main File: project.py - Contains the main code for the email scheduler.
Test File: test_project.py - Contains the test cases for the functions in project.py.

#### Features:
Schedule Emails: Users can schedule emails by specifying the recipient, subject, body, and time to send.
Email Validation: The email addresses are validated using the validators library to ensure correctness.
Queue System: A priority queue (PriorityQueue) is used to manage scheduled emails based on the scheduled time.
Threading: Uses a background thread to constantly check and process scheduled emails.
Logging: Logs are maintained to keep track of email scheduling and sending activities.
Environment Variables: Uses a .env file to securely manage sensitive information like Mailtrap SMTP credentials.

#### Dependencies:
Python 3.x
smtplib - For handling SMTP connections.
validators - For validating email addresses.
python-dotenv - For loading environment variables from a .env file.
pytest - For running the test cases.

#### Installation:

Clone the Repository:

git clone https://github.com/your-repo/email-scheduler.git
cd email-scheduler

Install Dependencies:

pip install -r requirements.txt

Setup Environment Variables:

Create a .env file in the root directory and add your Mailtrap SMTP credentials:

MAILTRAP_SMTP_SERVER=sandbox.smtp.mailtrap.io
MAILTRAP_SMTP_PORT=587
MAILTRAP_SMTP_USER=your_mailtrap_username
MAILTRAP_SMTP_PASSWORD=your_mailtrap_password

#### How to Run:

Start the Email Scheduler

run:
python project.py

Choose an Option

1. Schedule a new email: Follow the prompts to enter the sender's email, recipient's email, subject, body, and scheduled time.
2. Exit: Quit the application.

Keep the Program Running: The program needs to be kept running for the scheduled emails to be sent successfully.

