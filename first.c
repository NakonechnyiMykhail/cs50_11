#include <cs50.h>
#include <stdio.h>

int main()
{
    char c = '\n';
    string answer = get_string("What's your name?\n");
    printf("hello, %s%c", answer, c);


}