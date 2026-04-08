#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int n;
    cin >> n;
    
    vector<long long> a(n), b(n);
    for (int i = 0; i < n; i++) cin >> a[i];
    for (int i = 0; i < n; i++) cin >> b[i];
    
    int total = 1 << n;
    vector<long long> dp(total, LLONG_MAX);
    dp[0] = 0;
    
    for (int mask = 0; mask < total; mask++) {
        if (dp[mask] == LLONG_MAX) continue;
        
        // k = number of bits set = which index in 'a' we're assigning next
        int k = __builtin_popcount(mask);
        if (k == n) continue;
        
        // Try pairing a[k] with each unused b[j]
        for (int j = 0; j < n; j++) {
            if (mask & (1 << j)) continue; // b[j] already used
            
            int newMask = mask | (1 << j);
            long long cost = dp[mask] + (a[k] ^ b[j]);
            dp[newMask] = min(dp[newMask], cost);
        }
    }
    
    cout << dp[total - 1] << endl;
    return 0;
}
