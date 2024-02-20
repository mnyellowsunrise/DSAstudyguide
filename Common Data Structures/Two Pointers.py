# Problem: Given an array of integers nums and an integer target, return the indices of the two numbers such that they add up to target.
# Two Pointers:
def two_sum(nums, target):
    left, right = 0, len(nums) - 1  # Initialize two pointers at the start and end of the array.
    
    # Iterate until the pointers meet.
    while left < right:
        current_sum = nums[left] + nums[right]  # Calculate the sum of the elements at the pointers.
        
        # If the sum equals the target, return the indices.
        if current_sum == target:
            return [left, right]
        elif current_sum < target:  # If the sum is less than the target, move the left pointer to the right.
            left += 1
        else:  # If the sum is greater than the target, move the right pointer to the left.
            right -= 1
    
    return []

# Example usage:
nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))  # Output: [0, 1] (indices of elements [2, 7] that sum up to 9)
