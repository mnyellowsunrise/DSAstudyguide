"""
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

 

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:

Input: root = [1]
Output: [[1]]

Example 3:

Input: root = []
Output: []

 

Constraints:

    The number of nodes in the tree is in the range [0, 2000].
    -1000 <= Node.val <= 1000

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Importing the collections module to use deque for efficient queue implementation
import collections

class Solution:
    # Define the method levelOrder that takes a TreeNode object root as input
    # and returns a list of lists representing the level order traversal of the tree
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # Initialize an empty list to store the result of level order traversal
        res = []
        # Initialize a deque (double-ended queue) to store nodes for level order traversal
        q = collections.deque()
        
        # Check if the root node exists
        if root:
            # If the root exists, add it to the deque
            q.append(root)

        # Loop until the deque is empty
        while q:
            # Initialize an empty list to store the values of nodes at the current level
            val = []

            # Iterate over the nodes at the current level
            for i in range(len(q)):
                # Remove the leftmost node from the deque
                node = q.popleft()
                # Add the value of the current node to the list of values for the current level
                val.append(node.val)
                # If the current node has a left child, add it to the deque
                if node.left:
                    q.append(node.left)
                # If the current node has a right child, add it to the deque
                if node.right:
                    q.append(node.right)
            
            # Add the list of values for the current level to the result list
            res.append(val)
        
        # Return the result list containing the level order traversal of the binary tree
        return res
