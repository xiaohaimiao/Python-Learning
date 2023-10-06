import turtle as t
t.setup(1600, 900)
#print(t.window_width(), t.window_height())
x = -t.window_width()/2
y = -t.window_height()/2
z = 7
while True:
    t.speed('fastest')
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.circle(z)
    t.penup()
    x += 10
    y += 10
    z += 2
    
    pos = t.position
    #t.onclick()
    #t.write('(' + str(x) + ", " + str(y) + ')')
    if x >= 0:
        break
input()