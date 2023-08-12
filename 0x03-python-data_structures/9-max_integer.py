#!/usr/bin/python3
# which is highest int in list ?

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return (None)

    big = my_list[0]
    for x in range(len(my_list)):
        if my_list[x] > big:
            big = my_list[x]

    return (big)
