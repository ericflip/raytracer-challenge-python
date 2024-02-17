from typing import Union
from .primitives import Tuple, Vector
import numpy as np


def identity(dim: int = 4):
    matrix = np.eye(dim, dim)

    if dim == 4:
        return Matrix4x4(matrix)

    if dim == 3:
        return Matrix3x3(matrix)

    if dim == 2:
        return Matrix2x2(matrix)

    raise ValueError(f"{dim} is an invalid dimension for an identity matrix")


class Matrix:
    def __init__(self, matrix: list[list[float]]):
        self.matrix = np.array(matrix)

        assert len(self.matrix.shape) == 2, "Matrix is a 2d array"

    @property
    def rows(self):
        return self.matrix.shape[0]

    @property
    def cols(self):
        return self.matrix.shape[1]

    @property
    def inverse(self):
        return self.__class__(np.linalg.inv(self.matrix))

    @property
    def T(self):
        return self.__class__(self.matrix.T)

    def __getitem__(self, index):
        return self.matrix[index]

    def __setitem__(self, index, value):
        self.matrix[index] = value

    def __matmul__(self, other: "Matrix"):
        product = self.matrix @ other.matrix

        return self.__class__(product)

    def __eq__(self, other: "Matrix"):
        return np.allclose(self.matrix, other.matrix, rtol=1e-05, atol=1e-05)

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
        if isinstance(other, Matrix):
            return super().__matmul__(other)
        if isinstance(other, Tuple):
            other_matrix = np.array([[other.x], [other.y], [other.z], [other.w]])
            product = self.matrix @ other_matrix
            product = product.flatten()

            return other.__class__(product[0], product[1], product[2], product[3])


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

    e = Vector(1, 1, 1)
    f = Matrix4x4([[1, 1, 1, 1], [2, 3, 4, 5], [1, 1, 1, 1], [0, 0, 0, 0]])

    assert f @ e == Vector(3, 9, 3, 0)

    #     Scenario: Calculating the inverse of another matrix Given the following 4x4 matrix A:
    # | 8|-5| 9| 2| |7|5|6|1| |-6| 0| 9| 6| |-3| 0|-9|-4|
    # Then inverse(A) is the following 4x4 matrix:
    # | -0.15385 | -0.15385 | -0.28205 | -0.53846 | | -0.07692 | 0.12308 | 0.02564 | 0.03077 | | 0.35897 | 0.35897 | 0.43590 | 0.92308 | | -0.69231 | -0.69231 | -0.76923 | -1.92308 |
    # Scenario: Calculating the inverse of a third matrix Given the following 4x4 matrix A:
    # |9|3|0|9| | -5 | -2 | -6 | -3 | |-4| 9| 6| 4| |-7| 6| 6| 2|
    # Then inverse(A) is the following 4x4 matrix:
    # | -0.04074 | -0.07778 | 0.14444 | -0.22222 | | -0.07778 | 0.03333 | 0.36667 | -0.33333 | | -0.02901 | -0.14630 | -0.10926 | 0.12963 | | 0.17778 | 0.06667 | -0.26667 | 0.33333 |

    # implement the test cases above
    a = Matrix4x4([[8, -5, 9, 2], [7, 5, 6, 1], [-6, 0, 9, 6], [-3, 0, -9, -4]])
    b = Matrix4x4(
        [
            [-0.15385, -0.15385, -0.28205, -0.53846],
            [-0.07692, 0.12308, 0.02564, 0.03077],
            [0.35897, 0.35897, 0.43590, 0.92308],
            [-0.69231, -0.69231, -0.76923, -1.92308],
        ]
    )

    print(a.inverse)
    assert a.inverse == b

    c = Matrix4x4([[9, 3, 0, 9], [-5, -2, -6, -3], [-4, 9, 6, 4], [-7, 6, 6, 2]])
    d = Matrix4x4(
        [
            [-0.04074, -0.07778, 0.14444, -0.22222],
            [-0.07778, 0.03333, 0.36667, -0.33333],
            [-0.02901, -0.14630, -0.10926, 0.12963],
            [0.17778, 0.06667, -0.26667, 0.33333],
        ]
    )
    assert c.inverse == d

    assert c.inverse @ c == identity(4)
