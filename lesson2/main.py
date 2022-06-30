# def return_true():
#     return True
#
#
# def main():
#     pass
#     a = 2
#     b = 2
#
#     # if return_true():
#     #     print("a = b")
#     # else:
#     #     print("a != b")
#
#     # [если истина] if [выражение] else [если ложь]
#
#     # j=True if a == b else print("a != b")
#

#
#     while True:
#         print("Введите q для выхода")
#         arg1 = input("введите число 1 ")
#         arg2 = input("введите число 2 ")
#         operation = input("введите оперцаию [+ - * /]")
#
#         if arg1 == q or arg2 == q or arg3:
#
#
# if __name__ == '__main__':
#     main()

a = 1
b = 2
c = 3


def return_true():
    return True


def ask_user(msg):
    res = input(f"{msg}: ")
    if res == "q":
        print("Завершаем программу")
        exit(0)
    return res


def calc(arg1, arg2, operation):
    if operation == "+":
        print(arg1 + arg2)
    elif operation == "-":
        print(arg1 - arg2)
    elif operation == "/":
        print(arg1 / arg2)
    elif operation == "*":
        print(arg1 * arg2)


# def func1():
#     global a, b, c
#     a = 0
#     b = 0
#     raise RuntimeError("fatality")
#     c = 0
#
# def func2():
#     print("мирная функция")

def func1():
    raise RuntimeError("fatality")


def func2():
    print("мирная функция")


# def main():
#     # try:
#     #     func1()
#     # except BaseException as ex:
#     #     print(ex)
#     # print(f"{a}; {b}; {c}")
#     #
#     # while True:
#     #     try:
#     #         print("Введите q для выхода")
#     #         operation = ask_user("введите оперцаию [+ - * /]")
#     #         arg1 = int(ask_user("введите число 1"))
#     #         arg2 = int(ask_user("введите число 2"))
#     #         calc(arg1, arg2, operation)
#     #     except ZeroDivisionError as e:
#     #         print("Делить на ноль нельзя!")
#     #     except Exception as e:
#     #         print(e)
#     #     else:
#     #         print("Ошибок нет")
#     #     finally:
#     #         print("вышли из блока try")
#
#
# if __name__ == '__main__':
#     try:
#         main()
#     except:
#         print("Не помойманое исключение")


#     # test_list = [1, 2, 3, 4, 5, 6, 7]
#     # x = 10
#     # i = 0
#     # while i < len(test_list):
#     #     if test_list[i] == x:
#     #         print(f"Нашел число {x}")
#     #         break
#     #     i += 1
#     # else:
#     #     print(f"дошел до конца и не нашел числа {x}")

# start =0
# stop= 11
# step = 2
# current=start
#
# def get_next():
#     global current
#     current+=step
#     return current
#
# def main():
#     # test_list = ["x1", "x2", "x3", "x4", "x5", "x6", "x7"]
#     #
#     # a = range(1, 10)
#     # print(a.step)
#
#     # print(type(a))
#     # print(a.count(9))
#     # test_list = [0, 1, 2]
#     # gen_list = [el for el in range(1, 11, 2)]
#
#
#     # for el in gen_list:
#     #     print(el)
#
#     # for _ in range(0, 5, 3):
#     #     print("hello")
#     gen_list = [el for el in range(1, 11, 2)]
#     test_str = "hello world"
#
#     if 5 in range(1, 10):
#         print("Found!")
#     else:
#         print("not found")
#
#
#
#
# if __name__ == '__main__':
#     main()
#


class Node:

    def __init__(self, a_left=None, a_right=None, a_value=None):
        self.left = a_left
        self.right = a_right
        self.value = a_value

    def rebuild(self):
        if self.left is not None:
            self.left = self


def main():
    user_input = [1, '+', 2]

    my_tree = []
    rootnode = Node(None, None, 1)
    node2 = Node(rootnode, None, '+')
    node3 = Node(node2, None, 2)
    my_tree.append(rootnode, node2, node3)

    for node in my_tree:
        node.rebuild()


if __name__ == '__main__':
    main()
