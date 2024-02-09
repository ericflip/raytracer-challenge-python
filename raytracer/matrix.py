from abc import ABC
from typing import Union
from .primitives import Tuple


def identity(dim: int = 4):
    matrix = [[1 if i == j else 0 for j in range(dim)] for i in range(dim)]

    if dim == 4:
        return Matrix4x4(matrix)

    if dim == 3:
        return Matrix3x3(matrix)

    if dim == 2:
        return Matrix2x2(matrix)

    raise ValueError(f"{dim} is an invalid dimension for an identity matrix")


class Matrix(ABC):
    def __init__(self, matrix: list[list[float]]):
        self.matrix = matrix

    @property
    def rows(self):
        return len(self.matrix)

    @property
    def cols(self):
        return len(self.matrix[0])

    def _validate_index(self, index):
        if len(index) != 2:
            raise TypeError("Index must be a tuple of two integers")

        r, c = index
        valid = 0 <= r < self.rows and 0 <= c < self.cols

        if not valid:
            raise IndexError("Index out of range")

    def __getitem__(self, index):
        self._validate_index(index)

        r, c = index
        return self.matrix[r][c]

    def __setitem__(self, index, value):
        self._validate_index(index)

        r, c = index
        self.matrix[r][c] = value

    def __matmul__(self, other: "Matrix"):
        assert self.cols == other.rows

        product = [[0 for j in range(other.cols)] for i in range(self.rows)]

        for i in range(self.rows):
            for j in range(other.cols):
                val = 0
                for k in range(self.cols):
                    val += self[i, k] * other[k, j]

                product[i][j] = val

        return self.__class__(product)

    def __eq__(self, other: "Matrix"):
        same_dims = self.rows == other.rows and self.cols == other.cols

        if not same_dims:
            return False

        for i in range(self.rows):
            for j in range(self.cols):
                if self[i, j] != other[i, j]:
                    return False

        return True

    def __repr__(self):
        return "\n".join(
            ["\t".join([str(cell) for cell in row]) for row in self.matrix]
        )


class Matrix4x4(Matrix):
    def __init__(self, matrix):
        super().__init__(matrix)

        assert (
            self.rows == 4 and self.cols == 4
        ), "Rows and Cols have to be 4 for a 4x4 matrix"

    def __matmul__(self, other: Union["Matrix4x4", Tuple]):
        pass


class Matrix3x3(Matrix):
    def __init__(self, matrix):
        super().__init__(matrix)

        assert (
            self.rows == 3 and self.cols == 3
        ), "Rows and Cols have to be 3 for a 3x3 matrix"


class Matrix2x2(Matrix):
    def __init__(self, matrix):
        super().__init__(matrix)

        assert (
            self.rows == 2 and self.cols == 2
        ), "Rows and Cols have to be 2 for a 2x2 matrix"


if __name__ == "__main__":
    a = Matrix2x2([[1, 0], [0, 1]])
    b = Matrix2x2([[1, 0], [0, 1]])

    assert a == b

    print(a[0, 0])
    a[0, 0] = 10
    print(a[0, 0])

    assert a != b

    c = Matrix2x2([[1, 2], [3, 4]])
    d = Matrix2x2([[5, 6], [7, 8]])

    assert c @ d == Matrix2x2([[19, 22], [43, 50]])

    print(Matrix2x2([[10, 0], [0, 1]]))
