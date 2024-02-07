#!/usr/bin/python3
""" Square module."""


class Square:
    """ Defines a square """

    def __init__(self, size=0, position=(0, 0)):
        """ Initialize square values """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get for square"""
        return self.__size

    @size.setter
    def size(self, value):
        """ Square attribute size """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """ Get the square position """
        return self.__position

    @position.setter
    def position(self, value):
        """ Square attribute position """
        if not isinstance(value, tuple) or \
                len(value) != 2 or \
                not all(isinstance(num, int) for num in value) or \
                not all(num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ Return the area of square """
        return self.__size * self.__size

    def my_print(self):
        """ Printing """
        if self.__size == 0:
            print("")
            return
        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """Printing squares defines """
        if self.size == 0:
            return ""
        else:
            s = ""
            for _ in range(self.position[1]):
                s += '\n'
            for _ in range(self.size):
                s += ' ' * self.position[0]
                s += '#' * self.size + '\n'
            return s[:-1]
