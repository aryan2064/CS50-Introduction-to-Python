import pytest

from week5.test_fuel.fuel import convert, gauge


def test_convert_fraction_str():
    with pytest.raises(ValueError):
        convert("a/b")


def test_convert_fraction_float_str():
    with pytest.raises(ValueError):
        convert("1.2/3.4")


def test_convert_x_greater_y():
    with pytest.raises(ValueError):
        convert("2/1")


def test_convert_y_zero():
    with pytest.raises(ZeroDivisionError):
        convert("0/0")


def test_convert_x_negative():
    with pytest.raises(ValueError):
        convert("-3/4")


def test_convert_y_negative():
    with pytest.raises(ValueError):
        convert("3/-4")


def test_convert_fraction_valid():
    assert convert("3/4") == 75


def test_gauge_E():
    assert gauge(1) == "E"


def test_gauge_percent():
    assert gauge(2) == "2%"
    assert gauge(98) == "98%"


def test_gauge_F():
    assert gauge(99) == "F"
