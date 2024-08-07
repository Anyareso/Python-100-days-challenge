from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time


def play_game():

    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)

    # Creating the snake
    snake = Snake()

    # Creating the food
    food = Food()

    # Establishing the score
    scoreboard = ScoreBoard()

    # Controlling the snake by keyboard keys
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

    #   Detect collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()

    #   Detect collision with wall
        if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
            scoreboard.reset()
            snake.reset()

    #     Detect collision with tail
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                scoreboard.reset()
                snake.reset()
    # If the snake collides with any segment of the tail
    # trigger game over

# screen.exitonclick()


play_game()
