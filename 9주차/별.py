import random
import turtle


def star(n):
    t = turtle.Turtle()
    while n > 0:
        i = 0
        x = random.uniform(-300, 300)
        y = random.uniform(-300, 300)
        length = random.randint(1, 200)

        t.penup()
        t.goto(x, y)
        t.pendown()
        while i < 5:
            t.forward(length)
            t.right(144)
            i += 1
        n -= 1


num = int(input("몇 개의 별을 그리시겠습니까? : "))
star(num)
