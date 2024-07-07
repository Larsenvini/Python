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


if __name__ == "__main__":
    pytest.main()
