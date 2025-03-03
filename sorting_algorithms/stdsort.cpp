#include<algorithm>
extern "C" {
    void sort(double arr[], int n) {
        std::sort(arr, arr+n);
    }
}