import turtle as t
from turtle import Screen
import random

tim = t.Turtle()
colors = ["cyan", "olive", "maroon", "dark orchid", "brown", "wheat", "spring green", "dark sea green"]
directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")

for _ in range(200):
    tim.color(random.choice(colors))
    tim.forward(30)
    tim.setheading(random.choice(directions))

my_screen = Screen()
my_screen.exitonclick()