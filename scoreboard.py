from turtle import Turtle, Screen

ALIGNEMENT = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.update_scoreboard()

    def update_scoreboard(self):
        self.reset()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,250)
        self.write(f"score: {self.score} High score: {self.highscore}", align= ALIGNEMENT, font=FONT )

    def reset_score(self):
        if self.score > int(self.highscore):
            self.highscore = self.score
            with open("data.txt", mode="w") as data:
                data.write(str(self.highscore))
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

