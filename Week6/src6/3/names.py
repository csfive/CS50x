# Implements linear search for names

import sys

# A list of names
names = ["Bill", "Charlie", "Fred", "George", "Ginny", "Percy", "Ron"]

# Search for Ron
if "Ron" in names:
    print("Found")
    sys.exit(0)

print("Not found")
sys.exit(1)
