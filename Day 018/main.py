from turtle import Turtle, Screen
# challenge 1 get the turtle to draw a square 100 by 100
tim = Turtle()
tim.shape("turtle")
tim.color("green4")

# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

# for _ in range(15):
#     tim.forward(20)
#     tim.penup()
#     tim.forward(20)
#     tim.pendown()


def square():
    for _ in range(4):
        tim.right(90)
        tim.forward(100)


def agons():
    for _ in range(5):
        tim.right(60)
        tim.forward(100)

def triangle(side_length):
    for _ in range(3):
        tim.right(120)
        tim.forward(side_length)


triangle(100)
# square()
# agons()

class Shapes:
    def __init__(self):
        self.length = 0
        self.sides = 0

    def polygon(no_of_sides):
        for _ in range(no_of_sides):
            tim.right(360 / no_of_sides)
            tim.forward(100)
# pentagon = Shapes.polygon(100,5)
pentagon = Shapes.polygon(5)
hexagon = Shapes.polygon(6)
heptagon = Shapes.polygon(7)
octagon = Shapes.polygon(8)
nonagon = Shapes.polygon(9)















my_screen = Screen()
my_screen.exitonclick()
