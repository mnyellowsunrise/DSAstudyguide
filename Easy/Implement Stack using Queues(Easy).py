from collections import deque

class MyStack:

    # Constructor initializes an empty deque to represent the stack.
    def __init__(self):
        self.q = deque()
        
    # Function to push an element to the top of the stack.
    def push(self, x: int) -> None:
        # Append the new element to the end of the deque.
        self.q.append(x)
        
    # Function to pop and return the element from the top of the stack.
    def pop(self) -> int:
        # Move all elements in the deque, except the last one, to the back of the deque.
        for i in range(len(self.q) - 1):
            # Pop from the front and push to the back.
            self.push(self.q.popleft())
        # Return the last element in the deque, which was originally at the front.
        return self.q.popleft()
    
    # Function to return the element from the top of the stack without removing it.
    def top(self) -> int:
        # Return the last element in the deque without modifying the deque.
        return self.q[-1]
        
    # Function to check if the stack is empty.
    def empty(self) -> bool:
        # Return True if the deque is empty, indicating an empty stack; otherwise, return False.
        return len(self.q) == 0

        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()