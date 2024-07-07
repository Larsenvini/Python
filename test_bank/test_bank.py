import pytest
from bank import value

def test_hello():
    assert value("Hello") == 0
    assert value("hello") == 0
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


def test_int():
     with pytest.raises(TypeError):
          value(2)

if __name__ == "__main__":
    pytest.main()
