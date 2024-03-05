import pytest

from main import sum


def test_sum():
    print("hello")
    assert sum([1, 2, 3]) == 6, "Should be 6"


def test_sum_tuple():
    assert sum((1, 2, 2, 1)) == 6, "Should be 6"


def test_sum_7():
    assert sum([1, 2, 3, 1, 2, 3, 1]) == 13, "Should be 13"


def test_sum_error():
    with pytest.raises(AssertionError):
        assert sum((1, 2, 2)) == 13, "Should be 6"
