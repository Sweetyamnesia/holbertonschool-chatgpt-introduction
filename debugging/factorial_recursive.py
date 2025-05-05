#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function description:
    Calculates the factorial of a non-negative integer `n` recursively.

    Parameters:
    n (int): A non-negative integer whose factorial is to be computed.

    Returns:
    int: The factorial of the input integer `n`.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Read an integer from command line arguments, compute and print its factorial
f = factorial(int(sys.argv[1]))
print(f)
