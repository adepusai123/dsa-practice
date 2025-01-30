class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def detectCycle(head):
    if not head or not head.next:
        return None

    # Step 1: Detect if a cycle exists using slow and fast pointers
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return None

    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    # Step 3: Remove the cycle
    # Find the last node in the cycle
    cycle_start = slow
    ptr = cycle_start
    while ptr.next != cycle_start:
        ptr = ptr.next

    # Break the cycle
    ptr.next = None

    return cycle_start 

