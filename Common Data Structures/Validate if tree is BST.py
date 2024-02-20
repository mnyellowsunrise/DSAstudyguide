class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val          # Initialize a node with a value
        self.left = left        # Initialize the left child of the node
        self.right = right      # Initialize the right child of the node

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if root is None:            # If the tree is empty, it's considered a valid BST
            return True
        
        stack = []                  # Initialize an empty stack for iterative traversal
        prev = None                 # Initialize a variable to store the previously visited node
        
        while root is not None or stack:   # Iterate until all nodes are processed
            while root is not None:        # Traverse to the leftmost node while pushing nodes onto the stack
                stack.append(root)         # Push the current node onto the stack
                root = root.left           # Move to the left child of the current node
            
            root = stack.pop()              # Retrieve the top node from the stack
            if prev is not None and prev.val >= root.val:   # Check if the inorder traversal is in ascending order
                return False               # If not, the tree is not a valid BST
            prev = root                    # Update the previous node
            root = root.right              # Move to the right child of the current node
            
        return True                         # If the inorder traversal is in ascending order, the tree is a valid BST
