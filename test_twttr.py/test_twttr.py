import pytest
from twttr import shorten

def test_transf():
    assert shorten("Twitter") == "Twttr"

def test_str():
    with pytest.raises()


