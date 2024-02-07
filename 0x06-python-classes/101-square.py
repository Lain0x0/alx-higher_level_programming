#!/usr/bin/python3

"""Module of a square"""


class Square:
    """ Defines a square """

    def __init__(self, size=0, position=(0, 0)):
        """ Initialize square values """
        self.size = size
        self.position = position

    def area(self):
        """ Calcul the area of square """
        return (self.__size * self.__size)

    @property
    def size(self):
        """Get for square"""
        return self.__size

    @size.setter
    def size(self, value):
        """ Square attribute size """
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """ Get the square position """
        return self.__position

    @position.setter
    def position(self, value):
        """ Square attribute position """
        if len(value) is not 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if (type(value[0]) is not int or value[0] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (type(value[1]) is not int or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """ Printing """
        print(self.__str__())

    def __str__(self):
        """Printing squares defines """
        if self.size == 0:
            return
        else:
            str = '\n' * self.__position[1]
        for i in range(self.__size):
            str += ' ' * self.position[0]
            str += '#' * self.__size + '\n'
        return str[:-1]
