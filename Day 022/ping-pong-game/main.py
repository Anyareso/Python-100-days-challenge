from turtle import Turtle, Screen
from paddle import Paddle

UP = 90
DOWN = 270

screen = Screen()
screen.setup(width=1250, height=600)
screen.title("Ping Pong Game")
screen.bgcolor("black")
screen.tracer(0)

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


l_paddle = Paddle((-580, 0))
r_paddle = Paddle((580, 0))

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
game_is_on = True
while game_is_on:
    screen.update()



screen.exitonclick()
