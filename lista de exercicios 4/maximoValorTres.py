x = int(input("Insira um numero: "))
y = int(input("Insira um numero: "))
z = int(input("Insira um numero: "))

def maximo(x, y, z):
	if x > y:
		if x > z:
			return x
	else:
		if y > z:
			return y
		else:
			return z
	return z

print (maximo(x,y,z))
