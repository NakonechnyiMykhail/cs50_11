#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(int argc, string argv[])
{
    if (argc != 4)
    {
        printf("missing command-line args\n");
        return 1;
    }

    for (int i = 0; i < argc; i++)
    {
        // for (int j = 0, n = strlen(argv[i]); j < n; j++)
        // {
        //     printf("%c\n", argv[i][j]);
        // }
        printf("%s\n", argv[i]);
    }
    return 0;
}