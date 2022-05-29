# Prints popularity of titles in CSV, sorted by title

import csv

# For accumulating (and later sorting) titles
titles = {}

# Open CSV file
with open("favorites.csv", "r") as file:

    # Create DictReader
    reader = csv.DictReader(file)

    # Iterate over CSV file, adding each (uppercased) title to dictionary
    for row in reader:

        # Canoncalize title
        title = row["title"].strip().upper()

        # Count title
        if title in titles:
            titles[title] += 1
        else:
            titles[title] = 1

# Print titles in sorted order
for title in sorted(titles):
    print(title, titles[title])
