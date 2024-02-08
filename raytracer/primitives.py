from tuple import Tuple
from typing import Union


class Point(Tuple):
    def __init__(self, x: float, y: float, z: float, w: float = 1):
        assert w == 1, "`w` has to be 1 for `Point`"

        super().__init__(x, y, z, w)

    def __add__(self, other: "Vector"):
        if isinstance(other, Point):
            raise ValueError("Can't add `Point` to `Point`")
        elif isinstance(other, Vector):
            return super().__add__(other)

    def __sub__(self, other: "Vector"):
        if isinstance(other, Vector):
            return super().__sub__(other)
        elif isinstance(other, Point):
            raise ValueError("Can't substract `Point` from `Point`")

    def __mul__(self, scalar):
        raise ValueError("Can't multiply `Point` by a scalar")

    def __truediv__(self, scalar: float):
        raise ValueError("Can't divide `Point` by a scalar")


class Vector(Tuple):
    def __init__(self, x: float, y: float, z: float, w: float = 0):
        assert w == 0, "`w` has to be 0 for `Vector`"

        super().__init__(x, y, z, w)

    def __add__(self, other: Union["Vector", Point]):
        if isinstance(other, Vector):
            return super().__add__(other)
        elif isinstance(other, Point):
            return other.__add__(self)

    def __sub__(self, other: Union["Vector", Point]):
        if isinstance(other, Vector):
            return super().__sub__(other)
        elif isinstance(other, Point):
            raise ValueError("Can't subtract `Point` from `Vector`")

    def mag(self) -> float:
        return (self.x**2 + self.y**2 + self.z**2 + self.w**2) ** 0.5

    def norm(self) -> "Vector":
        return self / self.mag()

    def __matmul__(self, other: "Vector") -> float:
        return self.x * other.x + self.y * other.y + self.z * other.z + self.w * other.w

    def dot(self, other: "Vector"):
        return self @ other

    def cross(self, other: "Vector"):
        return Vector(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x,
        )


if __name__ == "__main__":
    a = Vector(1, 1, 1)
    b = Vector(2, 2, 2)
    c = Point(0, 0, 0)

    print(a + b)
    print(c + a)

    print(c - a)
    print(a / 3)
    print(a - b)

    d = Vector(1, 2, 3)

    assert d.mag() == 14**0.5

    e = Vector(4, 0, 0)

    assert e.norm() == Vector(1, 0, 0)

    a = Vector(1, 2, 3)
    b = Vector(2, 3, 4)
    assert a.dot(b) == 20

    a = Vector(1, 0, 0)
    b = Vector(0, 1, 0)

    assert a.cross(b) == Vector(0, 0, 1)
