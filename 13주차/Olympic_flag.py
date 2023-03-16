import turtle


t = turtle.Turtle()
t.pensize(10)

def draw(color,coordinate):
    t.color(color)
    # t.fillcolor(color)
    t.up()
    t.goto(coordinate)
    t.down()
    # t.begin_fill()
    t.circle(100)
    # t.end_fill()

color = ["blue", "black", "red", "yellow", "green"]
coordinate = [(-150, 100), (0, 100), (150, 100), (-110,-50), (110, -50)]
for i in range(5):
    draw(color[i], coordinate[i])

turtle.mainloop()
