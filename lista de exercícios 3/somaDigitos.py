num = input("Digite um número inteiro: ")
n = int(num)
casas = len(num)

s = 0
soma = 0

while casas > 0:
	s = (n / (10 ** (casas - 1))) % 10
	z = int(s)
	soma = soma + z
	casas = casas - 1
print (soma)
