"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

 

Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 300
    grid[i][j] is '0' or '1'.

"""

# DFS Version
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Check if the grid is empty
        if not grid or not grid[0]:
            return 0

        islands = 0
        visit = set()  # Set to keep track of visited cells
        rows, cols = len(grid), len(grid[0])

        # DFS function to traverse the grid
        def dfs(r, c):
            # Base cases for out of bounds or water cells
            if (
                r not in range(rows)
                or c not in range(cols)
                or grid[r][c] == "0"
                or (r, c) in visit
            ):
                return

            # Mark current cell as visited
            visit.add((r, c))
            # Define directions to move: right, left, down, up
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            # Explore each direction
            for dr, dc in directions:
                # Recursive call to DFS for neighboring cells
                dfs(r + dr, c + dc)

        # Loop through each cell in the grid
        for r in range(rows):
            for c in range(cols):
                # If cell is land and not visited, increment island count
                if grid[r][c] == "1" and (r, c) not in visit:
                    islands += 1
                    # Start DFS traversal from the current land cell
                    dfs(r, c)
        return islands


# BFS Version
class SolutionBFS:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Check if the grid is empty
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = set()  # Set to keep track of visited cells
        islands = 0

        # BFS function to traverse the grid
        def bfs(r, c):
            # Initialize a queue for BFS traversal
            q = deque()
            # Mark current cell as visited
            visited.add((r, c))
            q.append((r, c))  # Add current cell to the queue

            # While there are cells in the queue
            while q:
                row, col = q.popleft()
                # Define directions to move: down, up, right, left
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                # Explore each direction
                for dr, dc in directions:
                    # Calculate next cell coordinates
                    r, c = row + dr, col + dc
                    # Check if next cell is within bounds, land, and not visited
                    if (
                        r in range(rows)
                        and c in range(cols)
                        and grid[r][c] == '1'
                        and (r, c) not in visited
                    ):
                        # Add next cell to the queue and mark as visited
                        q.append((r, c))
                        visited.add((r, c))

        # Loop through each cell in the grid
        for r in range(rows):
            for c in range(cols):
                # If cell is land and not visited, increment island count
                if grid[r][c] == "1" and (r, c) not in visited:
                    islands += 1
                    # Start BFS traversal from the current land cell
                    bfs(r, c)
        return islands
    