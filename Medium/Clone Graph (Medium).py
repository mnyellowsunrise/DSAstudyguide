"""
133. Clone Graph
Medium
Topics
Companies

Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}

 

Test case format:

For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.

 

Example 1:

Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).

Example 2:

Input: adjList = [[]]
Output: [[]]
Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.

Example 3:

Input: adjList = []
Output: []
Explanation: This an empty graph, it does not have any nodes.

 

Constraints:

    The number of nodes in the graph is in the range [0, 100].
    1 <= Node.val <= 100
    Node.val is unique for each node.
    There are no repeated edges and no self-loops in the graph.
    The Graph is connected and all nodes can be visited starting from the given node.

"""

# Definition for a Node class representing a node in the graph
class Node:
    # Constructor initializing a node with a value and optional neighbors list
    def __init__(self, val = 0, neighbors = None):
        self.val = val  # Value of the node
        self.neighbors = neighbors if neighbors is not None else []  # List of neighbors

# Class Solution for cloning a graph
class Solution:
    # Method for cloning the graph given a reference to a node
    def cloneGraph(self, node: "Node") -> "Node":
        # Dictionary to map old nodes to their corresponding new nodes
        oldToNew = {}

        # Depth-first search (DFS) function to clone the graph
        def dfs(node):
            # If the node has already been visited and cloned, return its clone
            if node in oldToNew:
                return oldToNew[node]

            # Create a copy of the current node
            copy = Node(node.val)
            # Add the mapping from the original node to its clone in the dictionary
            oldToNew[node] = copy
            # Recursively clone the neighbors of the current node
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            # Return the clone of the current node
            return copy

        # Start the DFS from the given node to clone the entire graph
        return dfs(node) if node else None  # Return the cloned graph or None if the input is None
