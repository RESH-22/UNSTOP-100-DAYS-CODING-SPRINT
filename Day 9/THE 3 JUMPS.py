def min_cost(v):
    n = len(v)
    
    if n == 1:
        return 0

    dp = [float('inf')] * n
    dp[0] = 0

    for i in range(1, n):
        if i - 1 >= 0:
            dp[i] = min(dp[i], dp[i-1] + abs(v[i] - v[i-1]))
        if i - 2 >= 0:
            dp[i] = min(dp[i], dp[i-2] + abs(v[i] - v[i-2]))
        if i - 3 >= 0:
            dp[i] = min(dp[i], dp[i-3] + abs(v[i] - v[i-3]))

    return dp[n-1]


# Input
n = int(input())
v = list(map(int, input().split()))

print(min_cost(v))
