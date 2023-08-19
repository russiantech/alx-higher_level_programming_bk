#!/usr/bin/python3
# computes the square val of * int of a matrix using map
def square_matrix_map(matrix=[]):
    return (list(map(lambda x: list(map(lambda y: y**2, x)), matrix)))
