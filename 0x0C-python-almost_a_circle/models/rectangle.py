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
        return (self.__width)

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        """ height of rectangle """
        return (self.__height)

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        """ x of rectangle """
        return (self.__x)

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        """ y of rectangle """
        return (self.__y)

    @y.setter
    def y(self, value):
        self.__y = value

    def valid_int(self, name, value, eax=True):
        """ Method for valid the value """
        if (type(value) is not int):
            raise TypeError("{} must be an integer".format(name))
        if (eax and value < 0):
            raise ValueError("{} must be >= 0".format(name))
        else:
            if (eax and value <= 0):
                raise ValueError("{} must be > 0".format(name))

    def area(self):
        """ Calcul the area of rectangle """
        return (self.width * self.height)

    def display(self):
        """ Printing string '#' in rectangle  """
        s = '\n' * self.y + \
                (' ' * self.x + "#" * self.width + '\n') * self.height
        print(s, end='')

    def __str__(self):
        """ It returns [Rectangle] (<id>) <x>/<y> - <width>/<height> """
        return ("[{}] ({}) {:d}/{:d} - {:d}/{:d}".format(
            self.__class__.__name__, self.id, self.__x,
            self.__y, self.__width, self.__height))

    def display(self):
        """ printing str "#" in rectangle class. """
        for i in range(self.__y):
            print("")
        for j in range(self.__height):
            print(self.__x * " " + '#' * self.__width)

    def update(self, *args, **kwargs):
        """ method to assigns an argument to each att """
        if (args):
            for arguments in range(len(args)):
                if (arguments == 0):
                    self.id = args[arguments]
                if (arguments == 1):
                    self.__width = args[arguments]
                if (arguments == 2):
                    self.__height = args[arguments]
                if (arguments == 3):
                    self.__x = args[arguments]
                if (arguments == 4):
                    self.__y = args[arguments]

        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary
        representation of a Rectangle."""
        return {
                'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y
                }
