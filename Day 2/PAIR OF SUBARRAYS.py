def calculate_pairs(n, arr):
    from collections import defaultdict
    
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + arr[i]
    
    count = 0
    left_sums = defaultdict(int)
    
    # Iterate over possible second subarray start
    for start in range(1, n):
        
        # Add all subarrays ending at start-1 into map
        for L in range(start):
            s = prefix[start] - prefix[L]
            left_sums[s] += 1
        
        # Now count matching subarrays starting at 'start'
        for R in range(start, n):
            s = prefix[R + 1] - prefix[start]
            count += left_sums[s]
    
    return count


def main():
    import sys
    data = sys.stdin.read().strip().split()
    n = int(data[0])
    arr = list(map(int, data[1:n+1]))
    print(calculate_pairs(n, arr))


if __name__ == "__main__":
    main()
