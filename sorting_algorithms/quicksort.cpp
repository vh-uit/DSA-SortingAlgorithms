#include <iostream>
#include <stdlib.h>

extern "C"
{
    

    void _quicksort(int arr[], int low, int high)
    {
        if (low < high)
        {
            int pivot = arr[(low + high) >> 1];
            int i = low-1, j = high+1;
            while (true)
            {
                do
                {
                    i++;
                } while (arr[i] < pivot);

                do
                {
                    j--;
                } while (arr[j] > pivot);
                if (i > j)
                    break;
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
            _quicksort(arr, low, j);
            _quicksort(arr, i, high);
        }
    }

    void sort(int *base, int size)
    {
        _quicksort(base, 0, size - 1);
    }
}