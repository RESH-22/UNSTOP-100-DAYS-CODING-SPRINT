import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    L, R = map(int, input().split())
    if L == R:
        print(0)
    elif L <= R // 2:
        b = R // 2 + 1
        print(R % b)
    else:
        print(R - L)
