#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    string num = get_string("Number: ");
    int len = strlen(num);

    if (len != 13 && len != 15 && len != 16)
    {
        printf("INVALID\n");
        return 0;
    }

    bool flag = (len % 2 == 0) ? true : false;
    int checksum = 0;
    for (int i = 0; i < len; i++)
    {
        int tmp = num[i] - '0';
        if (flag)
        {
            tmp *= 2;
            if (tmp >= 10)
            {
                checksum += tmp - 9;
            }
            else
            {
                checksum += tmp;
            }
        }
        else
        {
            checksum += tmp;
        }
        flag = !flag;
    }

    if (checksum % 10 != 0)
    {
        printf("INVALID\n");
    }
    else
    {
        int check = (num[0] - '0') * 10 + (num[1] - '0');
        if (check == 34 || check == 37)
        {
            printf("AMEX\n");
        }
        else if (check >= 51 && check <= 55)
        {
            printf("MASTERCARD\n");
        }
        else if (check / 10 == 4)
        {
            printf("VISA\n");
        }
        else
        {
            printf("INVALID\n");
        }
    }
}
