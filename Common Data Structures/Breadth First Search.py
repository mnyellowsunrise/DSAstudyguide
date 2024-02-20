# Problem: Given a graph represented as an adjacency list and a starting node, perform breadth-first search (BFS) traversal and return the set of visited nodes.
# Breadth-First Search (BFS):
from collections import deque

def bfs(graph, start):
    visited = set()  # Initialize a set to store visited nodes.
    queue = deque([start])  # Initialize a queue with the starting node.
    
    while queue:  # Continue traversal until the queue is empty.
        node = queue.popleft()  # Dequeue the first node.
        if node not in visited:  # If the node has not been visited yet.
            visited.add(node)  # Mark the node as visited.
            for neighbor in graph[node]:  # Iterate over the neighbors of the current node.
                queue.append(neighbor)  # Enqueue each neighbor.
    
    return visited

# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
print(bfs(graph, 'A'))  # Output: {'A', 'B', 'C', 'D', 'E', 'F'} (nodes visited in BFS order)
