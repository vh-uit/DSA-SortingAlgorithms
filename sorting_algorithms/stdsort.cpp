#include<algorithm>
extern "C" {
    void sort(int arr[], int n) {
        std::sort(arr, arr+n);
    }
}