def min_parachutes(k, n):
    # 🔥 Edge cases
    if n == 0:
        return 0
    if k == 0:
        return 0
    
    dp = [0] * (k + 1)
    moves = 0
    
    while dp[k] < n:
        moves += 1
        
        for i in range(k, 0, -1):
            dp[i] = dp[i] + dp[i-1] + 1
    
    return moves


# Input
if __name__ == "__main__":
    n, k = map(int, input().split())
    print(min_parachutes(k, n))
