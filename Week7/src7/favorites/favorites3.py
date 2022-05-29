# Prints unique titles in CSV, case insensitively

import csv

# For accumulating (and later sorting) titles
titles = set()

# Open CSV file
with open("favorites.csv", "r") as file:

    # Create DictReader
    reader = csv.DictReader(file)

    # Iterate over CSV file, adding each (uppercased) title to set
    for row in reader:
        titles.add(row["title"].strip().upper())

# Print titles in sorted order
for title in sorted(titles):
    print(title)
