from window import Window, Line, Point
from cell import Cell

def Main():

    win = Window(800, 600)
    cell = Cell(win)
    cell.draw(100, 100, 150, 150)

    cell_no_left = Cell(win)
    cell_no_left.has_left_wall = False
    cell_no_left.draw(200, 200, 250, 250)
    cell_no_right = Cell(win)
    cell_no_right.has_right_wall = False
    cell_no_right.draw(300, 300, 350, 350)
    cell_no_top = Cell(win)
    cell_no_top.has_top_wall = False
    cell_no_top.draw(400, 400, 450, 450)
    cell_no_bottom = Cell(win)
    cell_no_bottom.has_bottom_wall = False
    cell_no_bottom.draw(500, 500, 550, 550)

    win.wait_for_close()

Main()