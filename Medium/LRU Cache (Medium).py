"""
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

    LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
    int get(int key) Return the value of the key if the key exists, otherwise return -1.
    void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.

The functions get and put must each run in O(1) average time complexity.

 

Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4

 

Constraints:

    1 <= capacity <= 3000
    0 <= key <= 104
    0 <= value <= 105
    At most 2 * 105 calls will be made to get and put.



 """

class Node:
    def __init__(self, key, val):
        # Initialize a Node with a key and a value
        self.key, self.val = key, val
        # Initialize pointers to previous and next nodes
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        # Initialize the capacity of the LRU cache
        self.cap = capacity
        # Initialize a dictionary to store key-node pairs for fast lookup
        self.cache = {}  # map key to node

        # Initialize two sentinel nodes for the linked list
        self.left, self.right = Node(0, 0), Node(0, 0)
        # Connect the left and right sentinels
        self.left.next, self.right.prev = self.right, self.left

    # Function to remove a node from the linked list
    def remove(self, node):
        # Get the previous and next nodes of the given node
        prev, nxt = node.prev, node.next
        # Update the pointers to skip the given node
        prev.next, nxt.prev = nxt, prev

    # Function to insert a node at the right end of the linked list
    def insert(self, node):
        # Get the previous and next nodes of the right sentinel
        prev, nxt = self.right.prev, self.right
        # Update pointers to insert the node between prev and nxt
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    # Function to get the value of a key from the cache
    def get(self, key: int) -> int:
        # Check if the key is in the cache
        if key in self.cache:
            # Remove the node from its current position and insert it at the end
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            # Return the value of the node
            return self.cache[key].val
        # If key not found, return -1
        return -1

    # Function to put a key-value pair into the cache
    def put(self, key: int, value: int) -> None:
        # If the key is already in the cache, remove it
        if key in self.cache:
            self.remove(self.cache[key])
        # Create a new node with the given key and value
        self.cache[key] = Node(key, value)
        # Insert the new node at the end of the linked list
        self.insert(self.cache[key])

        # If the size of the cache exceeds the capacity
        if len(self.cache) > self.cap:
            # Remove the least recently used node from the front of the linked list
            lru = self.left.next
            self.remove(lru)
            # Delete the corresponding key from the cache
            del self.cache[lru.key]

