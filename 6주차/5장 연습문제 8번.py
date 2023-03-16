import turtle

t = turtle.Turtle()
t.shape("turtle")

x1 = int(input("큰 원의 중심좌표 x1: "))
y1 = int(input("큰 원의 중심좌표 y1: "))
r1 = int(input("큰 원의 반지름: "))
x2 = int(input("작은 원의 중심좌표 x2: "))
y2 = int(input("작은 원의 중심좌표 y2: "))
r2 = int(input("작은 원의 반지름: "))

t.up()
t.goto(x1, y1)
t.down()
t.circle(r1)

t.up()
t.goto(x2, y2)
t.down()
t.circle(r2)

distance = ((x1-x2)**2 + (y1-y2)**2)**0.5
if distance <= r1+r2:
    print("큰 원 안에 작은 원이 포합됩니다.")
else:
    print("큰 원 안에 작은 원이 포합되지 않습니다.")
