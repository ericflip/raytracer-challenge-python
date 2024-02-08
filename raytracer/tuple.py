EPSILON = 0.00001


def equal(a, b):
    return abs(a - b) < EPSILON


class Tuple:
    def __init__(self, x, y, z, w):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    def __add__(self, other: "Tuple"):
        return self.__class__(
            self.x + other.x, self.y + other.y, self.z + other.z, self.w + other.w
        )

    def __sub__(self, other: "Tuple"):
        return self.__class__(
            self.x - other.x, self.y - other.y, self.z - other.z, self.w - other.w
        )

    def __mul__(self, scalar: float):
        return self.__class__(
            self.x * scalar, self.y * scalar, self.z * scalar, self.w * scalar
        )

    def __rmul__(self, scalar: float):
        return self * scalar

    def __truediv__(self, scalar: float):
        return self * (1 / scalar)

    def __eq__(self, other: "Tuple"):
        return (
            equal(self.x, other.x)
            and equal(self.y, other.y)
            and equal(self.z, other.z)
            and equal(self.w, other.w)
        )

    def __repr__(self):
        return f"<{self.x}, {self.y}, {self.z}, {self.w}>"


if __name__ == "__main__":
    a = Tuple(3, -2, 5, 1)
    b = Tuple(-2, 3, 1, 0)

    assert a + b == Tuple(1, 1, 6, 1)
