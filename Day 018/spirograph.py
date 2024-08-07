from turtle import Screen
import turtle as t
import random

tim = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


########### Challenge 5 - Spirograph ########
tim.speed("fastest")
for _ in range(180):
    tim.color(random_color())
    tim.circle(100)
    tim.left(10)

my_screen = Screen()
my_screen.exitonclick()
