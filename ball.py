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
        rand_angle_rightup = random.randrange(5, 70, 20)
        rand_angle_leftup=random.randrange(110, 175, 20)
        rand_angle_rightdown=random.randrange(290, 355, 20)
        rand_angle_leftdown=random.randrange(185, 250, 20)
        self.setheading(random.choice([rand_angle_rightdown,rand_angle_leftup,rand_angle_leftdown,rand_angle_rightup]))

    def bounce(self):
        i=self.heading()
        self.setheading(360-i)

    def hit_on_right(self):
        if self.heading()==0:
            self.setheading(180)
        elif self.heading()<90:
            aple=self.heading()
            self.setheading(aple+90)
        elif self.heading()>270:
            mango=self.heading()
            self.setheading(mango-90)
    def hit_on_left(self):
        if self.heading()==180:
            self.setheading(0)
        elif self.heading()<180:
            aple=self.heading()
            self.setheading(aple-90)
        elif self.heading()>180:
            mango=self.heading()
            self.setheading(mango+90)


    

