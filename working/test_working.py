from working import convert
import pytest

def test_valid_conversion():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"
    assert convert("12:00 PM to 12:00 AM") == "12:00 to 00:00"
    assert convert("11:59 AM to 12:01 PM") == "11:59 to 12:01"

def test_invalid_format():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("09:00 to 17:00")
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("13:00 AM to 5:00 PM")

def test_invalid_time():
    with pytest.raises(ValueError):
        convert("12:60 AM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("9:00 AM to 13:00 PM")
    with pytest.raises(ValueError):
        convert("9:00 AM to 5:60 PM")
    with pytest.raises(ValueError):
        convert("12:00 PM to 12:60 AM")

def test_edge_cases():
    with pytest.raises(ValueError):
        convert("9AM to 5PM")  # Missing spaces
    with pytest.raises(ValueError):
        convert("09:00 to 17:00")  # Missing AM/PM
    with pytest.raises(ValueError):
        convert("9:00AM to 5:00PM")  # No spaces between numbers and AM/PM
    with pytest.raises(ValueError):
        convert("9:00 PM to 5:00 AM to 7:00 PM")  # Extra time range

if __name__ == "__main__":
    pytest.main()
