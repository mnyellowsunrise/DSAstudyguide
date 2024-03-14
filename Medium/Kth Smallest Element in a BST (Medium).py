"""
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

 

Example 1:

Input: root = [3,1,4,null,2], k = 1
Output: 1

Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3

 

Constraints:

    The number of nodes in the tree is n.
    1 <= k <= n <= 104
    0 <= Node.val <= 104

 

Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []  # Initialize an empty stack to perform iterative inorder traversal
        curr = root  # Start traversal from the root node

        while stack or curr:  # Continue traversal until both stack and current node are empty
            while curr:  # Traverse to the leftmost node of the current subtree
                stack.append(curr)  # Push current node into the stack
                curr = curr.left  # Move to the left child of the current node
            curr = stack.pop()  # When reaching the leftmost node, pop it from the stack
            k -= 1  # Decrement k as we visit each node
            if k == 0:  # If k becomes 0, we have found the kth smallest node
                return curr.val  # Return the value of the kth smallest node
            curr = curr.right  # Move to the right child of the popped node

