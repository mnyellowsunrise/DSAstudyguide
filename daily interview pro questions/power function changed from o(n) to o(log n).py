#The power function calculates x raised to the nth power. If implemented in O(n) it would simply be a for loop over n and multiply x n times. Instead implement this power function in O(log n) time. You can assume that n will be a non-negative integer.

#Here's some starting code:

#def pow(x, n):
  # Fill this in.

#print(pow(5, 3))
# 125

def pow(x, n):
    # Base case: x^0 is always 1
    if n == 0:
        return 1

    # If n is even, divide the problem into two halves
    if n % 2 == 0:
        half_pow = pow(x, n // 2)
        return half_pow * half_pow
    # If n is odd, reduce it to an even power and multiply by x
    else:
        half_pow = pow(x, (n - 1) // 2)
        return x * half_pow * half_pow

# Test the function
result = pow(5, 3)
print(result)
# Output: 125
