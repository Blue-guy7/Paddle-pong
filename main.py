from turtle import Screen
from paddlef import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen=Screen()
screen.bgcolor("Black")
screen.setup(1000,600)
screen.title("Pong ")
screen.listen()
screen.tracer(0)

scoreboard=Scoreboard()
r_pad1=Paddle(455)
l_pad1=Paddle(-455)
ball=Ball()
screen.onkey(r_pad1.Up,"Up")
screen.onkey(r_pad1.Down,"Down")
screen.onkey(l_pad1.Up,"w")
screen.onkey(l_pad1.Down,"s")



game_is_on=True

while game_is_on==True:
    aple=0.01
    time.sleep(aple)
    ball.forward(5)
    if ball.ycor()>290 or ball.ycor()<-290:
        ball.bounce()
    if ball.distance(r_pad1)<50 and ball.xcor()>360:
        ball.hit_on_right()
        aple*=0.1
    if ball.distance(l_pad1)<50 and ball.xcor()<-360:
        ball.hit_on_left()
        aple*=0.1
    if ball.xcor()>480:
        scoreboard.l_win()
        ball.home()
        ball.start_rand_direction()
    if ball.xcor()<-480:
        scoreboard.r_win()
        ball.home()
        ball.start_rand_direction()
    screen.update()    






















screen.exitonclick()