// Counting

#include <stdbool.h>
#include <stdio.h>
#include <unistd.h>

int main(void)
{
    int i = 0;
    while (true)
    {
        printf("\r%i", i);
        i++;
    }
}
