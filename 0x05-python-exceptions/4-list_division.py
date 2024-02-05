#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []

    for k in range(list_length):
        try:
            new_list.append(my_list_1[k] / my_list_2[k])
        except ZeroDivisionError:
            new_list.append(0)
            print('division by 0')
            continue
        except IndexError:
            new_list.append(0)
            print('out of range')
            continue
        except TypeError:
            new_list.append(0)
            print('wrogn type')
            continue
        finally:
            pass

    return (new_list)
