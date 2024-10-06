from turtle import Turtle, Screen


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0
        self.color("white")
        self.goto(0,260)
        self.write(f"Score {self.score}", align="center", font=("Arial", 24, "normal"))

    def game_over(self):
        self.hideturtle()
        self.goto(0,0)
        self.clear()
        self.write(f"Game Over\n Score : {self.score}", align= "center", font=("Arial", 35, "normal"))

    def increase_score(self):
        self.reset()
        self.color("white")
        self.score += 1
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.write(f"Score {self.score}", align="center", font=("Arial", 24, "normal"))
