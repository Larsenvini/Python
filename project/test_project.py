from project import compose_email, schedule_email, send_email
from datetime import datetime, timedelta

def test_compose_email():
    sender = "test@example.com"
    recipient = "recipient@example.com"
    subject = "Test Subject"
    body = "Test email body"
    email_content = compose_email(sender, recipient, subject, body)
    assert "Test Subject" in email_content
    assert "Test email body" in email_content

def test_schedule_email():
    send_time = datetime.now() + timedelta(seconds=10)
    email_content = "Test content"
    recipient = "recipient@example.com"
    smtp_info = {'server': 'smtp.example.com', 'port': 587, 'username': 'user', 'password': 'pass'}
    try:
        schedule_email(send_time, email_content, recipient, smtp_info)
        assert True
    except ValueError:
        assert False

def test_send_email():
    email_content = "Test email content"
    recipient = "recipient@example.com"
    smtp_info = {'server': 'smtp.example.com', 'port': 587, 'username': 'user', 'password': 'pass'}
    try
