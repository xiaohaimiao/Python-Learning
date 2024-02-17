import turtle as t
from itertools import cycle
import random
c = cycle(['red', 'green', 'blue'])

def Draw_Star(r2):
    for i in range(angleb):
        t.forward(r2)
        t.right(anglec)
    return

def Draw_Shape(r13 , r2, angledelta):
    t.pencolor(next(c))
    t.penup()
    t.forward(r13)
    t.pendown()
    print(t.screensize(), t.pos())
    (x, y) = t.pos()
    (width, height) = t.screensize()
    if x >= width or x <= -width:
        return False
    if y >= height or y <= -height:
        return False
    if angleb == 1:
        t.circle(r2)
    else:
        Draw_Star(r2)
    t.penup()
    t.back(r13)
    t.right(angledelta)
     
    return True

t.speed('fastest')

'''r1 = int(input('请填写1号圆的半径：'))
r2 = int(input('请填写2号圆的半径：'))
rdelta = int(input('请填写2号圆半径的变化量：'))
angledelta = int(input('请填写角度的变化量：'))'''
r11 = 0
r12 = 1
r2 = 1
rdelta = 1
angledelta = 2
angle = ['1','3','5','7','9','11']
angleb2 = int(random.choice(angle))
count = 20
for i in range(1, count):
    angleb = int(random.choice(angle))
    anglec = 180 - (180 / angleb)
    r13 = r11 + r12 + 10
    inside = Draw_Shape(r11 , r2, angledelta)
    if not inside:
        break
    angledelta += 5
    r2 += rdelta
    r11 = r12
    r12 = r13
    
input()