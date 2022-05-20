#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Get input
    long num;
    do
    {
        num = get_long("Number: ");
    } 
    while (num <= 0);

    int checksum = 0;
    long checknum = num / 10;

    // Calculate checksum
    while (checknum > 0)
    {
        int remainder = checknum % 10 * 2;
        if (remainder < 10)
        {
            checksum += remainder;
        }
        else
        {
            checksum += remainder % 10;
            remainder /= 10;
            checksum += remainder;
        }
        checknum /= 100;
    }

    checknum = num;
    while (checknum > 0)
    {
        checksum += checknum % 10;
        checknum /= 100;
    }
    
    // First check
    if (checksum % 10 != 0)
    {
        printf("INVALID\n");
    }
    else
    {
        // Get the card length and starting digits
        int length = 2;
        while (num >= 100)
        {
            num /= 10;
            length++;
        }

        // Check and print the result
        if ((num == 34 || num == 37) && length == 15)
        {
            printf("AMEX\n");
        }
        else if (num >= 51 && num <= 55 && length == 16)
        {
            printf("MASTERCARD\n");
        }
        else if (num >= 40 && num <= 49 && (length == 13 || length == 16))
        {
            printf("VISA\n");
        }
        else
        {
            printf("INVALID\n");
        }
    }
}
