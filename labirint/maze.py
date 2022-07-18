class Maze:
    STATION_POS = (15, 15)

    def __init__(self):
        self.maze = []
        self._matrix = [[None] * 31] * 31

    def add_start_station(self, station):
        self._matrix[self.STATION_POS[0]][self.STATION_POS[1]] = station

    def add_space_object(self, space_object):
        self.maze.append(space_object, ())

    def check_is_free(self, direction):
        pass
        if not direction:
            raise ValueError("Direction can't be empty!")

        if self.maze:
            last_star = self.maze[-1]
            if direction == 1:
                delta = (-1, 0)

            elif direction == 2:
                delta = (0, 1)
            elif direction == 4:
                delta = (0, -1)
            elif direction == 8:
                delta = (1, 0)

        return True
