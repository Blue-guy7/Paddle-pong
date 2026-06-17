from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self,):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.resizemode("user")
        self.shapesize(1,1)
        self.start_rand_direction()
        self.speed(1)
    def start_rand_direction(self):
        rand_angle_rightup = random.randrange(20, 70, 20)
        rand_angle_leftup=random.randrange(110, 165, 20)
        rand_angle_rightdown=random.randrange(290, 345, 20)
        rand_angle_leftdown=random.randrange(195, 250, 20)
        self.setheading(random.choice([rand_angle_rightdown,rand_angle_leftup,rand_angle_leftdown,rand_angle_rightup]))

    def bounce(self):
        i=self.heading()
        self.setheading(360-i)

    def hit_on_right(self):
        current_heading = self.heading()
        reflected_heading = (180 - current_heading) % 360
        self.setheading(reflected_heading)

    def hit_on_left(self):
        current_heading = self.heading()
        reflected_heading = (180 - current_heading) % 360
        self.setheading(reflected_heading)


    

