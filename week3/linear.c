#include <stdio.h>


int linear(int arr[], int x, int size);

int main(void)
{               // 0  1  2  3  4  5   6   7   8   9   10  11
    int array[] = {1, 4, 6, 7, 9, 12, 15, 22, 33, 43, 55, 77};
    int x = 43;
    int size = sizeof(array) / sizeof(int);
    printf("Element found at index: %i", linear(array, x, size));
}

int linear(int arr[], int x, int size)
{

    for(int index = 0; index < size; index++)
    {
        if(arr[index] == x)
        {
            return index;
        }
    }
    return -1;
}