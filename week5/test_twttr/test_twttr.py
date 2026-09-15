import pytest

from week5.test_twttr.twttr import shorten


def test_shorten_lowercase_str():
    assert shorten("twitter") == "twttr"


def test_shorten_uppercase_srt():
    assert shorten("TWITTER") == "TWTTR"


def test_shorten_empty_str():
    assert shorten("") == ""


def test_shorten_numbers_str():
    assert shorten("12345") == "12345"


def test_shorten_punctuation_str():
    assert shorten(".,:;?/^`{[]()}!@#$%¨&*-_=+") == ".,:;?/^`{[]()}!@#$%¨&*-_=+"


def test_shorten_no_word():
    with pytest.raises(TypeError):
        shorten()
