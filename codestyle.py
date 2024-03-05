# pylint: disable=missing-module-docstring
import string

LETTERS = string.ascii_letters + string.punctuation + string.digits
for letter in LETTERS:
    print(letter)

print("Hello!")
a, b, c = 5, 6, 3
if a < b:
    pass
else:
    if a > c:
        pass
    else:
        pass
