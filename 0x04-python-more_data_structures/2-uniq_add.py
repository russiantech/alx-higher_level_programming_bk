#!/usr/bin/python3
# adds * unique int in a list(only once for each int)
def uniq_add(my_list=[]):
    uniq_list = set(my_list)
    num = 0

    for i in uniq_list:
        num += i

    return (num)
