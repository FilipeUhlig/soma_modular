"""
Programa: ES
Descrição: Este móudulo provê funcionalidades de entrada e saída de dados para o programa soma_modular.py
autor: F
data: 07/07/2023
versão: 0.0.1
"""
##Entrada de dados
def leitora_numeros(): ###Função, a função tem um escopo local
    numeros = [] #numeros aqui só é estabelecido para a função leitora
    i = 0
    while i < 2:
        numeros.append(float(input(f"Digite o {i + 1}º número: ")))
        i += 1
    return numeros

##Saida de dados

def escritora_numeros(x,y,z): ###Função
    print(f" A soma dos números {x} e {y} é igual a {z}.")