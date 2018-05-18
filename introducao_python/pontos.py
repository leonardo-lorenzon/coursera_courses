import math

x1 = int(input("Digite o valor para x1: "))
y1 = int(input("Digite o valor para y1: "))
x2 = int(input("Digite o valor para x2: "))
y2 = int(input("Digite o valor para y2: "))

distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

if distancia >= 10:
	print("longe")
else:
	print("perto")
