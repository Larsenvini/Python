import pytest
from bank import value

def test_hello(msgn):
    if msgn.startswith("hello"):
        assert value(msgn) == "$0"

def test_h(msgn):
    if msgn.startswith("h"):
        assert value(msgn) == "$20"

def test_other(msgn):
    if test_hello() and test_h() == False:
        assert value(msgn) == "$100"

def test_int():
     with pytest.raises(TypeError):
          value("2")
