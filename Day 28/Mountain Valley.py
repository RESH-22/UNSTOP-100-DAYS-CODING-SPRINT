class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def countPeakNodes(head):
    count = 0
    prev = None
    curr = head
    
    while curr and curr.next:
        if prev and curr.data > prev.data and curr.data > curr.next.data:
            count += 1
        prev = curr
        curr = curr.next
    
    return count

# Input handling - N on first line, elements on second line
n = int(input().strip())
values = list(map(int, input().split()))

# Build linked list
head = None
tail = None
for val in values:
    node = Node(val)
    if not head:
        head = tail = node
    else:
        tail.next = node
        tail = node

print(countPeakNodes(head))
