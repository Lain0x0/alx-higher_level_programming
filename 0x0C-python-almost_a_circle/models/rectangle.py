#!/usr/bin/python3
""" Module for Rectangle class. """
from models.base import Base


class Rectangle(Base):
    """ Rectangle class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializes instances """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ rectangle width """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter """
        if (type(value) is not int):
            raise TypeError("width must be an integer")
        if (value <= 0):
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Rectangle height """
        return (self.__height)

    @height.setter
    def height(self, value):
        """ height setter """
        if (type(value) is not int):
            raise TypeError("height must be an integer")
        if (value <= 0):
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ x of Rectangle"""
        return (self.__x)

    @x.setter
    def x(self, value):
        """ x """
        if (type(value) is not int):
            raise TypeError("x must be an integer")
        if (value < 0):
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ y of Rectangler """
        return (self.__y)

    @y.setter
    def y(self, value):
        """ y """
        if (type(value) is not int):
            raise TypeError("y must be an integer")
        if (value < 0):
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Rectangle area """
        return (self.width * self.height)

    def display(self):
        """ displays a Rectangle """
        rectangle = self.y * "\n"
        for i in range(self.height):
            rectangle += (" " * self.x)
            rectangle += ("#" * self.width) + "\n"

        print(rectangle, end='')

    def __str__(self):
        """ str representation of rectangle object """
        s_rectangle = "[Rectangle] "
        s_id = "({}) ".format(self.id)
        s_xy = "{}/{} - ".format(self.x, self.y)
        s_wh = "{}/{}".format(self.width, self.height)

        return (s_rectangle + s_id + s_xy + s_wh)

    def update(self, *args, **kwargs):
        """ update method """
        if (args is not None and len(args) is not 0):
            list_atr = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, list_atr[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ method that returs a dictionary with properties """
        list_atr = ['id', 'width', 'height', 'x', 'y']
        dict_res = {}

        for key in list_atr:
            dict_res[key] = getattr(self, key)

        return (dict_res)
