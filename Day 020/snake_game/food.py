import random
from turtle import Turtle
import random


class Food(Turtle):
    # enabling food class to inherit from turtle instead of having to
    # use self.food = Turtle()
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("purple")
        self.speed("fast")
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)