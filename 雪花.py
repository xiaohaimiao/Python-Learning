import turtle as t
import random as r


def Draw_SnowFlower(pos, color, lines, size=10):
    t.penup()
    t.goto(pos)

    t.pencolor(color[0], color[1], color[2])
    t.pendown()
    tangle = 360 // lines
    for i in range(lines):
        t.forward(size)
        t.back(size)
        t.right(tangle)

width = 1600
height = 900
t.setup(width, height)    
t.pensize(1)
t.hideturtle()
t.tracer(False)

for i in range(500):
    x = r.randint(-width/2, width/2)
    y = r.randint(-height/2, height/2)
    pos = (x, y)

    R = r.random()
    G = r.random()
    B = r.random()
    color = (R, G, B)

    lines = r.randint(6, 12)
    Draw_SnowFlower(pos, color, lines)

input()
