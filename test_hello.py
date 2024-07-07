from hello import hello

def test_hello():
    assert hello("Vini") == "Hello, Vini"
    assert hello() == "Hello, World"

