from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students = deque(students)
        sandwiches = deque(sandwiches)

        count = 0

        # Continue the loop until either all students eat or no more changes happen
        while count < len(students):
            # If the student at the front prefers the top sandwich
            if students[0] == sandwiches[0]:
                sandwiches.popleft()  # Remove the top sandwich from the queue
                count = 0  # Reset the counter as a student took the sandwich
            else:
                # If the student doesn't prefer the top sandwich, move them to the end of the queue
                students.append(students[0])
                count += 1  # Increment the counter for uneaten students

            students.popleft()  # Remove the student from the front of the queue

        # Return the number of uneaten students (students still in the queue)
        return len(students)
