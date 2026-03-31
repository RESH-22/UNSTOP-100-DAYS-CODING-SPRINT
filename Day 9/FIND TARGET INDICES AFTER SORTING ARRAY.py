n = int(input())
arr = list(map(int, input().split()))
k = int(input())

arr.sort()

indices = []

for i in range(n):
    if arr[i] == k:
        indices.append(i)

print(len(indices))

if indices:
    print(*indices)
