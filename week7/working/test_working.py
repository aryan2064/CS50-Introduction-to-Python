import pytest

from working import convert


def test_convert_right_hours():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"


def test_convert_right_minutes():
    assert convert("9:30 AM to 5:30 PM") == "09:30 to 17:30"


def test_convert_off_hours():
    assert convert("9:00 AM to 5:00 PM") != "09:00 to 16:00"


def test_convert_off_minutes():
    assert convert("9:30 AM to 5:30 PM") != "9:00 AM to 5:00 PM"


def test_convert_no_to():
    with pytest.raises(ValueError):
        convert("9:30 AM 5:30 PM")


def test_convert_out_of_range_time():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")
