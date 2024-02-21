from test2 import Hanoi

x = [ c.zfill(2) for c in str(3132165) if c < '5' ]
y = list(str(3132165))
z = { c:c.zfill(2) for c in str(3132165) if c < '5' }
#print(x, ''.join(x))
#print(y, ''.join(y))
#print(z, "".join(z))

#print(f"{x[0]} + {y[0]} + {z['3']}")

x = Hanoi(5, 3, 1)