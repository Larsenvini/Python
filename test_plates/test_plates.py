import pytest
from plates import is_valid

def test_valid_plates():
    assert is_valid("CS50") == True
    assert is_valid("HUBA7") == True
    assert is_valid("LABA9") == True

def test_invalid_plates():
    assert is_valid("OPAH2340") == False
    assert is_valid("ROB776") == False
    assert is_valid("CS04") == False
    assert is_valid("LABAZ") == False  # Non-digit character in last two positions

def test_edge_cases():
    assert is_valid("") == False  # Empty string
    assert is_valid("A") == False  # Too short
    assert is_valid("ABCDEFGH") == False  # Too long
    assert is_valid("CS50!") == False  # Special characters

if __name__ == "__main__":
    pytest.main()

