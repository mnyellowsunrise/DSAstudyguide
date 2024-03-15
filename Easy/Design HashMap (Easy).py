"""
Design a HashMap without using any built-in hash table libraries.

Implement the MyHashMap class:

    MyHashMap() initializes the object with an empty map.
    void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
    int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
    void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.

 

Example 1:

Input
["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
[[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
Output
[null, null, null, 1, -1, null, 1, null, -1]

Explanation
MyHashMap myHashMap = new MyHashMap();
myHashMap.put(1, 1); // The map is now [[1,1]]
myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]
myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1], [2,2]]
myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value)
myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]
myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
myHashMap.get(2);    // return -1 (i.e., not found), The map is now [[1,1]]

 

Constraints:

    0 <= key, value <= 106
    At most 104 calls will be made to put, get, and remove.

"""

class ListNode:
    def __init__(self, key=-1, val=-1, next=None):
        # ListNode class constructor initializes a node with key, value, and next pointer.
        self.key = key  # Initialize key of the node.
        self.val = val  # Initialize value of the node.
        self.next = next  # Initialize next pointer of the node.

class MyHashMap:
    def __init__(self):
        # MyHashMap class constructor initializes the hashmap with an array of ListNode objects.
        # The length of the array is chosen as 1000 arbitrarily.
        self.map = [ListNode() for i in range(1000)]
        
    def hashcode(self, key):
        # hashcode function calculates the hash value for the given key.
        # It simply takes the modulo of the key with the length of the map array.
        return key % len(self.map)

    def put(self, key: int, value: int) -> None:
        # put function inserts a (key, value) pair into the HashMap.
        # If the key already exists in the map, it updates the corresponding value.
        # It traverses the linked list at the calculated hash index and updates or inserts the node.
        cur = self.map[self.hashcode(key)]  # Get the head node of the linked list at the calculated hash index.
        while cur.next:  # Traverse the linked list until reaching the end.
            if cur.next.key == key:  # If the key already exists, update the value.
                cur.next.val = value
                return
            cur = cur.next  # Move to the next node in the linked list.
        cur.next = ListNode(key, value)  # Insert a new node at the end of the linked list.

    def get(self, key: int) -> int:
        # get function returns the value associated with the specified key, or -1 if not found.
        # It traverses the linked list at the calculated hash index to find the node with the given key.
        cur = self.map[self.hashcode(key)].next  # Get the first node of the linked list at the calculated hash index.
        while cur and cur.key != key:  # Traverse the linked list until reaching the end or finding the key.
            cur = cur.next  # Move to the next node in the linked list.
        if cur:  # If the key is found, return its corresponding value.
            return cur.val
        return -1  # If the key is not found, return -1.

    def remove(self, key: int) -> None:
        # remove function removes the (key, value) pair with the specified key from the map.
        # It traverses the linked list at the calculated hash index to find and remove the node with the given key.
        cur = self.map[self.hashcode(key)]  # Get the head node of the linked list at the calculated hash index.
        while cur.next and cur.next.key != key:  # Traverse the linked list until reaching the end or finding the key.
            cur = cur.next  # Move to the next node in the linked list.
        if cur and cur.next:  # If the key is found, remove the node from the linked list.
            cur.next = cur.next.next  # Update the next pointer to skip the node.
