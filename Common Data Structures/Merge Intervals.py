# Problem: Given a collection of intervals, merge all overlapping intervals.
# Merge Intervals:
def merge(intervals):
    intervals.sort(key=lambda x: x[0])  # Sort the intervals based on the start value.
    merged = []  # Initialize a list to store the merged intervals.
    
    # Iterate through the sorted intervals.
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:  # If no overlap, add the interval to merged.
            merged.append(interval)
        else:  # If overlap, merge the intervals by updating the end value of the last merged interval.
            merged[-1][1] = max(merged[-1][1], interval[1])
    
    return merged

# Example usage:
intervals = [[1,3],[2,6],[8,10],[15,18]]
print(merge(intervals))  # Output: [[1, 6], [8, 10], [15, 18]] (merged intervals)
