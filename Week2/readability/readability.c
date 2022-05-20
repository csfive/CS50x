#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int count_letters(string text);
int count_words(string text);
int count_sentences(string text);

int main(void)
{
    // Get input
    string text = get_string("Text: ");

    // Get counts and compute the index
    double l = count_letters(text) * 100.0 / count_words(text);
    double s = count_sentences(text) * 100.0 / count_words(text);
    int grade = (int)round(0.0588 * l - 0.296 * s - 15.8);

    // Print
    if (grade < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (grade > 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", grade);
    }
}

int count_letters(string text)
{
    int cnt = 0;
    for (int i = 0, n = strlen(text); i < n; i++)
    {
        if (isalnum(text[i]))
        {
            cnt++;
        }
    }
    return cnt;
}

int count_words(string text)
{
    int cnt = 0;
    for (int i = 0, n = strlen(text); i < n; i++)
    {
        if (isspace(text[i]))
        {
            cnt++;
        }
    }
    // last has no space
    return cnt + 1;
}

int count_sentences(string text)
{
    int cnt = 0;
    for (int i = 0, n = strlen(text); i < n; i++)
    {
        if (text[i] == '.' || text[i] == '!' || text[i] == '?')
        {
            cnt++;
        }
    }
    return cnt;
}
