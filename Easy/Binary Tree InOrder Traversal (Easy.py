"""
Given the root of a binary tree, return the inorder traversal of its nodes' values.

 

Example 1:

Input: root = [1,null,2,3]
Output: [1,3,2]

Example 2:

Input: root = []
Output: []

Example 3:

Input: root = [1]
Output: [1]

 

Constraints:

    The number of nodes in the tree is in the range [0, 100].
    -100 <= Node.val <= 100

 
Follow up: Recursive solution is trivial, could you do it iteratively?
"""

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Iterative approach
        res, stack = [], []  # Initialize an empty list to store the result and an empty stack for traversal
        cur = root  # Start traversal from the root node

        while cur or stack:  # Continue traversal until both current node and stack are empty
            while cur:  # Traverse to the leftmost node of the current subtree
                stack.append(cur)  # Push current node into the stack
                cur = cur.left  # Move to the left child of the current node
            cur = stack.pop()  # When reaching the leftmost node, pop it from the stack
            res.append(cur.val)  # Append the value of the popped node to the result
            cur = cur.right  # Move to the right child of the popped node

        return res  # Return the result after completing the inorder traversal

        # Recursive approach
        res = []  # Initialize an empty list to store the result

        def helper(root):
            if not root:  # Base case: if the current node is None, return
                return
            helper(root.left)  # Recursively traverse the left subtree
            res.append(root.val)  # Append the value of the current node to the result
            helper(root.right)  # Recursively traverse the right subtree

        helper(root)  # Start the recursive traversal from the root node
        return res  # Return the result after completing the inorder traversal

