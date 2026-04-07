class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

def check(l1, l2):
    # Step 1: Store values of first list in a set
    values = set()
    curr = l1
    while curr:
        values.add(curr.val)
        curr = curr.next

    # Step 2: Check in second list
    curr = l2
    while curr:
        if curr.val in values:
            return 1
        curr = curr.next

    return 0


# Driver code (if required)
if __name__ == "__main__":
    n, m = map(int, input().split())
    
    list1 = list(map(int, input().split()))
    list2 = list(map(int, input().split()))

    # Create linked list 1
    head1 = Node(list1[0])
    curr = head1
    for val in list1[1:]:
        curr.next = Node(val)
        curr = curr.next

    # Create linked list 2
    head2 = Node(list2[0])
    curr = head2
    for val in list2[1:]:
        curr.next = Node(val)
        curr = curr.next

    print(check(head1, head2))
