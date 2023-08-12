#!/usr/bin/python3
import sys
# printing list of args & number

if __name__ == "__main__":
    count = len(sys.argv) - 1
    if count == 1:
        #print("1 argument:")
        #print("1: {}".format(sys.argv[1]))
        print("1 argument:\n1: {}".format(sys.argv[1]))
    elif count == 0:
        print("0 arguments.")
    else:
        print("{} arguments:".format(count))

        for i in range(count):
            print("{}: {}".format(i + 1, sys.argv[i + 1]))
