def countTriplets(n, arr):
    from collections import defaultdict
    
    # Step 1: Store pair AND counts
    pair_count = defaultdict(int)
    
    for i in range(n):
        for j in range(n):
            pair_count[arr[i] & arr[j]] += 1
    
    # Step 2: Check for third element
    result = 0
    
    for k in range(n):
        for val in pair_count:
            if (val & arr[k]) == 0:
                result += pair_count[val]
    
    return result


# 🔥 Input handling
n = int(input())
arr = list(map(int, input().split()))

print(countTriplets(n, arr))
