#!/usr/bin/python3
""" Defines load_from_json_file function """


import json


def load_from_json_file(filename):
    """ write function that create an obj from JSON file """
    with open(filename, "w", encoding="utf-8")as f:
        return (json.load(f))
