#!/usr/bin/python3
""" magic class mathcing a bytecode """

import math


class MagicClass:
    """ Define a circle """

    def __init__(self, radius=0):
        """ Initialize a Magic Class.
        Arg:
            radius(float or an int) : radius of the new magic class.
        """
        self.__radius = 0
        if (type(radius) is not int and type(radius) is not float):
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """ Return area of the magic class """
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """ Return the circumference of magic class """
        return (2 * math.pi * self.__radius)
