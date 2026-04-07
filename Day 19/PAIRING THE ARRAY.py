import math
from collections import defaultdict

def count_pairs_divisible_by_k(k, n, arr):
    freq = defaultdict(int)
    
    # Step 1: Count gcd frequencies
    for num in arr:
        g = math.gcd(num, k)
        freq[g] += 1
    
    # Step 2: Count valid pairs
    count = 0
    gcd_values = list(freq.keys())
    
    for i in range(len(gcd_values)):
        for j in range(i, len(gcd_values)):
            g1 = gcd_values[i]
            g2 = gcd_values[j]
            
            if (g1 * g2) % k == 0:
                if i == j:
                    # same group → nC2
                    count += freq[g1] * (freq[g1] - 1) // 2
                else:
                    count += freq[g1] * freq[g2]
    
    return count


# ---- Input ----
k = int(input())
n = int(input())
arr = list(map(int, input().split()))

print(count_pairs_divisible_by_k(k, n, arr))
