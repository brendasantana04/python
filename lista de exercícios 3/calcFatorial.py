num = input("Digite o valor de n: ")
n = int(num)

count = n
fat = 1

if n == 0:
	print("1")
else:
	while 1 < n:
		fat = fat * n
		n = n - 1
	print(fat)
