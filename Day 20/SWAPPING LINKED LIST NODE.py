class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swapNodes(head, k):
    # Step 1: Find kth node from beginning
    first = head
    for _ in range(k - 1):
        first = first.next

    # Step 2: Find kth node from end
    second = head
    temp = first
    while temp.next:
        temp = temp.next
        second = second.next

    # Step 3: Swap values
    first.val, second.val = second.val, first.val

    return head


# Driver code (if needed)
if __name__ == "__main__":
    N = int(input().strip())
    values = list(map(int, input().split()))
    k = int(input().strip())

    # Create linked list
    head = ListNode(values[0])
    curr = head
    for v in values[1:]:
        curr.next = ListNode(v)
        curr = curr.next

    # Swap nodes
    head = swapNodes(head, k)

    # Print result
    curr = head
    while curr:
        print(curr.val, end=" ")
        curr = curr.next
