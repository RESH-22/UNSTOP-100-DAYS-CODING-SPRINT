class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def build_balanced(arr, l, r):
    if l > r:
        return None

    mid = (l + r + 1) // 2   # choose upper middle
    root = Node(arr[mid])

    root.left = build_balanced(arr, l, mid - 1)
    root.right = build_balanced(arr, mid + 1, r)

    return root


def preorder_print(node):
    if not node:
        return

    left_val = str(node.left.val) if node.left else "."
    right_val = str(node.right.val) if node.right else "."

    print(f"{left_val} <- {node.val} -> {right_val}")

    preorder_print(node.left)
    preorder_print(node.right)


def userLogic(N, arr):
    arr.sort()
    root = build_balanced(arr, 0, N - 1)
    preorder_print(root)


N = int(input())
arr = list(map(int, input().split()))

userLogic(N, arr)
