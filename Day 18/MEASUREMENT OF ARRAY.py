import sys
from collections import Counter

input = sys.stdin.readline
MOD = 10**9 + 7

n = int(input())
a = list(map(int, input().split()))

# Sum of original indices
orig_sum = n * (n - 1) // 2

# For sorted array, find last occurrence index of each value
# Sort and find last index per value
count = Counter(a)
sorted_vals = sorted(count.keys())

# Build last_index map
last_idx = {}
pos = 0
for v in sorted_vals:
    pos += count[v]
    last_idx[v] = pos - 1  # last occurrence index in sorted array

# Sum of last indices (each element contributes its last_idx)
last_sum = sum(last_idx[x] for x in a)

print((orig_sum + last_sum) % MOD)
