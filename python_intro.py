# print("Hello, Django girls!")
#
# if 3 > 2:
#     print("It works!")
#
# if 5 > 2:
#     print("5 is endeed greater than 2")
# else:
#     print("5 is not greater than 2")
#

# chanhe the volume if it is too loud or too quiet
# if volume < 20 or volume > 80:
#     volume = 50
#     print("That's better")

#
# def hi(name):
#     if name == "Ola":
#         print("Hi, Ola!")
#     elif name == "Sonja":
#         print("Hi, Sonja")
#     else:
#         print("Hi anonymous")
#
# hi("Adam")


def hi(name):
    print('Hi ' + name + '!')


girls = ['Rachiel', 'Sonja', 'Monica', 'Ola', 'Anna']

for name in girls:
    hi(name)
    print('Next girl')
