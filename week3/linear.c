#include <stdio.h>
#include <cs50.h>
int linear(int arr[], int x, int size);
int binary_search(int arr[], int x, int left, int right);

int main(void)
{               // 0  1  2  3  4  5   6   7   8   9   10  11
    int array[] = {1, 4, 6, 7, 9, 12, 15, 22, 33, 43, 55, 77};
    int x = get_int("Enter a search number: ");
    int size = sizeof(array) / sizeof(int);
    //printf("Element found at index: %i", linear(array, x, size));

    printf("Element found at index: %i", binary_search(array, x, 0, size-1));
}

int binary_search(int arr[], int x, int left, int right) // from 0 to SIZE-1
{
    if(right >= left)
    {
        int middle = left + (right - left) / 2;

        if(arr[middle] == x)
        {
            return middle;
        }

        if(arr[middle] > x)
        {
            return binary_search(arr, x, left, middle-1);
        }
        else
        {
            return binary_search(arr, x, middle+1, right);
        }
    }



    return -1;
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