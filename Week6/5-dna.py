import csv  # Import the csv library to read and write CSV files
import sys  # Import the sys library to access command-line arguments


def main():
    # Check for command-line usage
    # Check if the number of command-line arguments is not equal to 3
    # If there are not enough arguments, exit the program
    if len(sys.argv) != 3:
        sys.exit()

    # Read database file into a variable
    # Open the file specified in the first command-line argument in read mode
    # Use csv.DictReader to read the file and create a list of dictionaries
    # Save the list of dictionaries in the data variable
    with open(sys.argv[1], "r") as file:
        reader = csv.DictReader(file)
        data = list(reader)
    # Read DNA sequence file into a variable
    # Open the file specified in the second command-line argument in read mode
    # Read the contents of the file and save it in the seq variable
    with open(sys.argv[2], "r") as file:
        seq = file.read()

    # Find longest match of each STR in DNA sequence
    # Create an empty list called STR
    # Loop over all the STRs in the database (except for the first column)
    # Call the longest_match function to find the longest match of the current STR in the DNA sequence
    # Append the length of the longest match to the STR list
    STR = []
    for i in range(1, len(reader.fieldnames)):
        STR.append(longest_match(seq, reader.fieldnames[i]))

    # Check database for matching profiles
    # Loop over all the people in the database
    # For each person, loop over all the STRs in the database (except for the first column)
    # If the length of the longest match of the current STR in the DNA sequence matches the value in the database, increment a counter
    # If the counter is equal to the number of STRs (except for the first column), print the name of the person and exit the program
    # If there are no matches, print "No match"
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


main()  # Call main function to execute code

