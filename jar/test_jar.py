import pytest
from jar import Jar

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

    jar = Jar(20)
    assert jar.capacity == 20
    assert jar.size == 0

    with pytest.raises(ValueError):
        Jar(-1)

def test_str():
    jar = Jar()
    assert str(jar) == ""

    jar.deposit(3)
    assert srt(jar) == "🍪🍪🍪"

def test_deposit():
    jar = Jar(10)
    jar.deposit(5)
    assert jar.size == 5

    jar.deposit(5)
    assert jar.size == 10

    with pytest.raises(ValueError):
        jar.deposit(1)

    with pytest.raises(ValueError):
        jar.deposit(-1)

def test_withdraw():
    jar = Jar(10)
    jar.deposit(5)
    jar.withdraw(2)
    assert jar.size == 3

    jar.withdraw(3)
    assert jar.size == 0

    with pytest.raises(ValueError):
        jar.withdraw(1)

    with pytest.raises(ValueError):
        jar.withdraw(-1)

def test_capacity():
    jar = Jar(5)
    assert jar.capacity == 5

def test_size():
    jar = Jar(5)
    assert jar.size == 0

    jar.deposit(3)
    assert jar.size == 3
