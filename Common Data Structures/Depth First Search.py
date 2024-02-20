# Problem: Given a graph represented as an adjacency list and a starting node, perform depth-first search (DFS) traversal and return the set of visited nodes.
# Depth-First Search (DFS):
def dfs(graph, node, visited):
    if node not in visited:  # If the node has not been visited yet.
        visited.add(node)  # Mark the node as visited.
        for neighbor in graph[node]:  # Iterate over the neighbors of the current node.
            dfs(graph, neighbor, visited)  # Recursively perform DFS on each neighbor.

# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
visited = set()
dfs(graph, 'A', visited)
print(visited)  # Output: {'A', 'B', 'C', 'D', 'E', 'F'} (nodes visited in DFS order)
