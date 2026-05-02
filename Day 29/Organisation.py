import sys
from collections import defaultdict

def solve():
    input_data = sys.stdin.read().split()
    v = int(input_data[0])
    
    if v == 1:
        print(0)
        return
    
    children = defaultdict(list)
    root = None
    has_parent = [False] * (v + 1)
    
    for i in range(1, v):
        boss = int(input_data[i])  # boss of employee (i+1)
        child = i + 1
        children[boss].append(child)
        has_parent[child] = True
    
    # Root is the one with no parent
    for i in range(1, v + 1):
        if not has_parent[i]:
            root = i
            break
    
    # Iterative post-order DFS to count subtree sizes
    count = [0] * (v + 1)  # count[i] = number of employees UNDER i
    
    # Topological order using iterative DFS
    order = []
    stack = [root]
    while stack:
        node = stack.pop()
        order.append(node)
        for child in children[node]:
            stack.append(child)
    
    # Process in reverse order (leaves first)
    for node in reversed(order):
        for child in children[node]:
            count[node] += count[child] + 1  # child itself + all under child
    
    print(*count[1:v+1])

solve()
