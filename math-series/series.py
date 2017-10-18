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


"""Lucas Numbers Function."""


def lucas(n):
    """Return the value of n in the Lucas Numbers."""
    if n == 0:
        return 0
    elif n == 1:
        return 2
    elif n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n + 1)

"""Sum Series Function."""


def sum_series(n, first=0, second=1):
    """Return n in sequence.

    User may provide first and second numbers.
    """
    if n == 0:
        return 0
    elif first == 0 and second == 1:
        return fib(n)
    elif first == 2 and second == 1:
        return lucas(n)
    else:
        for i in range(1, n):
            first, second = second, first + second
        return first
