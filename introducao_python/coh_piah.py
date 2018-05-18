import math
import re

def le_assinatura():
  #A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos
    print("Bem-vindo ao detector automático de COH-PIAH.")

    wal = float(input("Entre o tamanho medio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)



def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    cont = 0
    grau_similaridade = 0
    
    while cont < 6:
        grau_similaridade = math.sqrt((as_a[cont] - as_b[cont]) ** 2) + grau_similaridade
        cont = cont + 1
    
    grau_similaridade = grau_similaridade / 6
    
    return grau_similaridade





def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    wal = tamanho_medio_palavra(texto)
    ttr = type_token(texto)
    hlr = razao_hapax_legomana(texto)
    sal = tamanho_medio_sentenca(texto)
    sac = complexidade_media_sentenca(texto)
    pal = tamanho_medio_frase(texto)

    return [wal, ttr, hlr, sal, sac, pal]


def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    assinatura_aux = []
    grau_similaridade = 0
    cont = 1
    possivel_plagio = 1000000
    autor = 0
    for i in textos:
        assinatura_aux = calcula_assinatura(i)
        grau_similaridade = compara_assinatura(ass_cp, assinatura_aux)
        if grau_similaridade < possivel_plagio:
            possivel_plagio = grau_similaridade
            autor = cont
        cont = cont + 1

    print("\n""O autor do texto", autor, "está infectado com o COH-PIAH")
    return autor



def tamanho_medio_palavra(texto):
    lista_sentencas = separa_sentencas(texto)
    
    lista_frases = []
    for i in lista_sentencas:
        lista_frases = separa_frases(i) + lista_frases
    
    lista_palavras = []
    for n in lista_frases:
        lista_palavras = separa_palavras(n) + lista_palavras

    quantidade_palavras = len(lista_palavras)
    soma_caracteres = 0
    for j in lista_palavras:
        soma_caracteres = len(j) + soma_caracteres

    return soma_caracteres / quantidade_palavras

def type_token(texto):
    lista_sentencas = separa_sentencas(texto)
    
    lista_frases = []
    for i in lista_sentencas:
        lista_frases = separa_frases(i) + lista_frases
    
    lista_palavras = []
    for n in lista_frases:
        lista_palavras = separa_palavras(n) + lista_palavras

    quantidade_palavras = len(lista_palavras)
    numero_palavras_diferentes =  n_palavras_diferentes(lista_palavras)

    return numero_palavras_diferentes / quantidade_palavras


def razao_hapax_legomana(texto):
    lista_sentencas = separa_sentencas(texto)
    
    lista_frases = []
    for i in lista_sentencas:
        lista_frases = separa_frases(i) + lista_frases
    
    lista_palavras = []
    for n in lista_frases:
        lista_palavras = separa_palavras(n) + lista_palavras

    quantidade_palavras = len(lista_palavras)
    numero_palavras_unicas =  n_palavras_unicas(lista_palavras)

    return numero_palavras_unicas / quantidade_palavras


def tamanho_medio_sentenca(texto):
    lista_sentencas = separa_sentencas(texto)

    quantidade_sentencas = len(lista_sentencas)

    soma_caracteres = 0
    for i in lista_sentencas:
        soma_caracteres = len(i) + soma_caracteres

    return soma_caracteres / quantidade_sentencas


def complexidade_media_sentenca(texto):
    lista_sentencas = separa_sentencas(texto)
    
    lista_frases = []
    for i in lista_sentencas:
        lista_frases = separa_frases(i) + lista_frases

    quantidade_sentencas = len(lista_sentencas)
    quantidade_frases = len(lista_frases)

    return quantidade_frases / quantidade_sentencas

def tamanho_medio_frase(texto):
    lista_sentencas = separa_sentencas(texto)
    
    
    lista_frases = []
    for i in lista_sentencas:
        lista_frases = separa_frases(i) + lista_frases

    quantidade_frases = len(lista_frases)
    soma_caracteres = 0
    for i in lista_frases:
        soma_caracteres = len(i) + soma_caracteres

    return soma_caracteres / quantidade_frases


def main():
    assinatura_modelo = le_assinatura()
    lista_de_textos = le_textos()
    avalia_textos(lista_de_textos, assinatura_modelo)

main()
