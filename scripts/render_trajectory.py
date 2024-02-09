import sys

sys.path.append("../")

from raytracer.canvas import Canvas
from raytracer.color import Color
from raytracer.primitives import Point, Vector


def compute_trajectory(
    position: Point, velocity: Vector, gravity: Vector, wind: Vector
):
    trajectory = []

    while position.y >= 0:
        trajectory.append(position)
        position, velocity = tick(position, velocity, gravity, wind)

    return trajectory


def tick(position: Point, velocity: Vector, gravity: Vector, wind: Vector):
    position = position + velocity
    velocity = velocity + gravity + wind

    return position, velocity


if __name__ == "__main__":
    canvas = Canvas(100, 100)

    position = Point(0, 1, 0)
    velocity = Vector(1, 1, 0)
    gravity = Vector(0, -0.02, 0)
    wind = Vector(-0.001, 0, 0)

    trajectory = compute_trajectory(position, velocity, gravity, wind)

    for point in trajectory:
        x = int(point.x)
        y = canvas.height - int(point.y)

        if 0 <= x < canvas.width and 0 <= y < canvas.height:
            canvas.write_pixel(x, y, Color(0, 1, 0))

    canvas.save("../renders/trajectory.ppm")
