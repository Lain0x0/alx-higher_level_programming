#!/usr/bin/python3
""" Defines append_write function """


def append_write(filename="", text=""):
    """ function that appends a str at the end """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
