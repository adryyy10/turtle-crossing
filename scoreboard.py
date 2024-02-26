from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.score, align="center", font=FONT)

    def increase_point(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write('Game over', align="center", font=FONT)
