from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
positions = [0, -20, -40]

for i in range(0, 3):
    tim = Turtle(shape="square")
    tim.color("white")
    tim.goto(x=positions[i], y=0)









screen.exitonclick()
