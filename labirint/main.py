import json
import random


class SpaceObject:
    direction_n = 1
    direction_e = 2
    direction_s = 4
    direction_w = 8

    def __init__(self, direction):
        self.direction = direction

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
        self.maze = []

    def get_random_star(self):
        r_star = random.choice(self._stars_list)
        self._stars_list.remove(r_star)
        return r_star

    def add_spaceobject(self, space_object):
        if type(space_object) == Station:
            pass

        allow_directions = []
        if space_object.is_can_move_n():
            allow_directions.append("n")
        if space_object.is_can_move_e():
            allow_directions.append("e")
        if space_object.is_can_move_s():
            allow_directions.append("s")
        if space_object.is_can_move_w():
            allow_directions.append("w")
        new_derection = random.choice(allow_directions)
        return new_derection


def load_space_objects(so_fp):
    with open(so_fp, 'r') as f:
        so_json = json.load(f)
    return so_json


def main():
    pass

    stars_file = "space_objects.json"
    space_objects_json = load_space_objects(stars_file)
    l_builder = MazeBuilder(space_objects_json["stars"])
    random_star = l_builder.get_random_star()
    station = Station(space_objects_json["start_station"]["Name"], space_objects_json["start_station"]["Direction"])
    l_builder.add_spaceobject(station)


if __name__ == '__main__':
    main()
