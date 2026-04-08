def find_possible_combinations(n, b, c, a):
    result = []
    
    def backtrack(path, b, c, a):
        # If length reached
        if len(path) == n:
            result.append(path)
            return
        
        # Try B
        if b > 0:
            backtrack(path + 'B', b - 1, c, a)
        
        # Try C
        if c > 0:
            backtrack(path + 'C', b, c - 1, a)
        
        # Try A
        if a > 0:
            backtrack(path + 'A', b, c, a - 1)
    
    backtrack("", b, c, a)
    return result


# -------- Main --------
n, b, c, a = map(int, input().split())

res = find_possible_combinations(n, b, c, a)

for comb in res:
    print(comb)
