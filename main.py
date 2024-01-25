def sum(arg):
    total = 0
    for val in arg:
        total += val
    return total


def check_age(user):
    if user > 18:
        return True
    else:
        return False
