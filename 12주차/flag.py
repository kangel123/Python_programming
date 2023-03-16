import turtle


# 모양 그리는 함수
def draw_shape(radius, color1):
    t.left(270)
    t.width(3)
    t.color('black', color1)
    t.begin_fill()  # 안의 색 채우기(시작)
    t.circle(radius/2.0, -180)  # 반원 그리기
    t.circle(radius, 180)
    t.left(180)
    t.circle(-radius/2.0, -180)
    t.end_fill()    # 안의 색 채우기(종료)


# turtle 생성
t = turtle.Turtle()
t.reset()   # 위치 초기화

draw_shape(200, 'red')
t.setheading(180)   # 180도 회전
draw_shape(200, 'blue')
