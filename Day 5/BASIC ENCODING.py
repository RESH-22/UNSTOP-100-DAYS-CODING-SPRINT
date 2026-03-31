q = int(input())

freq = {}

for _ in range(q):
    A, B = map(int, input().split())
    freq[B] = freq.get(B, 0) + A   # add occurrences

if len(freq) <= 1:
    print(0)
else:
    max_freq = max(freq.values())
    min_freq = min(freq.values())

    max_nums = [num for num, f in freq.items() if f == max_freq]
    min_nums = [num for num, f in freq.items() if f == min_freq]

    highest = max(max_nums)
    lowest = min(min_nums)

    print(abs(highest - lowest))
