def calculate_sum(nums):
    s = set(nums)
    
    missing = 1
    while missing in s:
        missing += 1
    
    ascii_val = ord(str(missing)[0])
    
    return sum(nums) + ascii_val


n = int(input())
nums = list(map(int, input().split()))

print(calculate_sum(nums))
