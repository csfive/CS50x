# Prints popularity of titles in CSV, sorted by popularity, using a lambda function

import csv

# For accumulating (and later sorting) titles
titles = {}

# Open CSV file
with open("favorites.csv", "r") as file:

    # Create DictReader
    reader = csv.DictReader(file)

    # Iterate over CSV file
    for row in reader:

        # Canoncalize title
        title = row["title"].strip().upper()

        # Update counter
        if title in titles:
            titles[title] += 1
        else:
            titles[title] = 1

# Print titles in sorted order
for title in sorted(titles, key=lambda title: titles[title], reverse=True):
    print(title, titles[title])
