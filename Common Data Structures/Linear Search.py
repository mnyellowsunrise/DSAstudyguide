def linear_search(arr, target):
    """
    Perform linear search to find the target element in the array.

    Parameters:
    - arr: The list or array to search.
    - target: The element to search for.

    Returns:
    - index: The index of the target element if found, otherwise -1.
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Example usage:
my_list = [5, 3, 8, 1, 9, 2, 7]
target_element = 9
index = linear_search(my_list, target_element)
if index != -1:
    print(f"Element {target_element} found at index {index}.")
else:
    print(f"Element {target_element} not found in the list.")
