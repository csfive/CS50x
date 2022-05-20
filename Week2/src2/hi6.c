// Array of strings

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    string words[2];

    words[0] = "HI!";
    words[1] = "BYE!";

    for (int i = 0; i < 2; i++)
    {
        printf("%s\n", words[i]);
    }
}
