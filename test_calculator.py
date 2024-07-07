import pytest
from calculator import square

def main():
    test_positive()
    test_negative()
    test_zero()
    test_decimal()

def test_positive():
    assert square(2) == 4

    assert square(3) == 9

def test_negative():
    assert square(-10) == 100
    assert square(-5) == 25

def test_zero():
    assert square(0) == 0

def test_decimal():
    assert square(1.5) == 2.25

def test_str():
    with pytest.raises(TypeError):
        square("cat")




if __name__ == '__main__':
    main()
