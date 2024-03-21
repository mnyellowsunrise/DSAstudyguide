"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.

 

Constraints:

    1 <= nums.length <= 100
    0 <= nums[i] <= 400

"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        # Initialize variables to track the maximum amount of money that can be robbed
        rob1, rob2 = 0, 0

        # Iterate through each house
        for n in nums:
            # Calculate the maximum amount of money that can be obtained if the current house is robbed
            # The maximum amount is either the money from the current house plus the money from the house two steps back,
            # or the money from the previous house (i.e., not robbing the current house)
            temp = max(n + rob1, rob2)
            # Update rob1 to store the maximum amount of money obtained from robbing the previous house
            rob1 = rob2
            # Update rob2 to store the maximum amount of money obtained from robbing the current house
            rob2 = temp
        # Return the maximum amount of money that can be obtained without alerting the police
        return rob2
