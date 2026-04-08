class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def insert_node(head, val):
    new_node = ListNode(val)
    if head[0] is None:
        head[0] = new_node
        return
    
    temp = head[0]
    while temp.next:
        temp = temp.next
    temp.next = new_node


def deleteDuplicates(head):
    dummy = ListNode(0)
    dummy.next = head
    
    prev = dummy
    curr = head
    
    while curr:
        # Check if duplicate exists
        if curr.next and curr.val == curr.next.val:
            # Skip all duplicates
            while curr.next and curr.val == curr.next.val:
                curr = curr.next
            prev.next = curr.next
        else:
            prev = prev.next
        
        curr = curr.next
    
    return dummy.next


def print_list(head):
    if not head:
        print("null")
        return
    
    res = []
    while head:
        res.append(str(head.val))
        head = head.next
    
    print(" ".join(res))


if __name__ == "__main__":
    n = int(input().strip())
    
    head = [None]
    
    for _ in range(n):
        val = int(input().strip())
        insert_node(head, val)
    
    new_head = deleteDuplicates(head[0])
    
    print_list(new_head)
