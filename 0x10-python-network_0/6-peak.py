#!/usr/bin/python3
""" Write a function that finds a peak in a list of unsorted integers."""

def find_peak(list_of_integers):
    """A function that finds a peak in a list of unsorted integers"""
    if (not list_of_integers):
        return (None)

    left = 0
    right = len(list_of_integers) - 1

    while (left < right):
        m = (left + right) // 2
        if (list_of_integers[m] > list_of_integers[m + 1]):
            right = m
        else:
            left = m + 1
    return (list_of_integers[left])

