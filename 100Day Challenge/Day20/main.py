import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)
snake = Snake()
food = Food()
score_card = Scoreboard()
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
    # detect collision with food
    if snake.snake_head.distance(food) < 15:
        food.refresh_food()
        snake.extend()
        score_card.score += 1
        score_card.update_score()

    # detect collision with food
    if snake.snake_head.xcor() > 290 or snake.snake_head.xcor() < -290 or snake.snake_head.ycor() > 290 \
            or snake.snake_head.ycor() < -290:
        score_card.reset()
        snake.reset()

    # detect collision with itself
    for segment in snake.segments[1:]:
        if snake.snake_head.distance(segment) < 1:
            score_card.reset()
            snake.reset()


screen.exitonclick()
