#!/usr/bin/python3
# return * multiples of 2 in my_list

def divisible_by_2(my_list=[]):
    multiples = []
    for x in range(len(my_list)):
        if my_list[x] % 2 == 0:
            multiples.append(True)
        else:
            multiples.append(False)

    return (multiples)
