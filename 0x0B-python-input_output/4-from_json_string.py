#!/usr/bin/python3
""" Defines from_json_string function """


import json


def from_json_string(my_str):
    """ Function that returns an obj represent by json str """
    return (json.loads(my_str))
