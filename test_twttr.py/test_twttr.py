import pytest
from twttr import shorten

def test_transf():
    assert shorten("Twitter") == "Twttr"
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("twittER") == "twttR"
    assert shorten("tw!tt3r") == "tw!tt3r"
    assert shorten("AEIOUaeiou") == ""




