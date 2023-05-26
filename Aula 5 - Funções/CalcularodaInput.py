# Funções são iniciados como nome def
# Nosso códugo fica mais limpo e pode ser reaproveitado
# Não precisa declarar as variveis antes

def adicao  (num1,num2):
    total  = num1 + num2
    return total

def subtracao (num1,num2):
    resultado = num1 - num2
    return resultado

def multiplicacao (num1,num2):
    resultado = num1 * num2
    return resultado

def divisao (num1,num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Erro divisão por Zero"

# Função principal da calculadora
def calculadora():
    print("Bem-vindo à calculadora!")

    while True:
        print("Escolha uma operação:")
        print("1. Adição")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Sair")

        escolha = input("Digite o número da operação desejada: ")

        if escolha == "5":
            print("Obrigado por usar a calculadora. Até logo!")
            break

        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if escolha == "1":
            resultado = adicao(num1, num2)
            print("Resultado: ", resultado)
        elif escolha == "2":
            resultado = subtracao(num1, num2)
            print("Resultado: ", resultado)
        elif escolha == "3":
            resultado = multiplicacao(num1, num2)
            print("Resultado: ", resultado)
        elif escolha == "4":
            resultado = divisao(num1, num2)
            print("Resultado: ", resultado)
        else:
            print("Escolha inválida. Por favor, tente novamente.")

# Chama a função da calculadora
calculadora()

#print ("Total da subtração: ", subtracao(30,15))