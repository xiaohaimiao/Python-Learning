import turtle as t
from itertools import cycle

c = cycle(['red', 'green', 'blue'])
def Draw_Circle(r1 , r2, angledelta):
    t.pencolor(next(c))
    t.penup()
    t.forward(r1)
    t.pendown()
    t.circle(r2)
    t.penup()
    t.back(r1)
    t.right(angledelta)
    
    return

t.speed('fastest')

'''r1 = int(input('请填写1号圆的半径：'))
r2 = int(input('请填写2号圆的半径：'))
rdelta = int(input('请填写2号圆半径的变化量：'))
angledelta = int(input('请填写角度的变化量：'))'''
r1 =100
r2 = 1
rdelta = 1
angledelta = 2
count = int(360/angledelta)
for i in range(1, count):
    Draw_Circle(r1 , r2, angledelta)
    angledelta += 5
    r2 += rdelta
    
input()