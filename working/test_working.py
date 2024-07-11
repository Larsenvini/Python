from working.working import convert
import pytest

def test_convert():
    assert convert("9 AM TO 5 PM") == "09:00 to 17:00"
    assert convert("8 AM TO 6 PM") == "08:00 to 18:00"
    assert convert("10 AM TO 5 PM") == "10:00 to 17:00"
    assert convert("5 AM TO 10 PM") == "05:00 to 10:00"

def test_invalid_format():
    with pytest.raises(ValueError):
        convert("8 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("08:30 TO 17:30")
    with pytest.raises(ValueError):
        convert("6 AM 8 AM")
    with pytest.raises(ValueError):
        convert("8 AM until 22 PM")

def test_invalid_time():
    with pytest.raises(ValueError):
        convert("12:60 AM - 5: PM")
    with pytest.raises(ValueError):
        convert("08:30 TO 17:30")
    with pytest.raises(ValueError):
        convert("6 AM 8 AM")
    with pytest.raises(ValueError):
        convert("8 AM until 22 PM")

