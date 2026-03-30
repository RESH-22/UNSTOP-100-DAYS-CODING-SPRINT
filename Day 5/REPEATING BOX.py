n2 = int(input())
arr = list(map(int, input().split()))

target = n2 // 2
freq = {}

for x in arr:
    freq[x] = freq.get(x, 0) + 1
    if freq[x] == target:
        print(x)
        break
