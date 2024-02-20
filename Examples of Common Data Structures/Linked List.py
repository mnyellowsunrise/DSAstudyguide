# Node class represents an individual element in the linked list
class Node:
    def __init__(self, data):
        # Each node contains data and a reference to the next node in the list
        self.data = data
        self.next = None

# LinkedList class represents the entire linked list
class LinkedList:
    def __init__(self):
        # The linked list starts with an empty head
        self.head = None

    def is_empty(self):
        # Check if the linked list is empty
        return self.head is None

    def append(self, data):
        # Add a new node with the given data at the end of the linked list
        new_node = Node(data)
        if self.head is None:
            # If the list is empty, the new node becomes the head
            self.head = new_node
            return
        # Traverse to the end of the list and add the new node
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        # Add a new node with the given data at the beginning of the linked list
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        

    def delete(self, data):
        # Delete the node with the specified data from the linked list
        if self.head is None:
            # If the list is empty, nothing to delete
            return
        if self.head.data == data:
            # If the head node has the target data, update the head to the next node
            self.head = self.head.next
            return
        # Traverse the list to find the node with the target data and update references
        current_node = self.head
        while current_node.next and current_node.next.data != data:
            current_node = current_node.next
        if current_node.next:
            current_node.next = current_node.next.next

    def display(self):
        # Display the elements of the linked list
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

# Example usage:
my_list = LinkedList()

# Append elements to the linked list
my_list.append(1)
my_list.append(2)
my_list.append(3)

# Prepend an element to the linked list
my_list.prepend(0)

# Display the linked list
my_list.display()  # Output: 0 -> 1 -> 2 -> 3 -> None

# Delete an element from the linked list
my_list.delete(2)

# Display the linked list after deletion
my_list.display()  # Output: 0 -> 1 -> 3 -> None
