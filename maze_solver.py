from MazeSolver import Maze, Window


if __name__ == "__main__":
    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 600
    ROWS = 12
    COLUMNS = 16
    MARGIN = 50

    cell_size_x = (WINDOW_WIDTH - 2 * MARGIN) / COLUMNS
    cell_size_y = (WINDOW_HEIGHT - 2 * MARGIN) / ROWS
    win = Window(WINDOW_WIDTH, WINDOW_HEIGHT)

    maze = Maze(
        MARGIN,
        MARGIN,
        ROWS,
        COLUMNS,
        cell_size_x,
        cell_size_y,
        win,
        redraw_interval=0.001,
    )

    print("Solved!" if maze.solve() else "Not solvable!")

    win.wait_for_close()
