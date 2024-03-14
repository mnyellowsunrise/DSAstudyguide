"""
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

 

Example 1:

Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

Example 2:

Input: preorder = [-1], inorder = [-1]
Output: [-1]

Constraints:

    1 <= preorder.length <= 3000
    inorder.length == preorder.length
    -3000 <= preorder[i], inorder[i] <= 3000
    preorder and inorder consist of unique values.
    Each value of inorder also appears in preorder.
    preorder is guaranteed to be the preorder traversal of the tree.
    inorder is guaranteed to be the inorder traversal of the tree.


 """

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Check if either preorder or inorder list is empty, if so, return None
        if not preorder or not inorder:
            return None

        # Create a TreeNode with the value of the first element in preorder list
        root = TreeNode(preorder[0])
        
        # Find the index of the root value in the inorder list
        mid = inorder.index(preorder[0])
        
        # Recursively call buildTree to construct the left subtree
        # Preorder list for the left subtree: elements from index 1 to mid+1
        # Inorder list for the left subtree: elements from start to mid
        root.left = self.buildTree(preorder[1 : mid + 1], inorder[:mid])
        
        # Recursively call buildTree to construct the right subtree
        # Preorder list for the right subtree: elements from mid+1 to end
        # Inorder list for the right subtree: elements from mid+1 to end
        root.right = self.buildTree(preorder[mid + 1 :], inorder[mid + 1 :])
        
        # Return the constructed root of the binary tree
        return root

