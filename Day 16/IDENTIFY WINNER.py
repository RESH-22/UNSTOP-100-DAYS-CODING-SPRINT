import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

count = Counter(arr)

for num in arr:
    if count[num] == 1:
        print(num)
        break
else:
    print(0)
