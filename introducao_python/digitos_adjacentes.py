numero = int(input("Digite um número inteiro: "))

comparador_ant = numero % 10  
existem_adjacentes_iguais = False

while numero // 10 != 0 and not existem_adjacentes_iguais:
        numero = numero // 10
        comparador_pos = numero % 10
        if comparador_ant == comparador_pos:
                existem_adjacentes_iguais = True
        comparador_ant = comparador_pos
	

if existem_adjacentes_iguais:
	print("sim")
else:
	print("não")
