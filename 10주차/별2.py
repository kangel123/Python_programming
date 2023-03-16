import random
import turtle

s = turtle.Screen()
s.screensize(500, 500)
t = turtle.Turtle()


def getRGB():
    r = random.random()
    g = random.random()
    b = random.random()
    return (r, g, b)

def star(n):
    while n > 0:
        i = 0
        x = random.uniform(-300, 300)
        y = random.uniform(-300, 300)
        length = random.randint(1, 200)
        r, g, b = getRGB()

        t.color(r, g, b)
        t.penup()
        t.goto(x, y)
        t.pendown()
        while i < 5:
            t.forward(length)
            t.right(144)
            i += 1
        n -= 1

def drawline(x, y):
    t.color(0, 0, 0)
    t.pendown()
    t.goto(x, y)

s = turtle.Screen()
num = int(input("몇 개의 별을 그리시겠습니까? : "))
star(num)
t.screen.onclick(drawline)

turtle.mainloop()
