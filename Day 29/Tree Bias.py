import sys
from collections import deque

def solve():
    data = sys.stdin.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    
    if n == 1:
        print(0)
        return
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a, b = int(data[idx]), int(data[idx+1]); idx += 2
        adj[a].append(b)
        adj[b].append(a)
    
    # BFS from node 1
    visited = [False] * (n + 1)
    queue = deque([(1, 0)])  # (node, depth)
    visited[1] = True
    total = 0
    
    while queue:
        node, depth = queue.popleft()
        total += depth
        for neighbor in adj[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append((neighbor, depth + 1))
    
    print(total)

solve()
