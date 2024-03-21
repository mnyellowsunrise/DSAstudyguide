"""
207. Course Schedule
Medium
Topics
Companies
Hint

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

    For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

Return true if you can finish all courses. Otherwise, return false.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.

Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

 

Constraints:

    1 <= numCourses <= 2000
    0 <= prerequisites.length <= 5000
    prerequisites[i].length == 2
    0 <= ai, bi < numCourses
    All the pairs prerequisites[i] are unique.

"""

class Solution:
    # Method to check if it's possible to finish all courses
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Create a dictionary to map each course to its prerequisites
        preMap = {i: [] for i in range(numCourses)}

        # Map each course to its prerequisites
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        # Set to keep track of currently visiting courses during DFS
        visiting = set()

        # Depth-first search (DFS) function to check if all courses can be finished
        def dfs(crs):
            # If the course is currently being visited, there's a cycle, return False
            if crs in visiting:
                return False
            # If the course has no prerequisites, it can be finished, return True
            if preMap[crs] == []:
                return True

            # Mark the current course as visiting
            visiting.add(crs)
            # Recursively check prerequisites for the current course
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            # Mark the current course as visited and remove its prerequisites
            visiting.remove(crs)
            preMap[crs] = []
            return True

        # Iterate through all courses and check if they can be finished
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True  # All courses can be finished
