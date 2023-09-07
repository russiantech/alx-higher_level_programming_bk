#!/usr/bin/python3
"""creates/defines matrix division function."""


def matrix_divided(matrix, div):

    """
    Divide * elements of this matrix.

    Args:
        matrix (list): list of lists of (ints/floats).
        div (int/float): divisor.
    Raises:
        TypeError: when matrix has other elements than number(s)
        TypeError: when matrix row sizes varries.
        TypeError: when matrix division(div) is not an int/float.
        ZeroDivisionError: If div is 0.
    Returns:
        New matrix having the differences/result of the matrix division(div).
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
