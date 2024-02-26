#!/usr/bin/python3

""" Module for rectangle class. """

from models.base import Base


class Rectangle(Base):
    """ Rectangle class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Constructor """
        super().__init__(self, id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ width of rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        self.validate_integer("width", value)
        self.__width = value

    @property
    def height(self):
        """ height of rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        self.validate_integer("height", value)
        self.__height = value

    @property
    def x(self):
        """ x of rectangle """
        return self.__x

    @x.setter
    def x(self, value):
        self.validate_integer("x", value)
        self.__x = value

    @property
    def y(self):
        """ y of rectangle """
        return self.__y

    @y.setter
    def y(self, value):
        self.validate_integer("y", value)
        self.__y = value

    def validate_integer(self, name, value, min=0):
        """Method to validate input values."""
        if (type(value) is not int):
            raise TypeError("{} must be an integer".format(name))
        if (value < min):
            if (min == 1):
                raise ValueError("{} must be > 0".format(name))
            else:
                raise ValueError("{} must be >= 0".format(name))
