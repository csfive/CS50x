#include <cs50.h>
#include <stdbool.h>
#include <stdio.h>

string get_card_brand(long card);
bool is_valid_luhn(long card);
int count_digits(long card);
int get_prefix(long card);

int main(void)
{
    long card = get_long("Number: ");
    printf("%s\n", get_card_brand(card));
    return 0;
}

string get_card_brand(long card)
{
    if (!is_valid_luhn(card))
    {
        return "INVALID";
    }

    int digits = count_digits(card);
    int prefix = get_prefix(card);

    if (digits == 15 && (prefix == 34 || prefix == 37))
    {
        return "AMEX";
    }
    if (digits == 16 && prefix >= 51 && prefix <= 55)
    {
        return "MASTERCARD";
    }
    if ((digits == 13 || digits == 16) && prefix / 10 == 4)
    {
        return "VISA";
    }
    return "INVALID";
}

bool is_valid_luhn(long card)
{
    if (card <= 0)
    {
        return false;
    }

    int sum = 0;
    bool should_double = false;
    while (card > 0)
    {
        int digit = card % 10;
        if (should_double)
        {
            digit *= 2;
            sum += digit / 10 + digit % 10;
        }
        else
        {
            sum += digit;
        }
        card /= 10;
        should_double = !should_double;
    }
    return sum % 10 == 0;
}

int count_digits(long card)
{
    int digits = 0;
    while (card > 0)
    {
        card /= 10;
        digits++;
    }
    return digits;
}

int get_prefix(long card)
{
    while (card >= 100)
    {
        card /= 10;
    }
    return card;
}
