n = int(input())
a = list(map(int, input().split()))

total = sum(a)
half = total / 2

running = 0
for i in range(n):
    running += a[i]
    if running >= half:
        print(i + 1)
        break
