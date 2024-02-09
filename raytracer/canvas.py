from .color import Color


class Canvas:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

        # initialize canvas with black at every pixel
        self.canvas = [[Color(0, 0, 0) for i in range(width)] for j in range(height)]

    def pixel_at(self, x: int, y: int):
        return self.canvas[y][x]

    def write_pixel(self, x: int, y: int, color: Color):
        self.canvas[y][x] = color

    def to_ppm(self):
        ppm = f"""P3
{self.width} {self.height}
255"""

        for row in self.canvas:
            for color in row:
                ppm += f"\n{color.r} {color.g} {color.b}"

        return ppm

    def save(self, path: str):
        ppm = self.to_ppm()

        with open(path, "w") as f:
            f.write(ppm)


if __name__ == "__main__":
    canvas = Canvas(10, 20)
    red = Color(1, 0, 0)

    canvas.write_pixel(2, 3, red)
    assert canvas.pixel_at(2, 3) == red
