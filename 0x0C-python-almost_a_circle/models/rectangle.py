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
        self.__width = value

    @property
    def height(self):
        """ height of rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        """ x of rectangle """
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        """ y of rectangle """
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value

    def valid_int(self, name, value, eax=True):
        """ Method for validating the value """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if eax and value < 0:
            raise ValueError("{} must be >= 0".format(name))
        elif eax and value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def area(self):
        """ Calculate the area of rectangle """
        return self.width * self.height

    def display(self):
        """ Print string '#' in rectangle """
        s = '\n' * self.y + (' ' * self.x + "#" * self.width + '\n')
        * self.height
        print(s, end='')

    def __str__(self):
        """ Return string representation of Rectangle """
        return "[{}] ({}) {:d}/{:d} - {:d}/{:d}".format(
            self.__class__.__name__, self.id, self.x,
            self.y, self.width, self.height)

    def display(self):
        """ Print string '#' in rectangle class """
        for _ in range(self.y):
            print("")
        for _ in range(self.height):
            print(self.x * " " + '#' * self.width)

    def update(self, *args, **kwargs):
        """ Method to assign
        arguments to each attribute """
        if (args):
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.width = arg
                elif i == 2:
                    self.height = arg
                elif i == 3:
                    self.x = arg
                elif i == 4:
                    self.y = arg
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Return the dictionary
        representation of a Rectangle """
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
