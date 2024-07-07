from twttr import shorten

def test_transf():
    assert shorten("Twitter") == "Twttr"
