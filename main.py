from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

tlt = Turtle()
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 360:
        ball.resetposition()
        scoreboard.l_point()

    if ball.xcor() < -360:
        ball.resetposition()
        scoreboard.r_point()

    if scoreboard.r_score == 5:
        game_is_on = False
        tlt.color("white")
        tlt.penup()
        tlt.write("Right Side Win", align="center", font=("Courier", 50, "normal"))
        print("Right Side Win")

    elif scoreboard.l_score == 5:
        game_is_on = False
        tlt.color("white")
        tlt.penup()
        tlt.write("Left Side Win", align="center", font=("Courier", 50, "normal"))
        print("Left Side Win")
    else:
        pass





screen.exitonclick()