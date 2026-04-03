def user_logic(n, arr):
    min_val = arr[0]
    max_diff = -1
    
    for j in range(1, n):
        diff = arr[j] - min_val
        
        if diff > max_diff:
            max_diff = diff
        
        if arr[j] < min_val:
            min_val = arr[j]
    
    if max_diff <= 0:
        return -1
    return max_diff


t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(user_logic(n, arr))
