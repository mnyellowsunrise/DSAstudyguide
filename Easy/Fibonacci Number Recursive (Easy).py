class Solution:
    # Define a method 'fib' within the 'Solution' class
    def fib(self, n: int) -> int:
        # Base case: if n is 0, return 0
        if n == 0:
            return 0
        # Base case: if n is 1, return 1
        if n == 1:
            return 1
        # Recursive case: F(n) = F(n-1) + F(n-2)
        # Call 'fib' method recursively for n-1 and n-2, then sum the results
        return self.fib(n-1) + self.fib(n-2)

# Example usage:
# Create an instance of the Solution class
sol = Solution()
# Call the 'fib' method with n = 4
result = sol.fib(4)
# Print the result
print(f"The 4-th Fibonacci number is: {result}")
