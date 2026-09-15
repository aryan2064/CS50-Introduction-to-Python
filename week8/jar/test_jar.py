import pytest

from jar import Jar


def test_init():
    jar = Jar(10)
    assert jar.capacity == 10
    assert jar.size == 0


def test_str():
    jar = Jar()
    assert str(jar) == ""

    jar.deposit(1)
    assert str(jar) == "🍪"

    jar.deposit(2)
    assert str(jar) == "🍪🍪🍪"


def test_deposit():
    jar = Jar(5)
    jar.deposit(0)

    with pytest.raises(ValueError):
        jar.deposit(-1)
        jar.deposit(6)
        jar.deposit("")


def test_withdraw():
    jar = Jar()
    jar.deposit(5)
    jar.withdraw(4)

    with pytest.raises(ValueError):
        jar.withdraw(2)
        jar.withdraw(-1)
        jar.withdraw("")
