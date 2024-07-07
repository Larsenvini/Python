import pytest
from bank import greet

def test_bank(msgn):
    if msgn.startswith("hello"):
        assert greet(msgn) == "$0"

    elif msgn.startswith("h"):
        assert greet(msgn) == "$20"

    else:
        assert greet(msgn) == "$100"
