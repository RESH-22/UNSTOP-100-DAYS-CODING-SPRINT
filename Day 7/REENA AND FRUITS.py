n = int(input())
arr = list(map(int, input().split()))

arr.sort()

result = sum(arr[i] for i in range(0, n, 2))

print(result)
