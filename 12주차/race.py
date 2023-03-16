# 거북이 경주 게임
import turtle
import random


# 거북이 이동 함수 (이동 거리는 랜덤)
def forward_turtle(t):
    d = random.randint(1, 6)
    t.forward(d)


screen = turtle.Screen()

t1 = turtle.Turtle()    # 첫번째 거북이 생성
t2 = turtle.Turtle()    # 두번째 거북이 생성
t3 = turtle.Turtle()    # 세번째 거북이 생성

# 첫번째 거북이 설정
t1.color('pink')
t1.shape('turtle')
t1.shapesize(5)
t1.pensize(5)

# 두번째 거북이 설정
t2.color('blue')
t2.shape('turtle')
t2.shapesize(5)
t2.pensize(5)

# 세번째 거북이 설정
t3.color('red')
t3.shape('turtle')
t3.shapesize(5)
t3.pensize(5)

# 거북이들 시작 위치
t1.penup()
t1.goto(-300, 0)
t1.pendown()
t2.penup()
t2.goto(-300, -100)
t2.pendown()
t3.penup()
t3.goto(-300, -200)
t3.pendown()

# 거북이들 달리기 시작
for i in range(100):
    forward_turtle(t1)
    forward_turtle(t2)
    forward_turtle(t3)

screen.mainloop()
