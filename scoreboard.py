from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.l_score=0
        self.r_score=0
        self.color("white")
        self.new_score()

    def new_score(self):
        self.setposition(-100,250)
        self.write(self.l_score,False,"center",("Arial", 24, "normal"))
        self.setposition(100,250)
        self.write(self.r_score,False,"center",("Arial", 24, "normal"))

    def l_win(self):
        self.clear()
        self.l_score+=1
        self.new_score()
    def r_win(self):
        self.clear()
        self.r_score+=1
        self.new_score()

    def game_over(self):
        if self.l_score>=10:
            self.setposition(0,100)
            self.write("Left paddle wins",False,"center",("Arial", 24, "normal"))
            return True
        elif self.r_score>=10:
            self.setposition(0,100)
            self.write("Right paddle wins",False,"center",("Arial", 24, "normal"))
            return True
