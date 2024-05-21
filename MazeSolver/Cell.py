from MazeSolver.Line import Line
from MazeSolver.Point import Point
from MazeSolver.Window import Window
from typing import Optional


class Cell:

    def __init__(self, window: Window) -> None:

        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._win = window

    def draw(
        self,
        x1: int,
        y1: int,
        x2: int,
        y2: int,
        fill_color: Optional[str] = "black",
    ) -> None:
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line, fill_color)
        else:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line, "white")
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line, fill_color)
        else:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line, "white")
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line, fill_color)
        else:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line, "white")
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line, fill_color)
        else:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line, "white")

    def draw_move(self, to_cell: "Cell", undo: bool = False) -> None:
        half_length_1 = abs(self._x2 - self._x1) // 2
        x_center_1 = self._x1 + half_length_1
        y_center_1 = self._y1 + half_length_1

        half_length_2 = abs(to_cell._x2 - to_cell._x1) // 2
        x_center_2 = to_cell._x1 + half_length_2
        y_center_2 = to_cell._y1 + half_length_2

        line = Line(Point(x_center_1, y_center_1), Point(x_center_2, y_center_2))

        fill_color = "red" if undo else "gray"

        self._win.draw_line(line, fill_color)
