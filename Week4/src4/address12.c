// Prints an array using pointer arithmetic

#include <stdio.h>

int main(void)
{
    // An array of numbers
    int numbers[] = {4, 6, 8, 2, 7, 5, 0};

    // Print numbers
    printf("%i\n", *numbers);
    printf("%i\n", *(numbers + 1));
    printf("%i\n", *(numbers + 2));
    printf("%i\n", *(numbers + 3));
    printf("%i\n", *(numbers + 4));
    printf("%i\n", *(numbers + 5));
    printf("%i\n", *(numbers + 6));
}
