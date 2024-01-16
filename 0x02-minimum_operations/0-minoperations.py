#!/usr/bin/python3
"""
calculates the fewest number of operations needed to
result in exactly n H characters in the file.
"""


def minOperations(n):
    """
    n represents the characters we are aiming
    if its less than two we return 0 since no need for operation
    """
    min_operations, divisor = 0, 2
    if n < 2:
        return 0

    while n > 1:
        if n % divisor == 0:
            n = n / divisor
            min_operations += divisor
        else:
            divisor += 1
    return min_operations
