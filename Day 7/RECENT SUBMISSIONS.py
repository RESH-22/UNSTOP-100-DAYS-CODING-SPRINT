from collections import deque

n = int(input())
arr = list(map(int, input().split()))

q = deque()
max_size = 0

for t in arr:
    q.append(t)

    while q and q[0] <= t - 5000:
        q.popleft()

    max_size = max(max_size, len(q))

print(max_size)
