from paddle import Paddle
from turtle import Screen
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Pong")
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))

ball = Ball()
ball_speed = 0.09

scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.paddle_up, "Up")
screen.onkeypress(l_paddle.paddle_down, "s")
screen.onkeypress(r_paddle.paddle_down, "Down")
screen.onkeypress(l_paddle.paddle_up, "w")

game_is_on = True

while game_is_on:
    time.sleep(ball_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 60 and ball.xcor() >= 320:
        ball.bounce_x()
        if ball_speed > 0:
            ball_speed -= 0.005
        else:
            pass

    if ball.distance(l_paddle) < 60 and ball.xcor() <= -320:
        ball.bounce_x()
        if ball_speed > 0:
            ball_speed -= 0.005
        else:
            pass

    if ball.xcor() >= 400:
        scoreboard.change_l_score()
        ball.go_to_start()
        ball_speed = 0.085

    if ball.xcor() <= -400:
        scoreboard.change_r_score()
        ball.go_to_start()
        ball_speed = 0.1

    if scoreboard.provide_l_score() == 10 or scoreboard.provide_r_score() == 10:
        ball.hideturtle()
        ball.goto(0, 0)
        ball.write("GAME OVER", align="center", font=("Courier", 45, "normal"))
