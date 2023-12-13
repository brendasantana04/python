seg = input("Por favor, entre o número de segundos que deseja converter: ")
s1 = int(seg)

d = s1 // 86400

sd = s1 % 86400
ss = s1 % 3600
sr = ss + sd

h = sd // 3600

m = ss // 60
sss = ss % 60

print(d,"dias,",h,"horas",m,"minutos e",sss,"segundos.")
