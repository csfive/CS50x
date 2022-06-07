#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

typedef uint8_t BYTE;
const int BLOCK_SIZE = 512;

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./recover IMAGE\n");
        return 1;
    }

    FILE *input = fopen(argv[1], "r");
    if (input == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    BYTE buffer[BLOCK_SIZE];
    int cnt = 0;
    FILE *output = NULL;
    char filename[8];

    // Repeat to read 512 bytes to a buffer
    while (fread(&buffer, BLOCK_SIZE, 1, input))
    {
        // Check start of new JPEG
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            // Check first
            if (cnt)
            {
                fclose(output);
            }

            // Generate JPEG file
            sprintf(filename, "%03i.jpg", cnt);
            output = fopen(filename, "w");
            cnt++;
        }

        // Already found JPEG
        if (cnt)
        {
            fwrite(&buffer, BLOCK_SIZE, 1, output);
        }
    }

    fclose(input);
    fclose(output);
    return 0;
}
