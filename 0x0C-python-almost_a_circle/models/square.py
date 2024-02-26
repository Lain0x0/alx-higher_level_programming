#!/usr/bin/python3
""" Method for square class ."""

from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class square that inherit from Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        """ Constructor """
        super().__init__(size, size, x, y, id)
        self.size = size

        """ Return printable str """
    def __str__(self):
        return ("[{}] ({}) {:d}/{:d} - {:d}".format(
            self.__class__.__name__, self.id, self.x,
            self.y, self.size))

    """ Size getter and setter """
    @property
    def size(self):
        return (self.width)

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ method that assigns an argument to each att """
        if (args):
            for argmts in range(len(args)):
                if (argmts == 0):
                    self.id = args[argmts]
                if (argmts == 1):
                    self.size = args[argmts]
                if (argmts == 2):
                    self.x = args[argmts]
                if (argmts == 3):
                    self.y = args[argmts]

        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Returns dict"""
        return ({'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y})
