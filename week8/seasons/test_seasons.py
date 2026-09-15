from datetime import date
from seasons import validate_date, calculate_minutes_difference, format_minutes


def test_validate_date_valid():
    assert validate_date("2000-01-01") == date(2000, 1, 1)


def test_validate_date_invalid():
    assert validate_date("January 1, 2000") is None
    assert validate_date("") is None


def test_calculate_minutes_difference():
    assert calculate_minutes_difference(
        date(2000, 1, 1),
        date(2000, 1, 2)
    ) == 1440

    assert calculate_minutes_difference(
        date(2000, 1, 1),
        date(2000, 1, 10)
    ) == 12960


def test_format_minutes():
    assert format_minutes(2) == "Two minutes"
    assert format_minutes(60) == "Sixty minutes"
    assert format_minutes(1440) == "One thousand, four hundred forty minutes"
