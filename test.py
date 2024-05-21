from MazeSolver import Maze, Window
import unittest


class Tests(unittest.TestCase):

    def test_maze_create_cells(self):
        num_cols = 4
        num_rows = 2

        maze = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(maze._cells), num_rows)
        self.assertEqual(len(maze._cells[0]), num_cols)

    def test_maze_break_entrance_and_exit(self):
        num_cols = 4
        num_rows = 2

        maze = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(maze._cells), num_rows)
        self.assertEqual(len(maze._cells[0]), num_cols)
        self.assertEqual(
            maze._cells[0][0].has_top_wall,
            False,
        )
        self.assertEqual(
            maze._cells[num_rows - 1][num_cols - 1].has_bottom_wall,
            False,
        )

    def test_maze_reset_cells_visited(self):
        num_cols = 4
        num_rows = 2

        maze = Maze(0, 0, num_rows, num_cols, 10, 10)
        for row in maze._cells:
            for cell in row:
                self.assertEqual(
                    cell.visited,
                    False,
                )


if __name__ == "__main__":
    unittest.main()
