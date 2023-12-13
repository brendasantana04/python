num = input("Digite o valor de n: ")
n = int(num)

c = 0

while n > 0:
	if c % 2 == 0:
		c = c + 1
		n = n - 1
		print(c)
	else:
		c = c + 1
