class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swapPairs(head):
    dummy = ListNode(0)
    dummy.next = head
    
    prev = dummy
    
    while prev.next and prev.next.next:
        first = prev.next
        second = prev.next.next
        
        # Swapping
        first.next = second.next
        second.next = first
        prev.next = second
        
        # Move prev forward
        prev = first
    
    return dummy.next


# Helper functions for input/output
def build_list(arr):
    dummy = ListNode(0)
    temp = dummy
    for num in arr:
        temp.next = ListNode(num)
        temp = temp.next
    return dummy.next


def print_list(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    print(res)


if __name__ == "__main__":
    import ast
    arr = ast.literal_eval(input().strip())
    
    head = build_list(arr)
    new_head = swapPairs(head)
    
    print_list(new_head)
