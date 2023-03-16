import turtle

print("연습문제 4번")
t = turtle.Turtle()
t.shape("turtle")
t.speed(0)
radius = 50
t. circle(radius)

radius = radius + 20
t.up()              # 펜을 든다
t.goto(100, 0)       # 좌표 (a,b)로 이동
t.down()            # 펜을 내린다
t. circle(radius)

radius = radius + 20
t.up()
t.goto(200, 0)
t.down()
t. circle(radius)
