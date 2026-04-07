n = int(input())
heights = list(map(int, input().split()))

expected = sorted(heights)

count = sum(1 for i in range(n) if heights[i] != expected[i])
print(count)
