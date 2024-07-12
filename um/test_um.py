import pytest
from um import count

def main():
    test_okstr()




def test_okstr():
    assert count("um opa um") == 2
    assert count(" so i was thinking um umm maybe um we could um go out") == 3

def test_notokstr():
    with pytest.raises(ValueError):
        count("22123")

    


