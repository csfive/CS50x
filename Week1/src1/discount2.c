// Return value, multiple arguments

#include <cs50.h>
#include <stdio.h>

float discount(float price, int percentage);

int main(void)
{
    float regular_price = get_float("Regular Price: ");
    int percent_off = get_int("Percent Off: ");
    printf("Sale Price: %.2f\n", discount(regular_price, percent_off));
}

// Discount price
float discount(float price, int percentage)
{
    return price * (100 - percentage) / 100;
}
