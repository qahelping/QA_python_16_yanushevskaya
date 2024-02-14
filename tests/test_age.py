import pytest


def check_age(user):
    if 100 > user >= 18:
        return True
    else:
        return False


@pytest.mark.parametrize('age, result', [(19, True), (18, True), (56, True), (99, True),
                                         (-1, False), (1.3, False), (110, False), (101, False)])
def test_age(age, result):
    assert check_age(age) is result
