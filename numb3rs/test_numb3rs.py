import pytest
from numb3rs import validate

def test_true():
    assert validate("255.255.255.255") == True
    assert validate("512.512.512.512") == True
    assert validate("127.0.0.1") == True
    assert validate("12.0.0.1") == True
