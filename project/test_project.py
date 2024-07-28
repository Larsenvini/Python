# test_project.py
import pytest
import os
from datetime import datetime, timedelta
from project import get_email_address, compose_email, schedule_email, get_send_time, email_queue, send_email
from unittest.mock import patch

# Test get_email_address with valid input
def test_get_email_address(monkeypatch):
    # Simulate user input for email address
    monkeypatch.setattr('builtins.input', lambda _: 'test@example.com')
    email = get_email_address()
    assert email == 'test@example.com'  # Expect valid email address

# Test compose_email generates correct MIME format
def test_compose_email():
    sender = "test@example.com"
    recipient = "recipient@example.com"
    subject = "Test Subject"
    body = "This is a test email."

    email_content = compose_email(sender, recipient, subject, body)

    # Verify that headers and body are included in the email content
    assert "From: test@example.com" in email_content
    assert "To: recipient@example.com" in email_content
    assert "Subject: Test Subject" in email_content
    assert "This is a test email." in email_content

# Test schedule_email correctly adds emails to the queue
def test_schedule_email():
    send_time = datetime.now() + timedelta(minutes=5)
    email_content = "Test email content"
    recipient = "recipient@example.com"
    sender = "sender@example.com"

    schedule_email(send_time, email_content, recipient, sender)

    # Extract the top of the queue and check its contents
    scheduled_email = email_queue.get()
    assert scheduled_email == (send_time, email_content, recipient, sender)  # Verify tuple contents

# Test get_send_time with valid and invalid inputs
def test_get_send_time(monkeypatch):
    # Simulate user input for a valid future date and time
    future_time = (datetime.now() + timedelta(minutes=10)).strftime('%Y-%m-%d %H:%M:%S')
    monkeypatch.setattr('builtins.input', lambda _: future_time)

    send_time = get_send_time()
    assert send_time > datetime.now()  # Check if send time is in the future

    # Simulate user input for an invalid date format
    monkeypatch.setattr('builtins.input', lambda _: 'invalid date')
    with pytest.raises(ValueError):
        get_send_time()

# Test send_email to ensure SMTP interactions are correct (using patch to mock SMTP server)
def test_send_email():
    email_content = "Subject: Test\n\nThis is a test email."
    recipient = "recipient@example.com"
    sender = "sender@example.com"

    with patch('smtplib.SMTP') as MockSMTP:
        # Mock the SMTP instance and its methods
        instance = MockSMTP.return_value
        instance.sendmail.return_value = {}

        # Call send_email and check for interactions
        send_email(email_content, recipient, sender)
        instance.login.assert_called_with(os.getenv('MAILTRAP_SMTP_USER'), os.getenv('MAILTRAP_SMTP_PASSWORD'))
        instance.sendmail.assert_called_with(sender, recipient, email_content)

        # Check log entry for successful email sending
        with open('email_scheduler.log', 'r') as log_file:
            log_contents = log_file.read()
        assert f"Email sent to {recipient} from {sender}" in log_contents
