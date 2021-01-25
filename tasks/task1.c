#include <stdio.h>

int main(void)
{
    for (int index = 0; index < 20; ++index)
    {
        if (index % 2 == 0)
        {
            printf("%i\n", index);
        }
    }

}