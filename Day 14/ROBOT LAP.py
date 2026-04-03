def car_returns_to_origin(n, moves):
    x = 0
    y = 0

    for m in moves:
        if m == 'U':
            y += 1
        elif m == 'D':
            y -= 1
        elif m == 'R':
            x += 1
        elif m == 'L':
            x -= 1

    if x == 0 and y == 0:
        return "YES"
    else:
        return "NO"


n = int(input())
moves = input().strip()

print(car_returns_to_origin(n, moves))
