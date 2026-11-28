x_divided(matrix, div):
    """Divide all elements of a matrix by div."""

    if not isinstance(matrix, list) or not matrix:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

        for value in row:
            if type(value) not in (int, float):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if type(div) not in (int, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(value / div, 2) for value in row] for row in matrix]

