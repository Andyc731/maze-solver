from cell import Cell
from graphics import Line, Point, Window


def main():
    win = Window(800, 600)
    cell = Cell(20, 20, 40, 40, win)
    cell.draw()
    win.wait_for_close()


main()
