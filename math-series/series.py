"""Math Series Functions."""
"""Fibonacci Sequence Function."""


def fib(n):
    """Return the value of n in the Fibonacci Sequence."""
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n - 2) + fib(n - 1)
