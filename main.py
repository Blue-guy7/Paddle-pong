from turtle import Screen
from paddlef import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen = Screen()
screen.bgcolor("Black")
screen.setup(1000, 600)
screen.title("Pong")
screen.listen()
screen.tracer(0)
scoreboard = Scoreboard()
r_pad1 = Paddle(455)
l_pad1 = Paddle(-455)
ball = Ball()
screen.onkey(r_pad1.Up, "Up")
screen.onkey(r_pad1.Down, "Down")
screen.onkey(l_pad1.Up, "w")
screen.onkey(l_pad1.Down, "s")
BALL_RADIUS = 10
PAD_WIDTH = 20
PAD_HEIGHT = 100
frame_delay = 0.01  
game_is_on = True

while game_is_on:
    time.sleep(frame_delay)
    ball.forward(8)

    b_x, b_y = ball.xcor(), ball.ycor()
    r_x, r_y = r_pad1.xcor(), r_pad1.ycor()
    l_x, l_y = l_pad1.xcor(), l_pad1.ycor()
    if b_y > 290 or b_y < -290:
        ball.bounce()
    if (b_x + BALL_RADIUS >= r_x - (PAD_WIDTH / 2) and 
        b_x - BALL_RADIUS <= r_x + (PAD_WIDTH / 2) and 
        b_y + BALL_RADIUS >= r_y - (PAD_HEIGHT / 2) and 
        b_y - BALL_RADIUS <= r_y + (PAD_HEIGHT / 2)):
        
        ball.hit_on_right()
        frame_delay *= 0.90 
    elif (b_x + BALL_RADIUS >= l_x - (PAD_WIDTH / 2) and 
          b_x - BALL_RADIUS <= l_x + (PAD_WIDTH / 2) and 
          b_y + BALL_RADIUS >= l_y - (PAD_HEIGHT / 2) and 
          b_y - BALL_RADIUS <= l_y + (PAD_HEIGHT / 2)):
        
        ball.hit_on_left()
        frame_delay *= 0.90

    if b_x > 480:
        scoreboard.l_win()
        ball.home()
        ball.start_rand_direction()
        frame_delay = 0.01 
    elif b_x < -480:
        scoreboard.r_win()
        ball.home()
        ball.start_rand_direction()
        frame_delay = 0.01 
    if scoreboard.game_over():
        game_is_on = False
        
    screen.update()

screen.exitonclick()
