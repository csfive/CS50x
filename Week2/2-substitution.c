#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }

    if (strlen(argv[1]) != 26)
    {
        printf("Key must contain 26 characters.\n");
        return 1;
    }

    int exist[26] = {0};
    string key = argv[1];

    for (int i = 0; i < 26; i++)
    {
        exist[toupper(key[i]) - 'A']++;
    }
    
    for (int i = 0; i < 26; i++)
    {
        if (exist[i] != 1)
        {
            printf("Key must not contain repeated characters.\n");
            return 1;
        }
    }

    string text = get_string("plaintext:  ");
    for (int i = 0, n = strlen(text); i < n; i++)
    {
        if (isalpha(text[i]))
        {
            if (isupper(text[i]))
            {
                text[i] = toupper(key[text[i] - 'A']);
            }
            else
            {
                text[i] = tolower(key[text[i] - 'a']);
            }
        }
    }

    printf("ciphertext: %s\n", text);
    return 0;
}
