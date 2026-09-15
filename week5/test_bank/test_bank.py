import pytest

from week5.test_bank.bank import value


def test_bank_lowercase_hello():
    assert value("hello a") == 0


def test_bank_uppercase_hello():
    assert value("HELLO A") == 0


def test_bank_lowercase_h():
    assert value("hey") == 20


def test_bank_uppercase_h():
    assert value("HEY") == 20


def test_bank_lowercase_other_greeting():
    assert value("what's up") == 100


def test_bank_uppercase_other_greeting():
    assert value("WHAT'S UP") == 100


def test_bank_empty_str():
    assert value("") == 100


def test_bank_no_str():
    with pytest.raises(TypeError):
        value()
