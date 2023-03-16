import turtle
import math


def turnleft():
    player.left(5)


def turnright():
    player.right(5)


def fire():
    x, y = 0, 0
    velocity = 50   # 초기 속도
    angle = player.heading()    # 각도는 player(터틀)의 머리방향
    vx = velocity * math.cos(angle * 3.14 / 180.0)  # x-vector = vx = 속도 * cos(각도)
    vy = velocity * math.sin(angle * 3.14 / 180.0)  # y-vector = vy = 속도 * cos(각도)
    while player.ycor() >= 0:   # player의 y좌표가 음수가 될 때까지
        vx = vx
        vy = vy - 10
        x = x + vx
        y = y + vy
        player.goto(x, y)


player = turtle.Turtle()
player.shape('turtle')
screen = player.getscreen()

# 키보드 조작으로 움직임 제어
screen.onkeypress(turnleft, 'Left')
screen.onkeypress(turnright, 'Right')
screen.onkeypress(fire, 'space')
screen.listen()

screen.mainloop()
