// Stores names using an array
#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
int main(int argc, string argv[])
{
    if(argc != 2)
    {
        printf("missing 1 args\n");
        return 1;
    }
    int index = atoi(argv[1]) - 1; // ASCII to Integer
    // Names
    string names[4];
    names[0] = "EMMA";
    names[1] = "RODRIGO";
    names[2] = "BRIAN";
    names[3] = "DAVID";

    // Print Emma's name
    printf("%s\n", names[index]);

    // homework
    //printf("%c%c%c%c\n", names[0][0], names[0][1], names[0][2], names[0][3]);

}
// ./array 2