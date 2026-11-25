#include <cs50.h>
#include <stdio.h>

int get_cents(void);
int count_coins(int cents);

int main(void)
{
    int cents = get_cents();
    int coins = count_coins(cents);
    printf("%d\n", coins);
    return 0;
}

int get_cents(void)
{
    int n;
    do
    {
        n = get_int("Change owed: ");
    }
    while (n < 0);
    return n;
}

int count_coins(int cents)
{
    int count = 0;
    count += cents / 25;
    cents %= 25;
    count += cents / 10;
    cents %= 10;
    count += cents / 5;
    cents %= 5;
    count += cents;
    return count;
}
