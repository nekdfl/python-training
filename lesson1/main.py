# None
# int 1,2,3,4
# float, double 3.12345566789
# bool True False | None, 0 = False, остальное
# str "", '', str

# list - [] | list
# set - множество {} | set
# tuple - () | tuple
# dict - {key:value} | dict()


def string_examples():
    pass
    # mylist = [1,2,3,4,4,4,4]
    # print(mylist)
    # myset = {1,2,3,4,4,4,4, "sdfd", 12, 22}
    # print(myset)
    # mytuple = (1, 2, 3, 4, 4, 4, 4)
    # print(mytuple)
    # mydict = {"key" : "value"}
    # print(mydict)
    #
    # print(type(mydict))

    # mystring = 'hello "world"'
    # mystring = mystring.title()
    # print(mystring)
    #
    # for el in mystring:
    #     print(el)

    # myname="Николай"
    # %d
    # %f
    # %s
    # %b

    # digit1 = 4
    # digit2 = 10.123
    # mystring = "Меня зовут %s" % myname
    # mystring2 = "мое любимое число %s, %s" % (digit1, digit2)
    # mystring3 = "мое любимое число %s" % True
    # print(mystring3)

    # a = {1, 23}
    # a = "{12, 34, 14}"
    # mystring4 = "Мое любимое число {{1:.2f}}, {{0}}"
    # mystring4 = mystring4.format(digit1, digit2)
    # print(mystring4)

    # mystring = f"Мое любимое число {digit2}, {digit1}"
    # print(mystring)

    # mystring = "Мое любимое число " + str(digit1) + ", " + str(digit2)
    # print(mystring)


def exmaple_user_input():
    user_input = int(input("введите ваше любимое число: "))
    print(f"Ваше любомое число {user_input}")


def calc_time(v, s):
    t = v / s
    return t


def abc():
    pass


def main():
    pass
    # t = v/s
    task_description = """Дано: Велосипедист из А точки в точку Б едет со скоростью 12Км/ч. 
Расстояние до точки Б 30км. За сколько велосипидист доедет до точки Б."""
    print(task_description)
    s = 30
    v = 12
    t = calc_time(v, s)
    print(f"Велосипидст доедет до точки Б за: {t} часа")


if __name__ == '__main__':
    main()
