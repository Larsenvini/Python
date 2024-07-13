import pytest
from seasons import number_to_words, get_birthdate

def test_number_to_words():
    assert number_to_words(20) == "Twenty"

@patch('builtins.input', return_value="2005-03-02")
@patch('seasons.py')
def test_get_birthdate(mock_date, mock_input):
    mock_date.today.return_value = date(2024, 7, 11)
    mock_date.side_effect = lambda *args, **kw: date(*args, **kw)

    assert get_birthdate() == "Ten million, one hundred eighty five thousand, one hundred twenty"

if __name__ == "__main__":
    pytest.main()
