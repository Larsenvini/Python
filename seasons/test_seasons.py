import pytest
from datetime import date
from unittest.mock import patch
from seasons import number_to_words, get_birthdate

def test_number_to_words():
    assert number_to_words(20) == "Twenty"
    assert number_to_words(100) == "One hundred"
    assert number_to_words(1234) == "One thousand, two hundred thirty four"

@patch('builtins.input', return_value="2005-03-02")
@patch('seasons.date')  # Adjust 'seasons' to your actual module name
def test_get_birthdate(mock_date, mock_input):
    # Mock the current date
    mock_date.today.return_value = date(2024, 7, 11)
    mock_date.side_effect = lambda *args, **kw: date(*args, **kw)

    assert get_birthdate("2005-03-02") == "Ten million, one hundred eighty five thousand, one hundred twenty"
    assert get_birthdate("2020-01-01") == "Two million, two hundred ninety nine thousand, four hundred forty"
    assert get_birthdate("2023-07-11") == "Five hundred twenty five thousand, six hundred"


if __name__ == "__main__":
    pytest.main()
