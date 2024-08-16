from tkinter import Tk, BOTH, Canvas



class Window:

    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)


    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    
    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("Window has been closed")

    
    def close(self):
        self.__running = False


    def draw_line(self, line, fill_color):
        line.draw(self.__canvas, fill_color)


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2


    def draw(self, canvas, fill_color="black"):
        canvas.create_line(
            self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2
        )



class Cell:

    def __init__(self, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.point_x1 = None
        self.point_x2 = None
        self.point_y1 = None
        self.point_y2 = None
        self._win = win


    def draw_method(self, x1, x2, y1, y2):
        self.point_x1 = x1
        self.point_x2 = x2
        self.point_y1 = y1
        self.point_y2 = y2
        if self.has_left_wall:
            create_line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(create_line)
        if self.has_right_wall:
            create_line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(create_line)
        if self.has_top_wall:
            create_line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(create_line)
        if self.has_bottom_wall:
            create_line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(create_line)









