from graphics import Window
from line import Line
from point import Point


def main():
    win = Window(800, 600)
    point1 = Point(20, 40)
    point2 = Point(50, 20)
    line = Line(point1, point2)
    win.draw_line(line, "blue")
    win.wait_for_close()


main()
