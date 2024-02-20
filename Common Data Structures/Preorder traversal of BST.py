class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []              # Initialize a stack for DFS traversal
        result = []             # Initialize a list to store the preorder traversal result
        
        stack.append(root)      # Push the root node onto the stack
        
        while stack:            # Iterate until the stack is empty
            current = stack.pop()   # Pop the top node from the stack
            
            if current is not None:
                # Push unvisited neighbors (right and left children) onto the stack
                # Note: Order matters here for preorder traversal
                stack.append(current.right)
                stack.append(current.left)
                
                result.append(current.val)  # Append the value of the current node to the result list
        
        return result           # Return the preorder traversal result
