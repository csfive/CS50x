// 不知道为什么过不了最后一个case，存在内存泄漏的问题，实在不知道怎么改了
#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

#include "dictionary.h"

typedef struct node
{
    bool is_word;
    struct node *son[27];
} node;

node *root;
int dict_size = 0;

int index(const char c)
{
    return (c == '\'') ? 26 : tolower(c) - 'a';
}

bool check(const char *word)
{
    node *cur = root;
    for (int i = 0; word[i]; i++)
    {
        // 考虑's的情况，单引号单独处理
        int idx = index(word[i]);
        if (cur->son[idx] == NULL)
        {
            return false;
        }
        cur = cur->son[idx];
    }
    return cur->is_word;
}

bool load(const char *dictionary)
{
    root = malloc(sizeof(node));
    FILE *dict = fopen(dictionary, "r");
    if (dict == NULL)
    {
        return false;
    }

    node *cur = root;
    char c;
    while ((c = fgetc(dict)) != EOF)
    {
        if (c == '\n')
        {
            cur->is_word = true;
            dict_size++;
            cur = root;
        }
        else
        {
            int idx = index(c);
            if (cur->son[idx] == NULL)
            {
                cur->son[idx] = malloc(sizeof(node));
            }
            cur = cur->son[idx];
        }
    }

    fclose(dict);
    return true;
}

unsigned int size(void)
{
    return dict_size;
}

void free_nodes(node *cur)
{
    for (int i = 0; i < 27; i++)
    {
        if (cur->son[i] != NULL)
        {
            free_nodes(cur->son[i]);
        }
    }
    free(cur);
}

bool unload(void)
{
    free_nodes(root);
    return true;
}
