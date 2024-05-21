from MazeSolver.Cell import Cell
from MazeSolver.Window import Window
import random
from typing import List, Optional
import time


class Maze:
    def __init__(
        self,
        x1: int,
        y1: int,
        num_rows: int,
        num_cols: int,
        cell_size_x: int,
        cell_size_y: int,
        win: Optional[Window] = None,
        seed: Optional[int] = None,
        redraw_interval: Optional[int] = 0.05,
    ) -> None:
        self._cells: List[List[Cell]] = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        if seed:
            random.seed(seed)
        self._redraw_interval = redraw_interval

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _create_cells(self) -> None:

        for r in range(self._num_rows):
            col_cells = []
            for c in range(self._num_cols):
                cell = Cell(self._win)
                col_cells.append(cell)
            self._cells.append(col_cells)

        for r in range(self._num_rows):
            for c in range(self._num_cols):
                self._draw_cell(r, c)

    def _draw_cell(self, r: int, c: int) -> None:
        if self._win is None:
            return
        x1 = self._x1 + (c * self._cell_size_x)
        y1 = self._y1 + (r * self._cell_size_y)
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[r][c].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self) -> None:
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(self._redraw_interval)

    def _break_entrance_and_exit(self) -> None:
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_rows - 1][self._num_cols - 1].has_bottom_wall = False
        self._draw_cell(self._num_rows - 1, self._num_cols - 1)

    def _break_walls_r(self, r: int, c: int) -> None:
        self._cells[r][c].visited = True
        while True:
            next_index_list = []

            # Left Cell
            if c > 0 and not self._cells[r][c - 1].visited:
                next_index_list.append((r, c - 1))

            # Right Cell
            if c < self._num_cols - 1 and not self._cells[r][c + 1].visited:
                next_index_list.append((r, c + 1))

            # Top Cell
            if r > 0 and not self._cells[r - 1][c].visited:
                next_index_list.append((r - 1, c))

            # Bottom Cell
            if r < self._num_rows - 1 and not self._cells[r + 1][c].visited:
                next_index_list.append((r + 1, c))

            # No Cell then just break out
            if len(next_index_list) == 0:
                self._draw_cell(r, c)
                return

            # Pick next cell randomly
            next_index = next_index_list[random.randrange(len(next_index_list))]

            # Break walls between current cell and the next cell(s)
            # Left
            if next_index[1] == c - 1:
                self._cells[r][c].has_left_wall = False
                self._cells[r][c - 1].has_right_wall = False

            # Right
            if next_index[1] == c + 1:
                self._cells[r][c].has_right_wall = False
                self._cells[r][c + 1].has_left_wall = False

            # Top
            if next_index[0] == r - 1:
                self._cells[r][c].has_top_wall = False
                self._cells[r - 1][c].has_bottom_wall = False

            # Bottom
            if next_index[0] == r + 1:
                self._cells[r][c].has_bottom_wall = False
                self._cells[r + 1][c].has_top_wall = False

            self._break_walls_r(next_index[0], next_index[1])

    def _reset_cells_visited(self) -> None:
        for row in self._cells:
            for cell in row:
                cell.visited = False

    def solve(self) -> bool:
        return self._solve_r(0, 0)

    def _solve_r(self, r: int, c: int) -> bool:
        self._animate()

        self._cells[r][c].visited = True

        if r == self._num_rows - 1 and c == self._num_cols - 1:
            return True

        # Left Cell
        if (
            c > 0
            and not self._cells[r][c - 1].visited
            and not self._cells[r][c].has_left_wall
        ):
            self._cells[r][c].draw_move(self._cells[r][c - 1])
            if self._solve_r(r, c - 1):
                return True
            else:
                self._cells[r][c].draw_move(self._cells[r][c - 1], True)

        # Right Cell
        if (
            c < self._num_cols - 1
            and not self._cells[r][c + 1].visited
            and not self._cells[r][c].has_right_wall
        ):
            self._cells[r][c].draw_move(self._cells[r][c + 1])
            if self._solve_r(r, c + 1):
                return True
            else:
                self._cells[r][c].draw_move(self._cells[r][c + 1], True)

        # Top Cell
        if (
            r > 0
            and not self._cells[r - 1][c].visited
            and not self._cells[r][c].has_top_wall
        ):
            self._cells[r][c].draw_move(self._cells[r - 1][c])
            if self._solve_r(r - 1, c):
                return True
            else:
                self._cells[r][c].draw_move(self._cells[r - 1][c], True)

        # Bottom Cell
        if (
            r < self._num_rows - 1
            and not self._cells[r + 1][c].visited
            and not self._cells[r][c].has_bottom_wall
        ):
            self._cells[r][c].draw_move(self._cells[r + 1][c])
            if self._solve_r(r + 1, c):
                return True
            else:
                self._cells[r][c].draw_move(self._cells[r + 1][c], True)

        return False
