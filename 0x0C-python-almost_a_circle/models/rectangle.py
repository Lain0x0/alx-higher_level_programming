#!/usr/bin/python3
""" Definition of the Rectangle class """

from models.base import Base


class Rectangle(Base):
    """ Class representing a rectangle, inherits from Base """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializes a Rectangle instance """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    """ WIDTH GETTER, SETTER """
    @property
    def width(self):
        """ Getter method for width """
        return self.__width

    @width.setter
    def width(self, width):
        """ Setter method for width """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    """ HEIGHT GETTER, SETTER """
    @property
    def height(self):
        """ Getter method for height """
        return self.__height

    @height.setter
    def height(self, height):
        """ Setter method for height """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    """ X GETTER, SETTER """
    @property
    def x(self):
        """ Getter method for x """
        return self.__x

    @x.setter
    def x(self, x):
        """ Setter method for x """
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    """ Y GETTER, SETTER """
    @property
    def y(self):
        """ Getter method for y """
        return self.__y

    @y.setter
    def y(self, y):
        """ Setter method for y """
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    """ Public methods """

    def area(self):
        """ Returns the area of the rectangle """
        return self.__width * self.__height

    def display(self):
        """ Displays the rectangle using '#' character """
        for i in range(self.__y):
            print("")
        for j in range(self.__height):
            print(" " * self.__x + '#' * self.__width)

    def update(self, *args, **kwargs):
        """ Updates the attributes of the rectangle """
        if args:
            attrs = ['id', 'width', 'height', 'x', 'y']
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    """ Returns a string representation of the rectangle """
    def __str__(self):
        """ String representation of the rectangle """
        return f"[{self.__class__.__name__}]({self.id}) {self.__x}/{self.__y}
    - {self.__width}/{self.__height}"

    def to_dictionary(self):
        """ Returns the dictionary representation of the rectangle """
        return {'id': self.id, 'x': self.x, 'y': self.y,
                'width': self.width, 'height': self.height}
