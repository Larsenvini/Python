import pytest
from seasons import number_to_words, get_birthdate

def test_number_to_words():
    assert number_to_words(20) == "Twenty"

def test_get_birthdate():
    assert get_birthdate("2005-03-02") == "
