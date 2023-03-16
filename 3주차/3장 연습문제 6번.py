import turtle

print("\n3장 연습문제 6번")
t = turtle.Turtle()
t.shape("turtle")

x1 = int(input("x1: "))
y1 = int(input("y1: "))
x2 = int(input("x2: "))
y2 = int(input("y2: "))

t.up()
t.goto(x1, y1)
t.down()
t.goto(x2, y2)
t.write(((x2-x1)**2+(y2-y1)**2)**0.5)
