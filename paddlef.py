from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,aple):
        super().__init__()
        self.penup()
        self.color("white")
        self.setposition(int(aple),0)
        self.shape("square")
        self.resizemode("user")
        self.shapesize(0.5,5)
        self.setheading(90)
                
    def Up(self):
        self.forward(30)
    def Down(self):
        self.backward(30)

