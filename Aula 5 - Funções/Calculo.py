# Funções são iniciados como nome def
# Nosso códugo fica mais limpo e pode ser reaproveitado
# Não precisa declarar as variveis antes

def soma_valores (num1,num2):
    total = num1 + num2
    return total

def subtrai_valores (num1,num2):
    total = num1 - num2
    return total

print ("Digite os valores para somas: ", soma_valores(30,15))
print ("Digite os valores para subtração: ", subtrai_valores(30,15))