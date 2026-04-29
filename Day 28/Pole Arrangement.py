def solve():
    line1 = list(map(int, input().split()))
    n, x = line1[0], line1[1]
    arr = list(map(int, input().split()))
    
    # Alice reduces all tallest poles by X
    max_h = max(arr)
    arr = [max(0, h - x) if h == max_h else h for h in arr]
    
    # Find if any triplet i < j < k exists where arr[i] < arr[k] < arr[j]
    # (middle pole tallest, first shortest, last in between)
    
    # For each j (middle pole candidate), we need:
    # - some i < j with arr[i] < arr[j]
    # - some k > j with arr[i] < arr[k] < arr[j]
    
    # Precompute: min_left[j] = minimum value in arr[0..j-1]
    min_left = [float('inf')] * n
    for j in range(1, n):
        min_left[j] = min(min_left[j-1], arr[j-1])
    
    # For each j as middle pole, check if there exists k > j where
    # min_left[j] < arr[k] < arr[j]
    for j in range(1, n - 1):
        left_min = min_left[j]
        mid = arr[j]
        
        if left_min >= mid:
            continue  # middle must be tallest
        
        # Need some k > j with left_min < arr[k] < mid
        for k in range(j + 1, n):
            if left_min < arr[k] < mid:
                print(1)
                return
    
    print(0)

solve()
