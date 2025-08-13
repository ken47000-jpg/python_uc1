##
#Aula 08 - Atividade 02 - Exercício 01
#Author : Luis Rodrigo - Papagaio
# Data : 12/08/2025

"""
Exercícios envolvendo a função main ()
    -Modifique o seguinte código para usar a função main() corretamente
"""

def saudacao():
   print("\n\n\tOlá, mundo!\n")

def somar_numeros (n1, n2) :
    soma = n1 + n2
    return soma
def somar_numeros_v2 (n1, n2) :
    soma = n1 + n2
    print(f"{soma}")

def somar_numeros_v3 ():
   n1=float(input("Digite o primeiro numero: "))
   n2=float(input("Digite o segundo numero: "))
   soma = n1+n2
   print(f"A soma é:{soma}")

if __name__ == "__main__":
   #saudacao()
   #print(f"{somar_numeros(15,16)}")
   somar_numeros_v2 (15, 16)
   #somar_numeros_v3 ()