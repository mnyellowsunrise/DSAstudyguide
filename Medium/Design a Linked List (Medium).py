class MyLinkedList:
    def __init__(self):
        # Initialize an empty linked list with a dummy node as the head
        self.head = ListNode()
        # Initialize the length of the linked list
        self.length = 0

    def get(self, index):
        # Check if the index is valid
        if index < 0 or index >= self.length:
            return -1

        # Traverse the linked list to the specified index
        current = self.head.next
        for _ in range(index):
            current = current.next

        # Return the value of the node at the specified index
        return current.val

    def addAtHead(self, val):
        # Create a new node with the given value
        new_node = ListNode(val)
        # Insert the new node at the beginning of the linked list
        new_node.next = self.head.next
        self.head.next = new_node
        # Increment the length of the linked list
        self.length += 1

    def addAtTail(self, val):
        # Create a new node with the given value
        new_node = ListNode(val)
        # Traverse the linked list to the last node
        current = self.head
        while current.next:
            current = current.next
        # Append the new node to the end of the linked list
        current.next = new_node
        # Increment the length of the linked list
        self.length += 1

    def addAtIndex(self, index, val):
        # Check if the index is valid
        if index < 0 or index > self.length:
            return

        # Create a new node with the given value
        new_node = ListNode(val)
        # Traverse the linked list to the node before the specified index
        current = self.head
        for _ in range(index):
            current = current.next
        # Insert the new node at the specified index
        new_node.next = current.next
        current.next = new_node
        # Increment the length of the linked list
        self.length += 1

    def deleteAtIndex(self, index):
        # Check if the index is valid
        if index < 0 or index >= self.length:
            return

        # Traverse the linked list to the node before the specified index
        current = self.head
        for _ in range(index):
            current = current.next
        # Remove the node at the specified index
        current.next = current.next.next
        # Decrement the length of the linked list
        self.length -= 1