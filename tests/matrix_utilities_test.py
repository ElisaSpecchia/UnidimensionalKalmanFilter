import random
import numpy as np
import matrix_utilities as utilities


def test_is_symmetric():
    symmetric = np.zeros((5, 5))
    for i in range(5):
        for j in range(i, 5):
            symmetric[i, j] = random.uniform(0, 100)
            symmetric[j, i] = symmetric[i, j]

    assert utilities.is_symmetric(symmetric)


def test_is_not_symmetric():
    matrix = np.array([[0, 1], [5, 1]])

    assert utilities.is_symmetric(matrix) is False

