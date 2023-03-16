import turtle

t = turtle.Turtle()
t.shape("turtle")

xlist = []
ylist = []
x1 = int(input("x1: "))
xlist.append(x1)
y1 = int(input("y1: "))
ylist.append(y1)
x2 = int(input("x2: "))
xlist.append(x2)
y2 = int(input("y2: "))
ylist.append(y2)
x3 = int(input("x3: "))
xlist.append(x3)
y3 = int(input("y3: "))
ylist.append(y3)

t.goto(xlist[0], ylist[0])
t.goto(xlist[1], ylist[1])
t.goto(xlist[2], ylist[2])
