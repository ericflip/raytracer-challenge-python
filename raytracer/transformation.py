import numpy as np

from .matrix import Matrix4x4
from .primitives import Point


class Transformation(Matrix4x4):
    def __init__(self, matrix=None):
        if matrix is None:
            # set matrix to identity
            matrix = np.eye(4, 4)

        # make sure bottom right value is 1
        assert (
            matrix[3, 3] == 1
        ), "bottom right value of transformation matrix has to equal 1.0"

        # upper and lower triangular values are 0
        lower_i, lower_j = np.tril_indices(4, -1, 3)  # excludes main diagonal
        assert np.all(
            matrix[lower_i, lower_j] == 0
        ), "all lower diagonal values of transformation matrix has to equal 0.0"

        upper_i, upper_j = np.triu_indices(4, 1, 3)  # excludes main diagonal
        assert np.all(
            matrix[upper_i, upper_j] == 0
        ), "all upper diagonal values of transformation matrix has to equal 0.0"

        # a = np.tril_indices()

        super().__init__(matrix)

    def translate(self, x: float, y: float, z: float):
        translation_matrix = np.array(
            [[1.0, 0, 0, x], [0, 1.0, 0, y], [0, 0, 1.0, z], [0, 0, 0, 1.0]]
        )

        result = self.matrix @ translation_matrix

        return Transformation(result)


if __name__ == "__main__":
    transformation = Transformation()

    translate = Transformation().translate(5, -3, 2)
    p = Point(-3, 4, 5)

    assert translate @ p == Point(2, 1, 7)
