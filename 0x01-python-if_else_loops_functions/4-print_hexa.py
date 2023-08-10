#!/usr/bin/python3
# check question for example

"""Write a program that prints all numbers from 0 to 98 \
        in decimal and in hexadecimal (as in the following example)"""
for number in range(0, 99):
    print("{} = {}".format(number, hex(number)))
