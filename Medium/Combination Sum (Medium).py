"""
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the
frequency
of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

 

Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]

Example 3:

Input: candidates = [2], target = 1
Output: []

 

Constraints:

    1 <= candidates.length <= 30
    2 <= candidates[i] <= 40
    All elements of candidates are distinct.
    1 <= target <= 40

"""
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # Initialize an empty list to store the result (combinations that sum up to the target)
        res = []

        # Define a depth-first search (DFS) function to generate combinations recursively
        def dfs(i, cur, total):
            # Base case: if the total sum equals the target, append the current combination to the result list
            if total == target:
                res.append(cur.copy())
                return
            # Base case: if the index i exceeds the length of candidates or the total sum exceeds the target, stop recursion
            if i >= len(candidates) or total > target:
                return

            # Decision to include candidates[i] in the current combination
            cur.append(candidates[i])
            # Recur to explore combinations with candidates[i] included, incrementing the index and updating the total sum
            dfs(i, cur, total + candidates[i])
            # Backtrack: remove candidates[i] from the current combination to explore other possibilities
            cur.pop()
            # Recur to explore combinations without including candidates[i], incrementing the index
            dfs(i + 1, cur, total)

        # Start DFS with index 0, an empty current combination, and a total sum of 0
        dfs(0, [], 0)
        # Return the final result containing all combinations
        return res
