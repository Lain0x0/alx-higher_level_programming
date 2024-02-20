#!/usr/bin/python3
""" Defines save_to_json function """


import json


def save_to_json_file(my_obj, filename):
    """ write a script that add all arguments """
    with open(filename, 'w', encoding="utf-8")as f:
        json.dumps(my_obj, f)
