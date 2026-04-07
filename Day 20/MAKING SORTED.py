class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def user_logic(bst1_nodes, bst2_nodes):
    # Merge both BST node values
    merged = bst1_nodes + bst2_nodes
    
    # Sort the merged list
    merged.sort()
    
    return merged


# Driver code (DO NOT MODIFY if platform already handles input)
if __name__ == "__main__":
    N = int(input().strip())
    bst1_nodes = list(map(int, input().split()))
    
    M = int(input().strip())
    bst2_nodes = list(map(int, input().split()))
    
    result = user_logic(bst1_nodes, bst2_nodes)
    
    print(*result)
