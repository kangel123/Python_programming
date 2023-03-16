import turtle
colors = ["red", "purple", "blue", "green", "yellow", "orange"]      # array
t = turtle.Turtle()

turtle.bgcolor("black")     # background color
t.speed(0)                  # speed(0) : 가장 빠름, speed(1~10) : 속도 증가
t.width(3)                  # 굵은 선
length = 10
while length < 500:
    t.forward(length)
    t.pencolor(colors[length % 6])
    t.right(89)
    length += 5
