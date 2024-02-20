#!/usr/bin/python3
""" Defines save_to_json function """


import json


def save_to_json_file(my_obj, filename):
    """ write a function that write an obj to a txt """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
