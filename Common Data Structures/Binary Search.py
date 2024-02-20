# Problem: Given a sorted array and a target value, perform binary search to find the index of the target value in the array.
# Binary Search:
def binary_search(nums, target):
    left, right = 0, len(nums) - 1  # Initialize pointers at the start and end of the array.
    
    while left <= right:  # Continue search until the left pointer is less than or equal to the right pointer.
        mid = left + (right - left) // 2  # Calculate the middle index.
        if nums[mid] == target:  # If the target is found at the middle index.
            return mid
        elif nums[mid] < target:  # If the target is greater than the middle element, search the right half.
            left = mid + 1
        else:  # If the target is less than the middle element, search the left half.
            right = mid - 1
    
    return -1  # Return -1 if the target is not found in the array.

# Example usage:
nums = [1, 3, 5, 7, 9, 11, 13]
target = 9
print(binary_search(nums, target))  # Output: 4 (index of target element)
