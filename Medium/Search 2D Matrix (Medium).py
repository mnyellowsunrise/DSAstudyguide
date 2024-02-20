#You are given an m x n integer matrix matrix with the following two properties:

    #Each row is sorted in non-decreasing order.
    #The first integer of each row is greater than the last integer of the previous row.

#Given an integer target, return true if target is in matrix or false otherwise.

#You must write a solution in O(log(m * n)) time complexity.

#Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
#Output: false

#Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
#Output: true


#Constraints:

    #m == matrix.length
    #n == matrix[i].length
    #1 <= m, n <= 100
    #-104 <= matrix[i][j], target <= 104


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Get the number of rows and columns in the matrix
        ROWS, COLS = len(matrix), len(matrix[0])

        # Initialize top and bottom pointers for binary search on rows
        top, bot = 0, ROWS - 1
        
        # Binary search to find the row where the target may be located
        while top <= bot:
            # Calculate the middle row
            row = (top + bot) // 2
            # If target is greater than the last element of the current row, move to the next row
            if target > matrix[row][-1]:
                top = row + 1
            # If target is smaller than the first element of the current row, move to the previous row
            elif target < matrix[row][0]:
                bot = row - 1
            # If target may be in the current row, break the loop
            else:
                break

        # If top pointer exceeds the bottom pointer, target is not present in the matrix
        if not (top <= bot):
            return False
        
        # Get the row index where target may be located
        row = (top + bot) // 2
        
        # Initialize left and right pointers for binary search on columns
        l, r = 0, COLS - 1
        
        # Binary search to find the target in the identified row
        while l <= r:
            # Calculate the middle column
            m = (l + r) // 2
            # If target is greater than the middle element, search in the right half
            if target > matrix[row][m]:
                l = m + 1
            # If target is smaller than the middle element, search in the left half
            elif target < matrix[row][m]:
                r = m - 1
            # If target is found, return True
            else:
                return True
        # If target is not found in the identified row, return False
        return False
