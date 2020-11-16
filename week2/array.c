#include <stdio.h>

int main(void)
{
    int count = 8;
    int arr[] = {1, 3, 5, 3, 4, 2, 7, 9};

    for(int i = 0; i < count; ++i)
    {
        printf("%i ", arr[i]);
    }

    return 0;
}