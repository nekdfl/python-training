import json
import random

from labirint.maze import Maze


class SpaceObject:
    direction_n = 1
    direction_e = 2
    direction_s = 4
    direction_w = 8

    def __init__(self, direction):
        self.direction = direction
        self._x = None
        self._y = None
        self._next = None

    def set_x(self, x):
        self._x = x

    @property
    def x(self):
        return self._x

    def set_y(self, y):
        self._y = y

    @property
    def y(self):
        return self._y

    def set_next_direction(self, direction):
        self._next = direction

    @property
    def next(self):
        return self._next

    def __is_can_move(self, direction):
        return self.direction & direction

    def is_can_move_n(self):
        return self.__is_can_move(self.direction_n)

    def is_can_move_e(self):
        return self.__is_can_move(self.direction_e)

    def is_can_move_s(self):
        return self.__is_can_move(self.direction_s)

    def is_can_move_w(self):
        return self.__is_can_move(self.direction_w)


class Station(SpaceObject):

    def __init__(self, name, direction):
        super(Station, self).__init__(direction)
        self.name = name

    def __str__(self):
        return f"start station {self.name}"


class Star(SpaceObject):

    def __init__(self, name, id, planet_quantity, type, direction):
        super().__init__(direction)
        self.name = name
        self.id = id
        self.planet_quantity = planet_quantity
        self.type = type

    def __str__(self):
        return f"star name {self.name}"


class MazeBuilder:

    def __build_star_list(self, stars_json):
        for star in stars_json:
            n = star["Name"]
            i = star["id"]
            pq = star["planet_quantity"]
            t = star["Type"]
            d = star["Direction"]
            self._stars_list.append(Star(n, i, pq, t, d))

    def __init__(self, stars_json):
        self._stars_list = []
        self.__build_star_list(stars_json)
        self.maze = Maze()

    def get_random_star(self):
        while self._stars_list:
            r_star = random.choice(self._stars_list)
            self._stars_list.remove(r_star)
            yield r_star

    def add_start_station(self, station):
        self.maze.add_start_station(station)

    def add_spaceobject(self, space_object):

        allow_directions = []
        if space_object.is_can_move_n():
            allow_directions.append(1)
        if space_object.is_can_move_e():
            allow_directions.append(2)
        if space_object.is_can_move_s():
            allow_directions.append(4)
        if space_object.is_can_move_w():
            allow_directions.append(8)

        new_direction = random.choice(allow_directions)
        while not self.maze.check_is_free(new_direction):
            allow_directions.remove(new_direction)
            new_direction = random.choice(allow_directions)
        space_object.set_next_direction(new_direction)
        self.maze.add_space_object(space_object)

    def get_maze(self):
        return self.maze


def load_space_objects(so_fp):
    with open(so_fp, 'r') as f:
        so_json = json.load(f)
    return so_json


def build_maze(l_builder, station):
    l_builder.add_spaceobject(station)
    for star in l_builder.get_random_star():
        l_builder.add_spaceobject(star)


def main():
    pass

    stars_file = "space_objects.json"
    space_objects_json = load_space_objects(stars_file)
    l_builder = MazeBuilder(space_objects_json["stars"])
    station = Station(space_objects_json["start_station"]["Name"], space_objects_json["start_station"]["Direction"])
    build_maze(l_builder, station)
    maze = l_builder.get_maze()
    print(maze)


if __name__ == '__main__':
    main()
