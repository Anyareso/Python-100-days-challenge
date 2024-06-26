# from turtle import Turtle, Screen
# # challenge 1 get the turtle to draw a square 100 by 100
# tim = Turtle()
# tim.shape("turtle")
# tim.color("green4")

# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

# for _ in range(15):
#     tim.forward(20)
#     tim.penup()
#     tim.forward(20)
#     tim.pendown()

# My_solution start
# class Shapes:
#     def __init__(self):
#         pass
#
#     def polygon(self, no_of_sides, color):
#         for _ in range(no_of_sides):
#             tim.color(color)
#             tim.right(360 / no_of_sides)
#             tim.forward(100)

# shape = Shapes()
# shape.polygon(3, "yellow")
# shape.polygon(5, "orange")
# shape.polygon(6, "blue")
# shape.polygon(7, "pink")
# shape.polygon(8, "purple")
# shape.polygon(9, "brown")

import random
import turtle as t
from turtle import Screen
tim = t.Turtle()
colors = ["light cyan", "olive", "maroon", "dark orchid", "rosy brown", "wheat", "spring green", "dark sea green"]


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)


for shape_side_n in range (3,11):
    tim.color(random.choice(colors))
    draw_shape(shape_side_n)


my_screen = Screen()
my_screen.exitonclick()
