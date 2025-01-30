class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def detectCycle(head):
    '''
    https://leetcode.com/problems/linked-list-cycle-ii/
    Input: head = [3,2,0,-4], pos = 1
    Output: tail connects to node index 1
    Explanation: There is a cycle in the linked list, where tail connects to the second node.
    '''
    if not head or not head.next:
        return None

    # Step 1: Detect if a cycle exists using slow and fast pointers
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast: # Cycle detected
            # Step 2: Find the start of the cycle
            slow = head # Reset slow to the head
            while slow != fast:
                slow = slow.next
                fast = fast.next
             # The node where slow and fast meet is the start of the cycle
            return slow
    return None


# Create a linked list with a cycle
node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node1  # Creates a cycle at node2

cycle_start = detectCycle(node1)

print(cycle_start.value if cycle_start else "No cycle")  # Output: 2