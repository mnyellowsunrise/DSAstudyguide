# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to serve as the starting point of the merged list
        dummy = ListNode()
        # Initialize a tail pointer to keep track of the last node in the merged list
        tail = dummy

        # Loop until either l1 or l2 becomes None
        while l1 and l2:
            # Compare the values of the current nodes in l1 and l2
            if l1.val < l2.val:
                # If the value in l1 is smaller, append it to the merged list
                tail.next = l1
                # Move to the next node in l1
                l1 = l1.next
            else:
                # If the value in l2 is smaller or equal, append it to the merged list
                tail.next = l2
                # Move to the next node in l2
                l2 = l2.next
            # Move the tail pointer to the newly added node in the merged list
            tail = tail.next

        # After the loop, one of the linked lists is exhausted. Append the remaining nodes.
        # If there are remaining nodes in l1, append them to the merged list
        if l1:
            tail.next = l1
        # If there are remaining nodes in l2, append them to the merged list
        elif l2:
            tail.next = l2

        # The merged list starts from the next node of the dummy node
        return dummy.next

        