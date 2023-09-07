#!/usr/bin/python3

""" matrix multiplication using  NumPy."""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """returns the product of (multiplying) 2 matrices.

    Args:
        m_a (a list of lists of (ints/floats) ): 1st matrix.
        m_b (a list of lists of (ints/floats) ): 2nd matrix.
    """

    return (np.matmul(m_a, m_b))
