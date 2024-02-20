#!/usr/bin/python3
""" Represents read_file function """


def read_file(filename=""):
    """ read file with utf-8 """
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
