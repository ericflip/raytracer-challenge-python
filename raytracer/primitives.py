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


if __name__ == "__main__":
    a = Vector(1, 1, 1)
    b = Vector(2, 2, 2)
    c = Point(0, 0, 0)

    print(a + b)
    print(c + a)

    print(c - a)
    print(a / 3)
    print(a - b)
