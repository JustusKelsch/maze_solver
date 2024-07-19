from window import Window, Line, Point
from cell import Cell

def Main():

    win = Window(800, 600)
    cell = Cell(win)
    cell.draw(100, 100, 150, 150)

    cell_no_left = Cell(win)
    cell_no_left.has_left_wall = False
    cell_no_left.draw(225, 225, 275, 275)
    cell_no_right = Cell(win)
    cell_no_right.has_right_wall = False
    cell_no_right.draw(180, 230, 230, 280)
    cell_no_right.draw_move(cell_no_left)


    # cell_no_top = Cell(win)
    # cell_no_top.has_top_wall = False
    # cell_no_top.draw(400, 400, 450, 450)
    # cell_no_bottom = Cell(win)
    # cell_no_bottom.has_bottom_wall = False
    # cell_no_bottom.draw(500, 500, 550, 550)

    win.wait_for_close()

Main()