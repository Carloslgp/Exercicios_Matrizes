import random


def criar_matriz(linha, coluna):
    matriz =[]
    for j in range(0,linha):
        linhas = []
        for i in range(0, coluna):
            num = int(input(f"Digite um número para adicionar a matriz M:{j}:{i} = "))
            linhas.append(num)
        matriz.append(linhas)
    return matriz


def imprimir_matriz(matriz):
    for linhas in matriz:
        print(linhas)

def soma_pares_matriz(matriz):
    soma_par = 0
    for linhas in matriz:
        for elemento in linhas:
            if elemento % 2 == 0:
                soma_par += elemento
    return soma_par
def somar_coluna_escolhida(matriz, numero_coluna_escolhida):
    soma_coluna_escolhida = 0
    for i in range (0, len(matriz)):
        soma_coluna_escolhida += matriz[i][numero_coluna_escolhida]
    print(soma_coluna_escolhida)

def somar_linha_escolhida(matriz, numero_linha_escolhida, numero_de_colunas_matriz):
    soma_linha_escolhida = 0
    for i in range (0, (numero_de_colunas_matriz)):
        soma_linha_escolhida += matriz[numero_linha_escolhida][i]
    print(soma_linha_escolhida)
def funcao_maior_valor_linha(matriz, linha_escolhida_maior, numero_coluna):
    maior_numero = -10000000
    for i in range(0, numero_coluna):
        numero = matriz[linha_escolhida_maior][i]
        if numero > maior_numero:
            maior_numero = numero
        print(maior_numero)







linhas_matriz = int(input("Diga o número de linhas da matriz:"))
colunas_matriz = int(input("Diga o número de colunas na matriz:"))
matriz = criar_matriz(linhas_matriz, colunas_matriz)
soma_pares = soma_pares_matriz(matriz)
soma_colunas = somar_coluna_escolhida(matriz, 1)
soma_linhas= somar_linha_escolhida(matriz, 0, colunas_matriz)
maior_valor_linha = funcao_maior_valor_linha(matriz, 2, colunas_matriz) 
print(f"A soma dos pares da matriz é: {soma_pares_matriz(matriz)}")
imprimir_matriz(matriz)
print(soma_colunas)
