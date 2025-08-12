##
#Aula 08 - Atividade 01 - Exercício 01
#Author : Luis Rodrigo - Papagaio
# Data : 12/08/2025

"""
Função Saudação
    -Imprime uma mensagem de boas vindas
"""

def saudacao() :
    print(f"\n\n\tOlá usuário, seja bem vindo !!!\n\n")
# saudacao()

"""
Função soma
    -Somar dois números e retornar o resultado.
"""
def somar_numeros (n1, n2) :
    soma = n1 + n2
    return soma
#print(f"{somar_numeros( 1, 15)}")


##
# Corpo do Programa
##




numero1=float(input("Digite o 1o Numero : "))
numero2=float(input("Digite o 1o Numero : "))
resultado=somar_numeros(numero1, numero2)
print(f"O resultado da soma de {numero1} com {numero2} é {resultado}")