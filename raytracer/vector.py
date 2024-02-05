from tuple import Tuple


class Vector(Tuple):
    def __init__(self, x: float, y: float, z: float):
        super().__init__(x, y, z, 0)
