import pytest
from plates import is_valid

def test_plate1():
    assert is_valid("OPAH2340") == False

def test_plate2():
    assert is_valid("ROB776") == False

def test_plate3():
    assert is_valid("CS50") == True

def test_plate4():
    assert is_valid("HUBA7") == True

def test_plate5():
    assert is_valid("CS04") == False

def test_plate6():
    assert is_valid("AB12CD") == True

def test_plate7():
    assert is_valid("XY00YZ") == False

def test_plate8():
    assert is_valid("Aa23Bb") == False

def test_plate9():
    assert is_valid("12ab34") == False

def test_plate10():
    assert is_valid("AB1234") == False

def test_plate_empty():
    assert is_valid("") == False

def test_plate_short():
    assert is_valid("ABC1") == False

def test_plate_long():
    assert is_valid("ABC12345") == False

def test_plate_invalid_characters():
    assert is_valid("AB$123") == False

if __name__ == "__main__":
    pytest.main()

