from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 30, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 250)
        self.color("white")
        self.speed("fastest")
        self.hideturtle()
        self.score = [0, 0]
        self.prompt = ""
        self.refresh_prompt()

    def refresh_prompt(self):
        self.clear()
        self.prompt = f"{self.score[0]}    {self.score[1]}"
        self.write(self.prompt, align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.color("yellow")
        self.write("GAME OVER", align=ALIGN, font=("Arial Black", 20, "bold"))
        self.goto(0, -35)
        if self.score[0] < self.score[1]:
            self.write("You Lose", align=ALIGN, font=("Arial Black", 16, "bold"))
        elif self.score[0] > self.score[1]:
            self.write("You Win", align=ALIGN, font=("Arial Black", 16, "bold"))

    def increase_score(self, which_side):
        if which_side == "left":
            self.score[0] += 1
        elif which_side == "right":
            self.score[1] += 1
        else:
            pass
        self.refresh_prompt()

