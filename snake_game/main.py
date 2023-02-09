from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.07)
    snake.move()
    if snake.get_head().distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    if snake.get_head().xcor() > 280 or snake.get_head().xcor() < -280 or snake.get_head().ycor() > 280 or snake.get_head().ycor() < -280:
        score.game_over()
        snake.reset()

    for segment in snake.get_body():
        if snake.get_head().distance(segment) < 10 and segment != snake.get_head():
            score.game_over()
            snake.reset()

screen.exitonclick()
