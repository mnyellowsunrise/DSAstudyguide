"""
Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Implement KthLargest class:

    KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
    int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.

 

Example 1:

Input
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
Output
[null, 4, 5, 5, 8, 8]

Explanation
KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3);   // return 4
kthLargest.add(5);   // return 5
kthLargest.add(10);  // return 5
kthLargest.add(9);   // return 8
kthLargest.add(4);   // return 8

 

Constraints:

    1 <= k <= 104
    0 <= nums.length <= 104
    -104 <= nums[i] <= 104
    -104 <= val <= 104
    At most 104 calls will be made to add.
    It is guaranteed that there will be at least k elements in the array when you search for the kth element.

"""
import heapq
from typing import List

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        # Initialize the KthLargest object with the specified k value and a list of integers (nums).
        # Create a minHeap to store the K largest integers.
        self.minHeap, self.k = nums, k
        # Convert the list into a minHeap.
        heapq.heapify(self.minHeap)
        # Remove elements from the minHeap until its size is equal to k, keeping only the K largest elements.
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        # Add the new value (val) to the minHeap.
        heapq.heappush(self.minHeap, val)
        # If the size of the minHeap exceeds k, remove the smallest element (since it's a minHeap).
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        # Return the smallest element in the minHeap, which represents the kth largest element.
        return self.minHeap[0]
