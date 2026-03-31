n = int(input())
arr = list(map(int, input().split()))

total = sum(arr)

arr.sort(reverse=True)

sub_sum = 0
result = []

for x in arr:
    sub_sum += x
    result.append(x)
    
    if sub_sum > total - sub_sum:
        break

print(*result)
