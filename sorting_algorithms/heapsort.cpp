extern "C"
{
    void heapify(double arr[], int n, int i)
    {
        int largest = i;
        int l = 2 * i + 1;
        int r = 2 * i + 2;

        if (l < n && arr[l] > arr[largest])
        {
            largest = l;
        }

        if (r < n && arr[r] > arr[largest])
        {
            largest = r;
        }

        if (largest != i)
        {
            double temp = arr[i];
            arr[i] = arr[largest];
            arr[largest] = temp;

            heapify(arr, n, largest);
        }
    }

    void sort(double arr[], int n)
    {
        for (int i = n / 2 - 1; i >= 0; i--)
        {
            heapify(arr, n, i);
        }

        for (int i = n - 1; i > 0; i--)
        {
            double temp = arr[0];
            arr[0] = arr[i];
            arr[i] = temp;

            heapify(arr, i, 0);
        }
    }
}
