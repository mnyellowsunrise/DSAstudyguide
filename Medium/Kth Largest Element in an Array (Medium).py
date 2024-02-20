#Kth Largest Element in an Array
#Given an integer array nums and an integer k, return the kth largest element in the array.

#Note that it is the kth largest element in the sorted order, not the kth distinct element.

#Can you solve it without sorting?

 

#Example 1:

#Input: nums = [3,2,1,5,6,4], k = 2
#Output: 5

#Example 2:

#Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
#Output: 4

 

#Constraints:

    #1 <= k <= nums.length <= 105
    #-104 <= nums[i] <= 104

# Solution: Sorting
# Time Complexity:
#   - Best Case: O(n)
#   - Average Case: O(n*log(n))
#   - Worst Case: O(n*log(n))
# Extra Space Complexity: O(n)
class Solution1:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Sort the input list of numbers in ascending order
        nums.sort()
        # Return the kth largest element, which is at index len(nums) - k after sorting
        return nums[len(nums) - k]


# Solution: QuickSelect
# Time Complexity:
#   - Best Case: O(n)
#   - Average Case: O(n)
#   - Worst Case: O(n^2)
# Extra Space Complexity: O(1)
class Solution2:
    def partition(self, nums: List[int], left: int, right: int) -> int:
        # Choose the rightmost element as the pivot
        pivot, fill = nums[right], left

        # Iterate through the list
        for i in range(left, right):
            # If the current element is less than or equal to the pivot
            if nums[i] <= pivot:
                # Swap the current element with the element at the fill index
                nums[fill], nums[i] = nums[i], nums[fill]
                # Increment the fill index
                fill += 1

        # Swap the pivot element with the element at the fill index
        nums[fill], nums[right] = nums[right], nums[fill]

        # Return the index of the pivot element after partitioning
        return fill

    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Convert k to the index of the kth largest element
        k = len(nums) - k
        # Initialize left and right pointers
        left, right = 0, len(nums) - 1

        # Iterate until the left pointer is less than the right pointer
        while left < right:
            # Partition the list and get the index of the pivot element
            pivot = self.partition(nums, left, right)

            # If the pivot index is less than k, update the left pointer
            if pivot < k:
                left = pivot + 1
            # If the pivot index is greater than k, update the right pointer
            elif pivot > k:
                right = pivot - 1
            # If the pivot index is equal to k, break the loop
            else:
                break

        # Return the kth largest element
        return nums[k]

