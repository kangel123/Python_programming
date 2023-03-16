import turtle
import random


# 왼쪽으로 30도
def turnleft():
    player.left(30)


# 오른쪽으로 30도
def turnright():
    player.right(30)


# 앞으로 이동
def play():
    player.forward(2)
    for i in range(10):
        a[i].forward(2)
    screen.ontimer(play, 10)    # 10ms 후 play 실행(play 함수를 반복한다)


def play2():
    for i in range(10):
        a[i].right(random.randint(0, 360))
    screen.ontimer(play2, 20)   # 10ms 후 play2 실행(play2 함수를 반복한다)


player = turtle.Turtle()
player.color('blue')
player.shape('turtle')
player.penup()
player.speed(0)

screen = player.getscreen()    # screen = turtle.Screen()과 동일

a = []
for t in range(10):
    t = turtle.Turtle()
    t.color('red')
    t.shape('circle')
    t.penup()
    t.speed(0)
    t.goto(random.randint(-300, 300), random.randint(-300, 300))
    a.append(t)

# 키보드 조작으로 움직임 제어
screen.onkeypress(turnleft, "Left")
screen.onkeypress(turnright, "Right")
screen.listen()

screen.ontimer(play, 10)    # 10ms 후 play 실행
screen.ontimer(play2, 1)  # 1ms 후 play2 실행
screen.mainloop()
