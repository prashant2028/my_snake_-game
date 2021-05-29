from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):

        super().__init__()
        self.penup()
        self.goto(x=0, y=270)
        self.score=0
        self.color("yellow")
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))
        self.hideturtle()

    def gameover(self):
        self.goto(0,0)
        self.write("Gameover",align="center",font=("arial",24,"normal"))
    def increase_score(self):
        self.score+=1
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))






