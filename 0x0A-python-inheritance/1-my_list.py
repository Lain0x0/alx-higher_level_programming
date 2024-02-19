#!/usr/bin/python3
""" Module for my list """


class MyList(list):
    """ MyList class """

    def print_sorted(self):
        """ method for printing sorted list """
        print(sorted(self))
