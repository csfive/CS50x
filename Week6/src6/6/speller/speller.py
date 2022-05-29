import re
import sys
import time

from dictionary import check, load, size, unload

# Maximum length for a word
# (e.g., pneumonoultramicroscopicsilicovolcanoconiosis)
LENGTH = 45

# Default dictionary
WORDS = "dictionaries/large"

# Check for correct number of args
if len(sys.argv) != 2 and len(sys.argv) != 3:
    print("Usage: speller [dictionary] text")
    sys.exit(1)

# Benchmarks
time_load, time_check, time_size, time_unload = 0.0, 0.0, 0.0, 0.0

# Determine dictionary to use
dictionary = sys.argv[1] if len(sys.argv) == 3 else WORDS

# Load dictionary
before = time.process_time()
loaded = load(dictionary)
after = time.process_time()

# Exit if dictionary not loaded
if not loaded:
    print(f"Could not load {dictionary}.")
    sys.exit(1)

# Calculate time to load dictionary
time_load = after - before

# Try to open text
text = sys.argv[2] if len(sys.argv) == 3 else sys.argv[1]
file = open(text, "r", encoding="latin_1")
if not file:
    print("Could not open {}.".format(text))
    unload()
    sys.exit(1)

# Prepare to report misspellings
print("\nMISSPELLED WORDS\n")

# Prepare to spell-check
word = ""
index, misspellings, words = 0, 0, 0

# Spell-check each word in file
while True:
    c = file.read(1)
    if not c:
        break

    # Allow alphabetical characters and apostrophes (for possessives)
    if re.match(r"[A-Za-z]", c) or (c == "'" and index > 0):

        # Append character to word
        word += c
        index += 1

        # Ignore alphabetical strings too long to be words
        if index > LENGTH:

            # Consume remainder of alphabetical string
            while True:
                c = file.read(1)
                if not c or not re.match(r"[A-Za-z]", c):
                    break

            # Prepare for new word
            index, word = 0, ""

    # Ignore words with numbers (like MS Word can)
    elif c.isdigit():

        # Consume remainder of alphanumeric string
        while True:
            c = file.read(1)
            if not c or (not c.isalpha() and not c.isdigit()):
                break

        # Prepare for new word
        index, word = 0, ""

    # We must have found a whole word
    elif index > 0:

        # Update counter
        words += 1

        # Check word's spelling
        before = time.process_time()
        misspelled = not check(word)
        after = time.process_time()

        # Update benchmark
        time_check += after - before

        # Print word if misspelled
        if misspelled:
            print(word)
            misspellings += 1

        # Prepare for next word
        index, word = 0, ""

# Close file
file.close()

# Determine dictionary's size
before = time.process_time()
n = size()
after = time.process_time()

# Calculate time to determine dictionary's size
time_size = after - before

# Unload dictionary
before = time.process_time()
unloaded = unload()
after = time.process_time()

# Abort if dictionary not unloaded
if not unloaded:
    print(f"Could not load {dictionary}.")
    sys.exit(1)

# Calculate time to determine dictionary's size
time_unload = after - before

# Report benchmarks
print(f"\nWORDS MISSPELLED:     {misspellings}")
print(f"WORDS IN DICTIONARY:  {n}")
print(f"WORDS IN TEXT:        {words}")
print(f"TIME IN load:         {time_load:.2f}")
print(f"TIME IN check:        {time_check:.2f}")
print(f"TIME IN size:         {time_size:.2f}")
print(f"TIME IN unload:       {time_unload:.2f}")
print(f"TOTAL TIME:           {time_load + time_check + time_size + time_unload:.2f}\n")

# Success
sys.exit(0)
