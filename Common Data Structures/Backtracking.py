# Problem: Generate all subsets of a given set of integers.
# Backtracking:
def generate_subsets(nums):
    def backtrack(start, path):
        result.append(path)  # Add the current subset to the result.
        for i in range(start, len(nums)):  # Iterate over remaining elements to build subsets.
            backtrack(i + 1, path + [nums[i]])  # Recursively build subsets.

    result = []  # Initialize a list to store all subsets.
    backtrack(0, [])  # Start backtracking from index 0 with an empty subset.
    return result  # Return all subsets.

# Example usage:
nums = [1, 2, 3]
print(generate_subsets(nums))  # Output: [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]] (all subsets)
