# Problem: Compute the nth Fibonacci number using dynamic programming.
# Dynamic Programming (DP):
def fibonacci(n):
    dp = [0] * (n + 1)  # Initialize an array to store Fibonacci numbers.
    dp[1] = 1  # Set the base cases.
    
    for i in range(2, n + 1):  # Iterate from the third Fibonacci number.
        dp[i] = dp[i - 1] + dp[i - 2]  # Compute Fibonacci number using the previous two numbers.
    
    return dp[n]  # Return the nth Fibonacci number.

# Example usage:
print(fibonacci(6))  # Output: 8 (6th Fibonacci number)
