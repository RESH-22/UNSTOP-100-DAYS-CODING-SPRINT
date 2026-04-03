from collections import deque
import sys

def solve():
    data = sys.stdin.read().split()
    idx = 0
    n = int(data[idx]); idx+=1
    m = int(data[idx]); idx+=1
    
    grid = []
    for i in range(n):
        row = [int(data[idx+j]) for j in range(m)]
        idx += m
        grid.append(row)
    
    visited = [[False]*m for _ in range(n)]
    results = []
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1 and not visited[i][j]:
                queue = deque()
                queue.append((i, j))
                visited[i][j] = True
                cells = [(i, j)]
                
                while queue:
                    r, c = queue.popleft()
                    for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                        nr, nc = r+dr, c+dc
                        if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc] and grid[nr][nc] == 1:
                            visited[nr][nc] = True
                            queue.append((nr, nc))
                            cells.append((nr, nc))
                
                # Sort cells by row-major order (top-to-bottom, left-to-right)
                cells.sort(key=lambda x: (x[0], x[1]))
                first = cells[0]   # upper-left in scan order
                last = cells[-1]   # bottom-right in scan order
                results.append((first[0], first[1], last[0], last[1]))
    
    results.sort(key=lambda x: (x[0], x[1]))
    
    for r in results:
        print(*r)

solve()
