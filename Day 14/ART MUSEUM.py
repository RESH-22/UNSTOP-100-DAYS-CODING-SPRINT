def user_logic(n, positions):
    xs = sorted([p[0] for p in positions])
    ys = sorted([p[1] for p in positions])

    if n % 2 == 1:
        return 1
    else:
        x_count = xs[n//2] - xs[n//2 - 1] + 1
        y_count = ys[n//2] - ys[n//2 - 1] + 1
        return x_count * y_count


n = int(input())
positions = [tuple(map(int, input().split())) for _ in range(n)]

print(user_logic(n, positions))
