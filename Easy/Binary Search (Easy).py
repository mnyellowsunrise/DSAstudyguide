#Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

#You must write an algorithm with O(log n) runtime complexity.

 

#Example 1:

#Input: nums = [-1,0,3,5,9,12], target = 9
#Output: 4
#Explanation: 9 exists in nums and its index is 4

#Example 2:

#Input: nums = [-1,0,3,5,9,12], target = 2
#Output: -1
#Explanation: 2 does not exist in nums so return -1

 

#Constraints:

    #1 <= nums.length <= 104
    #-104 < nums[i], target < 104
    #All the integers in nums are unique.
    #nums is sorted in ascending order.

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Initialize left and right pointers for binary search
        l, r = 0, len(nums) - 1

        # Perform binary search until the left pointer exceeds the right pointer
        while l <= r:
            # Calculate the middle index to divide the search space
            m = l + ((r - l) // 2)  # (l + r) // 2 can lead to overflow
            
            # If the middle element is greater than the target, update the right pointer
            if nums[m] > target:
                r = m - 1
            # If the middle element is less than the target, update the left pointer
            elif nums[m] < target:
                l = m + 1
            # If the middle element equals the target, return its index
            else:
                return m
        
        # If the target is not found, return -1
        return -1
    

