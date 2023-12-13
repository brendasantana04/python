import math

xa = input()
x1 = int(xa)
ya = input()
y1 = int(ya)

xb = input()
x2 = int(xb)
yb = input()
y2 = int(yb)

d = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

if d > 10:
	print("longe")
else:
	print("perto")

