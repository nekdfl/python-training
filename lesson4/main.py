import os
import codecs

# modes
# w - запись
# r - чтение
# + - и чтение и запись
# x - создание файла
# a - дозапись


def write_file():
    lines = ["Hello world", "test hello", "Миру мир"]
    with open("temp/test1.txt", 'w', encoding='utf-8') as f:
        for line in lines:
            f.write(line + "\n")


def main():
    pass
    write_file()

    data = ""

    # BOM byte order mask


    pass
    print(data)


if __name__ == '__main__':
    main()
