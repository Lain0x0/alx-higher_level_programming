#!/usr/bin/python3
"""Module for add_int"""


def add_integer(a, b=98):
    """Adds 2 int

    Args:
        a: 1st int
        b: 2nd int, default 98

    Raises:
        TypeError: if a, b are not int or float

    Returns:
        The sum of the 2 int
    """

    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
