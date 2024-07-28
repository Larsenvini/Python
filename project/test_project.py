# test_project.py

import pytest
from datetime import datetime, timedelta
from project import get_email_address, compose_email, schedule_email, get_send_time, email_queue

def test_get_email_address(monkeypatch):
    # Simulate user input for email address
    monkeypatch.setattr('builtins.input', lambda _: 'test@example.com')
    email = get_email_address()
    assert email == 'test@example.com'

def test_compose_email():
    sender = "test@example.com"
    recipient = "recipient@example.com"
    subject = "Test Subject"
    body = "This is a test email."

    email_content = compose_email(sender, recipient, subject, body)
    assert "From: test@example.com" in email_content
    assert "To: recipient@example.com" in email_content
    assert "Subject: Test Subject" in email_content
    assert "This is a test email." in email_content

def test_schedule_email():
    send_time = datetime.now() + timedelta(minutes=5)
    email_content = "Test email content"
    recipient = "recipient@example.com"

    schedule_email(send_time, email_content, recipient)
    scheduled_email = email_queue.get()
    assert scheduled_email == (send_time, email_content, recipient)

def test_get_send_time(monkeypatch):
    # Simulate user input for a valid future date and time
    future_time = (datetime.now() + timedelta(minutes=10)).strftime('%Y-%m-%d %H:%M:%S')
    monkeypatch.setattr('builtins.input', lambda _: future_time)

    send_time = get_send_time()
    assert send_time > datetime.now()

    # Simulate user input for an invalid date format
    monkeypatch.setattr('builtins.input', lambda _: 'invalid date')
    with pytest.raises(ValueError):
        get_send_time()
