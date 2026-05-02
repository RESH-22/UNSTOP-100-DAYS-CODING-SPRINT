import sys

def solve():
    data = sys.stdin.read().split()
    idx = 0
    n, q = int(data[idx]), int(data[idx+1]); idx += 2
    arr = list(map(int, data[idx:idx+n])); idx += n
    queries = list(map(int, data[idx:idx+q]))
    
    results = []
    for center in queries:
        c = center - 1  # 0-indexed
        
        r = 0
        while (c - r - 1 >= 0 and c + r + 1 < n and 
               arr[c - r - 1] == arr[c + r + 1]):
            r += 1
        
        # If no expansion possible AND no left neighbor exists → 0
        # Otherwise minimum is 1 (center itself)
        if r == 0 and c == 0:
            results.append(0)
        else:
            results.append(2 * r + 1)
    
    print(*results)

solve()
