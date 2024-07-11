from working.working import convert
import pytest

def test_convert():
    assert convert("9 AM TO 5 PM") == "09:00 to 17:00"
    assert convert("8 AM TO 6 PM") == "08:00 to 18:00"
    assert convert("10 AM TO 5 PM") == "10:00 to 17:00"
    assert convert("5 AM TO 10 PM") == "05:00 to 10:00"

def test_excep():
    with pytest.raises(ValueError):
        convert("8 AM TO 5 PM") == "09:00 to 17:00"
        convert("8:30 AM TO 5:30 PM") == "08:31 to 17:30"
        convert("6 AM 8 AM")
        convert("15 AM TO 26 PM")
