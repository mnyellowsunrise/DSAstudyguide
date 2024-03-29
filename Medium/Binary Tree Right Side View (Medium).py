"""
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

 

Example 1:

Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]

Example 2:

Input: root = [1,null,3]
Output: [1,3]

Example 3:

Input: root = []
Output: []

Constraints:

    The number of nodes in the tree is in the range [0, 100].
    -100 <= Node.val <= 100

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Importing deque from collections module
import collections

class Solution:
    # Function to return the values of the nodes on the right side of the binary tree
    def rightSideView(self, root: TreeNode) -> List[int]:
        # List to store the result (values of nodes on the right side)
        res = []
        # Initializing a deque (double-ended queue) with the root node
        q = collections.deque([root])

        # Loop until the deque is not empty
        while q:
            # Initializing a variable to store the rightmost node in the current level
            rightSide = None
            # Getting the current length of the deque (number of nodes at the current level)
            qLen = len(q)

            # Iterating through each node at the current level
            for i in range(qLen):
                # Removing the leftmost node from the deque and storing it in 'node'
                node = q.popleft()
                # Checking if 'node' is not None
                if node:
                    # Updating 'rightSide' to the current node (rightmost node)
                    rightSide = node
                    # Adding the left child of 'node' to the deque
                    q.append(node.left)
                    # Adding the right child of 'node' to the deque
                    q.append(node.right)
            
            # Checking if 'rightSide' is not None (if there was at least one node at the current level)
            if rightSide:
                # Appending the value of the rightmost node to the result list
                res.append(rightSide.val)
        
        # Returning the list containing the values of nodes on the right side of the binary tree
        return res

