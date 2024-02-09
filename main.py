from raytracer.canvas import Canvas
from raytracer.color import Color


if __name__ == "__main__":
    canvas = Canvas(100, 100)

    canvas.write_pixel(0, 0, Color(1, 0, 0))

    canvas.save("./1.ppm")

    # canvas.
