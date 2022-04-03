from math import pi, cos, sin
from circle import circle_midpoint


def piechart (xc, yc, r, data):
    data = [5, 15, 25, 30, 65]
   
    circle_points = circle_midpoint(xc, yc, r)

    sumData = sum(data)
    prevAngle = 0

    lines = []
    for d in data:
        angle = 2 * pi * d / sumData + prevAngle
        x = xc + r * cos(angle)
        y = yc + r * sin(angle)
        lines.append([xc, yc, x, y])
        prevAngle = angle

    return circle_points, lines
