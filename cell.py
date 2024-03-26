from graphics import Line, Point, Window


class Cell:
    def __init__(self, x1, y1, x2, y2, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self._win = win

    def draw(self):
        if self.has_left_wall:
            point1 = Point(self._x1, self._y1)
            point2 = Point(self._x1, self._y2)
            line = Line(point1, point2)
            self._win.draw_line(line, "blue")

        if self.has_top_wall:
            point1 = Point(self._x1, self._y1)
            point2 = Point(self._x2, self._y1)
            line = Line(point1, point2)
            self._win.draw_line(line, "blue")

        if self.has_right_wall:
            point1 = Point(self._x2, self._y1)
            point2 = Point(self._x2, self._y2)
            line = Line(point1, point2)
            self._win.draw_line(line, "blue")

        if self.has_bottom_wall:
            point1 = Point(self._x1, self._y2)
            point2 = Point(self._x2, self._y2)
            line = Line(point1, point2)
            self._win.draw_line(line, "blue")
