def criar_matriz():
    matriz =[]
    for j in range(0, 10):
        linhas = []
        for i in range(10):
            if i == j :
                num = 3 * j ** 2 + 1
            elif j > i:
                num = 4 * j ** 3 + 5 * i ** 2 + 1
            else:
                num = 2 * j + 7 * i ** 2
            linhas.append(num)
        matriz.append(linhas)   
    return matriz

matriz = criar_matriz()
for linhas in matriz:
    print(linhas)