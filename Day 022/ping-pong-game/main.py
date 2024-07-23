from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

UP = 90
DOWN = 270

screen = Screen()
screen.setup(width=1250, height=600)
screen.title("Ping Pong Game")
screen.bgcolor("black")
screen.tracer(0)

# Creating the barrier
tim = Turtle()
tim.hideturtle()
tim.color("white")
tim.penup()
tim.setpos(0, 300)
tim.right(90)
for _ in range(30):
    tim.forward(10)
    tim.penup()  # Lift the pen
    tim.forward(10)
    tim.pendown()

l_paddle = Paddle((-580, 0))
r_paddle = Paddle((580, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 260 or ball.ycor() < -260:
        ball.bounce_y()

    # Detect collision with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 540:
        ball.bounce_x()

    # Detecting collision with left paddle
    if ball.distance(l_paddle) < 50 and ball.xcor() < -540:
        ball.bounce_x()

    # Detect when right paddle misses
    if ball.xcor() > 600:
        ball.reset_position()
        scoreboard.l_point()

    # Detect when left paddle misses
    if ball.xcor() < -600:
        ball.reset_position()
        scoreboard.r_point()









screen.exitonclick()
