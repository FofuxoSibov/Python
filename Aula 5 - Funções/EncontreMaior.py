

def maior_numero(num1, num2, num3):
    # Verificamos se o primeiro número é maior que o segundo número e se o primeiro número é maior que o tarceiro número
    if (num1 > num2 and num1 > num3):
        return num1
    # Verificamos se o segundo número é maior que o primeiro número e se o segundo número é maior que o tarceiro número
    elif (num2 > num1 and num2 > num3):
        return num2
    # Verificamos se o segundo número é maior que o primeiro número e se o segundo número é maior que o tarceiro número
    elif (num3 > num1 and num3 > num2):
        return num3

# Declarar variaveis inteiras e receber valores do teclado
numero1 = int (input("Digite o primeiro numero: "))
numero2 = int (input("Digite o segundo numero: "))
numero3 = int (input("Digite o terceiro numero: "))

#Exemplo de uso da função
print("O maior número é:", maior_numero(numero1, numero2, numero3))