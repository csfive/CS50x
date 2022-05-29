# Uppercases string one character at a time

from cs50 import get_string

before = get_string("Before: ")
print("After:  ", end="")
for c in before:
    print(c.upper(), end="")
print()
