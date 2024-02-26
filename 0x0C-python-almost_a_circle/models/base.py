#!/usr/bin/python3
""" Module for base class """


class Base:
    """ Definning base as OOP """

    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor"""
        if (id is None):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
