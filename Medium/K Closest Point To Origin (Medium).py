"""
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

 

Example 1:

Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].

Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
Explanation: The answer [[-2,4],[3,3]] would also be accepted.

 

Constraints:

    1 <= k <= points.length <= 104
    -104 <= xi, yi <= 104

"""

import heapq
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Initialize a list to store tuples of (distance from origin, x-coordinate, y-coordinate).
        minHeap = []
        # Calculate the distance from origin for each point and add it to the minHeap.
        for x, y in points:
            # Calculate the squared distance using the Euclidean distance formula: (x^2 + y^2).
            dist = (x ** 2) + (y ** 2)
            # Append the tuple (distance, x-coordinate, y-coordinate) to the minHeap.
            minHeap.append((dist, x, y))
        
        # Convert the list of tuples into a min heap.
        heapq.heapify(minHeap)
        
        # Initialize an empty list to store the k closest points.
        res = []
        # Iterate k times to extract the k closest points from the minHeap.
        for _ in range(k):
            # Pop the closest point (tuple) from the minHeap.
            _, x, y = heapq.heappop(minHeap)
            # Append the x and y coordinates of the closest point to the result list.
            res.append([x, y])
        
        # Return the list of k closest points.
        return res
