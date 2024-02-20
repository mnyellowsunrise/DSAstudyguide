# Problem: You are given a list of intervals representing the start and end times of meetings. 
# Find the minimum number of meeting rooms required to schedule all meetings without overlaps.

def minMeetingRooms(intervals):
    if not intervals:
        return 0
    
    # Separate the start times and end times of meetings
    start_times = sorted([interval[0] for interval in intervals])
    end_times = sorted([interval[1] for interval in intervals])
    
    # Initialize pointers and count
    start_ptr = end_ptr = count = 0
    
    # Iterate through all meetings
    while start_ptr < len(intervals):
        # If the current meeting starts after the previous meeting ends,
        # we can reuse the same meeting room
        if start_times[start_ptr] >= end_times[end_ptr]:
            count -= 1
            end_ptr += 1
        
        # Increment the count and move to the next meeting
        count += 1
        start_ptr += 1
    
    return count

# Example usage:
intervals = [[0, 30], [5, 10], [15, 20]]
print(minMeetingRooms(intervals))  # Output: 2 (Two meeting rooms required)
