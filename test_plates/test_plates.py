import pytest
from plates import is_valid

def test_validornah():
    assert is_valid("OPAH2340") == False
    assert is_valid("ROB776") == False
    assert value("Hello there") == 0

def test_h():
    assert value("hi") == 20
    assert value("hey") == 20

def test_other():
    assert value("good morning") == 100

def test_case_insensitivity():
    assert value("HELLO") == 0
    assert value("HeLLo") == 0
    assert value("hI") == 20
    assert value("HAPPY") == 20


if __name__ == "__main__":
    pytest.main()
