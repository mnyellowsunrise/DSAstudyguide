"""
You are given an m x n grid where each cell can have one of three values:

    0 representing an empty cell,
    1 representing a fresh orange, or
    2 representing a rotten orange.

Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

 

Example 1:

Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.

 

Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 10
    grid[i][j] is 0, 1, or 2.

"""

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Initialize a deque to store positions of rotten oranges
        q = collections.deque()
        # Initialize a variable to count the number of fresh oranges
        fresh = 0
        # Initialize a variable to track the time elapsed
        time = 0

        # Loop through the grid to find fresh and rotten oranges
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                # If the cell contains a fresh orange, increment fresh count
                if grid[r][c] == 1:
                    fresh += 1
                # If the cell contains a rotten orange, add its position to the deque
                if grid[r][c] == 2:
                    q.append((r, c))

        # Define the 4-directions to check for adjacent oranges
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        # Loop until there are fresh oranges remaining or the queue is empty
        while fresh > 0 and q:
            # Get the number of oranges in the current state of the queue
            length = len(q)
            # Process all oranges in the current state of the queue
            for i in range(length):
                # Pop the first orange from the queue
                r, c = q.popleft()

                # Check all 4 directions from the current orange
                for dr, dc in directions:
                    # Calculate the next position
                    row, col = r + dr, c + dc
                    # Check if the next position is valid and contains a fresh orange
                    if (
                        row in range(len(grid))
                        and col in range(len(grid[0]))
                        and grid[row][col] == 1
                    ):
                        # Turn the fresh orange into a rotten orange
                        grid[row][col] = 2
                        # Add the position of the rotten orange to the queue
                        q.append((row, col))
                        # Decrement the count of fresh oranges
                        fresh -= 1
            # Increment the time after processing all oranges in the current minute
            time += 1
        
        # Return the time if all fresh oranges are rotten, otherwise return -1
        return time if fresh == 0 else -1
