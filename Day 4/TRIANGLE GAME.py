n = int(input())

row = [1]

for k in range(1, n + 1):
    row.append(row[-1] * (n - k + 1) // k)

print(*row)
