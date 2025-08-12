from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard

screen = Screen()
r_paddle = Paddle(370, 0)
l_paddle = Paddle(-370, 0)
ball = Ball()
score = ScoreBoard()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

screen.listen()
screen.onkey(key="Up", fun=r_paddle.up)
screen.onkey(key="Down", fun=r_paddle.down)
screen.onkey(key="w", fun=l_paddle.up)
screen.onkey(key="s", fun=l_paddle.down)
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision with top and bottom
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with right paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 340) or (ball.distance(l_paddle) < 50 and ball.xcor() < -340):
        ball.bounce_x()

    # detect right paddle misses
    if ball.xcor() > 390:
        ball.reset_position()
        score.increase_l()

    # detect left paddle misses
    if ball.xcor() < -390:
        ball.reset_position()
        score.increase_r()

screen.exitonclick()
