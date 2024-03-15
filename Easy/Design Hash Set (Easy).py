"""
Design a HashSet without using any built-in hash table libraries.

Implement MyHashSet class:

    void add(key) Inserts the value key into the HashSet.
    bool contains(key) Returns whether the value key exists in the HashSet or not.
    void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.

 

Example 1:

Input
["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
[[], [1], [2], [1], [3], [2], [2], [2], [2]]
Output
[null, null, null, true, false, null, true, null, false]

Explanation
MyHashSet myHashSet = new MyHashSet();
myHashSet.add(1);      // set = [1]
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(1); // return True
myHashSet.contains(3); // return False, (not found)
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(2); // return True
myHashSet.remove(2);   // set = [1]
myHashSet.contains(2); // return False, (already removed)
"""
class ListNode:
    # ListNode class represents each node in the linked list
    def __init__(self, key):
        # Constructor to initialize a ListNode object with a given key
        self.key = key  # Stores the key (value) associated with this node
        self.next = next  # Pointer to the next node in the linked list (initialized as None)

class MyHashSet:

    def __init__(self):
        # Constructor to initialize a MyHashSet object
        self.set = [ListNode(0) for i in range(10**4)]  # Initialize an array of ListNode objects (buckets)

    def add(self, key: int) -> None:
        # Method to add a key to the HashSet
        index = key % len(self.set)  # Calculate the index to insert the key
        cur = self.set[index]  # Get the ListNode object at the calculated index

        while cur.next:
            # Traverse the linked list until reaching the end
            if cur.next.key == key:
                # If the key already exists in the HashSet, do nothing
                return
            cur = cur.next

        # If the key does not exist in the HashSet, add it to the end of the linked list
        cur.next = ListNode(key)

    def remove(self, key: int) -> None:
        # Method to remove a key from the HashSet
        cur = self.set[key & len(self.set)]  # Get the ListNode object at the calculated index

        while cur.next:
            # Traverse the linked list until reaching the end
            if cur.next.key == key:
                # If the key is found, remove it from the linked list
                cur.next = cur.next.next
                return
            cur = cur.next

    def contains(self, key: int) -> bool:
        # Method to check if a key exists in the HashSet
        cur = self.set[key % len(self.set)]  # Get the ListNode object at the calculated index

        while cur.next:
            # Traverse the linked list until reaching the end
            if cur.next.key == key:
                # If the key is found, return True
                return True
            cur = cur.next

        # If the key is not found in the HashSet, return False
        return False

        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)