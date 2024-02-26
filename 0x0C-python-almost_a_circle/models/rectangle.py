#!/usr/bin/python3
""" Module for rectangle class. """
from models.base import Base


class Rectangle(Base):
    """ Rectangle class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Constructor """
        super().__init__(id)
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

    def validate_integer(self, name, value, eq=True):
        """ Method for validation value """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if (eq and value < 0):
            raise ValueError("{} must be >= 0".format(name))
        elif not eq and value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def area(self):
        """ Calculate the area of rectangle """
        return self.width * self.height

    def display(self):
        """ Printing string '#' in rectangle """
        s = ('\n' * self.y
             + (' ' * self.x + '#' * self.width + '\n') * self.height)
        print(s, end='')

    def __str__(self):
        """ str define the rectangle object """
        return f"[Rectangle]({self.id}) {self.x}/{self.y}
        - {self.width}/{self.height}"
