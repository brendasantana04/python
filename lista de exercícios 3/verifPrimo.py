num = input("Insira um número inteiro: ")
n = int(num)

if n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0:
	if n == 2 or n == 3 or n == 5 or n == 7:
		print("primo")
	else:
		print ("não primo")
else:
	print ("primo")
		
