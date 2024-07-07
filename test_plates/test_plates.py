import pytest
from plates import is_valid

def test_validornah():
    assert is_valid("OPAH2340") == False
    assert is_valid("ROB776") == False
    assert is_valid("CS50") == True
    assert is_valid("HUBA7") == True

if __name__ == "__main__":
    pytest.main()
