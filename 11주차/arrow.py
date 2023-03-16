import turtle


def turn_left():
    t.left(10)
    t.forward(10)


def turn_right():
    t.right(10)
    t.forward(10)


t = turtle.Turtle()
screen = turtle.Screen()
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")

screen.listen()
screen.mainloop()
