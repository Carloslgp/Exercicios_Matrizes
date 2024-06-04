import os
import time

cadastrados = []

def menu():
    os.system("cls")
    print("-*" * 20)
    print(" 1 - Cadastrar mais pessoas")
    print(" 2 - Sair")
    print("-*" * 20)

def escolhendo_opção():
    try:
        escolha = int(input("Digite o número escolhido: "))
        if escolha == 1:
            cadastrar()
        elif escolha == 2:
            finalizar()
        else:
            opcao_invalida()  
    except:
        opcao_invalida()
        
def opcao_invalida():
    print("Opção Inválida!!!")
    input("Digite qualquer coisa para voltar ao menu principal: ")
    main()
    
    
def main():
    menu()
    escolhendo_opção()
    
def cadastrar():
    os.system("cls")
    cadastro = []
    nome = input("Digite o nome: ")
    cpf = input("Digite o CPF: ")
    idade = int(input("Digite a idade: "))
    renda = float(input("Digite a renda mensal: "))
    cadastro.append([nome, cpf, idade , renda])
    cadastrados.append(cadastro)
    main()
    
def media_idade():
    if cadastrados:
        soma = 0
        for pessoa in cadastrados:
            soma += pessoa[0][2]  
        media_idades = soma / len(cadastrados)
        print("Média das idades:", media_idades)
    else:
        print("Nenhum cadastro encontrado.")
        
def media_salario():
    if cadastrados:
        soma = 0
        for pessoa in cadastrados:
            soma += pessoa[0][3]  
        media_salarios = soma / len(cadastrados)
        print("Média dos salarios:", media_salarios)
    else:
        print("Nenhum cadastro encontrado.")


def finalizar():
    os.system("cls")
    print("Obrigado por utilizar o programa")
    for indice in cadastrados:
        print(indice)
    media_idade() 
    media_salario()




main()

