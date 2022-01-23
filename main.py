from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("teal")
screen.title("Snake")
screen.tracer(0)
starting_positions = [(0, 0), (-20, 0), (-40,0)]
snake = Snake()
food = Food()
score = Scoreboard()


def clean_screen():
    screen.resetscreen()


screen.listen()
screen.onkey(key="w", fun=snake.up)
screen.onkey(key="s", fun=snake.down)
screen.onkey(key="d", fun=snake.right)
screen.onkey(key="a", fun=snake.left)
screen.onkey(key="c", fun=clean_screen)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food and update score
    if snake.head.distance(food) < 18:
        food.refresh()
        snake.extend()
        score.update_score()

    # Detect collision with wall
    if snake.head.xcor() > 390 or snake.head.xcor() < -390 or snake.head.ycor() > 390 or snake.head.ycor() < -390:
        game_is_on = False
        score.game_over()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()


screen.exitonclick()