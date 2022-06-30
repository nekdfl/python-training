import codecs

# file_location = "jumper.sub"
#
# with open(file_location, 'wb') as f:
#     f.write(codecs.BOM_UTF8)
#
# with open(file_location, 'at') as f:
#     mystr = "hello world".encode(hex)
#     f.write(f"mystr{} \n")
#
#
#
#
# with open(file_location, 'rb') as f:
#     print(f.read())
#
#
#
#

res = ':'.join(hex(ord(x))[2:] for x in 'Hello, World!')
print(res)

















# import codecs
#
# def main():
#
#     def create_file():
#         lines = ["hello world", "this is a test row"]
#         f = open("test.txt", mode="wt", encoding='utf-8')
#         f.writelines(lines)
#         f.close()
#
#     def read_bin_file():
#         f = open("test.txt", mode="r")
#         print(f.read())
#         f.close()
#
#     create_file()
#     read_bin_file()
#
#
# if __name__ == '__main__':
#     main()
#
#










# import codecs
# import commands
#
# file_location = "jumper.sub"
# file_encoding = commands.getoutput('file -b --mime-encoding %s' % file_location)
#
# file_stream = codecs.open(file_location, 'r', file_encoding)
# file_output = codecs.open(file_location+"b", 'w', 'utf-8')
#
# for l in file_stream:
#     file_output.write(l)
#
# file_stream.close()
# file_output.close()