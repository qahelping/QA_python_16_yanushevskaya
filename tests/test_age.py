import pytest


# 19
# 18
# 0 Erorr
# -1 Erorr
# 17 Erorr
# 110
# 1,5 Erorr
# 56

# от 18 и до 100
def check_age(user):
    if 100 > user >= 18:
        return True
    else:
        return False


@pytest.mark.parametrize('age, result', [(19, True), (18, True), (56, True), (99, True),
                                         (-1, False), (1.3, False), (110, False), (101, False)])
def test_age(age, result):
    assert check_age(age) is result

