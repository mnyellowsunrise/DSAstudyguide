# Problem: Given a linked list, determine if it has a cycle in it.
# Fast and Slow Pointers:
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def has_cycle(head):
    slow = fast = head  # Initialize two pointers at the head of the linked list.
    
    # Move the fast pointer twice as fast as the slow pointer.
    while fast and fast.next:
        slow = slow.next  # Move the slow pointer one step.
        fast = fast.next.next  # Move the fast pointer two steps.
        
        # If the fast pointer meets the slow pointer, there is a cycle.
        if slow == fast:
            return True
    
    return False

# Example usage:
head = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(0)
head.next.next.next = ListNode(-4)
head.next.next.next.next = head.next  # Create a cycle in the linked list.
print(has_cycle(head))  # Output: True (cycle exists)
