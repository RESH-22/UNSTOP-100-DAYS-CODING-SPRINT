class TreeNode:
    def __init__(self, x):
        self.val = int(x)
        self.left = None
        self.right = None


def insertLevelOrder(arr, i):
    if i >= len(arr) or arr[i] == "null":
        return None
    
    root = TreeNode(arr[i])
    root.left = insertLevelOrder(arr, 2*i + 1)
    root.right = insertLevelOrder(arr, 2*i + 2)
    
    return root


def rob(root):
    
    def dfs(node):
        if not node:
            return (0, 0)  # (rob_this, skip_this)
        
        left = dfs(node.left)
        right = dfs(node.right)
        
        # If we rob this node
        rob_this = node.val + left[1] + right[1]
        
        # If we skip this node
        skip_this = max(left) + max(right)
        
        return (rob_this, skip_this)
    
    result = dfs(root)
    return max(result)


# ---- Input Handling ----
arr = input().split()
root = insertLevelOrder(arr, 0)

print(rob(root))
