from turtle import Turtle
from random import randint, choice

BALL_SIZE = 13
X_BORDER = 400
Y_BORDER = 300

STEP = 10


class Ball(Turtle):

    def __init__(self):
        super().__init__()

        self.penup()
        self.color("white")
        self.shape("circle")
        self.shapesize(stretch_wid=BALL_SIZE/20, stretch_len=BALL_SIZE/20)
        # self.goto(0, -Y_BORDER+20)
        # self.setheading(135)
        self.refresh()
        self.speed("fastest")
        self.step = STEP

    def move(self):
        self.forward(self.step)

    def bounce_paddle(self):
        current_angle = self.heading()
        self.setheading(180-current_angle)
        self.step += 2

    def bounce_wall(self):
        current_angle = self.heading()
        self.setheading(-current_angle)


    def refresh(self):
        rand_angle = randint(10, 70)
        add_180 = choice([0, 180])
        minus_one = choice([1, -1])
        angle = (rand_angle + add_180) * minus_one

        self.goto(0, 0)
        self.setheading(angle)
        self.step = STEP





