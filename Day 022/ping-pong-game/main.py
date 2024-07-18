from turtle import Turtle, Screen

UP = 90
DOWN = 270

screen = Screen()
screen.setup(width=1250, height=600)
screen.title("Ping Pong Game")
screen.bgcolor("black")
# screen.tracer(0)

paddle_1 = Turtle()
paddle_1.color("white")
paddle_1.right(90)
paddle_1.shape("square")
paddle_1.shapesize(stretch_wid=1, stretch_len=5)
paddle_1.penup()
paddle_1.goto(x=550, y=0)

# Creating the barrier
# tim = Turtle()
# tim.hideturtle()
# tim.color("white")
# tim.penup()
# tim.setpos(0, 300)
# tim.right(90)
# for _ in range(30):
#     tim.forward(10)
#     tim.penup()  # Lift the pen
#     tim.forward(10)
#     tim.pendown()

screen.exitonclick()
