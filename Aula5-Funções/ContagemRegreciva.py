#importar biblioteca Time

from time import sleep

def contagem_regressiva(num1):
    # Verificamos se o primeiro número é maior que o segundo número 
    while (num1 > 0):
        print(num1)
        num1 = num1 - 1
        sleep (1)
        
# Exemplo de uso da função
numero1 = int (input("Digite um numero: "))
contagem_regressiva(numero1)
