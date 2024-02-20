class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val          # Initialize a node with a value
        self.left = left        # Initialize the left child of the node
        self.right = right      # Initialize the right child of the node

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []                  # Initialize an empty stack for iterative traversal
        
        while root is not None or stack:   # Iterate until all nodes are processed
            while root is not None:        # Traverse to the leftmost node while pushing nodes onto the stack
                stack.append(root)         # Push the current node onto the stack
                root = root.left           # Move to the left child of the current node
            
            root = stack.pop()              # Retrieve the top node from the stack
            k -= 1                         # Decrement k to track the current position in the inorder traversal
            if k == 0:                     # If k reaches 0, it means we've found the kth smallest element
                return root.val            # Return the value of the current node
            
            root = root.right              # Move to the right child of the current node
        
        return -1                         # Return -1 if the kth smallest element is not found (should not happen for valid k values)
