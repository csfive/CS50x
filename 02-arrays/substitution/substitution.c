#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

bool is_valid(string s);

int main(int argc, string argv[])
{
    if (argc != 2 || !is_valid(argv[1]))
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }

    string key = argv[1];
    string text = get_string("plaintext:  ");

    printf("ciphertext: ");
    for (int i = 0, n = strlen(text); i < n; i++)
    {
        char c = text[i];
        if (isupper(c))
        {
            printf("%c", toupper(key[c - 'A']));
        }
        else if (islower(c))
        {
            printf("%c", tolower(key[c - 'a']));
        }
        else
        {
            printf("%c", c);
        }
    }
    printf("\n");

    return 0;
}

bool is_valid(string s)
{
    if (strlen(s) != 26)
    {
        return false;
    }

    bool seen[26] = {false};
    for (int i = 0; i < 26; i++)
    {
        if (!isalpha(s[i]))
        {
            return false;
        }

        int index = toupper(s[i]) - 'A';
        if (seen[index])
        {
            return false;
        }
        seen[index] = true;
    }

    return true;
}
