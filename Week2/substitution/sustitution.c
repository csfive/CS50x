#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int main(int argc, string argv[])
{
    // Get key
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
        exist[toupper(key[i]) - 65]++;
    }
    for (int i = 0; i < 26; i++)
    {
        if (exist[i] != 1)
        {
            printf("Key must contain 26 characters.\n");
            return 1;
        }
    }

    // Get input text and encrypt
    string text = get_string("plaintext:  ");
    for (int i = 0, n = strlen(text); i < n; i++)
    {
        // skip the punctuation
        if (isalpha(text[i]))
        {
            if (isupper(text[i]))
            {
                text[i] = toupper(key[text[i] - 65]);
            }
            else
            {
                text[i] = tolower(key[text[i] - 97]);
            }
        }
    }

    // Print the result
    printf("ciphertext: %s\n", text);
    return 0;
}
