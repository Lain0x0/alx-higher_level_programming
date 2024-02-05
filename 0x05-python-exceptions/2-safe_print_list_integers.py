#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    n, c = 0, 0
    while (n < x):
        try:
            print("{:d}".format(my_list[n]), end='')
            c += 1
        except (ValueError, TypeError):
            pass
        n += 1
    print()
    return (c)
