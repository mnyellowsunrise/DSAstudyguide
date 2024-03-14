"""
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

 

Example 1:

Input: piles = [3,6,7,11], h = 8
Output: 4

Example 2:

Input: piles = [30,11,23,4,20], h = 5
Output: 30

Example 3:

Input: piles = [30,11,23,4,20], h = 6
Output: 23

 

Constraints:

    1 <= piles.length <= 104
    piles.length <= h <= 109
    1 <= piles[i] <= 109

"""

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Initialize the left pointer to the minimum possible eating speed
        l = 1
        # Initialize the right pointer to the maximum number of bananas in a pile
        r = max(piles)
        # Initialize the result to the maximum number of bananas in a pile (worst case)

        # Binary search loop
        while l <= r:
            # Calculate the middle eating speed
            k = (l + r) // 2
            # Initialize the total hours required to eat all bananas
            hours = 0
            # Calculate the total hours required to eat all bananas with eating speed k
            for p in piles:
                # Calculate the number of hours needed to eat the current pile
                hours += math.ceil(p / k)
            # If the total hours needed is less than or equal to h
            if hours <= h:
                # Update the result to the minimum eating speed found so far
                res = min(res, k)
                # Update the right pointer to search for a smaller eating speed
                r = k - 1
            # If the total hours needed exceeds h
            else:
                # Update the left pointer to search for a larger eating speed
                l = k + 1
            
        # Return the minimum eating speed required to eat all bananas within h hours
        return res
