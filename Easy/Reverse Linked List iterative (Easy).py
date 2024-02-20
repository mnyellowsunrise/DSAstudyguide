# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize two pointers, prev and curr
        prev, curr = None, head

        # Traverse the linked list
        while curr:
            # Store the next node in the original list
            nxt = curr.next

            # Reverse the direction of the current node's pointer
            curr.next = prev

            # Move prev and curr pointers one step forward
            prev = curr
            curr = nxt

        # After the loop, prev is the new head of the reversed list
        return prev
