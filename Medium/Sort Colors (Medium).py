#Sort Colors
#Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

#We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

#You must solve this problem without using the library's sort function.

 

#Example 1:

#Input: nums = [2,0,2,1,1,0]
#Output: [0,0,1,1,2,2]

#Example 2:

#Input: nums = [2,0,1]
#Output: [0,1,2]

 

#Constraints:

    #n == nums.length
    #1 <= n <= 300
    #nums[i] is either 0, 1, or 2.  

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # Initialize pointers for low, mid, and high
        low = 0
        high = len(nums) - 1
        mid = 0

        # Iterate until mid pointer crosses the high pointer
        while mid <= high:
            # If the current element is 0, swap it with the element at low pointer
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                # Increment low and mid pointers
                low += 1
                mid += 1
            # If the current element is 1, simply increment the mid pointer
            elif nums[mid] == 1:
                mid += 1
            # If the current element is 2, swap it with the element at high pointer
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                # Decrement the high pointer
                high -= 1
        # Return the sorted array
        return nums

