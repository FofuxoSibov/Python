""" Operadores Relacionais
>   : maior
<   : menor
==  : igual
!=  : diferente
>=  : maior ou igual
<=  : menor ou igual
"""

# Solicita que o usuário digite um número e converte para ponto flutuante
nota1 = float(input("Digite a primeiro nota: "))

# Solicita que o usuário digite um número e converte para ponto flutuante
nota2 = float(input("Digite a segunda nota: "))

# Solicita que o usuário digite um número e converte para ponto flutuante
nota3 = float(input("Digite a terceira nota: "))

# Calcula a media de tres numero
media = (nota1 + nota2 + nota3) / 3

# Condicional de Aprovação se a média for maior que 6
if media >= 6:
    print ("Você foi Aprovado")

elif media >= 5:
    print ("Você foi para Conselho de Classe")
else:
    print ("Você foi Reprovado")


# Exibe a média das notas
print("A media de :", nota1, "+", nota2, "+", nota3, "=", media)