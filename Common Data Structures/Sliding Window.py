# Problem: Given an array of integers nums and an integer k, find the maximum sum of a subarray of length k.
# Sliding Window:
def max_subarray_sum(nums, k):
    max_sum = float('-inf')  # Initialize the maximum sum to negative infinity.
    window_sum = 0  # Initialize the sum of the current window.
    window_start = 0  # Initialize the start index of the window.
    
    # Iterate through the array using a sliding window approach.
    for window_end in range(len(nums)):
        window_sum += nums[window_end]  # Add the current element to the window sum.
        
        # If the window size exceeds k, move the window by decrementing the window start.
        if window_end >= k - 1:
            max_sum = max(max_sum, window_sum)  # Update the maximum sum if needed.
            window_sum -= nums[window_start]  # Subtract the element at the window start.
            window_start += 1  # Move the window start to the right.
    
    return max_sum

# Example usage:
nums = [1, 4, 2, 10, 2, 3, 1, 0, 20]
k = 4
print(max_subarray_sum(nums, k))  # Output: 24 (sum of [10, 2, 3, 1])
