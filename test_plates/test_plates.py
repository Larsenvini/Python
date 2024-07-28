import pytest
from plates import is_valid

def test_valid_plate1():

    assert is_valid("CS50") == True
def test_valid_plate2():
    assert is_valid("HUBA7") == True

def test_invalid_plate1():
    assert is_valid("OPAH2340") == False

def test_valid_plate2():
    assert is_valid("ROB776") == True


def test_invalid_plate4():
    assert is_valid("AAA22A") == False

def test_invalid_plate6():
    assert is_valid("AAA.") == False

def test_invalid_plate7():
    assert is_valid("AAA 22") == False

def test_invalid_plate8():
    assert is_valid("1AAA22") == False

def test_invalid_plate9():
    assert is_valid("CS.") == False

def test_beggining():
    assert is_valid
if __name__ == "__main__":
    pytest.main()

