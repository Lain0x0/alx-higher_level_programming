#!/usr/bin/python3
""" Defines save_to_jsonn function """


import json


def save_to_json_file(my_obj, filename):
    """ write a script that add all arguments """
    with open(filename, "w", encoding="utf-8")as f:
        return (json.dump(my_obj, f))
