import pytest
from datetime import date
from unittest.mock import patch
from seasons import number_to_words, get_birthdate

def test_number_to_words():
    assert number_to_words(20) == "Twenty"
    assert number_to_words(100) == "One hundred"
    assert number_to_words(1234) == "One thousand, two hundred thirty four"

def test_get_birthdate():
    assert get_birthdate("2005-03-02") == "Ten million, one hundred eighty five thousand, one hundred twenty"
    assert get_birthdate("2020-01-01") == "Two million, three hundred eighty three thousand, two hundred"
    assert get_birthdate("2023-07-11") == "Five hundred twenty five thousand, six hundred"


if __name__ == "__main__":
    pytest.main()
