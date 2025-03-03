extern "C"
{
    void _quicksort(double arr[], int low, int high)
    {
        if (low < high)
        {
            double pivot = arr[(low + high) >> 1];
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
                double temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
            _quicksort(arr, low, j);
            _quicksort(arr, i, high);
        }
    }

    void sort(double *base, int size)
    {
        _quicksort(base, 0, size - 1);
    }
}
