class Figure(object):

    def print_square(self):
        pass

    def print_hello(self):
        print("hello")


class Square(Figure):

    def __init__(self, side_length):
        self.__side_length = side_length

    def __init(self):
        pass

    def __init__(self, side1, side2, side3, side4):
        pass

    def print_square(self):
        self.__square = 2
        pass


class Circle(Figure):

    def __init__(self, radius, square):
        self.__square = square
        self.__radius = radius

    def print_tadius(self):
        pass

    def print_square(self):
        pass
        self.__square.print_square()


def main():
    pass

    # mysqure = Square(10)
    # mycycle = Circle(4, mysqure)
    # mycycle.print_square()

    # list_of_int = [1,2,3,4, "3"]
    #
    # list_of_figure = [mycycle, mysqure ]
    #[**********]
    #
    #[]
    mystr = "hello "
    mystr.__add__("world")
    mystr = mystr + "wold"

    print(mystr)


if __name__ == '__main__':
    main()
