# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def hasCycle(head):
    """
    :type head: ListNode
    :rtype: bool
    """
    # using 2 pointer approach, slow and fast 
    slow , fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        # if slow anf fast equal then cycle exists
        if fast == slow:
            return True
    return False


# Example   
head = [3,2,0,-4]
node1 = ListNode(head[0])
node2 = ListNode(head[1])
node3 = ListNode(head[2])
node4 = ListNode(head[3])

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2


print(hasCycle(node1))