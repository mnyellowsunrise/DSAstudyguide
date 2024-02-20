class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val          # Initialize a node with a value
        self.left = left        # Initialize the left child of the node
        self.right = right      # Initialize the right child of the node

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        inorder = []            # Initialize an empty list to store the inorder traversal result
        nodes = []              # Initialize an empty list to simulate the stack for iterative traversal

        if root is None:        # If the tree is empty, return the empty inorder traversal result
            return inorder

        while root is not None or nodes:  # Loop until all nodes are processed
            # Traverse to the leftmost node while pushing nodes onto the stack
            while root is not None:
                nodes.append(root)          # Push the current node onto the stack
                root = root.left           # Move to the left child of the current node

            # Retrieve the top node from the stack and store its value
            root = nodes.pop()              # Pop the top node from the stack
            inorder.append(root.val)        # Add the value of the current node to the inorder traversal result

            root = root.right               # Move to the right child of the current node

        return inorder                      # Return the final inorder traversal result

