#!/usr/bin/python3
""" Represents write_file function """


def write_file(filename="", text=""):
    """ write function that write text (utf-8) """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
