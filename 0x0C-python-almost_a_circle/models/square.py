#!/usr/bin/python3
""" Module for square class . """

from models.rectangle import Rectangle


class Square(Rectangle):
    """ square class. """

    def __init__(self, size, x=0, y=0, id=None):
        """ Return str info of square """
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}")
