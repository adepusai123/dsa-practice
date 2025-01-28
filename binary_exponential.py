def myPow(x, n):
    """
    :type x: float
    :type n: int
    :rtype: floait
    https://leetcode.com/problems/
    x = 2, n = 10 (+ve)
    x = 2, n = -2 (-ve)
    """
    r = 1 # initial value
    is_negative = n < 0 # flag is exponent is -ve
    n = abs(n) # converting to +ve number
    while n > 0:
        if n % 2 == 1: #if 1 then result * base
            r *= x
        x *= x # if 0, base * base
        n /= 2 # reminder 1
    return 1 / r if is_negative else r

print('Ans:', myPow(2, 10)) #1024

# This function calculates x raised to the power n (x^n) using binary exponentiation.
# Binary exponentiation is an efficient algorithm to compute power of a number.
# It works by reducing the problem size by half in each step, making it logarithmic in complexity.
# The function handles both positive and negative exponents.
# If the exponent is negative, it computes the reciprocal of the result.
# The time complexity of this function is O(log n).