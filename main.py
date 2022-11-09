from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

X_BORDER = 400
Y_BORDER = 300

WINNING_SCORE = 10


def draw_pong_table():
    wall = Turtle()
    wall.hideturtle()
    wall.color("white")
    wall.penup()
    wall.goto(-X_BORDER, -Y_BORDER)
    wall.setheading(90)
    wall.pendown()
    while wall.ycor() < Y_BORDER:
        wall.forward(1)
    wall.right(90)
    while wall.xcor() < X_BORDER:
        wall.forward(1)
    wall.right(90)
    while wall.ycor() > -Y_BORDER:
        wall.forward(1)
    wall.right(90)
    while wall.xcor() > -X_BORDER:
        wall.forward(1)
    wall.penup()

    wall.goto(0,-Y_BORDER)
    wall.setheading(90)
    # wall.pendown()
    i = 5
    while wall.ycor() < Y_BORDER:
        wall.forward(1)
        i += 1
        if i % 10 == 0:
            if wall.isdown():
                wall.penup()
            elif not wall.isdown():
                wall.pendown()
    wall.penup()


screen = Screen()
screen.setup(width=2*X_BORDER+30, height=2*Y_BORDER+30)
screen.bgcolor("black")
screen.title("My PONG Game")
screen.tracer(0)

draw_pong_table()
scoreboard = Scoreboard()

l_paddle_x_pos = -X_BORDER + 10
left_paddle = Paddle(l_paddle_x_pos, 0)

screen.listen()
screen.onkeypress(left_paddle.move_up, "Up")
screen.onkeypress(left_paddle.move_down, "Down")

r_paddle_x_pos = X_BORDER - 10
right_paddle = Paddle(r_paddle_x_pos, 0)

ball = Ball()

game_on = True

while game_on:
    screen.update()

    right_paddle.move_automatically()
    ball.move()

    if (ball.distance(left_paddle) < 40 or ball.distance(right_paddle) < 40) \
            and r_paddle_x_pos - 10 < abs(ball.xcor()) < r_paddle_x_pos:
        ball.bounce_paddle()
    elif ball.xcor() > X_BORDER - 10:
        ball.refresh()
        scoreboard.increase_score("left")
    elif ball.xcor() < -X_BORDER + 10:
        ball.refresh()
        scoreboard.increase_score("right")

    if abs(ball.ycor()) > Y_BORDER - 15:
        ball.bounce_wall()

    if scoreboard.score[0] == WINNING_SCORE or scoreboard.score[1] == WINNING_SCORE:
        scoreboard.game_over()
        game_on = False

screen.exitonclick()

