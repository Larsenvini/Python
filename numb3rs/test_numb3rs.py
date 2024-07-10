import pytest
from numb3rs import validate

def test_true():
    assert validate("255.255.255.255") == True
    assert validate("127.0.0.1") == True
    assert validate("12.0.0.1") == True

def test_false():
    assert validate("1.2.3.1000") == False
    assert validate("45.137.315.27") == False
    assert validate("cat") == False
    assert validate("512.512.512.512") == False
    assert validate("o123.0.0.1") == False
    assert validate("127.0.0.1 opaa arroba") == False

def check_first():
    with pytest.raises(ValueError):
        validate("127.0.1")

