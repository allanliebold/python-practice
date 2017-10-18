"""Tests Math Series Functions."""
import pytest

"""Tests for fib function
Fibonacci Sequence: 0 1 1 2 3 5 8 13 21 34 55...
"""


def test_fib_1():
    """Test fib with n of 1, should equal 0."""
    from series import fib
    assert fib(1) == 0


def test_fib_2():
    """Test fib with n of 2, should equal 1."""
    from series import fib
    assert fib(2) == 1


def test_fib_5():
    """Test fib with n of 5, should equal 3."""
    from series import fib
    assert fib(5) == 3


def test_fib_10():
    """Test fib with n of 10, should equal 34."""
    from series import fib
    assert fib(10) == 34
