from tkinter import BOTH

from point import Point


class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def draw(self, canvas, color):
        canvas.create_line(
            self.point1.x,
            self.point1.y,
            self.point2.x,
            self.point2.y,
            fill=color,
            width=2,
        )
        canvas.pack(fill=BOTH, expand=1)
