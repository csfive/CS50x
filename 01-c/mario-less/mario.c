#include <cs50.h>
#include <stdio.h>

int get_height(void);
void print_pyramid(int height);
void print_chars(char c, int count);

int main(void)
{
    int n = get_height();
    print_pyramid(n);
    return 0;
}

int get_height(void)
{
    int n;
    do
    {
        n = get_int("Height: ");
    }
    while (n <= 0);
    return n;
}

void print_pyramid(int height)
{
    for (int i = 1; i <= height; i++)
    {
        print_chars(' ', height - i);
        print_chars('#', i);
        printf("\n");
    }
}

void print_chars(char c, int count)
{
    for (int i = 0; i < count; i++)
    {
        printf("%c", c);
    }
}
