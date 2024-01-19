#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    n_list = []
    if (my_list):
        for number in my_list:
            n_list.append(False if num % 2 else True)
        return (n_list)
