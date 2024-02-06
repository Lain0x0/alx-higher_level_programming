#!/usr/bin/python3
""" sqaure module """


class Square:

    """ Represent a square """
    def __init__(self, size=0):
        """ contructor.
    Args:
        size: length of side of square
    """
        self.size = size

    @property
    def size(self):
        """Property for the length
        Raise:
            TypeError:If size is not int
            ValueError:If size is less than
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        if (not isinstance(value, int)):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Area of sqaure
        Returns:
            the size of square
        """
        return (self.__size ** 2)

    def __equal__(self, other):
        return (self.area() == other.area())

    def __notequal__(self, other):
        return (self.area() != other.area())

    def __greaterthan__(self, other):
        return (self.area() > other.area())

    def __greaterequal__(self, other):
        return (self.area() <= other.area())

    def __lessthan__(self, other):
        return (self.area() < other.area())

    def __lessequal__(self, other):
        return (self.area() <= other.area())
