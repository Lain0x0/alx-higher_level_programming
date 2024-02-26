#!/usr/bin/python3
""" method for square class. """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class Square that inherist from Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        """ Constructor """
        super().__init__(size, size, x, y, id)
        self.size = size
