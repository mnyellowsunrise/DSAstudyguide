"""
You are given the root of a binary search tree (BST) and an integer val.

Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.

 

Example 1:

Input: root = [4,2,7,1,3], val = 2
Output: [2,1,3]
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Define a method named searchBST which takes root node of a binary search tree (BST) and an integer val as input
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # If the root is None, meaning the tree is empty, return None
        if not root:
            return None
        # If the value of the root node is equal to the target value 'val', return the root node
        if root.val==val:
            return root
        # If the value of the root node is greater than the target value 'val', recursively search in the left subtree
        elif root.val>val:
            return self.searchBST(root.left,val)
        # If the value of the root node is less than the target value 'val', recursively search in the right subtree
        elif root.val<val:
            return self.searchBST(root.right,val)
