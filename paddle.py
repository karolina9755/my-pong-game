from turtle import Turtle
import time

Y_BORDER = 300

PADDLE_LENGTH = 80
PADDLE_WIDTH = 4
UP = 90
DOWN = 270
STEP = 20


class Paddle(Turtle):

    def __init__(self, x_position, y_position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=PADDLE_WIDTH/20,stretch_len=PADDLE_LENGTH/20)
        self.speed("fastest")
        self.color("white")
        self.penup()
        self.setheading(90)
        self.goto(x_position, y_position)

    def move_up(self):
        if self.ycor() < Y_BORDER - PADDLE_LENGTH/2:
            self.forward(STEP)

    def move_down(self):
        if self.ycor() > -Y_BORDER + PADDLE_LENGTH/2:
            self.backward(STEP)

    def move_automatically(self):
        if self.heading() == UP:
            if self.ycor() < Y_BORDER - PADDLE_LENGTH / 2:
                self.forward(STEP)
                time.sleep(0.07)
            else:
                self.setheading(DOWN)
        elif self.heading() == DOWN:
            if self.ycor() > -Y_BORDER + PADDLE_LENGTH / 2:
                self.forward(STEP)
                time.sleep(0.07)
            else:
                self.setheading(UP)




