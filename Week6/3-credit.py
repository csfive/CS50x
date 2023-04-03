
# Define a function to check if a credit card number is valid using Luhn's algorithm
def luhn_check(number):
    # Initialize a variable to store the sum of digits
    sum = 0
    # Convert the number to a string and reverse it
    number = str(number)[::-1]
    # Loop through every digit in the reversed number
    for i in range(len(number)):
        # Convert the digit to an integer
        digit = int(number[i])
        # If the digit is in an odd position (starting from 0), multiply it by 2
        if i % 2 == 1:
            digit *= 2
        # If the digit is greater than 9, subtract 9 from it
        if digit > 9:
            digit -= 9
        # Add the digit to the sum
        sum += digit
    # The number is valid if the sum is divisible by 10
    return sum % 10 == 0

# Define a function to determine the type of credit card based on its length and first digits
def card_type(number):
    # Convert the number to a string
    number = str(number)
    # Get the first two digits of the number
    first_two = number[:2]
    # Get the length of the number
    length = len(number)
    # If the length is 15 and the first two digits are 34 or 37, it is an American Express card
    if length == 15 and first_two in ["34", "37"]:
        return "AMEX"
    # If the length is 13 or 16 and the first digit is 4, it is a Visa card
    elif length in [13, 16] and number[0] == "4":
        return "VISA"
    # If the length is 16 and the first two digits are between 51 and 55, it is a MasterCard card
    elif length == 16 and 51 <= int(first_two) <= 55:
        return "MASTERCARD"
    # Otherwise, it is an invalid card
    else:
        return "INVALID"

# Define a function to prompt the user for a credit card number and report its type or validity
def main():
    # Prompt the user for a credit card number and remove any spaces or hyphens
    credit_card = input("Number: ").replace(" ", "").replace("-", "")
    # Check if the input is entirely numeric
    if credit_card.isdigit():
        # Check if the input is valid using Luhn's algorithm
        if luhn_check(credit_card):
            # Print the type of credit card using card_type function
            print(card_type(credit_card))
        else:
            # Print INVALID if the input is not valid
            print("INVALID")
    else:
        # Print INVALID if the input is not numeric
        print("INVALID")

# Call the main function if this file is executed as a script
if __name__ == "__main__":
    main()
