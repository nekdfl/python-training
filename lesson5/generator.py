import os
import random
from functools import reduce
import shutil

"""
{generator}-{iter1}-{iter2}-{iter3}...{iter_n}-{}
{iter1}.value = 2
{iter}.next() 
{iter1}.prev() 
"""


def infinite_sequence(num):
    n = 0
    while n < num:
        print("point 0")
        yield n
        print("point 1")
        n += 1


def generator_example():
    x = infinite_sequence(5)
    for _ in range(0, 10):
        try:
            print("before generator")
            print(next(x))
            print("after generator")
            # x = infinite_sequence(5)
        except StopIteration:
            x = infinite_sequence(5)
            print("Exception, restart generator")
            print(next(x))


def gen_list_example():
    # res_list = []
    # for x in range(0, 10):
    #     res_list.append(x)

    gen_list = [x for x in range(0, 10)]
    print(gen_list)


def summ_add_10(arg):
    return arg + 10


def lambda_example():
    x_func = lambda a: a + 10
    res = x_func(10)
    print(res)


def map_func(x):
    x = x - 1
    return x


def map_example_1():
    test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    res_list = [x for x in map(map_func, test_list)]
    print(res_list)

    # x = 0xffffff23
    # y = x
    # print(y)
    # rename_func = map_func
    # print(rename_func(2))


def map_example_2():
    test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    res_list = [x for x in map(lambda x: x - 1, test_list)]
    print(res_list)


def reduce_example():
    test_list = ["1", "2", "3"]
    # [3, 3]
    # 3 = [3]
    res_list = reduce(lambda prev, next: prev + next, test_list)
    print(res_list)

def filter_example():
    test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    filtred_list = [x for x in filter(lambda x: x % 2 == 0, test_list)]
    print(filtred_list)


def shutil_example():
    print(os.getcwd())
    print(shutil.disk_usage(os.getcwd()))

if __name__ == '__main__':
    pass
    # generator_example()
    # gen_list_example()
    # map_example_1()
    # reduce_example()
    # filter_example()
    # shutil_example()



