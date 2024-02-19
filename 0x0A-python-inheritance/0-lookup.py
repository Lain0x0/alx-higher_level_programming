#!/usr/bin/python3
""" Module for lookup """


def lookup(obj):
    """ lookup obj att and methode
    Args:
        obj : the object to list

    Returns:
        list: the list of att
    """
    return dir(obj)
