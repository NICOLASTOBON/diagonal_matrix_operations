#!/usr/bin/python3
import random
import numpy as np


def sum_diagonal(matrix):

    result = 0
    number = 0

    for i in range(len(matrix)):
        result += matrix[i][i] + matrix[i][-i-1]

        # check the number where the diagonals are intercepted
        if matrix[i][i] == matrix[i][-i-1]:
            number = matrix[i][i]
    print()
    print(f"Number of interception: {number}")

    return result


if __name__ == "__main__":
    """ to create matrix """
    size_of_matrix = int(input("Print size of matrix: "))

    matrix = np.random.randint(100, size=(size_of_matrix, size_of_matrix))
    print(matrix)

    # function sum diagonals matrix
    result = sum_diagonal(matrix)

    print(f"The sum of diagonals is: {result}")
