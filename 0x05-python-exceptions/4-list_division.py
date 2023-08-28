#!/usr/bin/python3
"""
    Divide 2 lists element by element.

    Args:
        my_list_1 (list): 1st list[].
        my_list_2 (list): 2nd list[].
        list_length (int): num of elements to divide.

    Returns:
         new list of length list_length having * the divisions.
"""


def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(0, list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            div = 0
        except ZeroDivisionError:
            print("division by 0")
            div = 0
        except IndexError:
            print("out of range")
            div = 0
        finally:
            new_list.append(div)
    return (new_list)
