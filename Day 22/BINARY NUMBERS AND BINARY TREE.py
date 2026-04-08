class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def make_tree(idx, n, arr):
    if idx >= n:
        return None
    
    root = TreeNode(arr[idx])
    root.left = make_tree(2 * idx + 1, n, arr)
    root.right = make_tree(2 * idx + 2, n, arr)
    
    return root


def sum_root_to_leaf(root):
    def dfs(node, current):
        if not node:
            return 0
        
        # Convert binary path
        current = current * 2 + node.val
        
        # If leaf node
        if not node.left and not node.right:
            return current
        
        return dfs(node.left, current) + dfs(node.right, current)
    
    return dfs(root, 0)


# -------- Input Handling --------
n = int(input())
arr = list(map(int, input().split()))

root = make_tree(0, n, arr)

print(sum_root_to_leaf(root))
