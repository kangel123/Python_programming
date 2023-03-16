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
    a1.forward(2)
    a2.forward(2)
    screen.ontimer(play, 10)    # 10ms 후 play 실행(play 함수를 반복한다)


player = turtle.Turtle()
player.color('blue')
player.shape('turtle')
player.penup()
player.speed(0)

screen = player.getscreen()    # screen = turtle.Screen()과 동일

a1 = turtle.Turtle()
a1.color('red')
a1.shape('circle')
a1.penup()
a1.speed(0)
a1.goto(random.randint(-300, 300), random.randint(-300, 300))

a2 = turtle.Turtle()
a2.color('red')
a2.shape('circle')
a2.penup()
a2.speed(0)
a2.goto(random.randint(-300, 300), random.randint(-300, 300))

# 키보드 조작으로 움직임 제어
screen.onkeypress(turnleft, "Left")
screen.onkeypress(turnright, "Right")
screen.listen()

screen.ontimer(play, 10)    # 10ms 후 play 실행
screen.mainloop()
