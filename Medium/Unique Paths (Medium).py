"""
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.

 

Example 1:

Input: m = 3, n = 7
Output: 28

Example 2:

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down

 

Constraints:

    1 <= m, n <= 100


"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Initialize a list 'row' with all elements set to 1. 
        # This represents the number of unique paths for the first row of the grid.
        row = [1] * n

        # Iterate through each row of the grid, except the last one.
        for i in range(m - 1):
            # Create a new list 'newRow' with all elements set to 1.
            newRow = [1] * n
            # Iterate through each column of the current row, starting from the second last column and moving towards the first.
            for j in range(n - 2, -1, -1):
                # Calculate the number of unique paths to reach the current cell by summing up the number of paths from the cell to its right and the cell below it.
                # Update the corresponding element in 'newRow' with this calculated value.
                newRow[j] = newRow[j + 1] + row[j]
            # Update 'row' to represent the 'newRow' for the next iteration.
            row = newRow
        # Return the number of unique paths to reach the bottom-right corner of the grid, which is the first element of the 'row' list.
        return row[0]
