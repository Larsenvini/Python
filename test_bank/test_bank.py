import pytest
from bank import greet

def test_hello(msgn):
    if msgn.startswith("hello"):
        assert greet(msgn) == "$0"

def test_h(msgn):
    if msgn.startswith("h"):
        assert greet(msgn) == "$20"

def test_other(msgn):
    if msgn.startswith("h", "hello") == False:
        assert greet(msgn) == "$100"

def test_int():
     with pytest.raises(TypeError):
          greet("2")
