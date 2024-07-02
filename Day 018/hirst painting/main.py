# import colorgram
#
# # Extract 6 colors from an image.
# colors = colorgram.extract('image.jpg', 50)
#
# rbg_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rbg_colors.append(new_color)
#
# print(rbg_colors)
import random
import turtle
from turtle import Turtle, Screen
turtle.colormode(255)

color_list = [(180, 170, 162), (212, 208, 203), (217, 228, 221), (226, 216, 221), (218, 223, 229), (187, 179, 181),
              (169, 179, 184), (155, 175, 161), (206, 196, 165), (140, 86, 62), (57, 105, 121), (65, 115, 89),
              (209, 184, 178), (135, 71, 80), (65, 32, 25), (202, 186, 189), (160, 148, 62), (129, 29, 39),
              (17, 54, 70), (119, 37, 28), (74, 21, 28), (189, 102, 85), (177, 201, 188), (17, 58, 43),
              (190, 191, 196), (18, 92, 70), (99, 146, 115), (84, 149, 157), (21, 83, 95), (177, 97, 104),
              (175, 198, 204), (79, 73, 42), (120, 126, 146)]

tim = Turtle()
tim.speed("fast")


def make_dots():
    tim.dot(20)
    tim.penup()
    tim.forward(50)
    tim.dot(20)


def row():
    for _ in range(10):
        tim.color(random.choice(color_list))
        make_dots()


n = 0
for _ in range(10):
    row()
    tim.home()
    n += 40
    tim.teleport(y=n)


my_screen = Screen()
my_screen.exitonclick()
