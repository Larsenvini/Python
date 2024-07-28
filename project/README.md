# RacerMail
#### Video Demo: https://youtu.be/EtG1M1yLsNI
#### Description:

RacerMail is a robust and straightforward email scheduling application designed as the final project for the CS50P course, developed by Vinicius Larsen Santos. This command-line interface (CLI) tool allows users to schedule emails to be sent at a specified future time, providing an intuitive way to manage outgoing emails. The project leverages Mailtrap as a testing service, enabling users to test email sending capabilities without needing a live email server setup.

The application makes use of Python's smtplib library for handling SMTP connections, ensuring that emails are reliably sent. It also employs threading to efficiently manage scheduling tasks, enabling seamless email dispatching at the specified times without requiring constant user intervention. The application is a testament to the power of Python for creating practical, real-world applications, blending ease of use with essential email management functionalities.

# Project Structure:

Main File: project.py
The core of the email scheduler, project.py, contains all the necessary logic and functions for managing user inputs, validating email addresses, composing emails, scheduling, and sending emails. It integrates Python's built-in libraries alongside external dependencies to deliver a smooth email scheduling experience.

Test File: test_project.py
This file includes test cases for each of the custom functions in project.py. It employs the pytest framework to validate the accuracy and reliability of the program's components, ensuring that the email scheduling process functions as intended. This comprehensive test suite verifies everything from input validation to email composition.

# Features:

Email Scheduling:
Users can schedule emails to be sent at a specific future time, specifying the recipient, subject, body, and the precise time the email should be dispatched.

Email Validation:
The application ensures that the provided email addresses are valid using the validators library, preventing incorrect email formats from being processed.

Queue System:
A priority queue, implemented via Python's PriorityQueue, efficiently manages scheduled emails, ensuring they are sent at the correct times based on priority (earliest first).

Threading:
A background thread continuously checks the queue and processes emails at their scheduled times, ensuring the main program remains responsive and efficient.

Logging:
Logging is integrated to record all email scheduling and sending activities, aiding in troubleshooting and providing a detailed activity history.

Environment Variables:
The application uses a .env file to manage sensitive information such as Mailtrap SMTP credentials securely, promoting good security practices by keeping credentials out of the main source code.

# Design Choices:

Command-Line Interface (CLI):
The decision to implement a CLI was driven by the desire to create a lightweight and accessible tool that doesn't require a graphical interface. This approach simplifies the interaction model and makes the tool suitable for a wide range of environments, including headless servers.

Mailtrap for Testing:
Mailtrap was chosen as the email testing service to provide a secure and controlled environment for email testing. This choice eliminates the risks associated with sending emails from personal accounts during the development and testing phases.

Use of Threading:
Implementing threading allows the application to handle email scheduling independently of the main user interface, providing a smoother user experience without blocking the main thread for scheduling tasks.

Priority Queue for Scheduling:
Using a priority queue ensures that emails are managed efficiently, with the earliest scheduled emails taking precedence. This choice simplifies email management, automatically prioritizing tasks based on their time constraints.

Environment Variables for Security:
By leveraging the dotenv library, the application maintains a separation between code and sensitive information, adhering to best practices in software security by using environment variables.

# Dependencies:

Python 3.x:
The application is built using Python 3.x, taking advantage of its modern syntax and library support.

smtplib:
Used for handling SMTP connections to send emails, ensuring robust communication with the email server.

validators:
This library is used to validate email addresses, ensuring that only correctly formatted emails are processed.

python-dotenv:
Facilitates loading environment variables from a .env file, securing sensitive data like SMTP credentials.

pytest:
Employed for running test cases, verifying the correctness and stability of the application.

# Installation:

Clone the Repository:

git clone https://github.com/code50/135841562.git
cd project

Install Dependencies:

pip install -r requirements.txt

Setup Environment Variables:

Sign up for MailTrap and create a project, then copy the smtp credentials

Create a .env file in the root directory and add your Mailtrap SMTP credentials:

MAILTRAP_SMTP_SERVER=sandbox.smtp.mailtrap.io
MAILTRAP_SMTP_PORT=587
MAILTRAP_SMTP_USER=your_mailtrap_username
MAILTRAP_SMTP_PASSWORD=your_mailtrap_password

# How to Run:

Start the Email Scheduler:

Run the following command:
python project.py

Choose an Option:

Schedule a new email: Follow the prompts to enter the sender's email, recipient's email, subject, body, and scheduled time.
Exit: Quit the application.

Keep the Program Running:
The program needs to remain active to ensure that scheduled emails are sent successfully at their designated times. If you exit the program, unsent emails in the queue will not be dispatched.

# Testing:
To run the test suite, use the following command in the project's root directory:

pytest test_project.py
This command will execute the unit tests defined in test_project.py, checking for correct functionality and ensuring that each component operates as expected.

# Conclusion:

RacerMail offers a practical solution for scheduling emails through a simple command-line interface. By leveraging Python's robust standard libraries and third-party modules, it provides a reliable platform for managing outgoing emails, supported by a strong foundation in software design principles. This project not only fulfills the requirements of the CS50P final project but also showcases the potential of Python in building efficient, user-friendly applications. Whether for personal use or as a stepping stone for further development, RacerMail demonstrates how a well-architected codebase can deliver significant utility in everyday tasks.
