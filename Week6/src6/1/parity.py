# Calculates a remainder

from cs50 import get_int

# Prompt user for integer
n = get_int("n: ")

# Check parity of integer
if n % 2 == 0:
    print("even")
else:
    print("odd")
