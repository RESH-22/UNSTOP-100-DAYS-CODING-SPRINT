from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def create_tree(data):
    if not data or data[0] == 'N':
        return None

    root = TreeNode(int(data[0]))
    queue = deque([root])
    i = 1

    while queue and i < len(data):
        curr = queue.popleft()

        # Left child
        if i < len(data) and data[i] != 'N':
            curr.left = TreeNode(int(data[i]))
            queue.append(curr.left)
        i += 1

        # Right child
        if i < len(data) and data[i] != 'N':
            curr.right = TreeNode(int(data[i]))
            queue.append(curr.right)
        i += 1

    return root


def left_view(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        size = len(queue)

        for i in range(size):
            node = queue.popleft()

            # First node of this level
            if i == 0:
                result.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return result


# Driver code
if __name__ == "__main__":
    n = int(input().strip())
    data = input().split()

    root = create_tree(data)
    result = left_view(root)

    print(*result)
