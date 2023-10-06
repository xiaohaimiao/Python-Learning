import turtle as t 
colors = ['red', 'orange','yellow','green','blue','purple']
def circle(z):  
    t.pendown
    t.circle(z + 5)
    t.penup
    
def fangcheng(x):
    for i in range(0,100):
        x = i
        y = x*2 + 5
        #t.penup()
        t.goto(x,y)
        t.pendown()
fangcheng(10)      


input()