x = str(input("Insira uma Letra"))

def vogal (x):
	if (vogal == "A") or (vogal == "E") or (vogal == "I") or (vogal == "O") or (vogal == "U"):
		return False
	else:
		return True
		
res = vogal(x)

print(res)
