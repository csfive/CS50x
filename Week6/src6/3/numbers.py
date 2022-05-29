# Implements linear search for numbers

import sys

# A list of numbers
numbers = [4, 6, 8, 2, 7, 5, 0]

# Search for 0
if 0 in numbers:
    print("Found")
    sys.exit(0)

print("Not found")
sys.exit(1)
