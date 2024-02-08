from tuple import Tuple
from typing import Union


class Color(Tuple):
    def __init__(self, r: float, g: float, b: float, _: float = 0):
        super().__init__(r, g, b, 0)

    @property
    def r(self):
        return self.x

    @property
    def g(self):
        return self.y

    @property
    def b(self):
        return self.z

    def __mul__(self, other: Union[int, float, "Color"]):
        if isinstance(other, int) or isinstance(float):
            return super().__mul__(other)
        if isinstance(other, Color):
            return Color(self.r * other.r, self.g * other.g, self.b * other.b)
