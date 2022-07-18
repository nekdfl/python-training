from tkinter import *

from labirint.maze import SpaceObject


def create_test_maze():
    maze=[]
    coords = [(0,1), (0,2), (0,3), (1,3) , (2,3), (2,2)]
    for coord in coords:
        so = SpaceObject(15)
        so.set_x(coord[0])
        so.set_y(coord[1])
        maze.append(so)

    return maze

class SpasObject:

    arrow_space = 10
    arrow_size = 5
    size = 20

    def __init__(self, can, x, y):
        self.can = can
        self.x = x
        self.y = y

    def create_station(self):
        id_object = self.can.create_rectangle(self.x, self.y, self.x + 20, self.y + 20, fill="black")

    def create_star(self):
        id_object = self.can.create_oval(self.x, self.y, self.x + 20, self.y + 20, fill="black")

    def create_arrow(self, arrow_x, arrow_y):
        id_arrow = self.can.create_oval(arrow_x, arrow_y, arrow_x + self.arrow_size, arrow_y + self.arrow_size, fill="green")

    def create_arrow_n(self):
        pass
        x_arrow = self.x + (self.x/2)
        y_arrow = self.y + self.arrow_space +self.arrow_size
        self.create_arrow(x_arrow, y_arrow)

    def create_arrow_e(self):
        pass
        x_arrow = self.x + self.size+  self.arrow_space
        y_arrow = self.y + (self.y / 2)
        self.create_arrow(x_arrow, y_arrow)

    def create_arrow_s(self):
        pass
        x_arrow = self.x + (self.x/2)
        y_arrow = self.y + self.size + self.arrow_space
        self.create_arrow(x_arrow, y_arrow)

    def create_arrow_w(self):
        pass
        x_arrow = self.x - self.arrow_space - self.arrow_size
        y_arrow = self.y - (self.size/2)
        self.create_arrow(x_arrow, y_arrow)

class Renderer:
    def __init__(self, maze, start_point, can):
        self.maze = maze
        self.can = can
        self.step = 35
        self.starting_point = start_point
        self.image_size = 20

    def rendering(self):

        for iter, so in enumerate(self.maze):
            delta_x = 0
            delta_y =0
            delta_x = self.starting_point.x + (self.maze[iter].x * self.step) + (self.maze[iter].x * self.image_size)
            delta_y = self.starting_point.y + (self.maze[iter].y * self.step) + (self.maze[iter].y * self.image_size)
            # if self.starting_point.x > self.maze[iter].x:
            #     x = self.starting_point.x - self.step
            # else:
            #     x = self.starting_point.x + self.step
            # if self.starting_point.y > self.maze[iter].y:
            #     y = self.starting_point.y - self.step
            # else:
            #     y = self.starting_point.y + self.step
            star = SpasObject(self.can, delta_x, delta_y)
            star.create_star()
            if so.is_can_move_n():
                star.create_arrow_n()
            if so.is_can_move_e():
                star.create_arrow_e()
            if so.is_can_move_s():
                star.create_arrow_s()
            if so.is_can_move_w():
                star.create_arrow_w()




def main():
    tk = Tk()
    can = Canvas(tk, width=1000, height=1000)
    can.pack()
    station = SpasObject(can, 500, 500)
    station.create_station()

    mymaze = create_test_maze()

    map = Renderer(mymaze, station, can)
    map.rendering()

    tk.mainloop()


if __name__ == '__main__':
    main()
