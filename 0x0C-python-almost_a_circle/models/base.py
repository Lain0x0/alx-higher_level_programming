#!/usr/bin/python3
""" Module for Base class. """

import json
import csv
import turtle


class Base:
    """ Defines base as OOP """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Constructor """
        if (id is not None):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON serialization of a list of dict """
        if (list_dictionaries is None or list_dictionaries == []):
            return ("[]")
        return (json.dumps(list_dictionaries))
