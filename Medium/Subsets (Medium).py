"""
Given an integer array nums of unique elements, return all possible
subsets
(the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:

Input: nums = [0]
Output: [[],[0]]

 

Constraints:

    1 <= nums.length <= 10
    -10 <= nums[i] <= 10
    All the numbers of nums are unique.

"""

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Initialize an empty list to store the result (subsets)
        res = []

        # Initialize an empty list to represent the current subset being constructed
        subset = []

        # Define a depth-first search (DFS) function to generate subsets recursively
        def dfs(i):
            # Base case: if the index i exceeds the length of nums, all elements have been considered
            if i >= len(nums):
                # Append a copy of the current subset to the result list (res)
                res.append(subset.copy())
                return
            
            # Decision to include nums[i] in the current subset
            subset.append(nums[i])
            # Recur to explore subsets with nums[i] included, incrementing the index
            dfs(i + 1)
            
            # Decision NOT to include nums[i] in the current subset
            subset.pop()
            # Recur to explore subsets with nums[i] excluded, incrementing the index
            dfs(i + 1)

        # Start DFS with index 0 to generate all possible subsets
        dfs(0)
        # Return the final result containing all subsets
        return res
