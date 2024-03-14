"""
Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

    Search for a node to remove.
    If the node is found, delete the node.

 

Example 1:

Input: root = [5,3,6,2,4,null,7], key = 3
Output: [5,4,6,2,null,null,7]
Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.

Example 2:

Input: root = [5,3,6,2,4,null,7], key = 0
Output: [5,3,6,2,4,null,7]
Explanation: The tree does not contain a node with value = 0.

Example 3:

Input: root = [], key = 0
Output: []

 

Constraints:

    The number of nodes in the tree is in the range [0, 104].
    -105 <= Node.val <= 105
    Each node has a unique value.
    root is a valid binary search tree.
    -105 <= key <= 105
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # Check if the root is None
        if not root:
            # If root is None, return None
            return root
        
        # If the key to delete is greater than the value of the current root node
        if key > root.val:
            # Recursively call deleteNode on the right subtree with the same root and the key to delete
            root.right = self.deleteNode(root.right, key)
        # If the key to delete is less than the value of the current root node
        elif key < root.val:
            # Recursively call deleteNode on the left subtree with the same root and the key to delete
            root.left = self.deleteNode(root.left, key)
        # If the key to delete is equal to the value of the current root node
        else:
            # If the current node has no left child
            if not root.left:
                # Return the right child of the current node (promote the right child)
                return root.right
            # If the current node has no right child
            elif not root.right:
                # Return the left child of the current node (promote the left child)
                return root.left
            
            # If the current node has both left and right children
            # Find the minimum value node in the right subtree
            cur = root.right
            while cur.left:
                cur = cur.left 
            # Copy the value of the minimum value node to the current node
            root.val = cur.val
            # Delete the minimum value node from the right subtree
            root.right = self.deleteNode(root.right, root.val)
        
        # Return the root node reference (possibly updated) of the BST
        return root
