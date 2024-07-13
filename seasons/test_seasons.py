import pytest
from seasons import number_to_words

def test_number_to_words():
    assert number_to_words(20) == "Twenty"
