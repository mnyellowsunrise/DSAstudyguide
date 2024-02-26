"""
A non-empty array a of length n is called an array of all possibilities if it contains all numbers between 0 and a.length - 1 (both inclusive).

Write a method named IsAllPossibilities/isAllPossibilities/is_all_possibilities that accepts an integer array and returns true if the array is an array of all possibilities, else false.

Examples:

[1,2,0,3] => True
# Includes all numbers between 0 and a.length - 1 (4 - 1 = 3)

[0,1,2,2,3] => False
# Doesn't include all numbers between 0 and a.length - 1 (5 - 1 = 4)

[0] => True
# Includes all numbers between 0 and a.length - 1 (1 - 1 = 0).
"""
def is_all_possibilities(arr):
    # Check if the array is not empty
    # and compare the set of elements in the array with the set of all numbers from 0 to n-1
    # where n is the length of the array
    return bool(arr) and set(arr) == set(range(len(arr)))
