def verifCond():
    x = int(input("Digite um valor: "))
    while x < 2:
        print("Valor inválido. O valor deve ser maior ou igual a 2.")
        x = int(input("Digite um valor válido: "))
    return x

x = verifCond()

def éPrimo(xAnt):
	if (xAnt % 2 == 0) or (xAnt % 3 == 0) or (xAnt % 5 == 0) or (xAnt % 7 == 0):
		if (xAnt == 2) or (xAnt == 3) or (xAnt == 5) or (xAnt == 7):
			return True
		else:
			return False
	else:
		return True

def maior_primo(x):
	xAnt = x - 1
	
	while not éPrimo(xAnt):
		xAnt -= 1
	
	return xAnt

xAnt = maior_primo(x)

print (xAnt)
