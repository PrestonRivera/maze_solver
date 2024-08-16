from graphics import Line, Point


class Cell:

    def __init__(self, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._point_x1 = None
        self._point_x2 = None
        self._point_y1 = None
        self._point_y2 = None
        self._win = win


    def draw(self, x1, x2, y1, y2):
        self._point_x1 = x1
        self._point_x2 = x2
        self._point_y1 = y1
        self._point_y2 = y2
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line)
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line)
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line)
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line)


    def draw_move(self, to_cell, undo=False):
        half_length = abs(self._point_x2 - self._point_x1) // 2
        x_center = half_length + self._point_x1
        y_center = half_length + self._point_y1

        half_length_2 = abs(to_cell._point_x2 - to_cell._point_x1) // 2
        x_center_2 = half_length_2 + to_cell._point_x1
        y_center_2 = half_length_2 + to_cell._point_y1

        fill_color = "red"
        if undo:
            fill_color = "gray"

        line = Line(Point(x_center, y_center), Point(x_center_2, y_center_2))
        self._win.draw_line(line, fill_color)