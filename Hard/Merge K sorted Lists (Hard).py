# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # Check if the input list of linked lists is empty or not
        if not lists or len(lists) == 0:
            return None

        # Iterate until there's only one list left in the input list of lists
        while len(lists) > 1:
            # Create an empty list to store merged lists
            mergedLists = []
            # Iterate over the input list of lists by step size of 2
            for i in range(0, len(lists), 2):
                # Get the first list to merge
                l1 = lists[i]
                # Get the second list to merge, if it exists
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                # Merge the two lists and append the merged list to the list of mergedLists
                mergedLists.append(self.mergeList(l1, l2))
            # Replace the original list of lists with the merged lists
            lists = mergedLists
        
        # Return the single merged list
        return lists[0]

    def mergeList(self, l1, l2):
        # Create a dummy node to facilitate the merging process
        dummy = ListNode()
        # Initialize a pointer to the tail of the merged list
        tail = dummy

        # Iterate until either l1 or l2 becomes None
        while l1 and l2:
            # Compare the values of the nodes from l1 and l2
            if l1.val < l2.val:
                # Append the smaller node to the tail of the merged list
                tail.next = l1
                # Move the pointer in the smaller list to the next node
                l1 = l1.next
            else:
                # Append the smaller node to the tail of the merged list
                tail.next = l2
                # Move the pointer in the smaller list to the next node
                l2 = l2.next
            # Move the tail pointer to the newly appended node
            tail = tail.next
        
        # Append the remaining nodes from l1, if any
        if l1:
            tail.next = l1
        # Append the remaining nodes from l2, if any
        if l2:
            tail.next = l2
        
        # Return the head of the merged list (excluding the dummy node)
        return dummy.next
