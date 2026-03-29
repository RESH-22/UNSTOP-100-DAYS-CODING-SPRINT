n = int(input())
arr = list(map(int, input().split()))

non_zero = []
zero_count = 0

for x in arr:
    if x == 0:
        zero_count += 1
    else:
        non_zero.append(x)

result = non_zero + [0] * zero_count

print(*result)
