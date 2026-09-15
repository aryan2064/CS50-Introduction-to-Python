from um import count


def test_count_um_in_words():
    assert count("album") == 0


def test_count_um_words():
    assert count("um") == 1


def test_count_um_words_in_phrases():
    assert count("um, thanks for the, um... album.") == 2


def test_count_um_words_case_insensitive():
    assert count("Um UM uM") == 3
