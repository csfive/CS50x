# Searches CSV for popularity of a title

import csv

# Prompt user for title
title = input("Title: ").strip().upper()

# Open CSV file
with open("favorites.csv", "r") as file:

    # Create DictReader
    reader = csv.DictReader(file)

    # Iterate over CSV file, counting favorites
    counter = 0
    for row in reader:
        if row["title"].strip().upper() == title:
            counter += 1

# Print popularity
print(counter)
