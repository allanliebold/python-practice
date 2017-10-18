"""Tests Math Series Functions."""
import pytest

"""Fib Tests
Fibonacci Sequence: 0 1 1 2 3 5 8 13 21 34 55...
"""


def test_fib_0():
    """Test fib with n of 0, should return 0."""
    from series import fib
    assert fib(0) == 0


def test_fib_1():
    """Test fib with n of 1, should return 0."""
    from series import fib
    assert fib(1) == 0


def test_fib_2():
    """Test fib with n of 2, should return 1."""
    from series import fib
    assert fib(2) == 1


def test_fib_5():
    """Test fib with n of 5, should return 3."""
    from series import fib
    assert fib(5) == 3


def test_fib_10():
    """Test fib with n of 10, should return 34."""
    from series import fib
    assert fib(10) == 34


def test_fib_string():
    """Test fib with string, should raise TypeError."""
    from series import fib
    with pytest.raises(TypeError):
        fib('string')

"""Lucas Tests
Lucas Sequence: 2 1 3 4 7 11 18 29 47 76 123...
"""


def test_lucas_0():
    """Test lucas with n of 0, should return 0."""
    from series import lucas
    assert lucas(0) == 0


def test_lucas_1():
    """Test lucas with n of 1, should return 2."""
    from series import lucas
    assert lucas(1) == 2


def test_lucas_2():
    """Test lucas with n of 2, should return 1."""
    from series import lucas
    assert lucas(2) == 1


def test_lucas_5():
    """Test lucas with n of 5, should return 7."""
    from series import lucas
    assert lucas(5) == 7


def test_lucas_10():
    """Test lucas with n of 10, should return 76."""
    from series import lucas
    assert lucas(10) == 76


def test_lucas_string():
    """Test lucas with string, should raise TypeError."""
    from series import lucas
    with pytest.raises(TypeError):
        lucas('string')


"""Sum Series Tests."""


def test_sum_series_0():
    """Test sum_series with n of 0, should return 0."""
    from series import sum_series
    assert sum_series(0) == 0


def test_sum_series_501():
    """Test sum_series with n of 5, first of 0, second of 1.

    Should return 3
    """
    from series import sum_series
    assert sum_series(5, 0, 1) == 3


def test_sum_series_521():
    """Test sum_series with n of 5, first of 2, second of 1.

    Should return 7
    """
    from series import sum_series
    assert sum_series(5, 2, 1) == 7


def test_sum_series_555():
    """Test sum_series with n of 5, first of 5, second of 5.

    Should return 25
    """
    from series import sum_series
    assert sum_series(5, 5, 5) == 25


def test_sum_series_102030():
    """Test sum_series with n of 10, first of 20, second of 30.

    Should return 1410
    """
    from series import sum_series
    assert sum_series(10, 20, 30) == 1440


def test_sum_series_string():
    """Test sum_series with string, should raise TypeError."""
    from series import sum_series
    with pytest.raises(TypeError):
        sum_series('string')
