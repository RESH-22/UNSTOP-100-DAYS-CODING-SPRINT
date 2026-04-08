#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, k;
    cin >> n >> k;

    vector<long long> arr(n);

    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    // Step 1: Sort array
    sort(arr.begin(), arr.end());

    // Step 2: Flip negatives
    for (int i = 0; i < n && k > 0; i++) {
        if (arr[i] < 0) {
            arr[i] = -arr[i];
            k--;
        }
    }

    // Step 3: Sort again to get smallest element
    sort(arr.begin(), arr.end());

    // Step 4: If k is odd → flip smallest
    if (k % 2 == 1) {
        arr[0] = -arr[0];
    }

    // Step 5: Calculate sum
    long long sum = 0;
    for (auto x : arr) {
        sum += x;
    }

    cout << sum;

    return 0;
}
