# Problem: Given an array of integers nums and an integer k, return the k most frequent elements.
# Top K Elements:
import heapq

def top_k_frequent(nums, k):
    freq_map = {}  # Create a frequency map to count occurrences of each number.
    for num in nums:
        freq_map[num] = freq_map.get(num, 0) + 1
    
    min_heap = []  # Create a min heap to store k most frequent elements.
    for num, freq in freq_map.items():
        heapq.heappush(min_heap, (freq, num))  # Push elements into the heap.
        if len(min_heap) > k:  # If heap size exceeds k, pop the smallest element.
            heapq.heappop(min_heap)
    
    return [num for freq, num in min_heap]  # Return the elements in the heap.

# Example usage:
nums = [1, 1, 1, 2, 2, 3]
k = 2
print(top_k_frequent(nums, k))  # Output: [1, 2] (top 2 frequent elements)
