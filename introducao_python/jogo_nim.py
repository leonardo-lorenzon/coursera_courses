def main():
	print("Bem vindo ao jogo do NIM! Escolha:")
	tipo_de_jogo = 0
	print("1 - para jogar uma partida isolada")
	tipo_de_jogo = int(input("2 - para jogar um campeonato "))
	if tipo_de_jogo == 1:
		print("Você escolheu uma partida isolada!")
		partida()
	else:
		print("Você escolheu um campeonato!")
		campeonato()

def partida():		
	
	n = int(input("Quantas peças? "))
	m = int(input("Limite de peças por jogada? "))
	vez_do_usuario = False
	vez_do_computador = False
	pecas_tiradas = 0

	if n % (m + 1) == 0:
		print("Você começa!")
		pecas_tiradas = usuario_escolhe_jogada(n, m)
		n = n - pecas_tiradas
		if pecas_tiradas == 1:
			print("Você tirou uma peça.")
		else:
			print("Você tirou", pecas_tiradas, "peças.")
		if n > 1:
			print("Agora restam", n, "peças no tabuleiro.")
		else:
			if n == 1:
				print("Agora resta apenas uma peça no tabuleiro.")
			else:
				print("Fim de jogo! Você ganhou!")
		vez_do_usuario = True
	else:
		print("Computador começa!")
		pecas_tiradas = computador_escolhe_jogada(n, m)
		n = n - pecas_tiradas
		if pecas_tiradas == 1:
			print("Computador tirou uma peça.")
		else:
			print("Computador tirou", pecas_tiradas, "peças.")
		if n > 1:
			print("Agora restam", n, "peças no tabuleiro.")
		else:
			if n == 1:
				print("Agora resta apenas uma peça no tabuleiro.")
			else:
				print("Fim de jogo! O computador ganhou!")
		vez_do_computador = True

	while n > 0:
		if vez_do_computador == False:
			pecas_tiradas = computador_escolhe_jogada(n, m)
			n = n - pecas_tiradas
			if pecas_tiradas == 1:
				print("Computador tirou uma peça.")
			else:
				print("Computador tirou", pecas_tiradas, "peças.")
			if n > 1:
				print("Agora restam", n, "peças no tabuleiro.")
			else:
				if n == 1:
					print("Agora resta apenas uma peça no tabuleiro.")
				else:
					print("Fim de jogo! O computador ganhou!")
			vez_do_usuario = False
			vez_do_computador =True
		else:
			pecas_tiradas = usuario_escolhe_jogada(n, m)
			n = n - pecas_tiradas
			if pecas_tiradas == 1:
				print("Você tirou uma peça.")
			else:
				print("Você tirou", pecas_tiradas, "peças.")
			if n > 1:
				print("Agora restam", n, "peças no tabuleiro.")
			else:
				if n ==1:
					print("Agora resta apenas uma peça no tabuleiro.")
				else:
					print("Fim de jogo! Você ganhou!")
			vez_do_computador = False
			vez_do_usuario = True

	if vez_do_usuario == True:
		return 0
	else:
		return 1


def computador_escolhe_jogada(n, m):
	resposta_computador = 1
	resposta_valida = False
	while resposta_computador <= m and resposta_valida == False:
		if ((n - resposta_computador) % (m+1)) == 0:
			resposta_valida = True
		resposta_computador = resposta_computador + 1

	if resposta_valida == True:
		return resposta_computador - 1
	else:
		if m <= n:
			return m
		else:
			return n


def usuario_escolhe_jogada(n, m):
	pecas_tiradas = int(input("Quantas peças você vai tirar? "))
	
	while pecas_tiradas > m or pecas_tiradas < 1:
		print("Oops! Jogada inválida! Tente de novo.")
		pecas_tiradas = int(input("Quantas peças você vai tirar? "))

	return pecas_tiradas


def campeonato():
	cont_partidas = 1
	vitorias_usuario = 0
	vitorias_computador = 0
	while cont_partidas <= 3:
		print("**** Rodada", cont_partidas, "****")
		if partida() == 0:
			vitorias_usuario = vitorias_usuario + 1
			cont_partidas = cont_partidas + 1
		else:
			vitorias_computador = vitorias_computador + 1
			cont_partidas = cont_partidas + 1
	print("Placar: Você", vitorias_usuario, "X", vitorias_computador, "Computador")


main()
