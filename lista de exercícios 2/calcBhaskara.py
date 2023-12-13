import math

ar = input()
a1 = float(ar)

br = input()
b1 = float(br)

cr = input()
c1 = float(cr)

d = b1 ** 2 - 4 * a1 * c1
delta = float(d)


if delta < 0:
	print("esta equação não possui raízes reais")
else:
	if delta == 0:
		x1 = (-b1 + math.sqrt(delta))/2 * a1
		print("a raiz desta equação é",x1)
	else:
		x1 = (-b1 + math.sqrt(delta))/2 * a1
		x2 = (-b1 - math.sqrt(delta))/2 * a1	
		if x1 > x2:
			print("as raízes da equação são",x1,"e",x2)
		else:
			print("as raízes da equação são",x2,"e",x1)
