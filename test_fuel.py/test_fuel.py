import pytest
from fuel import convert, gauge

def test_convertion():
    assert convert("2/4") == 50

def test_empty():
    assert convert("1/4") == 25

def test_full():
    assert convert("4/4") == 100

def test_raises():
    with pytest.raises(ValueError):
        