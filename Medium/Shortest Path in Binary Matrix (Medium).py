"""
Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

    All the visited cells of the path are 0.
    All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).

The length of a clear path is the number of visited cells of this path.

 

Example 1:

Input: grid = [[0,1],[1,0]]
Output: 2

Example 2:

Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
Output: 4

Example 3:

Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
Output: -1

 

Constraints:

    n == grid.length
    n == grid[i].length
    1 <= n <= 100
    grid[i][j] is 0 or 1

"""

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # Get the size of the grid
        N = len(grid)
        # Initialize a deque with starting position (0, 0) and length 1
        q = deque([(0, 0, 1)]) # r, c, length
        # Initialize a set to keep track of visited cells
        visit = set((0, 0))
        # Define all 8 possible directions
        direct = [[0, 1], [1, 0], [0, -1], [-1, 0],
                  [1, 1], [-1, -1], [1, -1], [-1, 1]]
        # Loop until the queue is empty
        while q:
            # Pop the first element from the queue
            r, c, length = q.popleft()
            # Check if the current position is out of bounds or a blocked cell
            if (min(r, c) < 0 or max(r, c) >= N or
                grid[r][c]):
                # Skip to the next iteration if the conditions are met
                continue
            # Check if the current position is the target cell
            if r == N - 1 and c == N - 1:
                # If so, return the length of the path
                return length
            # Iterate through all 8 directions
            for dr, dc in direct:
                # Calculate the next position
                nr, nc = r + dr, c + dc
                # Check if the next position has not been visited
                if (nr, nc) not in visit:
                    # Add the next position to the queue with incremented length
                    q.append((nr, nc, length + 1))
                    # Mark the next position as visited
                    visit.add((nr, nc))
        # If no clear path is found, return -1
        return -1