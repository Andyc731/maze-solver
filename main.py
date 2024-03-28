from cell import Cell
from graphics import Line, Point, Window
from maze import Maze


def main():
    win = Window(800, 600)
    maze = Maze(0, 0, 10, 10, 10, 10, win)
    maze.solve()
    win.wait_for_close()


main()
