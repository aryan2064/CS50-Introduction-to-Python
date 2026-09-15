from numb3rs import validate


def test_validate_valid_ip():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True


def test_validate_all_zeros_ip():
    assert validate("0.0.0.0") == True


def test_validate_leading_zeros_ip():
    assert validate("000.001.010.100") == False


def test_validate_only_first_byte():
    assert validate("255") == False


def test_validate_only_first_byte_in_range():
    assert validate("255.256.256.256") == False


def test_validate_five_bytes():
    assert validate("255.255.255.255.255") == False
