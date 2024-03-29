#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    i_int = True
    try:
        print("{:d}".format(value))
    except Exception as error:
        print("Exception:", error, file=sys.stderr)
        i_int = False
    return (i_int)
