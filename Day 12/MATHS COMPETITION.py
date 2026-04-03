def minimum_time_to_solve_problems(n, k, times):
    if k == 0:
        return 0

    times = [t for t in times if t > 0]
    if not times:
        return -1

    left = 1
    right = min(times) * k
    ans = -1

    while left <= right:
        mid = (left + right) // 2
        
        problems = 0
        for t in times:
            problems += mid // t
        
        if problems >= k:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1

    return ans


n, k = map(int, input().split())
times = list(map(int, input().split()))
print(minimum_time_to_solve_problems(n, k, times))
