#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    n_list = []

    for n in range(list_length):
        try:
            n_list.append(my_list_1[n] / my_list_2[n])
        except ZeroDivisionError:
            n_list.append(0)
            print('division by 0')
            continue
        except IndexError:
            n_list.append(0)
            print('out of range')
            continue
        except TypeError:
            n_list.append(0)
            print('wrogn type')
            continue
        finally:
            pass

    return (n_list)
