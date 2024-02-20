class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Initialize a dictionary to store the previous encountered numbers' indices
        prevMap = {}  # val -> index

        # Iterate over the elements of the input list 'nums' along with their indices
        for i, n in enumerate(nums):
            # Calculate the difference between the target and the current number
            diff = target - n
            # Check if the difference exists in the 'prevMap'
            if diff in prevMap:
                # If the difference exists, return the indices of the two numbers that sum up to the target
                return [prevMap[diff], i]
            # Store the current number and its index in the 'prevMap'
            prevMap[n] = i
