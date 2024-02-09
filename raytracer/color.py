from .tuple import Tuple
from typing import Union
from .utils import clamp


class Color(Tuple):
    def __init__(self, r: float, g: float, b: float, _: float = 0):
        """
        Params:
            - r, g, b: floats between 0 and 1
        """
        super().__init__(r, g, b, 0)

    @property
    def r(self):
        return clamp(int(self.x * 255.999), 0, 255)

    @property
    def g(self):
        return clamp(int(self.y * 255.999), 0, 255)

    @property
    def b(self):
        return clamp(int(self.z * 255.999), 0, 255)

    def __mul__(self, other: Union[int, float, "Color"]):
        if isinstance(other, int) or isinstance(float):
            return super().__mul__(other)
        if isinstance(other, Color):
            return Color(self.r * other.r, self.g * other.g, self.b * other.b)

    def __repr__(self):
        return f"({self.r}, {self.g}, {self.b})"


if __name__ == "__main__":
    a = Color(1, 0.2, 0.4)
    b = Color(0.9, 1, 0.1)

    assert a * b == Color(0.9, 0.2, 0.04)
