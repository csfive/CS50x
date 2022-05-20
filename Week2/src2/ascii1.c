// Implicitly casts chars to ints

#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    string s = get_string("String: ");
    for (int i = 0; i < strlen(s); i++)
    {
        printf("%c %i\n", s[i], s[i]);
    }
}
