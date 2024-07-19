import random
from time import sleep
from cell import Cell


class Maze:

    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win=None,
            seed=None,
    ):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._create_cells()
        if seed is not None:
            random.seed(seed)

    def _create_cells(self):

        ## Creates the correct amount of Cells
        ## However the cells are copies of the same Cell

        # self._cells = [
        #     [Cell(self._win)] * self._num_rows
        # ] * self._num_cols

        # for i in range(len(self._cells)):
        #     for j in range(len(self._cells[i])):
        #         self._draw_cell(i, j)

        for i in range(self._num_cols):
            cols = []
            for j in range(self._num_rows):
                cols.append(Cell(self._win))
            self._cells.append(cols)

        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)


    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self._x1 + i * self._cell_size_x
        x2 = x1 + self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        y2 = y1 + self._cell_size_y

        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)

        self._cells[-1][-1].has_bottom_wall = False
        self._draw_cell(len(self._cells) - 1, len(self._cells[-1]) - 1)

    def _break_walls_r(self, i, j):

        self._cells[i][j].visited = True

        #The cell above (i-1, j)
        #The cell below (i+1, j)
        #The cell to the left (i, j-1)
        #The cell to the right (i, j+1)

        while True:
            to_visit = []
            for _ in range(4):
                if i > 0 and not self._cells[i-1][j].visited:
                    to_visit.append((i-1, j))

                if i < len(self._cells) - 1 and not self._cells[i+1][j].visited:
                    to_visit.append((i+1, j))

                if j > 0 and not self._cells[i][j-1].visited:
                    to_visit.append((i, j-1))

                if j < len(self._cells[i]) - 1 and not self._cells[i][j+1].visited:
                    to_visit.append((i, j+1))

            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return

            next_i, next_j = random.choice(to_visit)

            if next_i < i:
                self._cells[next_i][j].has_bottom_wall = False
                self._cells[i][j].has_top_wall = False
            elif next_i > i:
                self._cells[next_i][j].has_top_wall = False
                self._cells[i][j].has_bottom_wall = False
            elif next_j < j:
                self._cells[i][next_j].has_right_wall = False
                self._cells[i][j].has_left_wall = False
            elif next_j > j:
                self._cells[i][next_j].has_left_wall = False
                self._cells[i][j].has_right_wall = False
            
            self._break_walls_r(next_i, next_j)
            self._reset_cells_visited()

    def _reset_cells_visited(self):
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._cells[i][j].visited = False