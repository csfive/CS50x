import csv
import sys


def main():
    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        sys.exit()

    # TODO: Read database file into a variable
    with open(sys.argv[1], "r") as file:
        reader = csv.DictReader(file)
        data = list(reader)

    # TODO: Read DNA sequence file into a variable
    with open(sys.argv[2], "r") as file:
        seq = file.read()

    # TODO: Find longest match of each STR in DNA sequence
    STR = []
    for i in range(1, len(reader.fieldnames)):
        STR.append(longest_match(seq, reader.fieldnames[i]))

    # TODO: Check database for matching profiles
    for i in range(len(data)):
        matches = 0
        for j in range(1, len(reader.fieldnames)):
            if int(data[i][reader.fieldnames[j]]) == STR[j - 1]:
                matches += 1
            if matches == len(reader.fieldnames) - 1:
                print(data[i]['name'])
                return
    print("No match")


def longest_match(sequence, subsequence):
    """Returns length of the longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in sequence, return longest run found
    return longest_run


main()
