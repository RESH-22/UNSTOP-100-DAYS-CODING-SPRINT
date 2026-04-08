class Node:
    def __init__(self, x):
        self.val = x
        self.next = None


def reverse_list(head):
    prev = None
    while head:
        nxt = head.next
        head.next = prev
        prev = head
        head = nxt
    return prev


def maxPairSum(head):
    # Step 1: find middle + keep previous
    slow = head
    fast = head
    prev = None

    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next

    # 🔥 IMPORTANT: split the list
    prev.next = None

    # Step 2: reverse second half
    second = reverse_list(slow)
    first = head

    # Step 3: compute max pair sum
    max_sum = float('-inf')

    while second:
        max_sum = max(max_sum, first.val + second.val)
        first = first.next
        second = second.next

    return max_sum


# ---------- DRIVER CODE ----------
def build_linked_list(arr):
    head = Node(arr[0])
    temp = head
    for x in arr[1:]:
        temp.next = Node(x)
        temp = temp.next
    return head


# Input
N = int(input())
arr = list(map(int, input().split()))

head = build_linked_list(arr)
print(maxPairSum(head))
