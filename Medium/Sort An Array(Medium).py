class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        # Helper function to merge two sorted arrays
        def merge(arr, L, M, R):
            # Create two temporary arrays for the left and right halves
            left, right = arr[L:M+1], arr[M+1:R+1]
            
            i, j, k = L, 0, 0  # Initialize indices for the main array and the two halves
            
            # Merge the two halves into the main array in ascending order
            while j < len(left) and k < len(right):
                if left[j] <= right[k]:
                    arr[i] = left[j]
                    j += 1
                else:
                    arr[i] = right[k]
                    k += 1
                i += 1
            
            # Check if there are any remaining elements in the left half
            while j < len(left):
                nums[i] = left[j]
                j += 1
                i += 1
            
            # Check if there are any remaining elements in the right half
            while k < len(right):
                nums[i] = right[k]
                k += 1
                i += 1

        # Recursive function to perform merge sort on the array
        def mergeSort(arr, l, r):
            if l == r:
                return arr  # If the array has only one element, it is already sorted
            
            m = (l + r) // 2  # Calculate the middle index
            
            # Recursively sort the left and right halves
            mergeSort(arr, l, m)
            mergeSort(arr, m + 1, r)
            
            # Merge the sorted halves
            merge(arr, l, m, r)
            
            return arr
        
        # Call the mergeSort function with the initial indices
        return mergeSort(nums, 0, len(nums) - 1)
