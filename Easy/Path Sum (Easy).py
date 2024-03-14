"""
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

 

Example 1:

Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.

Example 2:

Input: root = [1,2,3], targetSum = 5
Output: false
Explanation: There two root-to-leaf paths in the tree:
(1 --> 2): The sum is 3.
(1 --> 3): The sum is 4.
There is no root-to-leaf path with sum = 5.

Example 3:

Input: root = [], targetSum = 0
Output: false
Explanation: Since the tree is empty, there are no root-to-leaf paths.

 

Constraints:

    The number of nodes in the tree is in the range [0, 5000].
    -1000 <= Node.val <= 1000
    -1000 <= targetSum <= 1000

"""

class Solution:
    def hasPathSum(self, root, sum):
        # Check if the root is None (empty tree), if so, return False
        if not root:
            return False
        # Initialize a deque with a tuple containing the root node and the difference between targetSum and the value of the root node
        de = [
            (root, sum - root.val),
        ]
        # Loop until the deque is empty
        while de:
            # Pop the last element (node, curr_sum) from the deque
            node, curr_sum = de.pop()
            # Check if the current node is a leaf node (no children) and if the current sum equals 0, if so, return True
            if not node.left and not node.right and curr_sum == 0:
                return True
            # If the current node has a right child, append a tuple containing the right child and the difference between the current sum and the value of the right child
            if node.right:
                de.append((node.right, curr_sum - node.right.val))
            # If the current node has a left child, append a tuple containing the left child and the difference between the current sum and the value of the left child
            if node.left:
                de.append((node.left, curr_sum - node.left.val))
        # If no root-to-leaf path with the target sum is found, return False
        return False
