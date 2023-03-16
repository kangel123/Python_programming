import turtle


def draw_maze(x, y):
    t.penup()
    t.goto(-x/2, y/2)
    t.pendown()
    for i in range(2):
        t.forward(x)
        t.right(90)
        t.forward(y*9/10)
        t.penup()
        t.forward(y / 10)
        t.pendown()
        t.right(90)

    for i in range(10):
        if i % 2 == 1:
            t.penup()
            t.goto(-x/2, y/2-y*i/10)
            t.pendown()
            t.forward(x * 9 / 10)
        else:
            t.penup()
            t.goto(x/2, y/2-y*i/10)
            t.pendown()
            t.backward(x * 9 / 10)


def turn_go():
    t.forward(10)


def turn_back():
    t.backward(10)


def turn_left():
    t.left(90)


def turn_right():
    t.right(90)


t = turtle.Turtle()
screen = turtle.Screen()
width = 500
length = 500

draw_maze(width, length)

t.penup()
t.color('blue')
t.goto(-width/2, length/2-length/20)
t.speed(1)
t.pendown()

screen.onkey(turn_go, "Up")
screen.onkey(turn_back, "Down")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")

screen.listen()
screen.mainloop()
