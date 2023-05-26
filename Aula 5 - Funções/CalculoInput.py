# Funções são iniciados como nome def
# Nosso códugo fica mais limpo e pode ser reaproveitado
# Não precisa declarar as variveis antes

num1 = float (input("Digite o primeiro valor para soma: "))
num2 = float (input("Digite o segundo valor para soma: "))

def soma_valores  (num1,num2):
    total  = num1 + num2
    return total

def subtrai_valores (num1,num2):
    resultado = num1 - num2
    return resultado

print ("Total da soma: ", soma_valores (num1, num2 ))

#print ("Total da subtração: ", subtrai_valores(30,15))