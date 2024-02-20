# Definition of a ListNode class representing a node in a doubly linked list
class ListNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

# Definition of the BrowserHistory class
class BrowserHistory:

    # Constructor to initialize the BrowserHistory object with a homepage
    def __init__(self, homepage: str):
        # Create a new ListNode representing the current page with the provided homepage
        self.cur = ListNode(homepage)

    # Method to visit a new URL, clearing forward history
    def visit(self, url: str) -> None:
        # Create a new ListNode for the visited URL with the current node as the previous node
        self.cur.next = ListNode(url, self.cur)
        # Move the current node to the newly visited URL
        self.cur = self.cur.next

    # Method to move back in history by a specified number of steps 
    def back(self, steps: int) -> str:
        # Iterate backward through the linked list while there are previous nodes and steps remaining
        while self.cur.prev and steps > 0:
            # Move the current node to its previous node
            self.cur = self.cur.prev
            # Decrement the steps counter
            steps -= 1
        # Return the URL of the current node after moving back in history
        return self.cur.val

    # Method to move forward in history by a specified number of steps
    def forward(self, steps: int) -> str:
        # Iterate forward through the linked list while there are next nodes and steps remaining
        while self.cur.next and steps > 0:
            # Move the current node to its next node
            self.cur = self.cur.next
            # Decrement the steps counter
            steps -= 1
        # Return the URL of the current node after moving forward in history
        return self.cur.val
