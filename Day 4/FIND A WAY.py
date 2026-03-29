import sys
from collections import deque

def bfs(start, graph, n):
    visited = [-1] * (n + 1)
    q = deque([start])
    visited[start] = 0
    farthest = start

    while q:
        node = q.popleft()
        for nei in graph[node]:
            if visited[nei] == -1:
                visited[nei] = visited[node] + 1
                q.append(nei)
                if visited[nei] > visited[farthest]:
                    farthest = nei

    return farthest, visited[farthest]


def main():
    input = sys.stdin.readline
    n = int(input().strip())

    graph = [[] for _ in range(n + 1)]

    for i in range(1, n + 1):
        l, r = map(int, input().split())

        if l != -1:
            graph[i].append(l)
            graph[l].append(i)

        if r != -1:
            graph[i].append(r)
            graph[r].append(i)

    # First BFS
    far_node, _ = bfs(1, graph, n)

    # Second BFS
    _, diameter = bfs(far_node, graph, n)

    print(diameter)


if __name__ == "__main__":
    main()
