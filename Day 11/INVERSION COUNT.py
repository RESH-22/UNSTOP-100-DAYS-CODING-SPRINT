def user_logic(n, arr):
    from collections import defaultdict
    
    groups = defaultdict(int)
    
    for x in arr:
        msb = x.bit_length()
        groups[msb] += 1
    
    result = 0
    
    for count in groups.values():
        result += count * (count - 1) // 2
    
    return result


n = int(input())
arr = list(map(int, input().split()))

print(user_logic(n, arr))
