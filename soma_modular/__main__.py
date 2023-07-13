
import ES

import aritmetico



def main(): #Função principal que invoca as funções
    #Atribuição de variáveis
    numeros = [] #numeros aqui eh invocado de fato
    soma = 0
    
    #Entrada de dados
    numeros = ES.leitora_numeros()
    
    #Processamento de dados
    soma = aritmetico.adicao(numeros[0],numeros[1])
    
    #Saida de dados
    ES.escritora_numeros(numeros[0], numeros[1], soma)
    
#Invocando main
if __name__ == "__main__":
    main()