from turtle import Turtle
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width= 800, height= 600)
screen.bgcolor("black")
screen.title("Aryan Pong Game")
#turn off the animation by tracer
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350, 0))
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

ball = Ball()
# ball.speed("slowest")

is_on = True
while is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    #detect collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #colision with paddle

    if ball.distance(r_paddle) < 50  and ball.xcor() >320 or ball.distance(l_paddle) < 50  and ball.xcor() < -320 :
        ball.bounce_x()


    if ball.xcor()> 380:
        # is_on = False
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()




screen.exitonclick()