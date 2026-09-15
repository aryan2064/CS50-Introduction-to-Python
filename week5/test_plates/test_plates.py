from week5.test_plates.plates import is_valid


def test_plates_numbers_first():
    assert is_valid("12") == False
    assert is_valid("12abc") == False


def test_plates_over_length():
    assert is_valid("aaaaaaa") == False


def test_plates_under_length():
    assert is_valid("a") == False


def test_plates_numbers_before_letters():
    assert is_valid("aaa12a") == False


def test_plates_zero_first_number():
    assert is_valid("aaa01") == False


def test_plates_non_alphanumeric():
    assert is_valid("aaa12.") == False


def test_plates_valid():
    assert is_valid("aabb10") == True
    assert is_valid("aa") == True
